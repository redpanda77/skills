# State Tracking

All mission control runtime state lives in `.mission-control/` inside the project. This is the source of truth for the current execution, separate from the task definitions in PLAN.md.

## Folder structure

```
.mission-control/
  state.json                    current execution state
  judge-rubric.md               evaluation rubric (readable by worker and judge)
  judge-verdicts/
    T001.json                   verdict for each judged task
    T002.json
    latest.json                 copy of the most recent verdict
  closure-records/
    T001-closure.json           evidence snapshot when task was closed
    T002-closure.json
  session-log.md                running log of significant events (optional)
```

Add `.mission-control/` to `.gitignore` if you don't want runtime state in version control. Or commit it if you want verdicts and closure records durable across machines.

---

## state.json schema

Written and updated by the worker Claude throughout execution. Read by `done-check.sh` and hooks.

```json
{
  "objective": "Refactor auth middleware to use JWT",
  "current_task": "T003",
  "last_completed_task": "T002",
  "last_verification": "2024-01-15T10:30:00Z",
  "last_verification_result": "pass",
  "session_name": "mission-control-auth-refactor",
  "judge_required": true,
  "judge_trigger": "per-task",
  "judge_confidence_threshold": 0.70,
  "last_judge_task": "T002",
  "last_judge_verdict": "pass",
  "blockers": []
}
```

**When to update state.json:**
- On session start: set `session_name`, confirm `current_task`
- After completing a task: update `current_task` and `last_completed_task`
- After validation: update `last_verification` and `last_verification_result`
- After judge run: update `last_judge_task` and `last_judge_verdict`
- When a blocker is hit: push to `blockers` array with description

Worker Claude is responsible for keeping this current. The `session-start-reminder.sh` hook includes a reminder to read and update it.

---

## Judge verdict schema (.mission-control/judge-verdicts/T002.json)

```json
{
  "task_id": "T002",
  "timestamp": "2024-01-15T10:45:00Z",
  "verdict": "pass",
  "confidence": 0.87,
  "judge_types_run": ["correctness", "test_quality"],
  "must_fix": [],
  "should_fix": [
    "Consider adding a test for token refresh edge case"
  ],
  "evidence": [
    "TokenService.verify() correctly throws TokenExpiredError for expired tokens (line 47)",
    "Tests cover happy path, expired token, and malformed token cases"
  ],
  "concerns": []
}
```

---

## Closure record schema (.mission-control/closure-records/T002-closure.json)

Snapshot of evidence when a task was closed. Complements CLOSED_TASKS.md (which is human-readable) with a machine-readable record.

```json
{
  "task_id": "T002",
  "task_name": "Add TokenService class",
  "closed_at": "2024-01-15T10:50:00Z",
  "closed_at_commit": "a3f92bc",
  "acceptance_criteria_met": [
    "src/auth/token.ts created",
    "TokenService.create(userId) returns signed JWT",
    "TokenService.verify(token) returns userId or throws",
    "npm test passes"
  ],
  "test_files_added": [
    "tests/auth/token.test.ts"
  ],
  "validation_result": "pass",
  "judge_verdict": "pass",
  "judge_confidence": 0.87,
  "invariants": [
    "TokenService.create() returns a JWT with exp claim",
    "TokenService.verify() throws for expired tokens, not returns null"
  ]
}
```

---

## How done-check.sh reads state

```bash
# Read state
STATE_FILE=".mission-control/state.json"

if [ -f "$STATE_FILE" ]; then
  JUDGE_REQUIRED="$(jq -r '.judge_required // false' "$STATE_FILE")"
  JUDGE_THRESHOLD="$(jq -r '.judge_confidence_threshold // 0.70' "$STATE_FILE")"
fi

# Check judge verdict if required
if [ "$JUDGE_REQUIRED" = "true" ]; then
  VERDICT_FILE=".mission-control/judge-verdicts/latest.json"

  if [ ! -f "$VERDICT_FILE" ]; then
    echo "Judge verdict required. Run /run-judge."
    exit 1
  fi

  # Check verdict is current (not stale from a previous task)
  CURRENT_TASK="$(jq -r '.current_task' "$STATE_FILE" 2>/dev/null)"
  JUDGED_TASK="$(jq -r '.task_id' "$VERDICT_FILE" 2>/dev/null)"

  if [ "$JUDGED_TASK" != "$CURRENT_TASK" ]; then
    echo "Judge verdict is stale (judged $JUDGED_TASK, current task is $CURRENT_TASK). Run /run-judge."
    exit 1
  fi

  VERDICT="$(jq -r '.verdict' "$VERDICT_FILE")"
  CONFIDENCE="$(jq -r '.confidence' "$VERDICT_FILE")"

  if [ "$VERDICT" != "pass" ]; then
    echo "Judge: $VERDICT"
    jq -r '.must_fix[]?' "$VERDICT_FILE"
    exit 1
  fi
fi
```

---

## Session log (optional)

`.mission-control/session-log.md` is a running append-only log of significant events. The worker appends to it at key moments. Useful for post-run review and for recovery after context loss.

Format:
```markdown
# Session Log

## 2024-01-15T09:00:00Z — Session started
Objective: Refactor auth middleware to use JWT
Current task: T001

## 2024-01-15T09:25:00Z — T001 closed
Commit: abc1234
Validation: pass
Notes: Found existing auth.ts uses session-based auth. T002 will need to modify login endpoint.

## 2024-01-15T10:45:00Z — T002 judge run
Verdict: pass (confidence: 0.87)
Judge types: correctness, test_quality

## 2024-01-15T10:50:00Z — T002 closed
Commit: a3f92bc
Validation: pass, Judge: pass
```

The worker appends entries using the `/mc-status` local skill or manually in the closure flow.
