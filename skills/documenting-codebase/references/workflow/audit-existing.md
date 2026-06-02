---
name: doc-audit-existing
description: How to audit existing documentation before creating new docs. Use when docs may already exist in the repo.
---

# Audit Existing Docs

## Overview
Before creating any new documentation, you must understand what already exists, what is stale, and what is missing. Skipping the audit leads to duplicate docs, stale information, and a fragmented knowledge base.

## Core Principle
The audit is not optional. It is the first step of every documentation pass.

## Step-by-Step Audit

### 1. Locate Existing Docs

Check these locations in order:

| Location | What to look for |
|----------|-----------------|
| Repo root | `AGENTS.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `README.md` |
| `docs/` | Any existing subdirectory or `.md` file |
| `.github/` | `CONTRIBUTING.md`, issue templates |
| `src/` or `app/` | Inline READMEs, `__docs__` folders |

### 2. Classify Each Doc

For every doc found, record:

```markdown
| Doc | Location | Status | Stale? | Action |
|-----|----------|--------|--------|--------|
| README.md | root | Exists | Maybe | Review |
| AGENTS.md | root | Exists | Likely | Check line count |
| ... | ... | ... | ... | ... |
```

**Status:** Exists / Missing / Partial
**Stale indicators:**
- Mentions files or paths that no longer exist
- References dependencies that have been removed
- Describes architecture that has been refactored
- No date or "last verified" timestamp
- Line count > 100 for a map doc

### 3. Determine the Gap

After classification, identify:
- **Missing docs** — no doc exists for this topic
- **Stale docs** — doc exists but does not reflect reality
- **Monolithic docs** — one giant file that should be split into `docs/`
- **Unlinked docs** — doc exists but is not reachable from the map

### 4. Write the Audit Summary

Create a brief summary (or append to the agent's working notes):

```markdown
## Documentation Audit

### Existing Docs
- [Doc] — [Status] — [Stale?]

### Gaps
- [Missing doc] — [Why it matters]

### Stale Docs
- [Doc] — [What's wrong] — [Fix needed]

### Monolithic Docs
- [Doc] — [Line count] — [Restructure into docs/]
```

## Verification Checklist
- [ ] Checked repo root for map docs
- [ ] Checked for `docs/` directory
- [ ] Checked source directories for inline docs
- [ ] Recorded status of every found doc
- [ ] Flagged stale docs with specific reasons
- [ ] Identified monolithic docs that need splitting
- [ ] Produced an audit summary
