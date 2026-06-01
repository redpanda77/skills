# State and Ledger

The tracking layer that remembers what passed, what failed, and what is next.

## Purpose

Prevent repeated work, stale artifacts, and lost progress. The state is derived by refresh scripts, not updated by agents directly.

## What it is

- **Delegation Ledger** — records of what agent was invoked for what target, with timestamps and hashes
- **Acceptance Manifest** — what artifacts passed validation and judging
- **Artifact Manifest** — what files exist, their hashes, and their provenance
- **Scope Registry** — current status of each scope (open, closed, blocked)
- **Current Status** — the router's view of the current state

## Rules

- Agents do not update router state. State is derived by refresh scripts.
- Closed scopes are immutable unless reopened through the router.
- Do not inspect derived diagnostics to dispute or bypass the router.
- Runtime files are observations, not authorities.
- A passing acceptance manifest closes a scope.

## Closed Batch Stability

Closed scopes are immutable. This includes closed batches, closed packs, and closed units.

Rules:
- Closed packs must not be bulk-regenerated. Regenerating them invalidates judge hashes and sends routing backward.
- Closed packs with old shapes remain valid. New packs use the new shape. The validator accepts both during migration.
- If a closed pack must change, it must be explicitly reopened through the router, not edited directly.
- The ledger records the exact hash of the pack that the judge evaluated. Any change to the pack requires re-judging.
- The source_paths in the ledger record which source files the pack was derived from. Changes to source files do not invalidate closed packs unless the pack is explicitly refreshed.

## State Hierarchy

```
Judge exists and passed
  → Judge wins, continue (unless mechanical validator fails)

Judge exists and failed
  → Judge wins, route repair from judge must_fix / concerns

Judge missing/stale/invalid
  → If precheck shows mechanical issue, route mechanical repair
  → If qualitative issue, delegate judge FIRST
```

## Failure Mode

If state is broken:
- The same task is repeated with unchanged inputs
- Passed upstream batches are recomputed when only a later target changed
- Stale generated files become accidental context
- The pipeline cannot resume after a crash

## Repair Authority

- Stale state → run refresh script, then re-run router
- Missing manifest → regenerate deterministically
- Corrupted ledger → audit from traces, rebuild from accepted artifacts
