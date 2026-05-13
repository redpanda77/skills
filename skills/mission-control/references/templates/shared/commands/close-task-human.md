---
description: Close a completed task in a human-in-the-loop project. Verifies outputs exist and notes are written, updates state and PLAN.md, writes closure record. Human runs this after reviewing the task's output.
---

Close task $ARGUMENTS (or current task from `.mission-control/state.json` if not specified).

This command is for **human-in-the-loop projects**. The human runs it after reviewing the task's output — the agent does not close tasks autonomously.

For autonomous loop projects, use the standard `close-task.md` template instead.

## Steps

1. **Identify task.** Use $ARGUMENTS if provided, else read `current_task` from `.mission-control/state.json`.

2. **Read task from PLAN.md.** Extract:
   - Outputs list
   - Acceptance criteria (every `- [ ]` item)
   - Closure contract requirements

3. **Verify each acceptance criterion:**
   - For each output file listed: check it exists and is non-empty (`[ -s path/to/file ]`)
   - For each `- [ ]` item: determine whether it is satisfied (file exists, row count reasonable, no key NULLs)
   - If Notes section is empty: **stop**. Tell the user: "The Notes section for [TASK_ID] in PLAN.md must be filled in before closing. Add observations, row counts, anomalies, or a brief summary of what was found."
   - If any criterion is not met: **stop**. Report which criteria failed. Do not close the task.

4. **Update PLAN.md:**
   - Change `Status: open` → `Status: closed`
   - Check all acceptance criteria checkboxes
   - Add `Closed at: [ISO timestamp]`

5. **Update `.mission-control/state.json`:**
   - `last_completed_task` → this task ID
   - `current_task` → next open task in PLAN.md (within the same phase, or first task of next phase if phase is complete)
   - `last_verification` → current timestamp
   - `last_verification_result` → "pass"
   - If this was the last task in a phase: update `current_phase`

6. **Write closure record** to `.mission-control/closure-records/[TASK_ID]-closure.json`:
   ```json
   {
     "task_id": "[TASK_ID]",
     "task_name": "[task name]",
     "closed_at": "[ISO timestamp]",
     "outputs": ["[list of output file paths]"],
     "acceptance_criteria_met": ["[list of verified criteria]"],
     "notes_summary": "[one sentence from the Notes section]"
   }
   ```

7. **Check phase gate.** If this was the last task in the current phase:
   Print: "Phase [N] complete. All tasks closed. Next phase: [phase name]. Suggest running `/session-start` to orient for the new phase."

8. **Confirm.** Print: "Task [TASK_ID] closed. Next task: [NEXT_TASK_ID] — [task name]."

   Do **not** automatically begin work on the next task. Wait for the user to confirm.
