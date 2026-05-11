Read `.plan/active.md`.

If `feature` is "none" or the file doesn't exist, list all folders under `.plan/features/` (excluding `_archive/`) with their task completion status. Use `AskUserQuestion` to ask which feature to start working on, then update `active.md`.

If an active feature is set:
1. Read `.plan/CONTEXT.md` if it exists
2. Read `.plan/features/[feature]/prd.md`
3. Read `.plan/features/[feature]/tasks.md`
4. Use `AskUserQuestion` to confirm which task to work on this session, showing In Progress tasks first, then Backlog. Include a "Something else" option.

Move the chosen task to In Progress in tasks.md if it isn't already. Update `last-session` in `active.md` to today's date.
