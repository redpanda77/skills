# Judge vs Validation

**Decision rule:** Could a non-expert with a regex pass this check?
- **Yes** → Validation script
- **No** → Judge subagent

## What goes where

| Validation | Judge |
|------------|-------|
| Tests pass, files exist, schema valid | Content quality, naturalness, semantic fit |
| No tampering, no blockers | Intent satisfaction, architecture consistency |
| Typecheck, lint | Security beyond static analysis |

## Rules

- No qualitative heuristics in scripts. No exceptions.
- A heuristic in a script is either trivial (adds no value) or complex (breaks on edge cases). Either way, it belongs to the judge.
- The worker invokes `/run-judge`, which spawns the judge subagent.
- The judge writes JSON verdicts; `done-check.sh` reads them.
- Judge output is authoritative. No script rewrites it.
- Invoke `write-a-skill` for detailed judge design. Never design judges manually.
