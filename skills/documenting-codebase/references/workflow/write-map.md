---
name: doc-write-map
description: How to write AGENTS.md or CLAUDE.md as the short map. Use as the final step after all other docs are written.
---

# Write the Map (AGENTS.md / CLAUDE.md)

## Overview
After all other docs are written, create the short map. This is the final step. The map lives at the repo root and is strictly under 100 lines.

## Core Principle
The map is a pointer, not a container. It tells the agent where to look, not what to know.

## Step-by-Step

### 1. Load the Guide

Read `references/doc-types/agents-map.md` for the full instructions.

### 2. List Every Doc

After all docs are written, list them with one-line descriptions:

```markdown
# Agent Map

## Core Docs
- [ARCHITECTURE.md](ARCHITECTURE.md) — Domain map, package layering, data flow
- [DESIGN.md](docs/DESIGN.md) — Design system inventory: tokens, typography, components
- [FRONTEND.md](docs/FRONTEND.md) — Frontend stack, directory structure, conventions

## Product & Quality
- [PRODUCT.md](docs/PRODUCT.md) — Product definition, features, UX flows, success metrics
- [RELIABILITY.md](docs/RELIABILITY.md) — Reliability targets and runbooks
- [SECURITY.md](docs/SECURITY.md) — Security model and threat surface

## Deep Dives
- [design-docs/](docs/design-docs/) — Feature design documents
- [product-specs/](docs/product-specs/) — Product specifications
- [plans/](docs/plans/) — Execution plans (via `writing-plans`)
- [references/](docs/references/) — External tool and design references
```

### 3. Verify Line Count

```bash
wc -l AGENTS.md
```

If >100 lines, move content to `docs/` and shorten the pointer.

### 4. Verify Every Link

Check that every link points to a real file:

```bash
# Check each link manually
[ -f ARCHITECTURE.md ] && echo "OK" || echo "MISSING"
[ -f docs/DESIGN.md ] && echo "OK" || echo "MISSING"
```

## Verification Checklist
- [ ] File is under 100 lines
- [ ] Every doc in `docs/` is listed
- [ ] Every link points to a real file
- [ ] No deep content — only one-line pointers
- [ ] No tables or code examples
- [ ] Includes "Last updated" date
