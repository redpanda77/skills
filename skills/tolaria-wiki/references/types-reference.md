# Types — schemas, routing, naming

The canonical reference for every note type. Read this when authoring (`authoring.md`) or maintaining (`maintenance.md`).

## Type table

| Type | Use for | Required frontmatter | Optional |
|------|---------|----------------------|----------|
| **Raw** | Unprocessed source material (transcripts, dumps, Slack pastes, screenshots, doc copies) | `type`, `date`, `status` | `category`, `source`, `source_type`, `related_to` |
| **Note** | General docs, scratchpad, drafts, reference content | `type` | `status`, `related_to`, `url` |
| **Meeting** | 1:1s, syncs, reviews | `type`, `date`, `attendees` | `category`, `related_to`, `status` |
| **Decision** | ADRs, product calls, pivots | `type`, `date`, `status` | `related_to`, `owner` |
| **Initiative** | Epic-level ongoing work | `type`, `status` | `priority`, `owner`, `timeline`, `related_to` |
| **Feature** | Specific feature specs | `type`, `status` | `initiative`, `owner`, `related_to` |
| **Research** | Reference research with external sources | `type` | `source`, `related_to`, `status` |
| **Person** | One per team member, stakeholder, contact | `type` | `role`, `team`, `email`, `related_to` |
| **Summary** | Daily / weekly / topic summaries (generated) | `type`, `summary_date`, `summary_type`, `generated_at` | `meeting_count`, `related_to` |
| **Type** | Type-definition notes at vault root (config) | `type: Type` | `_icon`, `_color`, `_order`, `_list_properties_display`, `_sort` |

## Frontmatter shape per type

### Raw
```yaml
---
type: Raw
date: 2026-05-11
status: Unprocessed       # Unprocessed | Processing | Processed | Stale
category: Meeting          # Meeting | Slack | Doc | Voice | Screenshot | Other
source: <path | URL | "[[wikilink]]">
source_type: <e.g., "Voice Recording", "Slack Thread", "Google Doc">
---
```

### Meeting
```yaml
---
type: Meeting
date: 2026-05-11
category: Data             # Data | Design | Engineering | Stakeholder | 1:1 | General
attendees:
  - "[[person-1]]"
  - "[[person-2]]"
related_to:
  - "[[initiative-or-feature]]"
---
```

### Decision
```yaml
---
type: Decision
date: 2026-05-11
status: Accepted           # Proposed | Accepted | Deprecated
related_to:
  - "[[affected-initiative]]"
---
```

### Initiative
```yaml
---
type: Initiative
status: Active             # Draft | Active | In Review | Completed | Archived | Blocked
priority: P1               # P0 | P1 | P2
owner: "[[person]]"
timeline: "Q2 2026"
related_to:
  - "[[motivating-research]]"
---
```

### Feature
```yaml
---
type: Feature
status: Active
initiative: "[[parent-initiative]]"
owner: "[[person]]"
---
```

### Research
```yaml
---
type: Research
status: Active
source: https://...
related_to:
  - "[[initiative]]"
---
```

### Person
```yaml
---
type: Person
role: <e.g., Engineer, Designer, Stakeholder>
team: <e.g., Search Ranking>
email: name@example.com
---
```

### Summary
```yaml
---
type: Summary
summary_date: "2026-05-11"           # or "2026-05-04 to 2026-05-11" for weekly
summary_type: daily                   # daily | weekly | topic
meeting_count: 4
generated_at: 2026-05-11T15:30:00
related_to:
  - "[[topic]]"
---
```

### Note (minimal)
```yaml
---
type: Note
status: Draft                          # optional
---
```

## How to choose between similar types

- **Note vs Research** — Research has explicit external sources and informs decisions. Plain reference info is Note.
- **Initiative vs Feature** — Initiative is multi-quarter, multi-feature, epic-level. Feature is one shippable thing inside (or independent of) an initiative.
- **Decision vs Note** — Decision has explicit status (Proposed / Accepted / Deprecated) and is irreversible record. Note is mutable.
- **Meeting vs Raw** — Raw is the unprocessed dump (transcript, voice memo). Meeting is the structured note created from it.
- **Person vs Note about a person** — One Person note per individual. Notes *about* the relationship or specific 1:1s go in `meetings/general/`.

## Folder routing

| Type | Folder | Example |
|------|--------|---------|
| Raw | `Raw/` | `Raw/2026-05-11-ds-huddle.md` |
| Raw (after processing) | `Raw/archive/` | `Raw/archive/2026-05-04-ds-huddle.md` |
| Meeting (Data) | `meetings/data/` | `meetings/data/2026-05-ranking-sync.md` |
| Meeting (Design) | `meetings/design/` | `meetings/design/2026-05-ux-review.md` |
| Meeting (Engineering) | `meetings/engineering/` | `meetings/engineering/2026-05-sprint-planning.md` |
| Meeting (Stakeholder) | `meetings/stakeholder/` | `meetings/stakeholder/2026-05-leadership.md` |
| Meeting (1:1, General) | `meetings/general/` | `meetings/general/2026-05-<person>-1on1.md` |
| Decision | `decisions/` | `decisions/use-zod-for-api-validation.md` |
| Initiative | `initiatives/` | `initiatives/ai-personalization-initiative.md` |
| Feature | `features/` | `features/favorites-overflow-menu.md` |
| Research | `research/` | `research/multi-stage-ranking-survey.md` |
| Person | `people/` | `people/mohamed-dahroug.md` |
| Daily Note | `daily/` | `daily/2026-05-11.md` |
| Summary (daily) | `summaries/` | `summaries/daily-2026-05-11.md` |
| Summary (weekly) | `summaries/` | `summaries/weekly-2026-05-04-to-2026-05-11.md` |
| Summary (topic) | `summaries/` | `summaries/topic-ai-personalization.md` |
| Note | wherever fits — `notes/` if it exists, vault root otherwise | — |
| Type definition | vault root | `feature.md`, `decision.md` |

If meeting subfolders don't exist (the user opted for flat `meetings/`), file everything under `meetings/` and ignore the category subfolder mapping.

## Raw → destination mapping

When processing a Raw note, use `category:` to pick the destination type.

| Raw `category` | Destination type | Destination folder |
|----------------|------------------|---------------------|
| Meeting | Meeting | `meetings/<meeting-category>/` |
| Slack | Meeting OR Initiative | `meetings/general/` or `initiatives/` |
| Doc | Initiative OR Feature OR Research | `initiatives/` or `features/` or `research/` |
| Voice | Meeting | `meetings/general/` (or whichever category the content implies) |
| Screenshot | Decision OR Research | `decisions/` or `research/` |
| Other | Determine from content | Varies — ask if unclear |

## Filename conventions

All filenames are **kebab-case**, lowercase, `.md` extension.

| Type | Pattern | Example |
|------|---------|---------|
| Raw | `YYYY-MM-DD-category-topic` | `2026-05-04-ds-huddle.md` |
| Meeting (monthly recurring) | `YYYY-MM-topic` | `2026-05-search-sync.md` |
| Meeting (one-off) | `YYYY-MM-DD-topic` | `2026-05-11-leadership-q2-review.md` |
| Meeting (1:1) | `YYYY-MM-<person>-1on1` | `2026-05-mohamed-1on1.md` |
| Decision | `descriptive-kebab` | `use-zod-for-api-validation.md` |
| Initiative | `descriptive-kebab[-initiative]` | `ai-personalization-initiative.md` |
| Feature | `descriptive-kebab` | `favorites-overflow-menu.md` |
| Research | `descriptive-kebab` | `multi-stage-ranking-survey.md` |
| Person | `firstname-lastname` | `mohamed-dahroug.md` |
| Daily | `YYYY-MM-DD` | `daily/2026-05-11.md` |
| Summary (daily) | `daily-YYYY-MM-DD` | `daily-2026-05-11.md` |
| Summary (weekly) | `weekly-YYYY-MM-DD-to-YYYY-MM-DD` | `weekly-2026-05-04-to-2026-05-11.md` |
| Summary (topic) | `topic-<kebab>` | `topic-ai-personalization.md` |
| Type definition | `<typename>` (lowercase, no kebab, vault root) | `feature.md`, `decision.md` |

Rules:
- No spaces, no underscores in filenames (except leading underscore for vault-meta like `_roster.md`).
- Dates always `YYYY-MM-DD` or `YYYY-MM`.
- Keep filenames short: 3–6 words.
- If a name collides, prepend the date or add a disambiguator (`-v2`, `-q2`) — ask the user.

## Status lifecycles

### Universal (Note, Initiative, Feature, Research, Squad Status)

```
Draft → Active → In Review → Completed
              ↓                  ↓
           Blocked            Archived
```

### Raw

```
Unprocessed → Processing → Processed
                  ↓
               Stale (abandoned)
```

### Decision

```
Proposed → Accepted
              ↓
          Deprecated
```

## Default status at creation

| Type | Default |
|------|---------|
| Raw | `Unprocessed` |
| Note | `Draft` (omit if stable reference) |
| Meeting | omit (date carries temporal context) |
| Decision | `Proposed` |
| Initiative | `Active` if work is starting, else `Draft` |
| Feature | `Draft` |
| Research | `Active` |
| Person | omit |
| Summary | omit |

## Relationship keys

Common relationship keys (any frontmatter property with `[[wikilinks]]` is a relationship):

| Key | Meaning |
|-----|---------|
| `related_to` | General "this is related to" — most common, multi-value |
| `belongs_to` | Hierarchical containment (legacy — preserve when editing notes that use it) |
| `attendees` | Meeting participants — multi-value list of `[[person]]` |
| `owner` | Single accountable person — scalar `"[[person]]"` |
| `initiative` | Feature → parent initiative — scalar `"[[initiative]]"` |
| `source` | Raw → upstream artifact (URL, path, or wikilink) |
| `processed_to` | Raw → its structured-note destination after processing |

Custom relationship names (`reports_to`, `depends_on`) are valid. Use when they add clarity.
