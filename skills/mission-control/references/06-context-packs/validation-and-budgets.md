# Validation and Budgets

## Context Pack Validation

Context packs are deterministic artifacts. Their validation belongs to scripts, not judges.

Add a validator that every renderer calls before writing:

```bash
python3 validate_context_pack.py \
  --input path/to/context_pack.json \
  --pack-kind plan_grouping_judge
```

## Required Checks

### Root Key Check

Allowed root keys only:

```text
schema_version
pack_kind
project
target
input_hashes
task
rows
indexes
risks
validation
output_contract
context_pack_hash
```

Unknown root keys fail.

### Schema Version Check

Only accepted current version:

```text
context_pack_v2
```

Legacy versions should fail for migrated renderers.

### Budget Check

Hard max size by pack kind:

| Pack Kind | Max Size |
|-----------|----------|
| `plan_worker` | 35 KB |
| `plan_grouping_judge` | 35 KB |
| `unit_judge` | 30 KB |
| `batch_judge` | 45 KB |
| `scope_judge` | 70 KB |

The renderer must fail if the pack exceeds budget.

No silent trimming after type construction unless the trimming is explicit, deterministic, and still passes validation.

### Nesting Check

Maximum nesting depth:

| Pack Kind | Max Depth |
|-----------|-----------|
| `plan_worker` | 4 |
| `plan_grouping_judge` | 4 |
| `unit_judge` | 4 |
| `batch_judge` | 4 |
| `scope_judge` | 5 |

Deep nested objects are a smell that the pack is copying artifacts rather than presenting evidence.

### Repeated Entity Check

The same logical entity must not be embedded in multiple places.

Examples that must fail:

```text
rows[].member_details[]
risks[].member full object
boundary_rows[].left.full_member
boundary_rows[].right.full_member
```

Allowed:

```text
target_ids: ["S003", "U009"]
evidence_refs: ["indexes.members.U009.phrase_seeds"]
```

### Raw Excerpt Check

Most packs must not include raw source excerpts.

Instead use compact spine rows:

```json
{
  "ref_id": "L04",
  "topic": "...",
  "element_summary": ["..."],
  "rule_summary": ["..."]
}
```

Raw excerpts may be allowed only for a specifically routed reference audit.

### Plan Minimalism Checks

Plan validators must reject canonical content fields:

- `member_details`
- `content_frames`
- `content_snippets`
- `dialogues`
- `exercises`
- `examples`
- full element metadata objects
- canonical content fields

## Tests

Required assertions:

- Migrated packs validate as `context_pack_v2`
- Migrated packs stay under budget
- Unknown root keys fail
- Repeated embedded child details fail
- Oversized packs fail
- Plan artifacts reject downstream content fields
- Risks remain represented as typed cases, not buried prose

## Failure Mode

When a pack fails validation:

1. The renderer fails hard
2. The pipeline stops
3. The developer fixes the renderer, not the validator
4. No trimming logic is added to make the validator pass

The validator is the contract. The renderer must conform to it.
