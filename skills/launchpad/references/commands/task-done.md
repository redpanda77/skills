Read `.plan/active.md` to find the active feature.
Read `.plan/features/[feature]/tasks.md`.

If $ARGUMENTS specifies a task id, use that. Otherwise use `AskUserQuestion` to ask which task to mark done, showing only In Progress and Backlog tasks.

Move the task to the Done section. Update the Status counter (e.g. "2/7 complete").
Update `current-task` in `active.md` to the next In Progress task, or "none" if none remain.

Ask via `AskUserQuestion`:
> "What's next?"
> Options: "Start next task now" | "Write a handoff first" | "Done for today"
