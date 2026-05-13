# Mission Control Resume

Run this when `PLAN.md` already exists.

## Step 1 — Assess current state

Read these files (if they exist):
- `PLAN.md` — find current task and last verification
- `CLOSED_TASKS.md` — see what's protected
- `validation-manifest.json` — check closed baseline
- `done-check.sh` — verify it's present and executable

Run `git status` and `git log --oneline -10` to understand current state.

Report to the user:
- Current task (first task with `Status: open`)
- Last completed task
- Last verification result (from PLAN.md Current State section)
- Whether `done-check.sh` is present
- Whether hooks are installed (check `.claude/settings.json` for hook entries)
- Any BLOCKED_AGENT markers

## Step 2 — Ask what they want

Ask via `AskUserQuestion`:

"Mission Control is already set up. What do you want to do?"

Options:
- **Resume execution** — continue from current task (run-agent.sh or direct execution prompt)
- **Check status** — just show current state, don't run
- **Upgrade tier** — add more hooks, judge layer, or anti-gaming controls
- **Reset a task** — reopen a closed task with explicit intent
- **View done-check status** — run done-check.sh and show output

## Step 3 — Execute the chosen action

### Resume execution
Print the execution prompt from `templates/prompts.md` and tell the user to either:
- Run `./run-agent.sh` if it exists
- Or paste the execution prompt into a new Claude session

### Check status
Run `./done-check.sh 2>&1 || true` and show the output.
Show the task table from PLAN.md.

### Upgrade tier
Walk through only the missing components from `setup.md` Steps 5–9, skipping what's already present.

### Reset a task
Ask which task. Confirm with the user. Update PLAN.md status from `closed` to `open` and add a note with the reason.

### View done-check status
Run `./done-check.sh 2>&1 || true` and explain each failure line.
