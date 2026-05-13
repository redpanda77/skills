---
description: Recovery mode — read current state, identify where to resume, continue execution without asking for confirmation.
---

Recovery mode. Do not ask whether to continue. Do not rely on conversation history.

1. Run `/mc-status` to get current state.

2. Run `git log --oneline -10` and `git status`.

3. Read `PLAN.md` in full:
   - Find first task with `Status: open`
   - Find last task with `Status: closed`
   - Check for any `BLOCKED_AGENT` markers

4. Run `./done-check.sh 2>&1 || true` — capture output without stopping.

5. Report findings:
   ```
   Recovery report:
   - Current task: [task ID and name]
   - Last closed: [task ID]
   - Done-check: [pass / fail — reason]
   - Blockers: [none / list]
   - Git: [last commit]
   ```

6. Resume:
   - If done-check passes: report complete, nothing to do.
   - If blockers exist: report them. Do not continue past a blocker without human input.
   - Otherwise: continue from the first open task in PLAN.md.

Do not re-do work from closed tasks. Start exactly where execution left off.
