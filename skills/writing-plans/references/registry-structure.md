# Registry Structure

The `docs/plans/README.md` is the canonical registry of all plans in a project. It is the single source of truth for what plans exist, their status, and where to find them.

## Structure

```markdown
# Project Plans

This directory contains implementation plans for major structural and design improvements.

## Plans

| ID | Name | Status | Description |
|---|---|---|---|
| P01 | [Name](P01-name/index.md) | In Progress | Brief description |
| P02 | [Name](P02-name/index.md) | Ready | Brief description |

## Plan Naming Convention

- `P{NN}` — Plan ID (e.g., P01, P02)
- `K{NN}` — Knockout (task within a plan)
- Stored in `docs/plans/P{NN}-<name>/`
- Each plan has an `index.md` with the full plan and links to sub-tasks

## Adding a New Plan

1. Create directory: `docs/plans/P{NN}-<name>/`
2. Write `index.md` with goal, phases, and exit criteria
3. Write detailed task files as needed
4. Update this README
5. Open a plan PR for review

## Plan Status

| Status | Meaning |
|---|---|
| Draft | Plan written but not reviewed |
| Ready | Reviewed and approved, ready to execute |
| In Progress | Actively being implemented |
| Complete | All phases done, validated, merged |
| Archived | Superseded by another plan |
```

## Rules

- Every plan must be listed in the registry
- The registry must be the first file a developer reads when looking for plans
- Status must be kept current as plans progress
- The registry must define the plan naming convention
- The registry must define the plan status values
- The registry must define the process for adding a new plan
