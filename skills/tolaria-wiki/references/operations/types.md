# Types — Generic Type System Framework

**When to read this:** When creating a note and you need to know what type to use, what frontmatter is required, or how to define a new type. Read after `references/operations/authoring.md` if the type is unclear.

## What is a Type?

A `type` is a schema contract. It defines:
- **Required frontmatter** — what fields must be present
- **Optional frontmatter** — what fields may be present
- **Status lifecycle** — valid states and transitions
- **Folder routing** — where notes of this type live
- **Relationship keys** — how this type connects to others

Types are domain-specific. A work vault uses `Meeting`, `Initiative`, `Decision`. A research vault uses `Paper`, `Experiment`, `Hypothesis`. A personal vault uses `Project`, `Area`, `Resource`. The skill generates type-definition files based on the user's domain during setup.

## The Universal Type System

Every type, regardless of domain, follows the same rules:

### Frontmatter
- `type:` is **required** on every note. Capitalized value.
- `status:` is required on most types (except `Note`, `Person`, `Type` when not applicable).
- `date:` is required when the note has a temporal anchor.
- `related_to:` is the universal relationship key — any note can link to any other note.

### Status Lifecycles

All types share one of these lifecycles:

**Universal (most structured types):**
```
Draft → Active → In Review → Completed
  |         |           |
  v         v           v
Blocked   Archived    Archived
```

**Raw (inbox material):**
```
Unprocessed → Processing → Processed
                  |
                  v
               Stale (abandoned)
```

**Decision (irreversible record):**
```
Proposed → Accepted
              |
              v
          Deprecated
```

### Default Status at Creation

| Type | Default |
|------|---------|
| Raw | `Unprocessed` |
| Note | `Draft` (omit if stable reference) |
| Decision | `Proposed` |
| Most structured types | `Draft` or `Active` depending on intent |

### Valid State Transitions

| From | To | Trigger |
|------|-----|---------|
| Draft | Active | User or agent ratification |
| Active | In Review | User or agent request |
| In Review | Completed | User or agent approval |
| Active | Blocked | Dependency identified |
| Blocked | Active | Dependency resolved |
| Any | Archived | Obsolete |
| Unprocessed | Processing | Agent starts processing |
| Processing | Processed | Structured note created |
| Unprocessed | Stale | >30 days, abandoned |
| Proposed | Accepted | User ratifies |
| Accepted | Deprecated | Newer decision supersedes |

### Invalid Transitions (refuse)

| From | To | Reason |
|------|-----|---------|
| Processed | Unprocessed | Raw is immutable |
| Archived | Active | Must create new note |
| Completed | Draft | Must create new note |
| Stale | Unprocessed | Must create new Raw |
| Deprecated | Accepted | Must create new decision |

## Example Domain: Team / Work

Common types for team and project work:

| Type | Use for | Required | Optional |
|------|---------|----------|----------|
| **Meeting** | 1:1s, syncs, reviews | `type`, `date`, `attendees` | `category`, `related_to`, `status` |
| **Decision** | ADRs, product calls, pivots | `type`, `date`, `status` | `related_to`, `owner` |
| **Initiative** | Epic-level ongoing work | `type`, `status` | `priority`, `owner`, `timeline`, `related_to` |
| **Feature** | Specific feature specs | `type`, `status` | `initiative`, `owner`, `related_to` |
| **Research** | Reference research with external sources | `type` | `source`, `related_to`, `status` |
| **Person** | One per team member, stakeholder | `type` | `role`, `team`, `email`, `related_to` |
| **Summary** | Daily / weekly / topic summaries | `type`, `summary_date`, `summary_type`, `generated_at` | `meeting_count`, `related_to` |

### Folder routing (Team / Work)

| Type | Folder | Example |
|------|--------|---------|
| Meeting | `meetings/<category>/` | `meetings/data/2026-05-sync.md` |
| Decision | `decisions/` | `decisions/use-zod-for-api-validation.md` |
| Initiative | `initiatives/` | `initiatives/ai-personalization-initiative.md` |
| Feature | `features/` | `features/favorites-overflow-menu.md` |
| Research | `research/` | `research/multi-stage-ranking-survey.md` |
| Person | `people/` | `people/mohamed-dahroug.md` |
| Summary | `summaries/` | `summaries/daily-2026-05-11.md` |
| Raw | `Raw/` | `Raw/2026-05-11-ds-huddle.md` |

### Relationship keys (Team / Work)

| Key | Meaning | Applies to |
|-----|---------|------------|
| `attendees` | Meeting participants | Meeting |
| `owner` | Single accountable person | Initiative, Feature, Decision |
| `initiative` | Feature → parent initiative | Feature |
| `source` | Raw → upstream artifact | Raw, Research |
| `processed_to` | Raw → structured destination | Raw |
| `source_evidence` | Generated note → sources | Summary |

## Example Domain: Personal / PARA

Common types for personal productivity (PARA methodology):

| Type | Use for | Required | Optional |
|------|---------|----------|----------|
| **Project** | Short-term work with a deadline | `type`, `status` | `deadline`, `area`, `related_to` |
| **Area** | Long-term responsibility | `type` | `status`, `related_to` |
| **Resource** | Reference material, notes, articles | `type` | `source`, `tags`, `related_to` |
| **Archive** | Completed / inactive material | `type` | `archived_date`, `related_to` |
| **Daily** | Daily journal / standup | `type`, `date` | `mood`, `energy`, `related_to` |

### Folder routing (Personal / PARA)

| Type | Folder | Example |
|------|--------|---------|
| Project | `projects/` | `projects/kitchen-renovation.md` |
| Area | `areas/` | `areas/health-and-fitness.md` |
| Resource | `resources/` | `resources/obsidian-tips.md` |
| Archive | `archive/` | `archive/completed-project.md` |
| Daily | `daily/` | `daily/2026-05-11.md` |
| Raw | `Raw/` | `Raw/2026-05-11-article-clip.md` |

## Example Domain: Research / Zettelkasten

Common types for research and writing:

| Type | Use for | Required | Optional |
|------|---------|----------|----------|
| **Fleeting** | Quick capture, temporary notes | `type`, `date` | `source`, `related_to` |
| **Literature** | Notes on a paper, book, article | `type`, `source` | `author`, `date`, `related_to` |
| **Permanent** | Evergreen insight, distilled idea | `type` | `related_to`, `tags` |
| **Index** | Map of content, hub note | `type` | `related_to` |
| **Experiment** | Lab notes, data, observations | `type`, `date` | `hypothesis`, `results`, `related_to` |

### Folder routing (Research / Zettelkasten)

| Type | Folder | Example |
|------|--------|---------|
| Fleeting | `fleeting/` | `fleeting/2026-05-11-idea.md` |
| Literature | `literature/` | `literature/smith-2024-network-effects.md` |
| Permanent | `permanent/` | `permanent/network-effects-are-non-linear.md` |
| Index | `index/` | `index/network-effects.md` |
| Experiment | `experiments/` | `experiments/2026-05-ab-test-results.md` |
| Raw | `Raw/` | `Raw/2026-05-11-paper-clip.md` |

## How to Choose Between Similar Types

- **Note vs Research** — Research has explicit external sources and informs decisions. Plain reference info is Note.
- **Initiative vs Feature** — Initiative is multi-quarter, multi-feature, epic-level. Feature is one shippable thing.
- **Decision vs Note** — Decision has explicit status (Proposed / Accepted / Deprecated) and is irreversible. Note is mutable.
- **Meeting vs Raw** — Raw is the unprocessed dump. Meeting is the structured note created from it.
- **Project vs Area (PARA)** — Project has a deadline and an end state. Area is ongoing responsibility.
- **Fleeting vs Literature vs Permanent (Zettelkasten)** — Fleeting is temporary capture. Literature is about a specific source. Permanent is a distilled insight.

## How to Define a Custom Type

1. Pick a **capitalized name** (e.g., `Experiment`, `Recipe`, `Trip`).
2. Decide **required frontmatter** — what every note of this type must have.
3. Decide **optional frontmatter** — what it may have.
4. Decide **status lifecycle** — Universal, Raw, or Decision.
5. Decide **folder routing** — where notes of this type live.
6. Decide **relationship keys** — how this type connects to others.
7. Write a **type-definition file** at vault root: `experiment.md` with `type: Type`.

### Type-definition file template

```yaml
---
type: Type
_icon: flask
_color: "#3b82f6"
_order: 0
_list_properties_display:
  - status
  - hypothesis
  - related_to
_sort: "property:status:asc"
---

# Experiment

Lab notes, data, and observations.
```

## Verification Rules

Every note must pass verification before being written:

1. `type:` must be present and match a type-definition file.
2. `status:` must be present (except when type defaults to omit).
3. Required fields for the type must be present.
4. Wikilinks in frontmatter must be quoted (`"[[name]]"`).
5. Dates must be `YYYY-MM-DD` format.
6. Filenames must be kebab-case, no spaces, no underscores.

## Collision Handling

If a filename already exists:

1. Check if the existing note is the same entity. If yes, update it.
2. If different, add a disambiguator: `topic-name-2.md`, `topic-name-alt.md`.
3. Never overwrite without confirmation.

See `references/operations/naming.md` for naming rules and `references/operations/health.md` for verification procedures.
