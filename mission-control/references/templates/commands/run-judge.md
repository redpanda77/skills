---
description: Spawn the judge subagent to evaluate the current task's implementation. Returns pass/fail/blocked verdict.
---

Run the judge for task $ARGUMENTS (or current task from .mission-control/state.json).

## Steps

1. **Identify task ID.** Use $ARGUMENTS if provided, else read `current_task` from `.mission-control/state.json`.

2. **Read task acceptance criteria** from PLAN.md — the specific task section.

3. **Read judge rubric** from `.mission-control/judge-rubric.md`.
   (For Tier 3 external: `../agent-control/judge-rubric-private.md`)

4. **Read closed-task invariants** from CLOSED_TASKS.md — all `Invariant:` sections.

5. **Get diff:** `git diff HEAD` (or `git diff HEAD~1 HEAD` if task has been committed).

6. **Run tests and capture output:** `{{TEST_CMD}} 2>&1 | tail -80` — continue even if tests fail.

7. **Identify the 3–5 source files most relevant to this task** from the diff.

8. **Spawn judge subagent** using the Agent tool:

   Subagent prompt:
   ```
   You are a read-only validation judge. Do not edit any files.
   Do not suggest refactors beyond what the rubric requires.
   Do not trust commit messages or the worker's summaries — evaluate the artifacts directly.

   Rubric:
   [contents of judge-rubric.md]

   Task being judged ([TASK_ID]):
   Acceptance criteria:
   [task acceptance criteria from PLAN.md]

   Closed-task invariants that must remain true:
   [invariant sections from CLOSED_TASKS.md]

   Git diff:
   [git diff output]

   Relevant source files:
   [file contents — 3–5 most relevant files, complete not excerpted]

   Test output:
   [test output]

   Instructions:
   - Check each assertion in added or modified test files for trivial-pass patterns
     (expect(true), assert result is not None, hardcoded return values in mocks)
   - For each must_fix item: include file path, line number, specific issue,
     and which acceptance criterion or invariant it violates
   - Return strict JSON only. No prose. No markdown outside the JSON.

   {
     "task_id": "[TASK_ID]",
     "timestamp": "[ISO timestamp]",
     "verdict": "pass|fail|blocked",
     "confidence": 0.0,
     "judge_types_run": [],
     "must_fix": [],
     "should_fix": [],
     "evidence": [],
     "concerns": []
   }
   ```

9. **Receive verdict JSON** from subagent.

10. **Write verdict:**
    - `.mission-control/judge-verdicts/[TASK_ID].json`
    - `.mission-control/judge-verdicts/latest.json`

11. **Update state.json:** set `last_judge_task` and `last_judge_verdict`.

12. **Interpret and report:**

    **pass (confidence ≥ 0.70):** Report pass. Proceed with closure.

    **pass (confidence < 0.70):** Report: "Judge passed with low confidence ([score]). Treating as fail."
    Show concerns. Do not close the task — continue fixing and re-run judge.

    **fail:** Show must_fix items clearly. Do NOT close the task. Address each item and re-run judge.

    **blocked:** Show must_fix and concerns. Add entry to PLAN.md Blockers section:
    ```
    ## Blockers
    [TASK_ID]: BLOCKED_AGENT — judge verdict. [summary of concern]. Human review required.
    ```
    Stop and wait for human input.
