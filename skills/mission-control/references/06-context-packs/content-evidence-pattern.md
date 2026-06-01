# Content Evidence Pattern

IDs are anchors. Content is evidence. The pack must carry the right amount of semantic detail so the agent can make a decision without browsing raw artifacts.

## The Core Rule

**Row-local semantic evidence first. IDs only as anchors.**

The row must contain enough meaning for the agent to understand what it is deciding. The index must contain enough detail for the agent to verify claims. But neither should embed the full canonical content of downstream units.

## What Went Wrong Before

Old packs used one of these broken patterns:

### Pattern 1: ID-only rows
```json
{
  "rows": [
    {"id": "S001", "members": ["U001", "U002"]}
  ],
  "indexes": {
    "units": {
      "U001": {"title": "...", "elements": ["..."], "example_seeds": ["..."], "capability": "..."}
    }
  }
}
```

**Problem:** The agent must constantly cross-reference IDs to indexes. The row has no standalone meaning. This creates cognitive load and invites the agent to browse raw artifacts.

### Pattern 2: Full-content rows
```json
{
  "rows": [
    {
      "id": "S001",
      "members": ["U001", "U002"],
      "member_details": [
        {"id": "U001", "title": "...", "elements": ["..."], "example_seeds": ["..."], "capability": "..."}
      ]
    }
  ]
}
```

**Problem:** The same entity is embedded in multiple places. The pack is oversized. The agent sees repeated content and gets confused about authority.

### Pattern 3: Separate ID maps for everything
```json
{
  "rows": [...],
  "indexes": {
    "plans": {...},
    "rules": {...},
    "boundaries": {...},
    "units": {...}
  }
}
}
```

**Problem:** The agent must assemble meaning from scattered maps. The pack structure is optimized for machine lookup, not for agent comprehension.

## The Correct Pattern

Row-local semantic evidence, compact and meaningful. Indexes hold only what the agent needs to verify claims.

```json
{
  "rows": [
    {
      "id": "S001",
      "title": "Identity Exchange",
      "members": ["U001", "U002"],
      "goal": "Enable identity exchange after greetings.",
      "rule_ids": ["rule_04", "rule_06"],
      "element_load": 11,
      "boundary_rationale": "Groups identity-related units after greeting units.",
      "risk_flags": ["future_dependency_leak"]
    }
  ],
  "indexes": {
    "members": {
      "U001": {
        "title": "Identity And Possession",
        "elements": ["who", "possessive"],
        "example_seeds": ["who is she", "my teacher"],
        "capability": "Ask who someone is and state simple affiliation."
      }
    }
  },
  "risks": [
    {
      "type": "future_dependency_leak",
      "severity": "fail",
      "target_ids": ["S001", "U002"],
      "evidence_refs": ["indexes.members.U002.phrase_seeds"],
      "message": "U002 example seeds require elements first introduced in S002.",
      "repair_hint": "Move prerequisite unit before U002, or move U002 later."
    }
  ]
}
```

**What the agent sees:**
- The row is self-contained: goal, load, rationale, risks
- IDs are anchors for cross-reference and risk targeting
- The index provides compact evidence for verification
- The risk is typed, targeted, and actionable

## Row Content Rules

### What a row must contain

- **Identity:** `id`, `title`
- **Relationships:** `members` (upstream IDs), `parent` or `children` (downstream IDs)
- **Rationale:** `goal`, `boundary_rationale`, `scope_goal`
- **Load:** `element_load`, `rule_count`, `size_hint`
- **Flags:** `risk_flags` as strings, not full objects

### What a row must NOT contain

- Full member objects
- Full canonical content (examples, dialogues, exercises)
- Raw excerpts or large prose blocks
- Arbitrary key-value dumps

### What an index must contain

- Compact metadata for the entity: title, capability, element list, example seeds
- Only what is needed for the agent to verify claims in the row
- No full canonical content unless the pack kind explicitly allows it

## Alignment Between Renderer and Router

The renderer constructs the pack. The router passes it to the agent. The prompt the agent sees must match the pack shape.

**Wrong:** The renderer writes `rows` and `indexes`, but the router handoff says:
```
You will see plan_summary, audit_cases, and boundary_cases.
```

**Right:** The renderer writes `rows` and `indexes`, and the router handoff says:
```
You will see task, rows, indexes, risks, and validation.
```

The prompt, the pack, and the agent's expected fields must all use the same vocabulary. Any mismatch causes the agent to ignore the pack or browse raw artifacts.

## Migration Rules

When changing the pack shape:

1. **Update the renderer first** — it must produce the new shape
2. **Update the router handoff** — the prompt must reference the new fields
3. **Update the agent prompt** — the agent must know what fields to expect
4. **Regenerate one pack** — verify the new pack passes validation
5. **Do NOT bulk-regenerate closed packs** — existing judge hashes depend on the old pack content

Closed packs with old shapes remain valid. New packs use the new shape. The validator accepts both during migration, but the renderer only writes the new shape.

## Source Paths Rule

Every context pack must record the exact source files it was derived from:

```json
{
  "input_hashes": {
    "source_paths": [
      "source/elements.json",
      "source/rules.json"
    ],
    "source_hashes": {
      "source/elements.json": "sha256:abc...",
      "source/rules.json": "sha256:def..."
    }
  }
}
```

Rules:
- `source_paths` lists all source files that contributed to the pack
- `source_hashes` records the hash of each source file at the time the pack was rendered
- The ledger stores these hashes so it can detect stale packs
- A stale pack is one where the source hash no longer matches the current file
- Do not include the full source content in the pack. The path and hash are enough.

## Size Verification

After alignment, verify the pack is actually compact:

```bash
wc -l path/to/pack.json
wc -c path/to/pack.json
```

The hard budget is the maximum. A well-optimized plan grouping pack should be much smaller — under 120 lines and under 4 KB is achievable when the row-local evidence is disciplined.

If the pack is larger, the row is carrying too much. Trim the row-local evidence or move detail into the index.
