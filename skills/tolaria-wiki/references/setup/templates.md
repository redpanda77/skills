# Templates — copy-paste content for setup

**When to read this:** During vault setup (Step 3–11 of `references/setup/setup.md`). Every file the setup workflow writes. Self-contained — no external dependencies.

---

## AGENTS.md template

```markdown
---
type: Note
_organized: true
---

# AGENTS.md — Tolaria vault

This is a [Tolaria](https://github.com/refactoringhq/tolaria) vault: a folder of Markdown files with YAML frontmatter forming a personal knowledge graph.

Keep edits compatible with this vault's current conventions. Prefer small, human-readable changes over heavy restructuring.

## Core conventions

- One Markdown note per file.
- The first H1 in the body is the preferred display title. Legacy `title:` frontmatter is read as a fallback but do not add it to new notes.
- Store note type in the `type:` frontmatter field.
- Type definitions live at the vault root as regular notes with `type: Type`.
- Saved views live in `views/*.yml`.
- Files in `attachments/` are assets, not notes.
- Frontmatter keys starting with `_` are Tolaria-managed state. Leave them alone unless explicitly asked.

## Notes

```yaml
---
type: Note
related_to: "[[other-note]]"
status: Active
url: https://example.com
---

# Example note

Body in Markdown.
```

## Types

Types are regular notes at the vault root with `type: Type`.

```yaml
---
type: Type
_icon: rocket
_color: "#3b82f6"
_order: 0
_list_properties_display:
  - related_to
_sort: "property:status:asc"
---

# <Type Name>
```

## Relationships

Any frontmatter property whose value contains `[[wikilinks]]` is a relationship. Common keys: `related_to`, `belongs_to`, `owner`, `source`. Custom names are valid.

Quoted wikilinks for scalar frontmatter values. YAML lists for multi-value.

## Wikilinks

- `[[filename]]` — link by filename
- `[[Note Title]]` — link by H1
- `[[filename|display text]]` — custom label

Works in frontmatter and body.

## Views

Saved views live in `views/*.yml`. Filename is the stable view ID — use kebab-case (`active-projects.yml`).

```yaml
name: Active Projects
icon: null
color: null
sort: "property:status:asc"
filters:
  all:
    - field: type
      op: equals
      value: Project
    - field: status
      op: equals
      value: Active
```

- `name` is required.
- `filters` root must be exactly one `all:` or `any:` group.
- Each condition has `field`, `op`, `value`.
- Operators: `equals`, `not_equals`, `contains`, `not_contains`, `any_of`, `none_of`, `is_empty`, `is_not_empty`, `before`, `after`.
- `regex: true` works with `equals`, `not_equals`, `contains`, `not_contains`.
- Never create `.view.json` files — Tolaria reads `.yml` only.

## Filenames

Use kebab-case: `my-note-title.md`. One note per file.

## How to operate this vault

### 1. Load the right files

Before doing anything, read `system/VAULT.md`. It is the single source of truth for this vault's conventions.

Then load the skill reference for your operation:
- **Setup**: `references/setup/setup.md`
- **Authoring**: `references/operations/authoring.md` + `references/operations/types.md`
- **Maintenance**: `references/operations/maintenance.md` + `references/orchestration/automation.md`
- **Health check**: `references/operations/health.md`
- **Integrations**: `references/operations/integrations.md`

### 2. Use bounded context (context packs)

Never read the entire vault. Always generate a context pack:

1. **Generate an index** — list relevant notes by type, date, or status.
2. **Read the index** — confirm the notes are relevant.
3. **Read the notes** — only the notes in the context pack.
4. **Record the pack** — append to `logs/maintenance-log.md`.

Max context pack size: 30 notes. If the index is larger, filter it.

### 3. Follow the pipeline

```
User request
  -> Detect situation (vault exists? Raw unprocessed? Note to create?)
  -> Load bounded context (index + relevant notes)
  -> Execute workflow
  -> Record in audit trail (logs/maintenance-log.md)
  -> Report to user
```

### 4. Automation rules

- **Auto-process unambiguous Raw notes.** If a Raw note has clear category, clear content, and clear destination, process it without asking.
- **Auto-link suggestions.** When creating a note, suggest related notes based on shared wikilinks.
- **Stop on ambiguity.** If any step is unclear, stop and ask the human.
- **Deterministic only.** Scripts expose evidence; models and humans decide.

See `references/orchestration/automation.md` for the full automation system.

## What agents should do

- Create and edit notes using the frontmatter and H1 conventions above.
- Add or modify relationships without breaking existing wikilinks.
- Create and edit saved views in `views/`.
- Generate context packs for every operation.
- Record every structural change in `logs/maintenance-log.md`.
- Check `system/VAULT.md` before acting to confirm vault conventions.

## What agents should avoid

- Do not move existing type files out of the vault root unless explicitly asked.
- Do not treat files in `attachments/` as notes.
- Do not silently overwrite an existing `AGENTS.md`.
- Do not modify `_`-prefixed keys without explicit config-editing intent.
- Do not read the entire vault. Use context packs.
- Do not make qualitative judgments in automation. Expose evidence; let the human decide.
```

---

## CLAUDE.md template

Fill in `<IDENTITY>`, `<CONFIDENTIALITY-DEFAULT>`, and adjust the Project-local skills section to match what's actually installed.

```markdown
---
type: Note
_organized: true
---

# <Vault name>

**<IDENTITY — one line, e.g., "Personal knowledge vault for Jane Doe — PM, design, research">**

Tolaria vault. Folder of markdown with YAML frontmatter forming a personal knowledge graph.

## Project-local skills

The `tolaria-wiki` skill (either user-global at `~/.claude/skills/tolaria-wiki/` or copied to `.claude/skills/tolaria-wiki/` here) handles:

- Setting up a vault
- Creating notes (any type defined in this vault)
- Processing raw notes, importing external sources, generating summaries
- Connecting external sources (recorders, transcripts, documents, trackers)

If a task touches the vault and `tolaria-wiki` isn't being used, run `/memory` to confirm it's loaded.

## Hard rules

- **IMPORTANT**: <CONFIDENTIALITY-DEFAULT — e.g., "Treat anything in this vault as confidential by default. Never share or summarize outside this vault unless explicitly asked in the current message.">
- **IMPORTANT**: Never invent dates, attendees, decisions, or quotes. If uncertain, say so explicitly and ask.
- Never delete a note. Move to `archive/` (or `Raw/archive/`) or change status to `Archived` / `Stale` instead.
- Never modify files in `attachments/`, `views/`, `.claude/`, `.tolaria/`, or `.obsidian/` as if they were notes.
- Frontmatter keys starting with `_` are Tolaria-managed. Don't touch unless explicitly editing config.
- Use `[[wikilinks]]`, not markdown links, for cross-references.

## Workflow

- Make minimal changes — do not "improve" notes I didn't ask you to change.
- After completing any task: list what changed, what's untouched, what needs my attention.
- When type, category, owner, or destination folder is unclear, ask before filing.
- Append structural changes (new note, processed Raw → archive, status moves) to `logs/maintenance-log.md`.

## Human approval required

YOU MUST ask before:
- Deleting or moving any note out of the vault.
- Bulk-renaming files or restructuring folders.
- Modifying type-definition files at the vault root.
- Editing notes marked `confidential: true` in frontmatter.
- Installing background scripts or watchers.

## Out of scope

- `attachments/` — binary files, not notes.
- `views/*.yml` — Tolaria view config.
- `.claude/`, `.tolaria/`, `.obsidian/` — tool config.
- `logs/` — append-only; never rewrite history.
- `Raw/archive/` — processed raw originals; preserved for audit.

---

@AGENTS.md
```

---

## VAULT.md template

This is the vault's system document. It is the single source of truth for this vault's conventions. The agent reads this before every operation on the vault.

```markdown
# <Vault Name>

## Purpose
<One line: what this vault is for>

## Structure

### Folder Layout
```
<folders>
Raw/
  archive/
summaries/
logs/
attachments/
views/
system/
  README.md
  VAULT.md
  CHANGELOG.md
archive/
```

### Naming Conventions
- Files: kebab-case, `.md`, dates as `YYYY-MM-DD` or `YYYY-MM`
- Folders: kebab-case, lowercase
- Type-definition files: lowercase at root
- Type values in frontmatter: Capitalized

### Folder Rules
- No notes at root. Only type definitions and system docs.
- If a folder has >50 files, create subfolders by year or subcategory.
- Max subfolder depth: 2
- Archive notes when status is `Archived` or >1 year old.

## Type System

Types used in this vault:
- <list types>

See type-definition files at vault root for schemas.

## Maintenance

### Health Check Schedule
- Weekly: orphans, dead links, stale Raw, empty notes, missing fields
- Monthly: folder size checks, naming compliance, audit

### Automation Rules
- Auto-process unambiguous Raw notes: enabled
- Context pack size: max 30 notes
- Auto-link suggestions: enabled
- Archive after: status=Archived or >1 year old

### Audit Policy
- Source evidence required for all summaries
- Hash-based freshness checks enabled
- Maintenance log: append-only
- Human override always possible

## Changelog

### YYYY-MM-DD — Vault bootstrap
- Created folder structure
- Added type definitions
- Created AGENTS.md, CLAUDE.md, VAULT.md, system/README.md
```

---

## system/README.md template

Human-readable quickstart for the vault.

```markdown
# <Vault Name>

<One paragraph: what this vault is for and who uses it>

## Quick navigation

- **<Type 1>:** `<folder-1>/` — <description>
- **<Type 2>:** `<folder-2>/` — <description>
- **Raw inbox:** `Raw/` — unprocessed source material
- **Summaries:** `summaries/` — generated summaries
- **System docs:** `system/` — this vault's conventions and rules

## How to browse

This vault uses `[[wikilinks]]` for cross-references. Every note links to related notes. The graph is the primary navigation.

For a quick view, check `views/*.yml` for saved views.

## How to add a note

1. Pick the right folder based on type
2. Use kebab-case filename
3. Add YAML frontmatter with `type:` and required fields
4. Cross-link to related notes with `[[wikilinks]]`
5. Append structural changes to `logs/maintenance-log.md`

## Conventions

See `system/VAULT.md` for the full conventions document.
```

---

## Default type-definition files (vault root)

These four types are universal — every vault gets them. Write them at the vault root during setup.

### note.md
```yaml
---
type: Type
_icon: file-text
_color: "#94a3b8"
_order: 0
---

# Note

General docs, drafts, scratchpad, reference content. Use when no other type fits.
```

### raw.md
```yaml
---
type: Type
_icon: inbox
_color: "#ef4444"
_order: 6
_list_properties_display:
  - date
  - status
  - category
  - source
_sort: "property:date:desc"
---

# Raw

Unprocessed source material — transcripts, voice memos, pastes, doc copies, screenshots. Status lifecycle: Unprocessed → Processing → Processed (move to `Raw/archive/`).
```

### summary.md
```yaml
---
type: Type
_icon: file-bar-chart
_color: "#64748b"
_order: 8
_list_properties_display:
  - summary_date
  - summary_type
_sort: "property:summary_date:desc"
---

# Summary

Daily, weekly, or topic summaries. Generated from existing notes.
```

### type.md
```yaml
---
type: Type
_icon: shapes
_color: "#a3a3a3"
_order: 99
---

# Type

The type of types. Type-definition notes live at the vault root with `type: Type`.
```

---

## Methodology-specific type-definition files

These are examples for common methodologies. Write only the ones that match the user's chosen methodology.

### Team / Work

```yaml
---
type: Type
_icon: users
_color: "#3b82f6"
_order: 1
_list_properties_display:
  - date
  - category
  - attendees
_sort: "property:date:desc"
---

# Meeting

1:1s, team syncs, stakeholder reviews. Categories: Data, Design, Engineering, Stakeholder, 1:1, General.
```

```yaml
---
type: Type
_icon: gavel
_color: "#f59e0b"
_order: 2
_list_properties_display:
  - date
  - status
  - related_to
_sort: "property:date:desc"
---

# Decision

ADRs, product calls, pivots. Status: Proposed → Accepted → Deprecated.
```

```yaml
---
type: Type
_icon: target
_color: "#8b5cf6"
_order: 3
_list_properties_display:
  - status
  - priority
  - owner
  - timeline
_sort: "property:priority:asc"
---

# Initiative

Epic-level product work spanning multiple features or quarters.
```

```yaml
---
type: Type
_icon: package
_color: "#10b981"
_order: 4
_list_properties_display:
  - status
  - initiative
  - owner
---

# Feature

Specific shippable feature specs. Usually belongs to an Initiative.
```

```yaml
---
type: Type
_icon: book
_color: "#06b6d4"
_order: 5
_list_properties_display:
  - status
  - source
---

# Research

Reference research with external sources. Used to inform decisions and initiatives.
```

```yaml
---
type: Type
_icon: user
_color: "#ec4899"
_order: 7
_list_properties_display:
  - role
  - team
---

# Person

Team members, stakeholders, contacts. One note per individual.
```

### PARA

```yaml
---
type: Type
_icon: target
_color: "#8b5cf6"
_order: 1
_list_properties_display:
  - status
  - deadline
  - area
_sort: "property:deadline:asc"
---

# Project

Short-term work with a deadline and an end state.
```

```yaml
---
type: Type
_icon: map
_color: "#3b82f6"
_order: 2
---

# Area

Long-term responsibility with a standard to maintain.
```

```yaml
---
type: Type
_icon: book
_color: "#06b6d4"
_order: 3
---

# Resource

Reference material, notes, articles, books, courses.
```

```yaml
---
type: Type
_icon: archive
_color: "#94a3b8"
_order: 4
---

# Archive

Completed or inactive material. Moved here when a project ends or a resource is no longer needed.
```

### Zettelkasten

```yaml
---
type: Type
_icon: pen-tool
_color: "#f59e0b"
_order: 1
---

# Fleeting

Quick capture, temporary notes. Processed into permanent notes.
```

```yaml
---
type: Type
_icon: book-open
_color: "#3b82f6"
_order: 2
---

# Literature

Notes on a paper, book, article. One note per source.
```

```yaml
---
type: Type
_icon: diamond
_color: "#10b981"
_order: 3
---

# Permanent

Evergreen insight, distilled idea. One idea per note.
```

```yaml
---
type: Type
_icon: map
_color: "#8b5cf6"
_order: 4
---

# Index

Map of content, hub note. Links to permanent notes.
```

---

## Daily note template (optional)

Write to `daily/_template.md` only if user opts in.

```markdown
---
type: Note
date: YYYY-MM-DD
---

# YYYY-MM-DD

## Yesterday

-

## Today

-

## Blockers

-

## Notes

-
```

---

## Initial `views/` (optional)

Generic starter views. Adapt to the user's methodology.

### views/unprocessed-raw.yml
```yaml
name: Unprocessed Raw
icon: inbox
sort: "property:date:desc"
filters:
  all:
    - field: type
      op: equals
      value: Raw
    - field: status
      op: equals
      value: Unprocessed
```

### views/active-notes.yml
```yaml
name: Active Notes
icon: file-text
sort: "property:modified:desc"
filters:
  all:
    - field: type
      op: equals
      value: Note
    - field: status
      op: equals
      value: Active
```

---

## Methodology-specific views

### Team / Work — active-initiatives.yml
```yaml
name: Active Initiatives
icon: target
sort: "property:priority:asc"
filters:
  all:
    - field: type
      op: equals
      value: Initiative
    - field: status
      op: equals
      value: Active
```

### Team / Work — recent-meetings.yml
```yaml
name: Recent Meetings
icon: users
sort: "property:date:desc"
filters:
  all:
    - field: type
      op: equals
      value: Meeting
```

### PARA — active-projects.yml
```yaml
name: Active Projects
icon: target
sort: "property:deadline:asc"
filters:
  all:
    - field: type
      op: equals
      value: Project
    - field: status
      op: equals
      value: Active
```

### Zettelkasten — recent-permanent.yml
```yaml
name: Recent Permanent Notes
icon: diamond
sort: "property:modified:desc"
filters:
  all:
    - field: type
      op: equals
      value: Permanent
```

---

## Maintenance log template

Write `logs/maintenance-log.md` with this header on first setup:

```markdown
---
type: Note
date: YYYY-MM-DD
---

# Maintenance Log

Append-only record of structural changes to this vault. Never rewrite history.

## YYYY-MM-DD — Vault bootstrap

### Created
- Folder structure
- Type definitions at vault root
- AGENTS.md
- CLAUDE.md
```

---

## Summary template with source evidence

Use this template when generating any summary. Every summary must include `source_evidence`.

```yaml
---
type: Summary
summary_date: "YYYY-MM-DD"
summary_type: daily                     # daily | weekly | topic
generated_at: YYYY-MM-DDTHH:MM:SS
generated_by: "tolaria-wiki"
source_evidence:
  - note: "[[path/to/source-note]]"
    hash: "abc123"
  - note: "[[path/to/another-note]]"
    hash: "def456"
related_to:
  - "[[topic-or-initiative]]"
---

# Summary: <Today | Week of YYYY-MM-DD | Topic>

## Overview
- **Notes:** N total
- **Key topics:** [linked list]

## Notes by type

### [Type] — [Note title]
**Related:** [[linked notes]]

**Key updates:**
- [bullet]

**Decisions:**
- [decision if noted]

**Action items:**
- [ ] [Owner]: [action] (from [[note-link]])

---

## Blockers identified
- [Description]

## Topics progressed
- [[note-name]]: [brief status update]

---

*Generated: YYYY-MM-DD HH:MM*
```

---

## Raw processing receipt template

When a Raw note is processed, update its frontmatter:

```yaml
---
type: Raw
date: YYYY-MM-DD
status: Processed
category: <type>
source: "path/to/source"
processed_date: YYYY-MM-DD
processed_to: "[[path/to/structured-note]]"
processed_by: "tolaria-wiki"
---
```

---

## Health check report template

Use this when reporting health check results:

```markdown
## YYYY-MM-DD
### Health Check

**Orphans:** N
- `path/to/note.md` — [suggestion]

**Dead Links:** N
- `path/to/note.md` → `[[target]]` (target does not exist) — [suggestion]

**Stale Raw:** N
- `Raw/YYYY-MM-topic.md` — >30 days unprocessed

**Empty Notes:** N
- `path/to/note.md` — [suggestion]

**Missing Fields:** N
- `path/to/note.md` — missing [field]

### Actions Taken
- [what was fixed]
- [what was flagged for user]
```

---

## Context pack template

Use this when recording a context pack for an operation:

```markdown
## YYYY-MM-DD
### Context Pack: [Operation Name]
- Index: N notes ([criteria])
- Notes read: N
- Total vault notes: N
- Notes included:
  - "[[note-1]]"
  - "[[note-2]]"
```

---

## Subagent templates

### Health-checker subagent frontmatter
```yaml
---
name: tolaria-health-checker
description: Run diagnostics on a Tolaria vault in isolation.
skills:
  - tolaria-wiki
---
```

### Raw-processor subagent frontmatter
```yaml
---
name: tolaria-raw-processor
description: Process unambiguous Raw notes in a Tolaria vault in isolation.
skills:
  - tolaria-wiki
---
```

### Summary-generator subagent frontmatter
```yaml
---
name: tolaria-summary-generator
description: Generate summaries with bounded context in a Tolaria vault in isolation.
skills:
  - tolaria-wiki
---
```

---

## Sample seed notes (optional)

Write to `_examples/` (folder the user can delete after learning). One of each major type.

### Generic example: note.md
```markdown
---
type: Note
date: 2026-01-15
status: Active
related_to:
  - "[[example-project]]"
---

# Example note — Getting started with Tolaria

This is an example note to demonstrate the Tolaria format.

## Key points

- Every note has a `type:` in frontmatter
- The first H1 is the display title
- Use `[[wikilinks]]` to cross-reference

## Next steps

- Create your own notes
- Link them together
- Process Raw notes when ready
```

### Generic example: raw.md
```markdown
---
type: Raw
date: 2026-01-15
status: Unprocessed
category: Doc
source: "https://example.com/article"
source_type: "Article"
---

# Example Raw — Article clip

This is an example Raw note. Raw notes are unprocessed source material.

< pasted content from external source >

## Key quotes

- "Important quote from the source"
- "Another insight"
```

### Team / Work example: meeting.md
```markdown
---
type: Meeting
date: 2026-01-15
category: Engineering
attendees:
  - "[[example-person]]"
related_to:
  - "[[example-initiative]]"
---

# 2026-01-15 — Sprint Planning

## Topics

- Sprint goal
- Story estimation

## Decisions

- Sprint goal: ship the auth refactor end-to-end.

## Action items

- [ ] [[example-person]]: write the auth migration plan by Friday
- [ ] [[example-person]]: review the API contract changes

## Next steps

- Re-check progress at Wednesday standup.
```

### Team / Work example: initiative.md
```markdown
---
type: Initiative
status: Active
priority: P1
owner: "[[example-person]]"
timeline: "Q1 2026"
---

# Example initiative — Auth refactor

## Goal

Replace session-based auth with stateless JWT, no user-visible behavior change.

## Scope

- Token issuance and refresh
- Server-side validation middleware
- Cookie → header migration path

## Out of scope

- OAuth providers (separate initiative)
- Admin role changes

## Milestones

- [ ] Migration plan written
- [ ] Shadow mode in staging
- [ ] Cutover
- [ ] Old code removed

## Open questions

- Token lifetime?
- Refresh strategy?
```

### PARA example: project.md
```markdown
---
type: Project
status: Active
deadline: "2026-03-15"
area: "[[home-maintenance]]"
---

# Kitchen renovation

## Goal

Complete kitchen renovation by March 15.

## Tasks

- [ ] Demo old cabinets
- [ ] Install new cabinets
- [ ] Countertop installation
- [ ] Backsplash

## Resources

- [[kitchen-design-inspiration]]
- [[contractor-contact]]
```

### Zettelkasten example: permanent.md
```markdown
---
type: Permanent
related_to:
  - "[[network-effects]]"
  - "[[platform-economics]]"
---

# Network effects are non-linear

The value of a network grows non-linearly with the number of participants.

## Key insight

Metcalfe's Law: value is proportional to n², not n.

## Sources

- [[literature/smith-2024-network-effects]]
```
