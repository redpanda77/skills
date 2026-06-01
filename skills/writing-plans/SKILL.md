---
name: writing-plans
description: Write, structure, or audit a project improvement plan. Use when the user asks to create a plan, write a P0N or K0N, set up an improvement plan, or structure a phased execution plan. Covers plan naming, directory layout, goal.md structure, knockout files, progress tracking, and methodology enforcement.
---

# Core Principles

Plans are execution contracts, not wish lists. Every plan must be actionable, bounded, and verifiable.

- **Progressive disclosure:** Plan index first, then goal, then knockouts, then methodology.
- **Goal.md is the contract:** It defines scope, boundaries, mandatory steps, and completion criteria.
- **Knockouts (KOs) are the work:** Each KO is an independent slice that can be executed, validated, and merged.
- **Methodology is the how:** Every KO must follow the same execution protocol (baseline, classify, map, change, verify, ledger, repeat).
- **Progress tracker is the source of truth:** Mutable table checked before and after each KO.
- **Deviation tracking is mandatory:** Blockers go in DEVIATIONS.md, not in memory.

---

# When Asked to Write a Plan

## 1. Determine Plan Type

- **Reorganization / Refactor** → See references/reorganization-plan.md
- **Theming / Design System** → See references/theming-plan.md
- **Feature Development** → See references/feature-plan.md
- **Audit / Remediation** → See references/audit-plan.md

## 2. Create Directory Structure

```
docs/plans/
├── README.md                           # Registry of all plans
├── P{NN}-<name>/
│   ├── README.md (or index.md)         # Plan index with KO links and progress tracker
│   ├── goal.md                         # Execution contract
│   ├── methodology.md                  # Execution protocol
│   ├── P{NN}-AUDIT.md                  # Current state audit (if applicable)
│   ├── P{NN}-FINDINGS.md               # Deep audit findings (if applicable)
│   ├── P{NN}-K{NN}-<description>.md  # Individual knockout files
│   ├── P{NN}-DEVIATIONS.md             # Blocker tracker
│   └── P{NN}-PHASED-APPROACH.md        # Phase dependencies and execution order
```

## 3. Write the Registry (README.md)

```markdown
# Project Plans

## Plans

| ID | Name | Status | Description |
|---|---|---|---|
| P01 | [Name](P01-name/index.md) | Ready | Brief description |

## Plan Naming Convention

- `P{NN}` — Plan ID (e.g., P01, P02)
- `K{NN}` — Knockout (task within a plan)
- Stored in `docs/plans/P{NN}-<name>/`
- Each plan has an `index.md` with goal, phases, and exit criteria

## Adding a New Plan

1. Create directory: `docs/plans/P{NN}-<name>/`
2. Write `index.md` with goal, phases, and exit criteria
3. Write detailed task files as needed
4. Update this README
5. Open a plan PR for review
```

## 4. Write the Execution Contract (goal.md)

Use the standard structure. See references/goal-structure.md for the full template.

```text
<goal>          → What success looks like
<context>       → Repository, important files, reference patterns, known state
<scope>         → Phase-by-phase allowed/not-allowed changes
<mandatory_first_steps> → What to read before starting
<progress_tracking>     → How to use the tracker
<refactoring_protocol>  → The 7-step execution protocol
<implementation_requirements> → Hard rules for the agent
<deletion_safety_gate>  → Required ledger before any deletion
<verification_requirements> → Commands to run before completion
<completion_contract>   → When the agent may stop
<final_response_format> → Required output format
```

## 5. Write the Methodology (methodology.md)

The 7-step protocol:

```text
1. Baseline — Record git status, run narrowest check, document pre-existing failures
2. Classify — Label each step: mechanical, boundary, or behavioral
3. Map Impact — Run impact analysis for files with >5 consumers
4. Change — One coherent move at a time, update imports in the same change set
5. Verify — Run narrowest check after each high-blast-radius change
6. Ledger — Record moved, merged, deleted paths with evidence
7. Repeat — Until KO acceptance criteria pass
```

## 6. Write Knockout Files (P{NN}-K{NN}-*.md)

Each KO file must contain:

```markdown
# P{NN}-K{NN}: <Title>

> **Type:** Mechanical move | Boundary refactor | Placement decision | Behavioral
> **Guarantee:** What is preserved (e.g., "No business logic changes")

## Problem
What is wrong and why it matters.

## Why It Matters
Impact on the codebase, developers, or users.

## Deep Audit Findings
Specific findings with file paths and evidence.

## Files To Audit And Change
| Source | Target | Notes |
|--------|--------|-------|
| `old/path` | `new/path` | Classification |

## Target Architecture
Directory tree after the KO.

## Plan
Phase-by-phase execution steps.

## Validation
Exit criteria and commands to run.

## Risks
What could go wrong and how to mitigate.

## Expected Outcome
What the codebase looks like after completion.

## Deletion Ledger
| Path | Action | Replacement | Reference Check | Validation |
|------|--------|-------------|-----------------|------------|
```

## 7. Write the Plan Index (index.md)

```markdown
# P{NN}: <Plan Name>

## Design Principles
1. **Principle name** — Description

## Scoring Model
| Priority | ID | Issue | Effort | Impact | Complexity | RICE | Plan |

## Execution Spine / Progress Tracker
| Done | Status | Phase | KO | Plan | Goal | Exit Gate |
|------|--------|-------|----|------|------|-----------|
| [ ] | Pending | Phase 1 | P{NN}-K01 | [link](...) | Brief goal | Exit criteria |

## KO Classification
### Mechanical Move | Boundary Refactor | Placement Decision

## Suggested Execution Order
1. Phase 1 — ...
2. Phase 2 — ...

## Enforcement Documents
- [methodology.md](methodology.md) — Execution protocol
- [enforcement.md](enforcement.md) — Tool-specific rules

## Plan Readiness Gate
What must be true before implementation begins.
```

---

# Key References

- `references/goal-structure.md` — Full goal.md template with all sections
- `references/ko-structure.md` — Knockout file template
- `references/index-structure.md` — Plan index template
- `references/methodology-structure.md` — Methodology and 7-step protocol
- `references/registry-structure.md` — Plans README.md template
- `references/enforcement-structure.md` — Enforcement documents
- `references/plan-types.md` — Plan types: reorganization, theming, feature, audit
- `references/audit-checklist.md` — What to audit per plan type (tools, commands, severity)
