# Judge Layer

## The judge is always a subagent

The judge is spawned via the Agent tool from within Claude Code — not via a shell script calling `claude -p`. Never write a `run-judge.sh` that shells out to the CLI.

Why this matters:
- Shell scripts can't use the Agent tool
- CLI calls are fragile (heredoc escaping, no structured output guarantee, process spawning overhead)
- Subagents run in the same session context, have proper tool access, and return results cleanly
- The worker Claude is the one deciding to run the judge and handling the verdict — this should stay inside Claude Code, not move to a shell process

The correct flow:

```
Worker Claude (mid-task, before closing a task):
  → reads .mission-control/judge-rubric.md
  → reads task acceptance criteria from PLAN.md
  → runs tests, captures output
  → spawns judge subagent via Agent tool
       - gives it: rubric + diff + source files + test output + CLOSED_TASKS.md invariants
       - instructions: read-only, return strict JSON verdict only
  → receives verdict JSON
  → writes verdict to .mission-control/judge-verdicts/{TASK_ID}.json
  → reads verdict:
       fail → addresses must_fix items, re-runs judge
       blocked → stops, reports to user (do not retry without human review)
       pass → proceeds to close task

done-check.sh (called by Stop hook):
  → reads .mission-control/state.json
  → if judge_required=true: checks .mission-control/judge-verdicts/latest.json
  → if verdict != "pass": exits 1 with message "Run /run-judge before stopping"
```

The worker decides when to run the judge. The Stop hook only checks that a passing verdict exists.

---

## When you need a judge

Deterministic validation (tests, typecheck, lint) tells you the code is technically correct. A judge tells you whether it's actually right.

Use a judge when:
- The implementation could pass all tests but still miss the intent (overfitting visible tests)
- Test quality is uncertain — Claude may write tests that trivially pass
- Architecture or consistency decisions matter and can't be encoded as lint rules
- Security properties need review beyond static analysis
- Closed-task invariants could be conceptually undermined without breaking tests

Don't use a judge when:
- Test coverage is strong and the task is purely mechanical
- Acceptance criteria are fully verifiable by scripts
- The task is short enough that you'll review the output yourself

---

## Judge types

### Correctness judge
**Question:** Does the implementation satisfy the actual intent of the task — not just what was testable?

Checks:
- Does behavior match acceptance criteria as written, including edge cases the tests don't cover?
- Does the implementation handle all stated failure modes?
- Did the worker solve a simpler adjacent problem instead of what was asked?

Best trigger: every task closure

---

### Test quality judge
**Question:** Are the tests meaningful, or are they testing the implementation rather than behavior?

Checks:
- Do tests assert on observable behavior or internal details?
- Trivially passing assertions (`expect(true).toBe(true)`, `assert result is not None`)
- Happy paths only, with failure modes missing
- `.skip`, `xit()`, `xdescribe()` patterns silencing failures
- Tests that would pass even if the function returned a hardcoded value

Best trigger: any task that adds or modifies test files

---

### Regression guard judge
**Question:** Does this diff conceptually threaten closed-task invariants, even if their tests still pass?

Different from `validate-closed-tasks.sh` which re-runs tests. This judge reads the diff and the invariants from CLOSED_TASKS.md and asks: could this change break the behavior those tests were written to protect, in ways the tests might not catch?

Best trigger: any task whose diff touches shared code or files that closed tasks depend on

---

### Architecture judge
**Question:** Is the new code consistent with the codebase's existing patterns?

Checks:
- Naming conventions, folder structure, abstraction patterns
- New dependencies introduced — are they appropriate?
- Correct abstraction level
- Duplication suggesting a missing abstraction

Best trigger: tasks introducing new files, modules, or dependencies

---

### Security judge
**Question:** Are there exploitable patterns in the new code?

Checks (select relevant ones for your stack):
- SQL injection via string concatenation
- Command injection via shell exec with user input
- Unvalidated redirects
- Hardcoded secrets
- Missing authorization checks on new endpoints
- Exposed internal errors in responses
- Missing rate limiting on new endpoints

Best trigger: tasks adding endpoints, handling user input, touching auth or database code

---

## Trigger strategy

### Per-task
Run after every closure attempt. Best for: long tasks, weak test suite, Claude writing tests.
Tradeoff: adds latency per task. If judge takes 30s and there are 15 tasks, that's 7+ minutes.

### Per-increment
Run after logical groups (e.g. every 3–4 tasks). Define checkpoints in PLAN.md as synthetic tasks:
```markdown
### T005-JUDGE: Judge checkpoint for T001–T005
Status: open
Acceptance Criteria:
- [ ] Judge verdict is pass for T001–T005
```
Claude treats this as a real task and spawns the judge before marking it closed.

### Final only
One judge run before `done-check.sh` can pass. Simplest. Best for: short tasks, strong tests.

### Recommendation

| Duration | Test confidence | Trigger |
|----------|----------------|---------|
| < 1 hr | Good | Final only |
| 1–3 hrs | Good | Per-increment (every 3–4 tasks) |
| 1–3 hrs | Partial/weak | Per-task |
| 3+ hrs | Any | Per-task for critical, per-increment for mechanical |

---

## The /run-judge local skill

Rather than a shell script, the judge workflow lives as a local slash command: `.claude/commands/run-judge.md`.

The worker invokes it with `/run-judge T002` (or whatever task ID).

Template for `.claude/commands/run-judge.md`:

```markdown
---
description: Spawn the judge subagent to evaluate the current task's implementation
---

Run the judge for task $ARGUMENTS (or current task if not specified).

## Steps

1. Identify task ID: use $ARGUMENTS if provided, otherwise read current task from .mission-control/state.json

2. Read task context from PLAN.md — find the task section and extract:
   - Acceptance criteria
   - Closure contract requirements

3. Read judge rubric from .mission-control/judge-rubric.md

4. Read closed-task invariants from CLOSED_TASKS.md

5. Get the diff: run `git diff HEAD` (or `git diff HEAD~1 HEAD` if this task has been committed)

6. Run tests and capture output: [TEST_CMD] 2>&1 | tail -80 — continue even if tests fail

7. Identify the 3–5 source files most relevant to this task (from the diff)

8. Spawn the judge subagent with:

   Agent prompt:
   """
   You are a read-only validation judge. Do not edit any files. Do not suggest refactors
   beyond what the rubric requires. Do not trust commit messages or worker summaries.
   Evaluate the artifacts directly.

   Rubric:
   [contents of judge-rubric.md]

   Task being judged ([TASK_ID]):
   Acceptance criteria:
   [task acceptance criteria from PLAN.md]

   Closed-task invariants that must remain true:
   [contents of CLOSED_TASKS.md invariant sections]

   Git diff:
   [git diff output]

   Relevant source files:
   [file contents — 3–5 most relevant files]

   Test output:
   [test output]

   Instructions:
   - Check each assertion in added/modified test files for trivial-pass patterns
   - For each must_fix item: include file path, line number, specific issue, which requirement it violates
   - Return strict JSON only. No prose, no markdown outside the JSON.

   {
     "verdict": "pass|fail|blocked",
     "confidence": 0.0,
     "must_fix": [],
     "should_fix": [],
     "evidence": [],
     "concerns": []
   }
   """

9. Receive verdict JSON from subagent

10. Write verdict to .mission-control/judge-verdicts/[TASK_ID].json
    Also write to .mission-control/judge-verdicts/latest.json

11. Update .mission-control/state.json: set last_judge_task and last_judge_verdict

12. Interpret verdict:
    - pass (confidence ≥ 0.70): report pass, proceed
    - pass (confidence < 0.70): treat as fail — "Judge passed with low confidence ([score]). Treating as fail."
    - fail: display must_fix items clearly, do NOT close the task, continue fixing
    - blocked: display must_fix and concerns, stop and report to user — do not retry without human input
```

---

## Writing the rubric

Rubric lives at `.mission-control/judge-rubric.md`. This is inside the project but readable by both the worker (to understand expectations) and the judge subagent. 

If you want it truly private (worker cannot read it), use Tier 3 external layout and place it in `agent-control/` outside the project.

### Bad criteria (vague, inconsistent verdicts)
```
- Is the code readable?
- Are the tests good?
- Does this follow best practices?
```

### Good criteria (specific, falsifiable)

**Correctness:**
```
- Does TokenService.verify() throw a specific error (not return null) for expired tokens?
- Does the login endpoint return 401 (not 200 or 403) for invalid credentials?
- Is the error message for invalid credentials intentionally vague (to prevent user enumeration)?
```

**Test quality:**
```
- Is there a test for TokenService.verify() with an expired token (not just an invalid signature)?
- Are there any assertions that would pass if the function returned undefined (e.g. expect(result).toBeDefined())?
- Does the test file import the actual implementation, or does it mock the module under test?
```

**Architecture:**
```
- Does the new service follow constructor injection (not module-level singletons)?
- Are there any direct database calls in the controller layer?
- Does error handling use the project's AppError class or a new ad-hoc pattern?
```

**Security:**
```
- Is userId taken from the validated JWT payload, not from the request body?
- Are all new SQL queries parameterized?
- Does the new endpoint have the auth middleware applied?
```

### Rubric template

```markdown
# Judge Rubric

## Objective
[from PLAN.md]

## Active judge types
- [ ] Correctness
- [ ] Test quality
- [ ] Regression guard
- [ ] Architecture
- [ ] Security

## Correctness criteria
- [specific falsifiable statement]
- [specific falsifiable statement]

## Test quality criteria
- [specific test coverage requirement]
- Anti-patterns to flag: .skip, xit(), xdescribe(), expect(true), trivially-passing assertions

## Architecture criteria
- [specific consistency requirement]

## Regression guard
Invariants that must remain true (keep in sync with CLOSED_TASKS.md):
- [invariant]

## Security criteria
- [specific security property]

## Verdict guide
Pass: all active criteria met, confidence ≥ 0.70
Fail: any criterion not met, or confidence < 0.70
Blocked: implementation is fundamentally misaligned — fixing must_fix won't be enough; human needed

## Confidence threshold
0.70
```

---

## Wiring judge into done-check.sh

The Stop hook calls `done-check.sh`. Done-check reads the judge verdict file — it does not spawn the judge itself.

```bash
# In done-check.sh, after other validators:

if [ "${JUDGE_REQUIRED:-false}" = "true" ] || [ -f .mission-control/judge-rubric.md ]; then
  VERDICT_FILE=".mission-control/judge-verdicts/latest.json"

  if [ ! -f "$VERDICT_FILE" ]; then
    echo "Judge verdict required but not found. Run /run-judge before stopping."
    exit 1
  fi

  VERDICT="$(jq -r '.verdict' "$VERDICT_FILE" 2>/dev/null || echo 'none')"
  CONFIDENCE="$(jq -r '.confidence' "$VERDICT_FILE" 2>/dev/null || echo '0')"
  JUDGED_TASK="$(jq -r '.task_id' "$VERDICT_FILE" 2>/dev/null || echo 'unknown')"

  # Verdict must be for the current task, not a stale one
  CURRENT_TASK="$(jq -r '.current_task' .mission-control/state.json 2>/dev/null || echo '')"
  if [ -n "$CURRENT_TASK" ] && [ "$JUDGED_TASK" != "$CURRENT_TASK" ]; then
    echo "Judge verdict is stale (for $JUDGED_TASK, current task is $CURRENT_TASK). Run /run-judge."
    exit 1
  fi

  if [ "$VERDICT" != "pass" ]; then
    echo "Judge verdict: $VERDICT"
    jq -r '.must_fix[]?' "$VERDICT_FILE" 2>/dev/null
    exit 1
  fi

  if [ "$(echo "$CONFIDENCE < 0.70" | bc -l 2>/dev/null || echo 1)" = "1" ]; then
    echo "Judge passed with low confidence ($CONFIDENCE). Run /run-judge again or review manually."
    exit 1
  fi
fi
```

---

## Verdict semantics

**pass** — criteria met, confidence ≥ threshold. Done-check proceeds.

**fail** — criteria not met. Worker receives `must_fix` items and continues. Each item must be:
- Specific: file path + line number + issue
- Actionable: fixable in one focused change
- Bounded: > 5 must_fix items means the task scope is too large — consider splitting

**blocked** — implementation is fundamentally misaligned. Fixing must_fix items won't recover it. Worker reports to user and stops. Wrapper loop detects this as a distinct state (not a retry loop):

```bash
# In PLAN.md, when worker encounters blocked:
# Update PLAN.md Blockers section:
## Blockers
T002: BLOCKED — judge verdict. Reason: [summary of concerns]. Human review required.
```

This causes `validate-no-blockers.sh` to catch it, which propagates to done-check, which blocks the Stop hook — keeping the session open for human intervention.
