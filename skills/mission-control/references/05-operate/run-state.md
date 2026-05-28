# State Tracking

Runtime state lives in `.mission-control/`. This is the source of truth for current execution.

## Files

- `state.json` — current task, last verification, judge status
- `judge-verdicts/` — verdict per task (single or multi-judge)
- `closure-records/` — evidence snapshot when task closed
- `session-log.md` — running event log (optional)

## state.json

Written by the worker. Read by `done-check.sh` and hooks.

Key fields:
- `current_task` — what the worker is working on
- `last_completed_task` — last closed task
- `last_verification` — when done-check last ran
- `last_verification_result` — pass or fail
- `judge_required` — whether judge is enabled
- `blockers` — array of blocker descriptions

Update on:
- Session start: confirm `current_task`
- Task complete: update `current_task`, `last_completed_task`
- Validation: update `last_verification`, `last_verification_result`
- Judge run: update `last_judge_task`, `last_judge_verdict`
- Blocker: push to `blockers`

## Judge verdict

JSON with `verdict`, `confidence`, `principle_scores`, `must_fix`, `should_fix`.

Task passes only when every principle scores >= threshold.

## Closure record

Snapshot of evidence when task closed. Complements `CLOSED_TASKS.md` with machine-readable record.

## Rules

- Worker keeps `state.json` current
- Verdict files are authoritative — no script rewrites them
- Closure records are append-only
- Invoke `write-a-skill` for detailed state schemas. Never design them manually.
