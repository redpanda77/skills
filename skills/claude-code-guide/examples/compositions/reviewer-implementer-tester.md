# Composition: reviewer → implementer → tester

**Intent:** keep noisy exploration and test output out of the main thread while preserving human steering.

## Flow

1. **Main:** states feature goal, constraints, and acceptance checks.
2. **Reviewer (read-only):** inspects current code and risks before edits.
3. **Implementer:** applies minimal diffs; returns file list + rationale.
4. **Tester / test-runner agent:** runs targeted tests; returns failures with excerpts.
5. **Main:** decides merge readiness and any follow-up spikes.

## When this works

- Medium-sized features with clear test commands.
- Teams that want independent review passes.

## Pitfalls

- Over-chaining without human checkpoints on high-risk migrations.
- Reviewer scope too broad → slow and shallow; narrow the prompt per hop.

See `references/agent-composition-patterns.md` for parallel review variants.
