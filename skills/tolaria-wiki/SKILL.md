---
name: tolaria-wiki
description: Set up, author in, and maintain a Tolaria knowledge vault (folder of Markdown + YAML frontmatter forming a personal knowledge graph). Use when the user wants to create a new Tolaria vault from scratch; create any vault note; process raw notes; import meeting recordings or transcripts; generate daily / weekly / topic summaries; or set up integrations with external sources. Tolaria is a folder-of-markdown vault format — github.com/refactoringhq/tolaria. Works on a fresh machine with no prior setup.
---

# Tolaria Wiki

A Tolaria vault is a folder of Markdown files with YAML frontmatter. Each file is one note. Relationships use `[[wikilinks]]`. No database, no proprietary format — plain files you can read with any editor and version with git.

## Router: Load only what you need

| Operation | Load these files |
|-----------|-----------------|
| **Setup vault** | `references/setup/setup.md` → `references/setup/templates.md` |
| **Create a note** | `references/operations/authoring.md` → `references/operations/types.md` |
| **Process raw notes** | `references/operations/maintenance.md` → `references/orchestration/automation.md` |
| **Generate summaries** | `references/operations/maintenance.md` → `references/orchestration/automation.md` |
| **Check vault health** | `references/operations/health.md` → `references/orchestration/automation.md` |

## No vault? Create one

If the user asks to create a note, process raw notes, or generate summaries and no vault exists:

1. Detect: `system/VAULT.md` and `logs/maintenance-log.md` are missing.
2. Offer: "No vault found. Set one up first?"
3. If yes → load `references/setup/setup.md` and run the setup workflow.
4. If no → stop and ask what the user wants to do.

## Critical Rules

1. **Never read the entire vault.** Always use a context pack (index → bounded subset). See `references/orchestration/automation.md`.
2. **Never delete a note.** Change status to `Archived` or `Stale`; move to `archive/`.
3. **Raw notes are immutable.** Never edit a Processed Raw. Create a new Raw if needed.
4. **Every new note links to at least one existing note.** No orphans.
5. **Every operation is recorded** in `logs/maintenance-log.md`. Append-only.
6. **State is derived from disk, not memory.** Re-read indexes before acting.
7. **Automation is deterministic.** Scripts expose evidence; humans decide.

## When to ask

- Type ambiguous (content fits multiple types).
- Destination folder unclear for a Raw note.
- Action item lacks an owner.
- Health check findings: fix all, fix selected, or just flag?

## What this is NOT

- Not a compiler OS (no multi-tier validation, no judge subagents).
- Not a sync system. Vault is local files.
- Not a transcription tool. Audio/PDFs are upstream.

## References

- `references/setup/setup.md` — create a vault from nothing
- `references/setup/templates.md` — copy-paste templates
- `references/setup/checklist.md` — master setup checklist
- `references/operations/authoring.md` — create, classify, file, cross-link any note
- `references/operations/maintenance.md` — process raw, import, generate summaries, audit
- `references/operations/health.md` — vault health checks
- `references/operations/types.md` — generic type system framework
- `references/operations/naming.md` — naming conventions
- `references/operations/format.md` — file format rules
- `references/operations/integrations.md` — connect external sources
- `references/orchestration/automation.md` — orchestration, context packs, deterministic steps
- `references/orchestration/automation-config.md` — configuration, defaults, VAULT.md settings
- `references/orchestration/automation-lifecycle.md` — triggers, lifecycle, error handling
- `references/orchestration/subagents.md` — when to invoke subagents, thresholds, return contracts
- `references/foundation/principles.md` — 12 core principles
- `references/foundation/architecture.md` — pipeline, layers, contracts
- `references/setup/methodology-modes.md` — PARA, Zettelkasten, LYT modes
- `references/orchestration/subagents/health-checker.md` — subagent: health check
- `references/orchestration/subagents/raw-processor.md` — subagent: raw processing
- `references/orchestration/subagents/summary-generator.md` — subagent: summary generation
