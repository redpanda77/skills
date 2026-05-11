# Hook Reference

## How hooks connect to validation scripts

Hooks and validation scripts serve different roles:

```
Validation scripts (done-check.sh, validate-*.sh)
  → decide whether work is done
  → run outside Claude
  → are the source of truth for completion

Hooks (.claude/hooks/*.sh)
  → enforce behavior inside Claude Code
  → run automatically in response to Claude's actions
  → feed information back to Claude or block actions
```

The connection point is the **Stop hook**: when Claude tries to stop, the Stop hook runs `done-check.sh`. If done-check exits non-zero, the hook blocks Claude from stopping and injects the failure reason as Claude's next input. Claude reads it and continues.

This is the core loop:
```
Claude tries to stop
  → stop-if-not-done.sh runs
  → done-check.sh runs (which calls validate-*.sh)
  → if any check fails, Claude is blocked + receives failure output
  → Claude continues working
  → Claude tries to stop again
  → ...repeat until done-check passes
```

All other hooks are supplemental. The Stop hook is the only one that is strictly necessary for the controlled execution guarantee.

---

## Hook aggressiveness levels

### Low — enforcement only
**Hooks:** Stop hook only

Claude can do anything except stop prematurely. No other restrictions.

Best for: short tasks (< 30 min), when you trust Claude's judgment on everything except stopping, or when you want to start simple and add hooks if problems arise.

Tradeoff: no protection against accidental destructive commands or context drift after resume.

### Medium — enforcement + safety
**Hooks:** Stop hook + block-dangerous + session-start-reminder

Adds two practical guards:
- `block-dangerous.sh`: prevents rm -rf, force push, kubectl apply, npm publish, and similar commands that can cause irreversible damage
- `session-start-reminder.sh`: re-injects the operating rules at session start and after context compaction, keeping Claude oriented after interruptions

Best for: most tasks over 30 minutes. The context cost of session-start-reminder is low (one injected message). The dangerous command blocker prevents the most common accidents without interfering with normal work.

Tradeoff: session-start-reminder adds a small amount of context to every session start. block-dangerous may occasionally flag legitimate commands — the user can approve them.

### High — enforcement + safety + anti-gaming
**Hooks:** All medium hooks + protect-control-files + post-edit-reminder

Adds two more:
- `protect-control-files.sh`: blocks Claude from editing hooks, validators, `done-check.sh`, `CLOSED_TASKS.md`, and `validation-manifest.json`. Prevents validation gaming.
- `post-edit-reminder.sh`: after every file edit, reminds Claude to run validation and update PLAN.md.

Best for: Tier 2/3 tasks, multi-hour runs, tasks where Claude is writing tests as part of the work (so test quality matters), or any case where you're worried Claude might subtly weaken validation to make done-check pass.

Tradeoff: Claude cannot update `CLOSED_TASKS.md` or `validation-manifest.json` through normal edits — you either need a separate closure script, use the external layout, or temporarily disable the hook. Post-edit-reminder creates some context noise; on very long tasks this can accumulate.

---

## Individual hook reference

### stop-if-not-done.sh
**Event:** Stop  
**Fires when:** Claude attempts to end the session

Calls `done-check.sh`. If it fails, returns a block decision with the failure reason injected back to Claude.

**Critical implementation note:** Must include the recursion guard. The Stop event can fire inside a stop-hook evaluation. Without the guard, the hook loops forever:
```bash
if echo "$input" | jq -e '.stop_hook_active == true' >/dev/null 2>&1; then
  exit 0
fi
```

**Path dependency:** This hook must know where `done-check.sh` is. If using inline layout, it calls `./done-check.sh`. If using external layout, it calls `../agent-control/done-check.sh "$PWD"`. Set the path correctly when writing the hook.

---

### block-dangerous.sh
**Event:** PreToolUse, matcher: Bash  
**Fires when:** Claude runs any bash command

Scans the command for dangerous patterns. Current list:
- `rm -rf` — recursive delete
- `git push --force` — overwrites remote history
- `git reset --hard` — discards local changes
- `kubectl apply` — production deployment
- `terraform apply` — infrastructure change
- `npm publish` / `pnpm publish` / `yarn publish` — package release
- `drop database` / `TRUNCATE TABLE` — data destruction
- `docker system prune` — removes all containers and images

Returns a block decision with the command quoted, telling Claude to ask the user before proceeding.

**Customization:** Add project-specific dangerous commands by editing the `grep -qE` pattern. For example, a project with a `./deploy.sh` script should add that.

---

### session-start-reminder.sh
**Event:** SessionStart  
**Fires when:** Claude Code starts, resumes, or context is compacted

Prints the operating protocol if `PLAN.md` exists. This is context injection, not enforcement — it just re-orients Claude.

Only meaningful if you have a `PLAN.md`. If PLAN.md doesn't exist, the hook exits silently.

**Context cost:** One injected message per session start. Low cost. Does not fire on every tool use.

---

### protect-control-files.sh
**Event:** PreToolUse, matcher: Write|Edit|MultiEdit  
**Fires when:** Claude attempts to write or edit any file

Extracts the target file path(s) from the tool input and checks against a protected list. Blocks if the target is:
- `done-check.sh`
- `run-agent.sh`
- Any `validate-*.sh`
- `close-task-check.sh`
- `judge-rubric*.md`
- `hidden-tests/` directory
- `.claude/hooks/` directory
- `.claude/settings.json`
- `validation-manifest.json`
- `CLOSED_TASKS.md`

**If Claude needs to update CLOSED_TASKS.md or validation-manifest.json:**
Three options:
1. Use a dedicated closure script that runs from outside Claude (run by the user or wrapper)
2. Temporarily remove the hook from `.claude/settings.json` (from the terminal), make the update, re-add the hook
3. Use the external `agent-control/` layout — those files are physically outside the workspace

For most Tier 2 setups, option 2 is practical: the hook protects against accidental edits, not deliberate ones.

---

### post-edit-reminder.sh
**Event:** PostToolUse, matcher: Write|Edit|MultiEdit  
**Fires when:** Claude successfully writes or edits a file

Injects a short reminder to run validation and update PLAN.md.

**Context cost:** Fires after every file edit. On a task with 50 edits, this injects 50 reminder messages. This accumulates. Recommend only for tasks where Claude has historically drifted (e.g. made several edits without running tests).

**Mitigation:** If the reminder is adding too much noise, remove it from `.claude/settings.json`. The Stop hook and session-start-reminder together are usually sufficient.

---

## Updating hooks after setup

If `protect-control-files.sh` is installed, Claude cannot edit hook files. To update hooks:

1. Edit the file directly from your terminal (not from Claude Code)
2. Or: remove the hook entry from `.claude/settings.json` in the terminal, make changes in Claude, re-add the entry

The hook only protects against edits made through Claude Code tool calls. Direct file system access bypasses it.
