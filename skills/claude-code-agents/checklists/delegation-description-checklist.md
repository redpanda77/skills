# Delegation Description Checklist

A good subagent `description` says:

1. **When** to use the agent (trigger situation).
2. **What** kind of task it handles (scope).
3. **What output** it returns (format/depth).
4. **Boundaries** or exclusions (what it is not for).

## Bad

> "Reviews code."

## Better

> "Use after code changes when the user wants an independent review for correctness, regressions, missing tests, maintainability, and security-sensitive behavior. Returns findings grouped by severity with file references."

## Self-test

- Could a **different** engineer guess correct delegation from the description alone?
- Does it mention at least one **artifact** the parent receives (summary, table, file list)?
