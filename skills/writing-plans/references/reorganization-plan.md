# Reorganization Plan

For restructuring code, moving files, consolidating directories, and establishing architectural boundaries.

## Key Characteristics

- **Mechanical moves first**: Move files before changing them
- **Impact analysis required**: Every file with >5 consumers needs analysis before moving
- **Deletion ledgers mandatory**: Every deleted path must have evidence
- **Green-to-green validation**: Build must pass after every move

## Directory Structure

```
docs/plans/P{NN}-<name>/
├── README.md (or index.md)
├── goal.md
├── methodology.md
├── P{NN}-AUDIT.md              # Current state audit
├── P{NN}-FINDINGS.md           # Deep audit findings
├── P{NN}-K01-foundation.md   # Mechanical move: foundation
├── P{NN}-K02-feature-extraction.md  # Boundary refactor: features
├── P{NN}-K03-storage.md      # Boundary refactor: infrastructure
├── P{NN}-K04-enforcement.md  # Enforcement: tooling
├── P{NN}-K05-cleanup.md      # Cleanup: temp removal
├── P{NN}-DEVIATIONS.md
└── P{NN}-PHASED-APPROACH.md
```

## Goal.md Emphasis

Reorganization goal.md files must emphasize:

- **No business logic changes**: The plan is structural only
- **No empty directories**: Create directories just-in-time
- **No dumping grounds**: Every file has a logical home
- **Import boundary enforcement**: Features do not import sibling features
- **Next.js route safety**: Route files never go inside feature/shared/infrastructure directories

## KO Structure

Reorganization KOs must include:

```markdown
## Deletion Ledger

| Path | Action | Replacement | Reference Check | Validation |
|------|--------|-------------|-----------------|------------|
| `old/path` | moved | `new/path` | `rg "old/path"` must return zero | `npm run build` passes |
```

## Validation

Reorganization plans must validate:

- `npm run build` passes after every KO
- `npm run lint` passes with zero issues
- No empty directories remain: `find app -type d -empty` returns nothing
- No old import paths remain: `rg "@/old/path"` returns zero
- No route files in wrong directories: `find app/features -name "page.tsx"` returns nothing
- Deletion ledger is complete for every moved/deleted path

## Rules

- Mechanical move KOs must be ranked first (highest RICE)
- Placement decision KOs (hooks, services, stores) require classification before moving
- Boundary refactor KOs must establish the target architecture before moving files
- Enforcement KOs must wait until the structure is stable
- Cleanup KOs must be last
- Every KO must have a guarantee (e.g., "No business logic changes")
