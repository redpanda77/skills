---
name: documenting-codebase
description: Create and maintain a structured in-repo knowledge base for a codebase. Use when the user asks to document a codebase, set up docs, create a knowledge base, write AGENTS.md, or audit existing documentation. Uses parallel audit subagents, a decision tree for planning, and parallel doc creation. Invokes writing-plans for execution plans.
---

# Documenting Codebase

Create a structured `docs/` directory as the system of record. A short `AGENTS.md` (or `CLAUDE.md`) serves as the map.

## Workflow

### Phase 1: Audit (Parallel Subagents)

Spawn 5 parallel subagents to audit the codebase. Each subagent analyzes a specific scope and returns a structured report.

1. **Tech Stack** — `references/audit/tech-stack.md`
2. **Architecture** — `references/audit/architecture.md`
3. **Testing** — `references/audit/testing.md`
4. **API & Database** — `references/audit/api-database.md`
5. **DevOps** — `references/audit/devops.md`

See `references/audit/orchestration.md` for how to spawn and synthesize.

### Phase 2: Plan (Decision Tree)

Use the 5 audit reports to decide what docs to create. Follow `references/planning/decision-tree.md`. Create a doc only if it is missing or stale. Never create a doc for code that does not exist.

### Phase 3: Create (Parallel Subagents)

Spawn parallel subagents (max 4 at a time) to write each planned doc. Each subagent loads the doc-type guide and template from `references/doc-types/` and `references/templates/`. See `references/workflow/create-docs.md`.

### Phase 4: Map & Validate

1. Write `AGENTS.md` under 100 lines. Follow `references/workflow/write-map.md`.
2. Validate all links work. Follow `references/validation/structure-check.md`.
3. Check `AGENTS.md` line count.

## When to Use GitNexus

- Before mapping domains in `ARCHITECTURE.md` — run `gitnexus context` on key symbols
- Before tracing data flows — run `gitnexus query` or `gitnexus impact`
- Before documenting directory structure — run `gitnexus cypher` for circular deps
- Before committing docs — run `gitnexus detect_changes` to verify structure

See `references/gitnexus/overview.md` for full commands and rules.

## When to Invoke `writing-plans`

If the user asks to create an execution plan, improvement plan, or phased roadmap:
- Invoke `writing-plans` skill
- Plans are stored in `docs/plans/` per the `writing-plans` convention

## Rules

- Never skip the audit phase. Always spawn parallel subagents.
- Never create a doc without first auditing the corresponding codebase part.
- Never create a monolithic AGENTS.md longer than 100 lines. Move deep content to `docs/`.
- If `docs/` already exists, clean and restructure it to match `references/directory-layout.md`.
- Never create docs for code that does not exist yet. Future plans go in `docs/plans/` via `writing-plans`.
- Never use `find` or `grep` as a substitute for GitNexus when GitNexus is available.
- Always name docs clearly: `frontend-architecture.md`, not `doc-3.md`.
- Always include a `docs/index.md` cataloging the directory contents.

## Error Handling

- Missing domain: Ask the user which area needs docs.
- Existing AGENTS.md is giant: Suggest restructuring into `docs/` + short map.
- No clear codebase structure: Ask the user to specify the tech stack or main entry points.
- GitNexus unavailable: Document the exception and proceed with manual analysis.
- Subagent fails: Retry once, then proceed without that audit scope and document the gap.
