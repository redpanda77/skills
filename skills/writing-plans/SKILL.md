---
name: writing-plans
description: Write, structure, or audit a project improvement plan. Use when the user asks to create a plan, write a P0N or K0N, set up an improvement plan, or structure a phased execution plan. Covers plan naming, directory layout, goal.md structure, knockout files, progress tracking, and methodology enforcement.
---

# Core Principles

Plans are execution contracts, not wish lists.

- **Progressive disclosure:** Plan index first, then goal, then knockouts, then methodology.
- **Goal.md is the contract:** It defines scope, boundaries, mandatory steps, and completion criteria.
- **Knockouts (KOs) are the work:** Each KO is an independent slice that can be executed, validated, and merged.
- **Deviation tracking is mandatory:** Blockers go in DEVIATIONS.md, not in memory.

## Workflow

1. **Determine plan type** — Reorganization, theming, feature, or audit. See `references/plan-types.md`.
2. **Create directory** — `docs/plans/P{NN}-<name>/`. See `references/registry-structure.md` for the root README.
3. **Write goal.md** — The execution contract. See `references/goal-structure.md`.
4. **Write methodology.md** — The 7-step protocol. See `references/methodology-structure.md`.
5. **Write knockout files** — One per independent task. See `references/ko-structure.md`.
6. **Write index.md** — The plan index with progress tracker. See `references/index-structure.md`.
7. **Audit before executing** — See `references/audit-checklist.md`.

## Directory Structure

```
docs/plans/
├── README.md                           # Registry of all plans
├── P{NN}-<name>/
│   ├── index.md                        # Plan index with KO links and progress tracker
│   ├── goal.md                         # Execution contract
│   ├── methodology.md                  # Execution protocol
│   ├── P{NN}-AUDIT.md                  # Current state audit (if applicable)
│   ├── P{NN}-K{NN}-<description>.md    # Individual knockout files
│   ├── P{NN}-DEVIATIONS.md             # Blocker tracker
│   └── P{NN}-PHASED-APPROACH.md        # Phase dependencies and execution order
```

## Key References

| Topic | File |
|-------|------|
| Goal.md template | `references/goal-structure.md` |
| Knockout file template | `references/ko-structure.md` |
| Plan index template | `references/index-structure.md` |
| Methodology (7-step protocol) | `references/methodology-structure.md` |
| Registry README | `references/registry-structure.md` |
| Enforcement documents | `references/enforcement-structure.md` |
| Plan types | `references/plan-types.md` |
| Audit checklist | `references/audit-checklist.md` |
