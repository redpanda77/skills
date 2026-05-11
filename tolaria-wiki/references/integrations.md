# Integrations — connecting external sources

The vault is the destination. Anything outside it (meeting recorders, transcripts, Slack, Jira/Linear, email, doc exports) is a **source**. This file documents the **contract** for connecting any source — not specific vendors. Vendors change; the contract doesn't.

## The contract

Any external source becomes a **Raw note** in `Raw/`. That's the only integration point. Once in `Raw/`, the maintenance workflow (`maintenance.md`) processes it like any other Raw — there's no source-specific code path past import.

A source needs to satisfy:

1. **Identifies itself.** Each item has a stable ID (file path, URL, message ID, ticket ID).
2. **Produces text.** Audio/video must be transcribed first; PDFs/docs must be extracted. The vault stores text, not media.
3. **Is idempotent.** Re-importing the same item is safe — dedup must work.
4. **Doesn't mutate the original.** Vault never modifies upstream data. Originals stay where they live.

If your source can satisfy those four, it works.

## The 4-step import procedure

For any source. Adapt to vendor.

### 1. Discover new items

Whatever produces a list of candidates. Examples:

- Filesystem: `ls <folder>` or `find <folder> -newer <marker>`
- API: `curl <endpoint>` returning JSON
- Email: IMAP search, mbox parsing
- Clipboard: user pastes into chat

### 2. Dedup check

Two strategies, use **either or both**:

**A. Marker file** (filesystem-friendly):
```bash
test -f <source-path>/.processed && echo "skip"
```
On macOS, dotfiles are invisible by default — visible with Cmd+Shift+. so the user can still see status.

**B. Reverse lookup** (works for non-filesystem sources):
```bash
grep -l "source:.*<stable-id>" Raw/ Raw/archive/ 2>/dev/null
```
The `source:` frontmatter field in existing Raw notes is the registry.

If either check finds a match → skip.

### 3. Create the Raw note

```yaml
---
type: Raw
date: <when-the-source-item-was-created, not when-imported>
status: Unprocessed
category: <Meeting | Slack | Doc | Voice | Screenshot | Other>
source: <stable-id — path, URL, or [[wikilink]]>
source_type: <human description: "Voice Recording", "Slack Thread", "Jira ticket">
---

# <Title — meeting topic, ticket title, doc name>

<Body — transcript, pasted text, extracted text>
```

Filename: `Raw/YYYY-MM-DD-<kebab-topic>.md`. If multiple items same day, add disambiguator.

### 4. Mark the source as processed

```bash
touch <source-path>/.processed       # if filesystem
```

For non-filesystem sources, the Raw note's `source:` field IS the marker (Step 2 reverse lookup picks it up on next run).

## Common source patterns

### Filesystem folder (meeting recorders, transcript outputs, downloaded docs)

The most common pattern. Examples of folders that fit:
- `~/Movies/<recorder>-recordings/<meeting-folder>/transcript.txt`
- `~/Documents/transcripts/`
- `~/Downloads/zoom-transcripts/`
- iCloud sync'd notes from a phone

Recipe:

```bash
SOURCE_DIR="$HOME/Movies/recordings"
for folder in "$SOURCE_DIR"/*/; do
  [ -f "$folder/.processed" ] && continue

  # Find transcript or audio
  transcript=$(find "$folder" -maxdepth 1 -name "*.txt" -o -name "*.json" -o -name "transcript*" | head -1)
  [ -z "$transcript" ] && continue

  # Derive date and topic
  meeting_name=$(basename "$folder")
  date=$(date -r "$folder" +%Y-%m-%d)

  # Hand to Claude with this info — Claude creates the Raw note
  echo "New: $folder ($date — $meeting_name)"
done
```

Don't run this as a daemon. Run on demand (when the user says "check for new recordings") or via a manual launchd/cron entry the user opted into. See `setup.md` § "Optional extras".

### Clipboard / pasted text (Slack, email, doc)

User pastes content directly in the conversation. Create the Raw note immediately:

1. Ask user for the source URL or context (one line).
2. Determine category from format hints (Slack format = `Slack`, doc-shaped = `Doc`).
3. Write `Raw/YYYY-MM-DD-<kebab-topic>.md`.
4. `source:` is the URL or "pasted from `<context>` on <date>".

### Ticket trackers (Jira, Linear, Asana, GitHub Issues)

Two flavors:

**A. Single-ticket import** — user shares a URL or ID.
1. Fetch ticket (via `gh` CLI for GitHub; vendor CLI or API for others).
2. Extract: title, body, status, assignee, comments.
3. Create Raw with `category: Doc`, `source: <URL>`, `source_type: "Jira ticket" (or vendor)`.
4. Body: ticket markdown + comments.

**B. Squad / project status dump** — user wants a snapshot.
1. Query the tracker for all tickets in a scope (JQL, Linear filter).
2. Group by status (In Progress, In Review, Done).
3. Create a single Raw with `category: Doc`, `source: <query>`, `source_type: "<vendor> status dump"`.
4. Process into a `Squad Status` summary note. See `maintenance.md` § "Generating summaries".

### Email forwards

User forwards an email to a script or pastes the raw text:

1. Strip the email headers; preserve sender, date, subject.
2. `category: Doc` or `Other`. `source_type: "Email"`.
3. Body: subject as H1, sender + date below, then body content.

### Voice memos (standalone, no meeting context)

1. Transcribe (vendor-agnostic — whatever the user has: Whisper, Apple Voice Memos with on-device transcription, online tool).
2. `category: Voice`. Filename: `YYYY-MM-DD-voice-<topic>.md`.
3. Body: transcript verbatim.

## Decisions to defer to the user

Never auto-install or auto-run integrations. Always ask:

- "Want me to scaffold a watcher script for `~/Movies/recordings`?" → user opts in.
- "Want me to import all 12 new transcripts?" → user confirms count.
- "Want me to add a `launchd` job to check hourly?" → explicit consent, and document where the plist lives in the maintenance log.

## Example scaffolded watcher (template)

Write this to `<vault>/.claude/scripts/check-recordings.sh` if the user opts in. **Never** install it as a daemon — they run it manually or hook it to something themselves.

```bash
#!/usr/bin/env bash
# Check for new meeting recordings and list them. Run manually or from cron.
# Usage: ./check-recordings.sh [SOURCE_DIR]
set -euo pipefail

SOURCE_DIR="${1:-$HOME/Movies/recordings}"
VAULT="${VAULT:-$HOME/Documents/Wiki}"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "Source not found: $SOURCE_DIR"
  exit 1
fi

new_count=0
for folder in "$SOURCE_DIR"/*/; do
  [ -f "$folder/.processed" ] && continue
  name=$(basename "$folder")
  echo "NEW: $folder"
  new_count=$((new_count + 1))
done

echo
echo "Found $new_count unprocessed item(s)."
echo "Run \`tolaria-wiki import\` in Claude Code to process them."
```

Make it executable: `chmod +x check-recordings.sh`.

## Privacy

- **Vault content stays local.** No integration uploads vault content anywhere unless the user explicitly asks.
- **Source content respects upstream privacy.** If the source is `confidential: true` upstream (e.g., a confidential Slack channel), set `confidential: true` on the Raw note's frontmatter.
- **API keys for integrations** belong in environment variables or a local `~/.config/<tool>/` file, **never** in vault notes.
