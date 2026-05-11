# Templates — copy-paste content for setup

Every file the setup workflow writes. Self-contained — no external dependencies.

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

# Initiative
```

## Relationships

Any frontmatter property whose value contains `[[wikilinks]]` is a relationship. Common keys: `related_to`, `belongs_to`, `attendees`, `owner`, `initiative`, `source`. Custom names are valid.

Quoted wikilinks for scalar frontmatter values. YAML lists for multi-value.

## Wikilinks

- `[[filename]]` — link by filename
- `[[Note Title]]` — link by H1
- `[[filename|display text]]` — custom label

Works in frontmatter and body.

## Views

Saved views live in `views/*.yml`. Filename is the stable view ID — use kebab-case (`active-initiatives.yml`).

```yaml
name: Active Initiatives
icon: null
color: null
sort: "property:status:asc"
filters:
  all:
    - field: type
      op: equals
      value: Initiative
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

## What agents should do

- Create and edit notes using the frontmatter and H1 conventions above.
- Add or modify relationships without breaking existing wikilinks.
- Create and edit saved views in `views/`.

## What agents should avoid

- Do not move existing type files out of the vault root unless explicitly asked.
- Do not treat files in `attachments/` as notes.
- Do not silently overwrite an existing `AGENTS.md`.
- Do not modify `_`-prefixed keys without explicit config-editing intent.
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
- Creating notes (Meeting, Decision, Initiative, Feature, Research, Person, Note, Raw)
- Processing raw notes, importing meeting recordings, generating summaries
- Connecting external sources (recorders, transcripts, Slack, Jira/Linear)

If a task touches the vault and `tolaria-wiki` isn't being used, run `/memory` to confirm it's loaded.

## Hard rules

- **IMPORTANT**: <CONFIDENTIALITY-DEFAULT — e.g., "Treat anything in `meetings/stakeholder/` as confidential by default. Never share or summarize outside this vault unless explicitly asked in the current message.">
- **IMPORTANT**: Never invent dates, attendees, decisions, or quotes. If uncertain, say so explicitly and ask.
- Never delete a note. Move to `archive/` (or `Raw/archive/`) or change status to `Archived` / `Stale` instead.
- Never modify files in `attachments/`, `views/`, `.claude/`, `.tolaria/`, or `.obsidian/` as if they were notes.
- Frontmatter keys starting with `_` are Tolaria-managed. Don't touch unless explicitly editing config.
- Use `[[wikilinks]]`, not markdown links, for cross-references.

## Workflow

- Make minimal changes — do not "improve" notes I didn't ask you to change.
- After completing any task: list what changed, what's untouched, what needs my attention.
- When type, category, owner, or destination folder is unclear, ask before filing.
- Append structural changes (new initiative, processed Raw → archive, status moves) to `logs/maintenance-log.md`.

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

## Type-definition files (vault root)

Write one of each at the vault root during setup.

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

### meeting.md
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

### decision.md
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

### initiative.md
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

### feature.md
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

### research.md
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

Unprocessed source material — transcripts, voice memos, Slack pastes, doc copies, screenshots. Status lifecycle: Unprocessed → Processing → Processed (move to `Raw/archive/`).
```

### person.md
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
  - meeting_count
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

If the user wants opinionated starter views, write these:

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

### views/active-initiatives.yml
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

### views/recent-meetings.yml
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

### views/open-decisions.yml
```yaml
name: Open Decisions
icon: gavel
sort: "property:date:desc"
filters:
  all:
    - field: type
      op: equals
      value: Decision
    - field: status
      op: equals
      value: Proposed
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

## Sample seed notes (optional)

Write to `_examples/` (folder the user can delete after learning). One of each major type.

### `_examples/example-meeting.md`
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

### `_examples/example-initiative.md`
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

### `_examples/example-decision.md`
```markdown
---
type: Decision
date: 2026-01-10
status: Accepted
related_to:
  - "[[example-initiative]]"
---

# Use Zod for runtime validation

## Context

We need runtime validation on all API boundaries. TypeScript types disappear at runtime.

## Options considered

- Zod — schema-first, infers types
- Joi — mature, no TS inference
- Hand-rolled validators

## Decision

Zod. The TS-inference benefit outweighs the bundle-size cost for our API surface.

## Consequences

- All `/api/*` handlers parse input with a Zod schema before doing work.
- Error messages from Zod become user-facing — wrap them in our standard error envelope.
```

### `_examples/example-person.md`
```markdown
---
type: Person
role: Senior Engineer
team: Platform
email: alex@example.com
---

# Alex Example

## Role

Senior Engineer on the Platform team. Owns the auth and observability stacks.

## Working on

- [[example-initiative]]

## Communication

- Prefers Slack DM for quick stuff
- Calendar tends to be packed; book 30 min slots
- Strong with TypeScript, learning Rust

## Notes

- Background in infra; came from $previous-company in 2024.
```
