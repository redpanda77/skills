# Composition: subagent with preloaded skills

**Intent:** the **agent owns behavior**; **skills inject conventions**.

## Pattern

```yaml
---
name: payments-implementer
description: Use when changing payment capture, refunds, or idempotency keys. Follows team payment conventions preloaded from skills.
skills:
  - payments-conventions
  - error-codes-catalog
tools: Read, Glob, Grep, Edit, Write, Bash
model: sonnet
---
```

Body prompt should say *how* to apply conventions (checklist, order of operations), not restate entire skill text.

## When to prefer this over `context: fork`

- Same specialized worker across many tasks.
- Conventions are reference material, not the full procedure.

See `references/skills-and-subagents.md`.
