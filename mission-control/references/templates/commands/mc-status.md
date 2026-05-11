---
description: Show Mission Control status — current task, last verification, judge verdict, blockers.
---

Read and display current mission control state.

1. Read `.mission-control/state.json`
2. Read `PLAN.md` — count tasks by status
3. Read `.mission-control/judge-verdicts/latest.json` if it exists
4. Run `git log --oneline -3`

Print:

```
─────────────────────────────────────
Mission Control Status
─────────────────────────────────────
Objective : [objective]
Session   : [session_name]

Tasks     : [N closed] / [total] complete
  Current : [current_task] — [task name]
  Last    : [last_completed_task]

Validation: [last_verification_result] at [last_verification]

Judge     : [enabled / disabled]
  Last    : [verdict] (confidence: [confidence]) for [last_judge_task]

Blockers  : [none / list]

Recent git:
  [git log output]
─────────────────────────────────────
```

Then: state the single next action Claude should take.
