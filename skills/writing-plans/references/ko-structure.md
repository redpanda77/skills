# Knockout (KO) Structure

Each KO file is an independent, executable slice of the plan. It can be executed, validated, and merged without depending on other KOs being complete.

## Required Sections

### Header

```markdown
# P{NN}-K{NN}: <Title>

> **Type:** Mechanical move | Boundary refactor | Placement decision | Behavioral
> **Guarantee:** What is preserved (e.g., "No business logic changes")
```

### Problem

What is wrong and why it matters. Be specific with file paths and counts.

```markdown
## Problem

The codebase has root-level `components/` (130 files) with no clear boundary between UI primitives, layout, and feature-specific code:
- `components/ui/` — 24 files (UI primitives)
- `components/layout/` — 5 files (App shell)
- `components/magicui/` — 2 files (decorative effects)
```

### Why It Matters

Impact on the codebase, developers, or users.

```markdown
## Why It Matters

- New files land in the wrong place because there is no clear rule
- Refactoring requires touching multiple directories for a single concept
- Root-level dumping ground makes navigation exhausting
```

### Deep Audit Findings

Specific findings with file paths, evidence, and ownership.

```markdown
## Deep Audit Findings

### 1. Dead artifacts
- `components/features/Card.tsx.new` — orphan backup file, no consumers
- Owned by P{NN}-K{NN} or P{NN}-K{NN+1}

### 2. Root clutter
- `app-initializer.tsx`, `client-wrapper.tsx` — Bootstrap files in root

### 3. Miscategorized directories
- `components/settings/` — 2 files that belong with features
```

### Files To Audit And Change

Table of source → target mappings with classification.

```markdown
## Files To Audit And Change

### Root-level directories to eliminate
| Source | Target | Notes |
|--------|--------|-------|
| `components/ui/` | `app/shared/ui/` | 24 UI primitives |
| `components/layout/` | `app/shared/layout/` | 5 app shell components |

### Root files to relocate
| File | Target | Classification |
|------|--------|---------------|
| `app-initializer.tsx` | `app/shared/runtime/app-initializer.tsx` | App bootstrap |

### Dead artifacts deferred
| File | Reason | Owner | Validation |
|------|--------|-------|------------|
| `Card.tsx.new` | Orphan backup | P{NN}-K{NN} | `rg` confirms zero consumers |
```

### Target Architecture

Directory tree after the KO.

```markdown
## Target Architecture

```
app/shared/
├── ui/              # Design system (24 files)
│   └── magicui/     # Decorative effects (2 files)
├── layout/          # App shell (5 files)
└── runtime/         # Runtime components (12 files)
```
```

### Plan

Phase-by-phase execution steps.

```markdown
## Plan

### Phase A: Root file relocation
1. Move `app-initializer.tsx` → `app/shared/runtime/app-initializer.tsx`
2. Move `client-wrapper.tsx` → `app/shared/runtime/client-wrapper.tsx`

### Phase B: Directory moves
1. Move `components/ui/` into `app/shared/ui/`
2. Move `components/layout/` into `app/shared/layout/`

### Phase C: Cleanup
1. Delete empty directories created by the above moves
2. Update all import paths for all moved files
```

### Validation

Exit criteria and commands to run.

```markdown
## Validation

- Root `components/ui/`, `components/layout/` do not exist after moves
- `app/shared/ui/`, `app/shared/layout/` exist with files
- KO deletion ledger exists for all moved paths
- `npm run build` or `npm run lint` passes
```

### Risks

What could go wrong and how to mitigate.

```markdown
## Risks

- Medium volume, but purely mechanical. Dozens of import paths change.
- Merge conflicts if other branches are active.
- Some files may have been missed in the audit and will break after move.
```

### Expected Outcome

What the codebase looks like after completion.

```markdown
## Expected Outcome

- Root `components/` top-level drops from 11 subdirectories to 4
- Every shared component has exactly one logical home
- New developers know where to put UI primitives without asking
```

### Deletion Ledger

Required before any deletion is considered complete.

```markdown
## Deletion Ledger

| Path | Action | Replacement / New Owner | Reference Check | Validation |
|------|--------|--------------------------|-----------------|------------|
| `components/ui/` | moved | `app/shared/ui/` | `rg "@/components/ui" app/` must return zero | `npm run build` passes |
| `components/layout/` | moved | `app/shared/layout/` | `rg "@/components/layout" app/` must return zero | `npm run build` passes |
```

## Rules

- Every KO must have a type classification (mechanical, boundary, placement, behavioral)
- Every KO must have a guarantee (what is preserved)
- Every KO must have a deletion ledger before any deletion is considered complete
- Every KO must have validation criteria that can be checked without human judgment
- Every KO should be completable independently of other KOs
- KOs should be ordered by dependency, not by preference
