# Maintenance — process raw, import sources, generate summaries

**When to read this:** When operating an existing vault: handling inbox material, generating periodic summaries, keeping the log clean, running health checks, and maintaining audit trail. Load this first, then `references/orchestration/automation.md` for the orchestration contract.

## Three core operations

1. **Process raw** — convert `Raw/X.md` into a structured note in the right folder.
2. **Import external** — bring material from outside the vault (recordings, transcripts, Slack copies, docs) in as Raw notes.
3. **Generate summaries** — daily / weekly / topic / squad-status summaries from existing notes.

Plus: maintaining `logs/maintenance-log.md`, running health checks, and checking freshness.

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
3. Decide destination type from `category:` + content. See `references/operations/types.md` § "Raw → destination mapping".
4. Generate a **context pack** (see `references/orchestration/automation.md` § "Context Packs"):
   - The Raw note itself
   - Existing notes of the same category
   - Related people and initiatives
5. Create the structured note using `authoring.md` § "The 7-step procedure".
6. Update the Raw:
   ```yaml
   status: Processed
   processed_date: YYYY-MM-DD
   processed_to: "[[path/to/structured]]"
   ```
7. Move: `Raw/X.md` → `Raw/archive/X.md`.
8. Append to `logs/maintenance-log.md`:
   ```markdown
   ## YYYY-MM-DD
   ### Processed
   - Raw/X.md → meetings/category/destination.md
   ```

### Batch processing

When the user says "process all raw notes":

1. List all unprocessed Raw files.
2. Show the user the count and one-line summary of each.
3. **Auto-process unambiguous notes** (see `references/orchestration/automation.md` § "Auto-Process"):
   - Clear category, clear content, clear destination → auto-process
   - Ambiguous → stop and ask
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
   - Whether a Raw note already references it (`grep -l "source:.*<filename>" Raw/ Raw/archive/`)
   - Whether a `.processed` marker file exists alongside the original
3. If either exists → skip (already imported).
4. If new → create a Raw note (frontmatter above), then `touch <original-path>/.processed`.

The marker keeps the original folder pristine and gives a Finder-visible indicator (Cmd+Shift+. on macOS).

See `references/operations/integrations.md` for the general integration pattern and an example script that turns any folder into an import source.

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

### Summary context pack

Before generating any summary, create a **context pack** (see `references/orchestration/automation.md` § "Summary Context Pack"):

1. Generate an index of relevant notes (date range, direct links, graph proximity).
2. Read the notes in the index.
3. Record the context pack in the maintenance log.

Never read the entire vault. Read the index, then the context pack.

### Daily summary

User says "today's summary" or "summarize today":

1. Filename: `summaries/daily-YYYY-MM-DD.md`.
2. Check if file already exists. If yes → **check freshness** first:
   - Read `source_evidence` from the existing summary.
   - Compare source note hashes to current hashes.
   - If stale → **update in place**, do not create new. Update `generated_at:` timestamp.
   - If fresh → report "Summary is fresh (generated at X). No update needed."
3. If no existing summary or stale:
   - Generate context pack: today's meetings + related initiatives + related decisions + related people.
   - Generate summary.
   - Record `source_evidence` with hashes.

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
generated_by: "tolaria-wiki"
source_evidence:
  - note: "[[meetings/data/2026-05-ranking-sync]]"
    hash: "abc123"
  - note: "[[initiatives/ai-personalization-initiative]]"
    hash: "def456"
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
3. Generate context pack: matching notes + notes directly linked + notes sharing wikilinks.
4. Filename: `summaries/topic-<kebab>.md`.
5. Group by note type (meetings, decisions, research). Cite source notes via `[[wikilinks]]`.
6. Record `source_evidence` with hashes.

### Display behavior for summaries

- Always **display** the summary to the user (full content).
- Always **persist** it to `summaries/`.
- Report both the displayed output and the file path.
- On update vs create: clearly say which happened.
- On stale vs fresh: report freshness status.

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

### Summaries
- Generated summaries/daily-YYYY-MM-DD.md (15 source notes, context pack: 15/127)

### Health checks
- Orphans: 3 found, 2 fixed, 1 flagged
- Dead links: 2 found, 2 fixed

### Notes
- [Optional human-readable context for unusual entries]
```

Group all actions from a single user session into one date heading.

---

## 5. Health checks

Run these weekly or on demand. See `references/operations/health.md` for the full procedure.

### Quick health check

```bash
# Orphans (notes with no incoming links)
# Dead links (wikilinks to non-existent notes)
# Stale Raw (>30 days unprocessed)
# Empty notes (no body content)
# Missing fields (required frontmatter absent)
```

Report findings and ask: fix all, fix selected, or just flag.

---

## 6. Freshness checks

Run these when generating summaries or on demand. See § "Audit" below for the full procedure.

### Check summary freshness

```
1. Read the summary's source_evidence.
2. For each source note, compare current hash to recorded hash.
3. If any mismatch → mark as stale.
4. Report: stale summaries and which sources changed.
```

---

## 7. Audit

### Source traceability

Every generated note (summary, structured note created from Raw) must trace back to its source notes. If a summary is wrong, you can trace back to which source caused it.

Generated notes carry `source_evidence:` frontmatter:

```yaml
source_evidence:
  - note: "[[meetings/data/2026-05-ranking-sync]]"
    hash: "abc123"
  - note: "[[initiatives/ai-personalization-initiative]]"
    hash: "def456"
```

### Hash-based freshness

Generated notes carry the hash of their source notes. When source notes change, the hash mismatch indicates the generated note is stale.

```
1. When generating a note, record the hash of each source note in source_evidence.
2. Later, check freshness:
   a. Read the generated note's source_evidence.
   b. Re-hash each source note.
   c. Compare to the recorded hash.
   d. If any mismatch → mark as stale.
3. If stale, regenerate or ask the user.
```

### Receipts

Every operation leaves a receipt:

- **Raw processing receipt:** `processed_date`, `processed_to`, `processed_by` in Raw frontmatter
- **Summary generation receipt:** `generated_at`, `source_evidence`, `generated_by` in Summary frontmatter
- **Note creation:** Recorded in `logs/maintenance-log.md`
- **Status change:** Recorded in `logs/maintenance-log.md`

### Audit rules

1. Every operation is recorded. No silent changes.
2. Source evidence is mandatory for generated notes.
3. Hashes are recorded at generation time.
4. Stale content is flagged and reported.
5. The log is append-only. History is never rewritten.
6. Human override is always possible.

### On-demand audit

```
User: "Audit the vault"

Agent:
1. Read the maintenance log.
2. Check for operations without receipts.
3. Check for stale summaries (hash mismatch).
4. Check for unprocessed Raw without log entries.
5. Check for missing source_evidence on generated notes.
6. Report: clean or issues found.
```

### Periodic audit

Run a full audit monthly:
1. Verify all summaries have `source_evidence`.
2. Verify all processed Raw notes have `processed_to`.
3. Verify all status changes are in the maintenance log.
4. Verify no silent modifications (compare log to actual state).

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
- Health check findings: fix all, fix selected, or just flag?
- Summary regeneration: stale summary with `_edited:` flag — overwrite or not?
