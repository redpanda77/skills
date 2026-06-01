# Plan Index Structure

The `index.md` (or `README.md`) is the master plan document. It contains the goal, phases, KO links, progress tracker, and design principles.

## Required Sections

### Header

```markdown
# P{NN}: <Plan Name>

Date: YYYY-MM-DD

Goal: One-sentence summary of the plan.
```

### Source Documents

```markdown
## Source Documents

| Document | Purpose |
|---|---|
| P{NN}-AUDIT.md | Full audit of current state |
| P{NN}-DESIGN.md | Design system inventory |
| P{NN}-COVERAGE-MAP.md | Traceability from audit to phases |
```

### Structural Documents

```markdown
## Structural Documents

| Document | Purpose |
|---|---|
| P{NN}-GOAL.md | Execution contract |
| P{NN}-METHODOLOGY.md | Execution protocol |
| P{NN}-PHASED-APPROACH.md | Phase dependencies and execution order |
| P{NN}-DEVIATIONS.md | Blocker tracker |
```

### Design Principles

```markdown
## Design Principles

1. **Principle name** — Description
2. **Principle name** — Description
```

### Scoring Model

```markdown
## Scoring Model

| Priority | ID | Issue | Effort | Impact | Complexity | RICE | Plan |
|---|---|---|---:|---:|---:|---:|:---|
| 1 | P{NN}-K01 | Foundation | 35 | 85 | 25 | 90 | [link](...) |
| 2 | P{NN}-K02 | Feature extraction | 40 | 80 | 35 | 76 | [link](...) |
```

### Execution Spine / Progress Tracker

```markdown
## Execution Spine / Progress Tracker

Use this table as the mutable progress tracker. Before checking off a KO, read the linked plan file and confirm its validation section passes.

| Done | Status | Phase | KO | Plan | Goal | Exit Gate |
|---|---|---|---|---|---|---|
| [ ] | Pending | Phase 1 | P{NN}-K01 | [link](...) | Brief goal | Exit criteria |
| [ ] | Pending | Phase 1 | P{NN}-K02 | [link](...) | Brief goal | Exit criteria |
| [ ] | Pending | Phase 2 | P{NN}-K03 | [link](...) | Brief goal | Exit criteria |
```

### KO Classification

```markdown
## KO Classification

### Mechanical Move (90% scripted moves, 10% classification)

| KO | Issue | Why It's Mechanical |
|---|---|---|
| **P{NN}-K01** | Foundation — merge root-level components | Mostly path changes |

### Placement Decisions (requires judgment)

| KO | Issue | Why It Needs Judgment |
|---|---|---|
| **P{NN}-K02** | Hook reorganization | Hooks must be classified before moving |

### Boundary Refactor

| KO | Issue | What It Establishes |
|---|---|---|
| **P{NN}-K03** | Feature extraction | Splits feature code from shared code |
```

### Suggested Execution Order

```markdown
## Suggested Execution Order

1. **Phase 1 — Mechanical moves** (P{NN}-K01, P{NN}-K02)
2. **Phase 2 — Boundary refactors** (P{NN}-K03, P{NN}-K04)
3. **Phase 3 — Enforcement** (P{NN}-K05)
4. **Phase 4 — Cleanup + validation** (P{NN}-K06)
```

### Enforcement Documents

```markdown
## Enforcement Documents

- [methodology.md](methodology.md) — Execution protocol
- [enforcement.md](enforcement.md) — Tool-specific rules
```

### Final Phase

```markdown
## Final Phase

After all KOs have landed, verify:
- `find app -mindepth 1 -maxdepth 2 -type d` shows expected structure
- No stale directories remain
- All validation commands pass
```

### Plan Readiness Gate

```markdown
## Plan Readiness Gate

Before implementation begins:
- Run baseline checks
- Capture outputs for all validation commands
- Confirm every KO is ready
```

## Rules

- The index is the single source of truth for plan progress
- The progress tracker table must be updated after every KO
- Status values: `Pending`, `In Progress`, `Blocked`, `Ready For Review`, `Done`
- The index must link to every KO file
- The index must contain the suggested execution order
- The index must contain the plan readiness gate
