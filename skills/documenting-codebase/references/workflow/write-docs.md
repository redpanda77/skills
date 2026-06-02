---
name: doc-write-docs
description: How to write individual documentation files. Use after creating the docs/ structure.
---

# Write Individual Docs

## Overview
After creating the `docs/` structure, write the individual documentation files. Create only what is needed and missing. Do not duplicate existing docs.

## Core Principle
Create docs that describe reality. Do not create docs for code that does not exist yet.

## Step-by-Step

### 1. Select Doc Type

From the analysis, determine which doc types are needed:

| If you need to document... | Create... | Load reference... |
|---------------------------|-----------|-------------------|
| Domain map, layering, data flow | `ARCHITECTURE.md` | `references/doc-types/architecture.md` |
| Design tokens, typography, components | `docs/DESIGN.md` | `references/doc-types/design.md` |
| Directory tree | `docs/directory-tree.md` | `references/doc-types/directory-structure.md` |
| Frontend stack, conventions | `docs/FRONTEND.md` | `references/doc-types/frontend.md` |
| Product definition, features, UX flows | `docs/PRODUCT.md` | `references/doc-types/product.md` |
| Quality grades | `docs/QUALITY_SCORE.md` | `references/doc-types/quality-score.md` |
| Reliability targets, runbooks | `docs/RELIABILITY.md` | `references/doc-types/reliability.md` |
| Security model, threats | `docs/SECURITY.md` | `references/doc-types/security.md` |

### 2. Follow the Doc-Type Guide

Each doc type has a detailed guide in `references/doc-types/`. Load the relevant guide and follow its step-by-step instructions.

**Rules:**
- Read the guide before writing the doc
- Follow the guide's structure and verification checklist
- Do not skip sections
- Use the guide's templates as starting points, not final text

### 3. Write Feature-Specific Docs

For feature-specific docs (e.g., `auth-flow.md`, `onboarding-spec.md`), store them in the appropriate subdirectory:

- Design documents → `docs/design-docs/`
- Product specs → `docs/product-specs/`
- External references → `docs/references/`

### 4. Update Indexes

After writing each doc, update the relevant `index.md`:

```markdown
| Doc | Description | Status |
|-----|-------------|--------|
| [DESIGN.md](DESIGN.md) | Design system inventory | Complete |
```

**Rules:**
- Update `docs/index.md` for every top-level doc
- Update subdirectory `index.md` for every subdirectory doc
- Set status to Complete only after verification

## Verification Checklist
- [ ] Only missing docs were created
- [ ] Each doc follows its doc-type guide
- [ ] No docs were created for non-existent code
- [ ] All indexes were updated
- [ ] Every doc has a clear, searchable filename
