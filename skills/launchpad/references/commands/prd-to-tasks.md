Read `.plan/features/$ARGUMENTS/prd.md`. If $ARGUMENTS is empty, use `AskUserQuestion` to ask which feature, listing all folders under `.plan/features/` (excluding `_archive/`).

Break the PRD into discrete tasks, each completable in one session. For each task:
- Assign a TASK-NNN id (sequential)
- Write a title (5–8 words, imperative)
- Assign a size: S (under 2h), M (half-day), L (full session)
- Write one "Done when" line — specific and testable

Save to `.plan/features/[feature]/tasks.md` using the tasks format (Backlog / In Progress / Done sections, Status counter).

After saving, scan the task list and ask yourself: does any task represent a repeatable workflow that would benefit from being a dedicated skill (multi-step, domain-specific, likely to recur)? If yes, call it out explicitly and ask via `AskUserQuestion`:
> "TASK-NNN looks like a good skill candidate. Create a skill for it now?"
> Options: "Yes, run /write-a-skill" | "Note it but skip for now" | "No, it's a one-off"

Then ask via `AskUserQuestion`:
> "Set this as the active feature?"
> Options: "Yes, update active.md" | "No, keep current feature active"
