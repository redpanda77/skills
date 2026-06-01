# Planning vs Content Boundaries

## Principle

Planning artifacts are routing and grouping contracts. Canonical artifacts are the detailed output that agents produce one unit at a time.

Plans must not preview or generate the detailed content that later workers create.

## The Core Mistake

```text
plan artifact != canonical content artifact
plan context pack != raw evidence dump
judge context pack != full downstream preview
```

When a plan contains canonical content, the agent that receives it will:
- Try to reason about the whole pipeline instead of its bounded task
- Re-read and get confused by contradictory detail levels
- Drift into content generation during a planning phase
- Produce oversized, unfocused output

## Correct Layer Responsibilities

### Tier N Plan

Purpose: define grouping, ordering, and boundaries for Tier N units.

Allowed:
- `id`, `title`
- `members` (list of upstream unit IDs)
- `goal` or `communicative_goal`
- `boundary_rationale`
- `risk_flags`
- `review_obligations`
- compact feasibility seeds (if needed for grouping logic)

Not allowed:
- `member_details` or nested full objects
- full content snippets
- dialogue content
- exercise design
- examples
- canonical content fields
- element assignments

### Canonical Unit (Tier N)

Purpose: generate one complete, detailed output unit.

Allowed:
- detailed metadata objects
- full content (examples, dialogues, exercise material)
- source evidence
- state deltas if required by schema

Generated one target at a time:
```text
U001
U002
...
```

### Tier N+1 Plan

Purpose: group Tier N units into larger units.

Allowed:
- `id`, `title`
- `members` (list of Tier N unit IDs)
- `session_goal` or `scope_goal`
- `review_obligations`
- `load_summary`
- `boundary_rationale`
- `risk_flags`

Not allowed:
- `member_details`
- dialogue frames
- content lists
- exercise tasks
- canonical content

### Tier N+1 Canonical Unit

Purpose: generate one complete, detailed larger unit.

Allowed:
- speech acts
- frames
- review structure
- examples
- dialogues
- exercise material
- state deltas if needed

Generated one target at a time:
```text
S001
S002
...
```

## Required Prompt Changes

Every plan worker prompt must include an explicit negative contract:

```text
Write only a grouping contract. Do not write examples, dialogue, exercises,
member_details, or canonical content.
```

Every canonical worker prompt must include an explicit positive contract:

```text
Generate one complete unit. Include all required content: examples, dialogues,
exercises, and illustrations as specified by the schema.
```

## Validation

Plan validators must reject downstream content fields. The deterministic validator is the enforcement layer:

- `validate_plan.py` must reject `member_details`, examples, dialogues, exercises
- `validate_canonical.py` must check for required content fields
- If a plan artifact contains canonical content, the pipeline fails hard
