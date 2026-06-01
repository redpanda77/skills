# Context Packs and Scope Discipline

Why multi-agent systems break: context packs grow too large, agents try to do everything at once, and planning phases drift into content generation.

This reference documents the two disciplines that prevent that failure.

## The Two Principles

1. **Typed, Budgeted Context Packs** — every context pack is a typed evidence surface with a hard schema, hard size budget, and deterministic validation.
2. **Input/Output Scope Discipline** — broad-scope work (plans, grouping, judging) carries minimal detail; deep-scope work (canonical content) happens one unit at a time.

## When to apply

Apply this discipline when:
- An agent needs context from upstream agents to do its work
- A plan is being passed to a judge or worker
- Multiple agents collaborate on a multi-step pipeline
- Context packs are being constructed by a renderer or pre-processor

## What changes

- Renderers must validate packs before writing
- Packs must use `rows` + `indexes` instead of repeated nested objects
- Plan prompts must explicitly forbid content generation
- Validators must reject downstream content fields in plan artifacts
- Budgets are hard limits, not soft targets

## Files

- `typed-context-packs.md` — the schema standard and type system
- `planning-content-boundaries.md` — the exact boundary between plans and canonical content
- `input-output-scope.md` — the broad-vs-deep scope rule
- `validation-and-budgets.md` — hard validation rules and budget tables
- `content-evidence-pattern.md` — how to structure row-local evidence vs. indexes, ID alignment, and migration rules
