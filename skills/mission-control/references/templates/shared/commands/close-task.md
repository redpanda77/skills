---
description: Run the full closure workflow for a task — verify acceptance criteria, run validation, run judge (if enabled), update tracking files, commit.
---

Close task $ARGUMENTS (or current task from .mission-control/state.json if not specified).

## Steps

1. **Identify task.** Use $ARGUMENTS if provided, else read `current_task` from `.mission-control/state.json`.

2. **Read task from PLAN.md.** Find the task section. Extract:
   - Acceptance criteria (every `- [ ]` item)
   - Closure contract requirements

3. **Verify each acceptance criterion.** For each item:
   - Run any implied command (test run, file existence check, grep)
   - Mark it satisfied or not
   - If any criterion is not met: stop. Fix it. Do not proceed to close the task.

4. **Run validation.** Run `./done-check.sh` (or `../agent-control/done-check.sh .` for external layout), skipping the judge check. If it fails: stop and fix.

5. **Run judge (if judge_required=true in .mission-control/state.json).** Run `/run-judge [TASK_ID]`.
   - fail → stop, address must_fix items, retry from step 3
   - blocked → stop, add BLOCKED_AGENT marker to PLAN.md Blockers section, report to user
   - pass → continue

6. **Update PLAN.md:**
   - Change `Status: open` → `Status: closed`
   - Check all acceptance criteria checkboxes
   - Add `Closed at: [timestamp] [commit TBD]`

7. **Update CLOSED_TASKS.md.** Add entry:
   ```markdown
   ## [TASK_ID]: [task name]
   Status: closed
   Closed at commit: [TBD — fill after commit]

   Acceptance:
   - [what was accepted]

   Protection:
   - [test files added or updated]

   Invariant:
   - [behavior that must not change unless explicitly reopened]

   Reopen Policy:
   - May only be reopened by an explicit task: `REOPEN [TASK_ID]: [task name]`
   ```

8. **Update validation-manifest.json.** Add entry:
   ```json
   {
     "id": "[TASK_ID]",
     "name": "[task name]",
     "status": "closed",
     "tests": ["[test file paths]"],
     "invariants": ["[invariant statements]"],
     "protected_files": ["[test file paths]"]
   }
   ```

9. **Update .mission-control/state.json:**
   - `last_completed_task` → this task ID
   - `current_task` → next open task in PLAN.md
   - `last_verification` → current timestamp
   - `last_verification_result` → "pass"

10. **Write closure record** to `.mission-control/closure-records/[TASK_ID]-closure.json`.

11. **Git commit:**
    ```
    git add -A
    git commit -m "Close [TASK_ID]: [task name]"
    ```
    Update PLAN.md and CLOSED_TASKS.md "Closed at commit" with the actual hash.

12. **Confirm and continue.** Print: "Task [TASK_ID] closed. Next task: [NEXT_TASK_ID]."
    Immediately begin work on the next open task. Do not stop.
