Read `.plan/features/$ARGUMENTS/tasks.md`. If $ARGUMENTS is empty, use the active feature from `.plan/active.md`.

Check if all tasks are in the Done section. If not, show the remaining tasks and ask via `AskUserQuestion`:
> "There are N incomplete tasks. Proceed anyway?"
> Options: "Yes, archive it" | "No, go back"

If proceeding:
1. Move `.plan/features/[feature]/` to `.plan/features/_archive/[feature]/`
2. Update `.plan/active.md`:
   - Remove the completed feature
   - If there are queued features, set the first one as active and remove it from the queue
   - Otherwise set `feature: none`

Tell the user the feature is archived and what (if anything) is now active.
