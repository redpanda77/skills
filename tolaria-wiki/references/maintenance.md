# Maintenance — process raw, import sources, generate summaries

For operating an existing vault: handling inbox material, generating periodic summaries, keeping the log clean.

## Three core operations

1. **Process raw** — convert `Raw/X.md` into a structured note in the right folder.
2. **Import external** — bring material from outside the vault (recordings, transcripts, Slack copies, docs) in as Raw notes.
3. **Generate summaries** — daily / weekly / topic / squad-status summaries from existing notes.

Plus: maintaining `logs/maintenance-log.md`.

---

## 1. Processing raw notes

### Find unprocessed Raw

```bash
grep -l "status: Unprocessed" Raw/*.md 2>/dev/null
```

Or by date:

```bash
ls Raw/*.md | head -20
```

### Per-Raw procedure

For each unprocessed file:

1. Read the file. Confirm `status:` is `Unprocessed` (or absent).
2. Change status: `Unprocessed → Processing` in frontmatter.
3. Decide destination type from `category:` + content. See `types-reference.md` § "Raw → destination mapping".
4. Create the structured note using `authoring.md` § "The 7-step procedure".
5. Update the Raw:
   ```yaml
   status: Processed
   processed_date: YYYY-MM-DD
   processed_to: "[[path/to/structured]]"
   ```
6. Move: `Raw/X.md` → `Raw/archive/X.md`.
7. Append to `logs/maintenance-log.md`:
   ```markdown
   ## YYYY-MM-DD
   ### Processed
   - Raw/X.md → meetings/category/YYYY-MM-topic.md
   ```

### Batch processing

When the user says "process all raw notes":

1. List all unprocessed Raw files.
2. Show the user the count and one-line summary of each.
3. Process them one by one, **stopping to ask** if any is ambiguous (unclear category, missing attendees, weird content). Don't blast through.
4. Single log append at the end summarizing all.

### Stale Raw

If a Raw note is over 30 days old and still Unprocessed, ask the user:

- Process now
- Mark as `Stale` (abandoned — keeps record but won't show in inbox)
- Delete (only with explicit confirmation)

---

## 2. Importing from external sources

Any external artifact (recording, transcript, doc, Slack thread) becomes a Raw note. The general procedure:

### Manual import

User pastes content or points at a file. Create `Raw/YYYY-MM-DD-<topic>.md`:

```yaml
---
type: Raw
date: 2026-05-11
status: Unprocessed
category: <Meeting | Slack | Doc | Voice | Screenshot | Other>
source: <URL, file path, or [[wikilink]] to original>
source_type: <e.g., "Voice Recording", "Slack Thread", "Google Doc">
---

# <Topic>

<Pasted content / transcript / summary>
```

### Watched-folder import (recorders, transcript output)

For any external source that produces files in a known location, use the **dedup contract**:

1. Check the folder for new items.
2. For each item, check both:
   - Whether a Raw note already references it (`grep -l "source:.*<filename>" Raw/Raw/archive/`)
   - Whether a `.processed` marker file exists alongside the original
3. If either exists → skip (already imported).
4. If new → create a Raw note (frontmatter above), then `touch <original-path>/.processed`.

The marker keeps the original folder pristine and gives a Finder-visible indicator (Cmd+Shift+. on macOS).

See `integrations.md` for the general integration pattern and an example script that turns any folder into an import source.

### Per-category routing on import

| External source | Raw `category` |
|------|------|
| Meeting recorder output (audio + transcript) | `Meeting` |
| Standalone voice memo | `Voice` |
| Slack copy-paste / export | `Slack` |
| Google Doc / Notion / PDF text | `Doc` |
| Screenshot with annotation | `Screenshot` |
| Email forward | `Doc` (or `Other`) |
| Linear / Jira ticket export | `Doc` |

---

## 3. Generating summaries

### Daily summary

User says "today's summary" or "summarize today":

1. Filename: `summaries/daily-YYYY-MM-DD.md`.
2. Check if file already exists. If yes → **update in place**, do not create new. Update `generated_at:` timestamp; report "Updated existing summary (previously generated at X)".
3. Find today's meeting notes: `find meetings -name "*.md" -exec grep -l "date: $(date +%Y-%m-%d)" {} \;`.
4. Aggregate using the structure below.

### Weekly summary

User says "this week" or "last week":

1. Filename: `summaries/weekly-YYYY-MM-DD-to-YYYY-MM-DD.md` (Mon → Sun or whatever the user uses).
2. Dedup check as above.
3. Pull meetings for the date range, group by day then by category.
4. Roll up action items by owner. Surface recurring blockers and cross-meeting dependencies.

### Summary structure

```yaml
---
type: Summary
summary_date: "2026-05-11"             # or range for weekly
summary_type: daily                     # daily | weekly | topic
meeting_count: 4
generated_at: 2026-05-11T15:30:00
related_to:
  - "[[<initiative-1>]]"
---

# Work Summary: <Today | Week of YYYY-MM-DD>

## Overview
- **Meetings:** N total (X Data, Y Engineering, Z Design, ...)
- **People spoken to:** N unique attendees
- **Initiatives discussed:** [linked list]

## Meetings by category

### [Category] — [Meeting title]
**Attendees:** [[names]]
**Related:** [[linked initiatives]]

**Key updates:**
- [bullet]

**Decisions:**
- [decision with owner if noted]

**Action items:**
- [ ] [Owner]: [action] (from [[meeting-link]])

---

## Blockers identified
- [Person/Team]: [blocker description]

## Initiatives progressed
- [[initiative-name]]: [brief status update]

## People spoken to
- [[person-link]] (in [Meeting 1], [Meeting 2])

---

*Generated: YYYY-MM-DD HH:MM*
```

### Topic summary

User says "summarize everything about <topic>" or "summarize <initiative>":

1. Search across notes for relevant material:
   ```bash
   grep -rl "<topic-or-wikilink>" meetings/ initiatives/ decisions/ research/
   ```
2. Read each match. Pull the relevant section.
3. Filename: `summaries/topic-<kebab>.md`.
4. Group by note type (meetings, decisions, research). Cite source notes via `[[wikilinks]]`.

### Display behavior for summaries

- Always **display** the summary to the user (full content).
- Always **persist** it to `summaries/`.
- Report both the displayed output and the file path.
- On update vs create: clearly say which happened.

---

## 4. Maintaining `logs/maintenance-log.md`

Append-only. Never rewrite history. Format:

```markdown
## YYYY-MM-DD

### Processed
- Raw/source.md → meetings/category/destination.md

### Created
- initiatives/new-initiative.md
- people/new-person.md

### Status changes
- Raw/old.md: Unprocessed → Stale (abandoned)

### Imports
- ~/path/to/source/recording-name → Raw/YYYY-MM-DD-topic.md

### Notes
- [Optional human-readable context for unusual entries]
```

Group all actions from a single user session into one date heading.

---

## What to refuse / escalate

- **Never delete a note** without explicit confirmation in the current message — even if the user is processing it. Move to `archive/` or change status instead.
- **Never modify a Processed Raw** — they're a historical record. If the user wants to reprocess, create a new Raw with a different filename.
- **Never silently overwrite a summary that has been hand-edited** — check for an `_edited:` flag in frontmatter or a `## Manual edits` section. If present, ask before regenerating.
- **Never sync, upload, or send the vault elsewhere** without explicit ask. Vault is local.

---

## When to use AskUserQuestion in maintenance

- Source-to-destination routing unclear (Slack copy → general meeting? initiative?).
- Multiple plausible destinations (a Raw note has both a decision and an initiative described — split or merge?).
- Action item lacks an owner (and the meeting wasn't ad-hoc).
- Stale Raw cleanup decisions (process / mark stale / delete).
