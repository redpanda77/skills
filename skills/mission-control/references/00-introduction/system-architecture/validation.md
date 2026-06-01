# Validation

Deterministic checks that enforce mechanical correctness.

## Purpose

Verify that artifacts exist, schemas are valid, hashes match, coverage is complete, and no tampering occurred. Validation is the completion authority alongside the judge.

## Validation vs. Judging

**Decision rule:** Could a non-expert with a regex pass this check?
- **Yes** → Validation script
- **No** → Judge subagent

| Validation | Judge |
|------------|-------|
| Tests pass, files exist, schema valid | Content quality, naturalness, semantic fit |
| No tampering, no blockers | Intent satisfaction, architecture consistency |
| Typecheck, lint, coverage | Security beyond static analysis |

## The Validator Stack

```
done-check.sh (top-level authority)
  ├── validate-global.sh         → typecheck + lint + full test suite
  ├── validate-schema.sh         → schema conformance
  ├── validate-coverage.sh       → coverage completeness
  ├── validate-no-blockers.sh    → no open tasks, no blocked markers
  ├── validate-closed-tasks.sh   → regression tests (Tier 2+)
  ├── validate-no-tampering.sh   → no test weakening or config changes (Tier 2+)
  └── validate-context-pack.py   → typed context pack shape, budget, nesting
```

## Rules

- `done-check.sh` is the completion authority. It decides when work is done.
- `done-check.sh` calls sub-validators. It does not check anything itself.
- Validators must produce clear, actionable error messages on failure.
- Validators are silent on success.
- No qualitative heuristics in scripts. No exceptions.
- A heuristic in a script is either trivial (adds no value) or complex (breaks on edge cases). Either way, it belongs to the judge.

## Plan Minimalism Checks

Plan validators must reject canonical content fields:

- `member_details` or nested full objects
- `content_frames`, `content_snippets`
- `dialogues` or `interactions`
- `practice`, `examples`, `exercises`
- full metadata objects
- canonical content fields

## Context Pack Validation

Every renderer must validate packs before writing:

- Root key check: only allowed top-level keys
- Schema version check: `context_pack_v2`
- Budget check: hard max size per pack kind
- Nesting check: max depth per pack kind
- Repeated entity check: no embedded full objects in multiple places
- Raw excerpt check: no large prose blocks unless explicitly routed

## Failure Mode

If validation is broken:
- Bad artifacts pass silently
- Schema violations accumulate
- Tampering goes undetected
- The judge is asked to evaluate mechanically broken output
- Context packs grow unbounded

## Repair Authority

- Bad deterministic output shape → script/schema repair
- Validator false positive → fix the validator, not the artifact
- Context pack oversize → fix the renderer, not the validator
