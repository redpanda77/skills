# Validators Setup

How to write validation scripts.

## What validators are

Deterministic scripts that check mechanical facts:
- Tests pass, files exist, schema is valid, no tampering

Validators do NOT judge quality. Quality is the judge's job.

## The stack

```
done-check.sh (top-level authority)
  ├── validate-no-blockers.sh    checks: no open tasks, no BLOCKED_AGENT markers
  ├── validate-global.sh         checks: typecheck + lint + full test suite
  ├── validate-closed-tasks.sh   checks: closed-task regression tests still pass (Tier 2+)
  ├── validate-no-tampering.sh   checks: no test weakening or config changes (Tier 2+)
  └── validate-context-pack.py   checks: typed context pack shape, budget, nesting (Tier 2+)
```

## Rules

- `done-check.sh` is the completion authority. It decides when work is done.
- `done-check.sh` calls sub-validators. It does not check anything itself.
- Validators must produce clear, actionable error messages on failure.
- Validators are silent on success.
- No qualitative heuristics in scripts. No exceptions.
- A heuristic in a script is either so trivial it adds no value, or so complex it breaks on edge cases. Either way, it belongs to the judge.
