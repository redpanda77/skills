# Typed Context Packs

Context packs are typed evidence surfaces. They are not dumps.

## The Standard Top-Level Shape

Every context pack must have exactly this structure:

```json
{
  "schema_version": "context_pack_v2",
  "pack_kind": "plan_worker | plan_grouping_judge | unit_judge | batch_judge | scope_judge",
  "project": "project_name",
  "target": "artifact_name",
  "input_hashes": {},
  "task": {},
  "rows": [],
  "indexes": {},
  "risks": [],
  "validation": null,
  "output_contract": {},
  "context_pack_hash": "..."
}
```

No other root keys are allowed.

## Pack Kinds

| Kind | Purpose | Typical Budget |
|------|---------|---------------|
| `plan_worker` | Worker that generates a plan or grouping | 35 KB |
| `plan_grouping_judge` | Judge that evaluates plan grouping/sequencing | 35 KB |
| `unit_judge` | Judge that evaluates one canonical unit | 30 KB |
| `batch_judge` | Judge that evaluates a batch of related units | 45 KB |
| `scope_judge` | Judge that evaluates a full scope/tier/phase | 70 KB |

## The Row + Index Rule

Rows are the scan surface. Indexes hold reusable details once.

**Wrong:** embed the same entity repeatedly
```json
{
  "rows": [
    {
      "id": "S001",
      "title": "...",
      "unit_details": [ { "id": "U001", "full_object": "..." } ]
    }
  ]
}
```

**Right:** reference by ID, look up in index
```json
{
  "rows": [
    {
      "id": "S001",
      "title": "...",
      "units": ["U001", "U002"]
    }
  ],
  "indexes": {
    "units": {
      "U001": { "title": "...", "capability": "..." }
    }
  }
}
```

## Row Types (Examples)

### Plan Worker Row
```json
{
  "id": "P001",
  "title": "...",
  "members": ["U001", "U002"],
  "goal": "...",
  "boundary_rationale": "...",
  "risk_flags": []
}
```

### Unit Judge Row
```json
{
  "id": "U001",
  "title": "...",
  "element_load": 12,
  "capability": "...",
  "risk_flags": []
}
```

### Risk Case
```json
{
  "type": "future_dependency_leak",
  "severity": "fail",
  "target_ids": ["S001", "U003"],
  "evidence_refs": ["indexes.units.U003.example_seeds"],
  "message": "U003 requires elements first introduced in S002",
  "repair_hint": "Move U003 to S002 or later"
}
```

## Forbidden Patterns

- Unknown root keys
- Repeated embedded entities (`rows[].unit_details[] full objects`)
- Raw excerpts or large prose blocks in most packs
- Deep nesting beyond the allowed depth for the pack kind
- Arbitrary key-value dumps without schema

## File Organization Invariant

Context packs are organized on disk by phase and target. The path encodes the pack kind, target, and tier.

```
.context-packs/
  plan_worker/
    P001.json
  plan_grouping_judge/
    P001.json
  unit_judge/
    U001.json
    U002.json
  batch_judge/
    batch_S001.json
  scope_judge/
    scope_Tier1.json
```

Rules:
- The pack filename is the target ID plus `.json`
- The parent directory is the pack kind
- The renderer writes to the correct directory based on the pack kind
- The router reads from the correct directory when passing the pack to an agent
- The validator checks the pack at its path against the expected pack kind
- The ledger records the pack path, pack hash, and source hashes

## Validation Contract

Every renderer must:
1. Construct the pack as a typed object
2. Validate root keys against the allowed set
3. Validate schema version
4. Check size against the budget for the pack kind
5. Check nesting depth
6. Reject repeated embedded entities
7. Fail hard if any check fails — no silent trimming

Write the validation as a script, not a judge. Context pack shape is deterministic.
