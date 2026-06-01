# Source and Graph

The evidence layer that feeds the entire pipeline.

## Purpose

Provide normalized, validated facts that the router and agents can reason about. Without this, the pipeline has no ground truth.

## What it is

- **Source** — raw input material (data catalogs, reference documents, external APIs, manually authored input)
- **Graph** — normalized, machine-readable projections of the source into nodes and edges
- **Indexes** — lookup tables that map IDs to compact metadata

## The Three-Layer Model

```
source evidence
  → normalized facts (deterministic scripts)
  → graph views (deterministic projections)
  → agent context (bounded packs)
```

## Source Rules

- Scripts normalize, validate, and route. They never cluster, group, title, or assign meaning.
- Source decides element legality; descriptors and references are inspiration evidence, not templates.
- Every planning and judging step compares against source evidence for calibration.

## Graph Views

Graph views are deterministic projections of accepted plans. They do not make qualitative decisions.

| View | Purpose |
|------|---------|
| Source graph | All facts, evidence, elements, prerequisites |
| Element graph | Where each element appears in the plan evidence |
| Rule graph | Where each rule or constraint is introduced |
| Capability graph | Which capabilities the plan claims to unlock |
| Scope graph | Coverage, prerequisites, and pacing for the whole scope |

## Context Efficiency

Every big thing needs three layers:

```
map   = small navigational index
unit  = bounded artifact for one decision
trace = large debug/provenance material, rarely opened
```

Agents should see the map and the unit, not the full graph or full project.

## Failure Mode

If source/graph is broken:
- Router has nothing to route
- Agents hallucinate or compensate by browsing raw artifacts
- Validation fails on legality checks
- The whole pipeline is built on sand

## Repair Authority

- Broken source legality → source/input/control repair
- Bad deterministic output shape → script/schema repair
- Never repair source by patching downstream artifacts
