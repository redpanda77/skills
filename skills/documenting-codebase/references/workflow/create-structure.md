---
name: doc-create-structure
description: How to create the docs/ directory structure. Use after analyzing the codebase and before writing individual docs.
---

# Create docs/ Structure

## Overview
After auditing existing docs and analyzing the codebase, create the `docs/` directory structure. This is the physical layout of the knowledge base.

## Core Principle
Structure follows function. Create directories only when they have a purpose.

## Step-by-Step

### 1. Create the Root Directory

```bash
mkdir -p docs
```

### 2. Create Subdirectories

Create only the directories you need:

```bash
mkdir -p docs/design-docs
mkdir -p docs/product-specs
mkdir -p docs/references
mkdir -p docs/plans        # writing-plans will populate this
mkdir -p docs/generated    # for machine-generated docs
```

**Rules:**
- Do not create empty directories. Every directory must have at least one file.
- `plans/` is created empty but managed by `writing-plans`.
- `generated/` is created empty but populated by scripts.

### 3. Write the Root Index

Create `docs/index.md` cataloging the directory:

```markdown
# Documentation

## Catalog

| Doc | Description | Status |
|-----|-------------|--------|
| [DESIGN.md](DESIGN.md) | Design system inventory | Draft |
| [FRONTEND.md](FRONTEND.md) | Frontend conventions | Draft |
| [PRODUCT.md](PRODUCT.md) | Product definition, features, UX flows | Draft |

## Subdirectories

- [design-docs/](design-docs/) — Feature design documents
- [product-specs/](product-specs/) — Product specifications
- [plans/](plans/) — Execution plans (via `writing-plans`)
- [references/](references/) — External tool references
- [generated/](generated/) — Auto-generated docs
```

**Rules:**
- `index.md` must list every top-level doc and subdirectory
- Include a status column (Draft / Review / Complete / Stale)
- Update `index.md` every time a new doc is added

### 4. Write Subdirectory Indexes

Every subdirectory with >2 files must have an `index.md`:

```markdown
# design-docs/

| Doc | Description | Status |
|-----|-------------|--------|
| [core-beliefs.md](core-beliefs.md) | Agent-first operating principles | Complete |
| [auth-flow.md](auth-flow.md) | Authentication flow design | Draft |
```

## Verification Checklist
- [ ] `docs/` directory exists
- [ ] Only needed subdirectories were created
- [ ] `docs/index.md` catalogs all top-level docs and subdirectories
- [ ] Every subdirectory with >2 files has an `index.md`
- [ ] No empty directories
