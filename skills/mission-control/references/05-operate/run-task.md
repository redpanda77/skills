# Task Design

Good tasks make the control system work. Bad tasks make it fight you.

## What makes a bad task

- Too large: "Implement the auth system" — not a task, it's a project
- Uncheckable criteria: "Code should be clean" — done-check.sh can't verify this
- Missing closure contract: Claude marks it closed based on conversational memory
- Circular: "Fix any remaining issues" — infinite loop

## What makes a good task

- Verifiable outcome: the result either exists or doesn't
- Criteria are commands: `npm test`, `curl -s localhost:3000/health`
- Closure contract specifies evidence: test file added, command passes, artifact created
- One thing at a time: not "implement X and add tests and update docs"

## Sizing

| Time | Verdict |
|------|---------|
| < 5 min | Too small — merge |
| 10–45 min | Good |
| 45–90 min | Borderline — split |
| > 90 min | Too large — split |

## Closure contract

Must specify:
- Evidence required (test file, command, artifact)
- What must remain true (invariants)
- How to verify it (done-check.sh passes)

## Rules

- Uncheckable criteria go to the judge, not acceptance criteria
- Invoke `write-a-skill` for detailed task design patterns. Never design them manually.
