# Reorganization Plan

For restructuring code, moving files, consolidating directories, and establishing architectural boundaries.

## Key Characteristics

- **Mechanical moves first**: Move files before changing them
- **Impact analysis required**: Every file with >5 consumers needs analysis before moving
- **Deletion ledgers mandatory**: Every deleted path must have evidence
- **Green-to-green validation**: Build must pass after every move

## Tools and Enforcement

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **GitNexus** | Impact analysis, circular dependency detection, safe renaming | Before any file move, before any deletion, for symbol renames |
| **Biome** | Linting, formatting, import sorting | After every KO, before any commit |
| **React Doctor** | React-specific linting, effect rules, hook rules | After every KO affecting React components |
| **TypeScript** | Type checking, `noEmit` validation | After every KO affecting types or imports |
| **ripgrep (`rg`)** | Text search for imports, references, patterns | During impact analysis, during cleanup verification |
| **find** | Directory inspection, empty directory detection | During audit, during cleanup |

### GitNexus Specific Commands

```bash
# Impact analysis before moving a file with >5 consumers
gitnexus_impact({target: "SymbolName", direction: "upstream", repo: "reponame"})

# Full context (callers, callees, process participation)
gitnexus_context({name: "SymbolName", repo: "reponame"})

# Circular dependency detection
# MATCH (a:File)-[r:CodeRelation {type: 'IMPORTS'}]->(b:File),
#       (b)-[r2:CodeRelation {type: 'IMPORTS'}]->(a)
# RETURN a.filePath, b.filePath

# Safe multi-file rename
gitnexus_rename({symbol_name: "OldSymbol", new_name: "NewSymbol", dry_run: true, repo: "reponame"})

# Detect changes before commit
gitnexus_detect_changes({scope: "all", repo: "reponame"})
```

### Biome Specific Commands

```bash
# Check after every KO
npx biome check --changed

# Fix auto-fixable issues
npx biome check --changed --write

# Check specific files
npx biome check app/shared/ui/
```

### React Doctor Specific Commands

```bash
# Check React components after move
npx react-doctor

# Note: React Doctor uses doctor.config.json or doctor.config.ts
# react-doctor.config.json is NOT accepted by current versions
```

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
