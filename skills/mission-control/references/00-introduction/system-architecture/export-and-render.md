# Export and Render

The output materialization layer that produces the final deliverable.

## Purpose

Transform build artifacts into the consumer-facing or user-facing output. Build artifacts are evidence; export is the product.

## What it is

- **Render scripts** — deterministic scripts that assemble and format output
- **Export directory** — the final output location (`out/`, `export/`)
- **Materialization** — the process of combining canonical units, judge verdicts, and state into a coherent whole

## Rules

- Export is deterministic, not model-authored
- The export layer does not make qualitative decisions
- It assembles accepted canonical units and ledgers
- Human-readable output should be findable without opening build artifacts
- Build artifacts are evidence, not repair targets

## The Three-Layer Output Model

```
build/canonical/          ← bounded units, rarely opened by humans
build/plans/              ← grouping contracts, machine-readable
out/                      ← consumer-facing output, human-readable
```

## Failure Mode

If export is broken:
- No deliverable exists despite passed artifacts
- Build artifacts are invisible to humans
- Output format is inconsistent or incomplete
- Stale build artifacts are mistaken for final output

## Repair Authority

- Bad export format → render script repair
- Missing output → run materialization script
- Inconsistent formatting → deterministic script fix
