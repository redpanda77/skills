# Quick Reference

**When to read this:** When you need a refresher on the core mechanics without diving into full reference files. Load this before any operation if you haven't touched the vault in a while.

---

## Router: What to load

| Operation | Load first | Load second |
|---|---|---|
| **Set up vault** | `references/setup/setup.md` | `references/setup/templates.md` |
| **Create a note** | `references/operations/authoring.md` | `references/operations/types.md` |
| **Process raw notes** | `references/operations/maintenance.md` | `references/orchestration/automation.md` |
| **Generate summaries** | `references/operations/maintenance.md` | `references/orchestration/automation.md` |
| **Check vault health** | `references/operations/health.md` | `references/orchestration/automation.md` |

Always read `system/VAULT.md` before acting on an existing vault.

---

## Critical Rules

1. **Never read the entire vault.** Always use a context pack (max 30 notes).
2. **Never delete a note.** Change status to `Archived` or `Stale`; move to `archive/`.
3. **Raw notes are immutable.** Never edit a processed Raw. Create a new Raw if needed.
4. **Every new note links to at least one existing note.** No orphans.
5. **Every operation is recorded** in `logs/maintenance-log.md`. Append-only.
6. **State is derived from disk, not memory.** Re-read indexes before acting.
7. **Automation is deterministic.** Scripts expose evidence; humans decide.

---

## Context Pack Rules

- **Mandatory** for every operation that reads multiple notes.
- **Bounded:** max 30 notes. If index is larger, filter by direct links → shared wikilinks → recency → category.
- **Indexed:** Generate an index first, then read the notes.
- **Ephemeral** by default. Record in maintenance log for critical operations.

---

## When to Ask the User

- Type is ambiguous (content fits multiple types).
- Destination folder unclear for a Raw note.
- Action item lacks an owner.
- Health check findings: fix all, fix selected, or just flag?
- Vault does not exist (offer to set one up).

---

## Common Tasks

| Task | Type | Folder | Filename |
|---|---|---|---|
| Generic note | Note | `notes/` | `<kebab-topic>.md` |
| Raw note | Raw | `Raw/` | `YYYY-MM-DD-<kebab-topic>.md` |
| Daily note | Note | `daily/` | `YYYY-MM-DD.md` |
| Summary | Summary | `summaries/` | `YYYY-MM-DD-<topic>.md` |

Methodology-specific tasks (e.g., Meeting, Decision, Initiative, Person for Team/Work; Project, Area, Resource for PARA; Fleeting, Literature, Permanent for Zettelkasten) are defined in `references/setup/methodology-modes.md` and `references/operations/types.md`.

---

## File Path Cheat Sheet

| File | Purpose |
|---|---|
| `system/VAULT.md` | Vault conventions, folder layout, automation config |
| `system/CLAUDE.md` | Behavioral contract for this vault |
| `system/AGENTS.md` | Tool-agnostic mechanics (format, wikilinks, views) |
| `logs/maintenance-log.md` | Append-only audit trail |
| `Raw/` | Inbox — unprocessed source material |
| `Raw/archive/` | Processed Raw originals |
| `archive/` | Archived notes (status=Archived or >1 year old) |

---

## Subagent Triggers

| Task | Threshold | Subagent |
|---|---|---|
| Health check | Always | `references/orchestration/subagents/health-checker.md` |
| Process raw notes | Batch > 5 | `references/orchestration/subagents/raw-processor.md` |
| Generate summary | Always | `references/orchestration/subagents/summary-generator.md` |

---

## The 10-Step Contract

1. Detect situation
2. Load `system/VAULT.md`
3. Load skill reference
4. Generate context pack
5. Execute workflow
6. Validate output
7. Record in audit trail
8. Report to user
9. Update `system/VAULT.md` if conventions changed
10. Stop on ambiguity — ask the user
