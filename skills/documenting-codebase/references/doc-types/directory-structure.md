---
name: doc-directory-structure
description: How to create a directory structure document. Use when documenting the project's file tree, especially during or after reorganization.
---

# Creating Directory Structure Doc

## Overview
A directory structure document is a complete, annotated tree of the project's directories. It shows what exists, what is new, what was moved, and what was deleted. It is essential for understanding the physical organization of the codebase.

## Core Principle
The directory tree is the ground truth. Every directory must have a role, a status, and a note.

## When to Create
- After a major reorganization or refactor
- When onboarding new developers
- When the directory structure is complex (>15 top-level dirs)
- When features are organized by domain (e.g., `app/features/`)

## Step-by-Step Creation

### 1. Generate the Tree

Run `tree` or `find` to get the full directory listing:

```bash
tree -L 3 -d --charset ascii
```

Or if `tree` is unavailable:
```bash
find . -maxdepth 3 -type d | sort
```

Use GitNexus to verify directory relationships and find moved files:

```bash
# Check for circular dependencies in the structure
npx gitnexus cypher "MATCH (a:File)-[r]->(b:File), (b)-[r2]->(a) WHERE r.type = 'IMPORTS' AND r2.type = 'IMPORTS' RETURN a.filePath, b.filePath"

# Understand component hierarchies
npx gitnexus context <DomainRoot>
```

### 2. Annotate Each Directory

For every directory, assign a status and a note:

| Status | Symbol | Meaning |
|--------|--------|---------|
| Existing | 🟢 | Directory already existed, no move needed |
| New | 🟡 | Directory created during this change |
| Moved | 🔵 | Directory moved from old location, imports updated |
| Deleted | 🔴 | Directory deleted during this change |

```markdown
# [Project] — Directory Tree

**Legend:**
🟢 = existing directory (no move needed)
🟡 = new directory (created during refactor)
🔵 = moved from old location (import paths updated)
🔴 = deleted during refactor

```
.
├── 🟢 app/                                 # Next.js App Router (thin routing shell)
│   ├── 🟢 animations/                      # Route: animations page
│   ├── 🟢 character-review/                # Route: character review page
│   └── 🟢 settings/                          # Route: settings page
│
├── 🟡 app/features/                          # Business domains (all user-facing features)
│   ├── 🟡 character-review/                    # Character review domain
│   │   ├── 🟡 ui/                             # From components/features/character-review/
│   │   ├── 🟡 services/
│   │   ├── 🟡 stores/
│   │   ├── 🟡 hooks/
│   │   ├── 🟡 types/
│   │   └── 🟡 utils/
│   └── 🟡 home/                               # Home domain
│       ├── 🟡 ui/                             # From components/features/home/
│       ├── 🟡 services/
│       ├── 🟡 stores/
│       ├── 🟡 hooks/
│       ├── 🟡 types/
│       └── 🟡 utils/
│
├── 🔴 components/features/                   # DELETED: migrated to app/features/
│   ├── 🔴 character-review/
│   ├── 🔴 home/
│   └── 🔴 quiz/
│
└── 🟢 lib/                                     # Shared utilities (unchanged)
    ├── 🟢 utils/
    └── 🟢 hooks/
```
```

### 3. Write a Summary

After the tree, add a summary section:

```markdown
## Summary

- **New directories:** 8 (all in `app/features/`)
- **Moved directories:** 6 (from `components/features/` to `app/features/`)
- **Deleted directories:** 3 (empty `components/features/*`)
- **Unchanged directories:** 4 (`lib/`, `app/routes/`, `public/`, `styles/`)
```

## Verification Checklist
- [ ] Every directory has a status symbol
- [ ] Every directory has a role note (what it contains)
- [ ] Legend is included at the top
- [ ] Summary counts new, moved, deleted, and unchanged directories
- [ ] Tree reflects the current state of the repo (run `tree` before writing)
