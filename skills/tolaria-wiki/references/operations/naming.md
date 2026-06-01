# Naming Conventions

**When to read this:** When naming a new file, folder, frontmatter key, or type. Also when setting up a vault and defining folder structure. For file format rules, see `references/operations/format.md`.

Single source of truth for all naming in the vault. Every file, folder, key, and type follows these rules.

## File naming

### Base rule

All filenames are **kebab-case**, lowercase, `.md` extension.

- `kebab-case.md` ✓
- `CamelCase.md` ✗
- `snake_case.md` ✗
- `with spaces.md` ✗
- `Mixed-Case.md` ✗

### Type-specific patterns

| Type | Pattern | Examples |
|------|---------|----------|
| Raw | `YYYY-MM-DD-<topic>` | `2026-05-11-ds-huddle.md` |
| Meeting (recurring) | `YYYY-MM-<topic>` | `2026-05-search-sync.md` |
| Meeting (one-off) | `YYYY-MM-DD-<topic>` | `2026-05-11-leadership-q2-review.md` |
| Meeting (1:1) | `YYYY-MM-<firstname>-1-on-1.md` | `2026-05-mohamed-1-on-1.md` |
| Decision | `<descriptive-kebab>` | `use-zod-for-api-validation.md` |
| Initiative | `<descriptive-kebab>` | `ai-personalization-initiative.md` |
| Feature | `<descriptive-kebab>` | `favorites-overflow-menu.md` |
| Research | `<descriptive-kebab>` | `multi-stage-ranking-survey.md` |
| Person | `<firstname>-<lastname>` | `mohamed-dahroug.md` |
| Daily | `YYYY-MM-DD` | `daily/2026-05-11.md` |
| Summary (daily) | `daily-YYYY-MM-DD` | `summaries/daily-2026-05-11.md` |
| Summary (weekly) | `weekly-YYYY-MM-DD-to-YYYY-MM-DD` | `summaries/weekly-2026-05-04-to-2026-05-11.md` |
| Summary (topic) | `topic-<kebab>` | `summaries/topic-ai-personalization.md` |
| Type definition | `<typename>` (lowercase, vault root) | `feature.md`, `decision.md` |
| System doc | `README.md`, `VAULT.md`, `CHANGELOG.md` | vault root or `system/` |

### Rules

- No spaces, no underscores (except leading `_` for meta like `_roster.md`).
- Dates always `YYYY-MM-DD` or `YYYY-MM`.
- Keep filenames short: 3–6 words, not counting the date.
- Never use `.txt`, `.markdown`, or other extensions. Always `.md`.

### Collision handling

If a filename already exists:

1. **Same entity?** Same topic, same date, same people → update the existing file, don't create a new one.
2. **Different entity?** Add a disambiguator:
   - By date: `2026-05-11-topic.md` (if the existing one is `2026-05-04-topic.md`)
   - By version: `topic-v2.md`, `topic-v2.md` (rare, use for major revisions)
   - By quarter: `topic-q2.md`, `topic-q3.md` (for recurring initiatives)
   - By context: `topic-data-team.md`, `topic-platform-team.md`
3. **Never overwrite without confirmation.**
4. **Never append numbers blindly** (`topic-2.md` is unclear; `topic-data-team.md` is clear).

### Archive naming

When moving a note to `archive/`:
- Keep the original filename.
- Add `archived-YYYY-MM-DD-` prefix if it helps: `archive/archived-2026-05-11-use-zod.md`.
- Or keep it simple: `archive/use-zod-for-api-validation.md`.

## Folder naming

### Base rule

All folder names are **kebab-case**, lowercase.

- `meetings/` ✓
- `MeetingNotes/` ✗
- `meeting_notes/` ✗
- `MyVault/` ✗

### Folder structure

```
meetings/           # Meeting notes, subfoldered by category
  data/
  design/
  engineering/
  stakeholder/
  general/          # 1:1s, ad-hoc, uncategorized
initiatives/        # Epic-level work
features/           # Specific feature specs
research/           # Reference research
decisions/          # ADRs and product calls
people/             # Team members, stakeholders
daily/              # Daily standup notes
Raw/                # Inbox — unprocessed source material
  archive/          # Processed Raw originals
summaries/          # Generated summaries
logs/               # Maintenance log (append-only)
attachments/        # Binary assets (images, PDFs)
views/              # Tolaria saved views (*.yml)
system/             # Vault system documentation
  README.md         # Vault purpose and quickstart
  VAULT.md          # System conventions (single source of truth)
  CHANGELOG.md      # Changes to vault conventions
archive/            # Archived notes (optional, for vault-wide archive)
```

### Folder rules

1. **No notes at root.** Only type-definition files (`feature.md`, `decision.md`) and system docs (`VAULT.md`, `README.md`) live at root.
2. **Folder size limit.** If a folder has >50 files, create subfolders by year (`2026/`, `2025/`) or by subcategory.
3. **Subfolder depth max 2.** Never nest deeper than `meetings/data/2026/`. Deep nesting makes browsing hard.
4. **Archive early.** Move notes to `archive/` when status is `Archived` or when the note is >1 year old and no longer active.
5. **One domain per folder.** Don't mix types in one folder. `meetings/` has only meetings. `initiatives/` has only initiatives.

### When to create a new folder

- Create a subfolder when a folder has >50 files.
- Create a new top-level folder when a new note type is introduced (e.g., `experiments/` for `Experiment` type).
- Don't create folders for one-off notes. Use a general-purpose folder (e.g., `meetings/general/` for ad-hoc meetings).
- Don't create a folder per person. Person notes go in `people/`. Meetings with that person go in `meetings/general/` or `meetings/stakeholder/`.

### When to flatten

- If a category has <5 files, don't create a subfolder. Use the parent folder or `general/`.
- If subfolders are mostly empty, collapse them.
- If a folder is rarely accessed, consider archiving its contents.

## Frontmatter key naming

### Base rule

All frontmatter keys are **snake_case**, lowercase.

- `related_to` ✓
- `summary_date` ✓
- `SummaryDate` ✗
- `summary-date` ✗

### Tolaria-managed keys

Keys starting with `_` are managed by the Tolaria app. Never modify them unless explicitly editing config.

- `_icon`
- `_color`
- `_order`
- `_organized`
- `_list_properties_display`
- `_sort`
- `_edited`

### Reserved keys

These keys have special meaning. Don't use them for other purposes:

- `type` — note type
- `status` — lifecycle status
- `date` — note date
- `related_to` — cross-links
- `attendees` — meeting participants
- `owner` — accountable person
- `initiative` — parent initiative
- `source` — upstream artifact
- `source_type` — type of upstream artifact
- `source_evidence` — generated note provenance
- `processed_to` — Raw → structured mapping
- `processed_date` — when Raw was processed
- `processed_by` — agent that processed Raw
- `summary_date` — summary date or range
- `summary_type` — daily | weekly | topic
- `generated_at` — generation timestamp
- `generated_by` — agent that generated
- `category` — Raw or Meeting category

### Custom keys

Custom keys are valid. Use them when they add clarity:

- `timeline` — Initiative timeline
- `priority` — Initiative priority (P0, P1, P2)
- `role` — Person role
- `team` — Person team
- `email` — Person email
- `url` — Note URL
- `confidential` — boolean flag

## Type naming

### Type-definition files

Type-definition files at vault root are **lowercase**, matching the type name:

- `meeting.md` defines `type: Meeting`
- `decision.md` defines `type: Decision`
- `initiative.md` defines `type: Initiative`

### Type values

Type values in frontmatter are **capitalized**:

- `Meeting`, `Decision`, `Initiative`, `Feature`, `Research`, `Note`, `Raw`, `Person`, `Summary`, `Type`

### Status values

Status values are **capitalized**:

- `Draft`, `Active`, `In Review`, `Completed`, `Blocked`, `Archived`, `Stale`
- `Unprocessed`, `Processing`, `Processed`
- `Proposed`, `Accepted`, `Deprecated`

## View naming

View files live in `views/` and are named with **kebab-case**, `.yml` extension:

- `active-initiatives.yml`
- `unprocessed-raw.yml`
- `recent-meetings.yml`

The filename is the stable view ID. Never create `.view.json` files.

## Date formats

- **Frontmatter dates:** `YYYY-MM-DD` (e.g., `2026-05-11`)
- **Filename dates:** `YYYY-MM-DD` or `YYYY-MM` (e.g., `2026-05-11` or `2026-05`)
- **Timestamps:** `YYYY-MM-DDTHH:MM:SS` (e.g., `2026-05-11T15:30:00`)
- **Date ranges:** `YYYY-MM-DD to YYYY-MM-DD` (e.g., `2026-05-04 to 2026-05-11`)

## Summary

| What | Format | Example |
|------|--------|---------|
| File names | kebab-case | `ai-personalization-initiative.md` |
| Folder names | kebab-case | `meetings/data/` |
| Frontmatter keys | snake_case | `related_to`, `summary_date` |
| Type values | Capitalized | `Meeting`, `Initiative` |
| Status values | Capitalized | `Active`, `Processed` |
| View files | kebab-case.yml | `active-initiatives.yml` |
| Dates | `YYYY-MM-DD` | `2026-05-11` |
| Timestamps | `YYYY-MM-DDTHH:MM:SS` | `2026-05-11T15:30:00` |
