# Methodology Structure

The `methodology.md` file describes the execution protocol for the plan. Every KO must follow the same methodology.

## Core Principles

```markdown
# P{NN} Methodology: <Protocol Name>

## Core Principles

1. **Principle name** — Description
2. **Principle name** — Description
```

## The 7-Step Protocol

### 1. Baseline

```markdown
### 1. Baseline

Before any changes:

```bash
# Record current state
git status
git diff --name-status

# Run narrowest relevant baseline check
npm run build
# OR
npm run lint

# If baseline fails, document whether failure is pre-existing
```
```

### 2. Classify

```markdown
### 2. Classify

Label the next step:

| Type | Allowed | Not Allowed |
|------|---------|-------------|
| **Mechanical** | File moves, import path updates, empty directory deletion | Business logic changes |
| **Boundary** | Module ownership changes, public surface changes | Runtime behavior changes |
| **Behavioral** | Design changes explicitly scoped by the KO | Any changes outside KO scope |
```

### 3. Map Impact

```markdown
### 3. Map Impact

For any file with >5 consumers or touching shared APIs:

```bash
# Impact analysis (upstream = what depends on this)
# Full context (callers, callees, process participation)
# Text search for all references
rg "from.*@/old/path" app/ components/
rg "import.*old/path" app/ components/
```

**Update order:** Interfaces/types first, implementations second, callers third, tests and validation last.
```

### 4. Change

```markdown
### 4. Change

Make one coherent move at a time:

Rules:
- Do not introduce compatibility wrappers, aliases, or shims unless explicitly required
- Do not opportunistically clean unrelated code
- Create target directories just-in-time as files move into them
- Do not leave empty placeholder directories
```

### 5. Verify

```markdown
### 5. Verify

After each high-blast-radius move:

```bash
# Narrowest useful check
npm run build
# OR
npm run lint
# OR targeted check
```

For mechanical steps, any runtime behavior change is a failure unless the KO explicitly allows it.
```

### 6. Ledger

```markdown
### 6. Ledger

Record in the KO's deletion ledger:

| Path | Action | Replacement / New Owner | Reference Check | Validation |
|------|--------|--------------------------|-----------------|------------|
| `old/path` | moved / merged / deleted-empty / deleted-dead | `new/path` or `none` | Search result | Command result |

Rules:
- `deleted-empty`: only when `find <path> -type f` returns no files
- `deleted-dead`: only when search shows zero consumers AND the KO explicitly lists the deletion
- `moved`: new file must exist and old imports must resolve to new path
- `merged`: requires side-by-side diff or written rationale
```

### 7. Repeat

```markdown
### 7. Repeat

Continue until the KO acceptance criteria pass, then run the KO-level verification suite.
```

## Risk Levels

```markdown
## Risk Levels

| Depth | Meaning | Action Required |
|-------|---------|----------------|
| d=1 | **WILL BREAK** — direct callers/importers | MUST update these before moving |
| d=2 | **LIKELY AFFECTED** — indirect dependencies | Should test after changes |
| d=3 | **MAY NEED TESTING** — transitive dependencies | Test if critical path |
```

## Pre-Commit Checklist

```markdown
## Pre-Commit Checklist

Before declaring any KO complete:

1. [ ] Impact analysis was run for all modified symbols
2. [ ] No HIGH/CRITICAL risk warnings were ignored
3. [ ] Changes confirm changes match expected scope
4. [ ] All d=1 (WILL BREAK) dependents were updated
5. [ ] KO deletion ledger is complete
6. [ ] Build or lint passes
7. [ ] No empty directories left behind
8. [ ] No old import paths remain
```

## Deviation Handling

```markdown
## Deviation Handling

If a KO cannot be completed as planned:

1. Mark the KO `Blocked` in the progress tracker
2. Record the blocker in `DEVIATIONS.md` with:
   - Exact evidence (command output, error messages, file paths)
   - What was attempted
   - Why it failed
   - Next required action
3. Do not proceed to the next KO until the blocker is resolved or the plan is revised
```

## Rules

- Every plan must have a methodology.md
- Every KO must follow the 7-step protocol
- The methodology must define the risk levels
- The methodology must define the pre-commit checklist
- The methodology must define the deviation handling process
