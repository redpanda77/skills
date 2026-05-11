List all folders under `.plan/features/` (excluding `_archive/`). For each, read its `tasks.md` Status line to show completion (e.g. "auth — 3/7 complete").

Use `AskUserQuestion` to ask which feature to switch to.

Update `.plan/active.md`: set `feature` to the chosen one, set `current-task` to the first In Progress task in its tasks.md (or first Backlog task if none in progress), update `last-session` to today.

Read the feature's PRD and tasks and confirm the current task to the user.
