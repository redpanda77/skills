# Tolaria Wiki Health System

**When to read this:** When running vault health checks or diagnosing vault problems. Load this first, then `references/orchestration/automation.md` for the orchestration contract. For automated health checks, invoke the health-checker subagent (see `references/orchestration/subagents/health-checker.md`).

## The Five Health Checks

| Check | What It Finds | Severity | How to Fix |
|-------|--------------|----------|------------|
| Orphan detection | Notes with no incoming wikilinks | Medium | Add `related_to` links or suggest related notes |
| Dead link detection | Wikilinks pointing to non-existent notes | High | Create stub, remove link, or fix typo |
| Stale Raw detection | Raw notes >30 days unprocessed | Medium | Process, mark Stale, or delete |
| Empty note detection | Notes with no body or nearly empty | Low | Add content, mark as Draft, or archive |
| Missing field detection | Notes missing required frontmatter | High | Add required fields or flag for human |

## 1. Orphan Detection

### What It Is

A note with no incoming wikilinks. No other note links to it. Orphans are hard to discover and often become forgotten.

### How to Detect

```bash
# Step 1: Build a list of all note filenames
find . -name "*.md" | sed 's|^.*/||; s|\.md$||' | sort > /tmp/all_notes.txt

# Step 2: Extract all wikilink targets from all notes
grep -roh '\[\[\([^\]]*\)\]\]' . --include="*.md" | sed 's|\[\[||; s|\]\]||; s|.*|\\||' | sort -u > /tmp/linked_targets.txt

# Step 3: Find notes that are never linked to
comm -23 /tmp/all_notes.txt /tmp/linked_targets.txt
```

### What to Do

For each orphan:
1. Check if it should be linked from an existing note. If yes, add the link.
2. If it is genuinely standalone (e.g., a research note that is not yet connected), flag it in the maintenance log as "orphan — needs linking."
3. If it is obsolete, mark as `Archived`.

### Maintenance Log Entry

```markdown
## YYYY-MM-DD
### Health Check: Orphans
- `research/old-topic.md` — orphan, no incoming links. Suggest linking from `initiatives/related-initiative.md`.
- `people/former-contractor.md` — orphan, mark as Archived.
```

## 2. Dead Link Detection

### What It Is

A wikilink `[[note-name]]` where the target note does not exist. This happens when notes are renamed, moved, or deleted (or never created).

### How to Detect

```bash
# Step 1: Build a list of all note filenames
find . -name "*.md" | sed 's|^.*/||; s|\.md$||' | sort > /tmp/all_notes.txt

# Step 2: Extract all wikilink targets (strip aliases)
grep -roh '\[\[\([^\]|]*\)\]\]' . --include="*.md" | sed 's|\[\[||; s|\]\]||' | sort -u > /tmp/all_links.txt

# Step 3: Find links that don't match any filename
comm -23 /tmp/all_links.txt /tmp/all_notes.txt
```

### What to Do

For each dead link:
1. Check if the target was renamed. If yes, update the link.
2. Check if the target should be created. If yes, create a stub.
3. If the link is a typo, fix it.
4. If the link is intentional but the target is not yet created, flag it in the maintenance log.

### Maintenance Log Entry

```markdown
## YYYY-MM-DD
### Health Check: Dead Links
- `meetings/data/2026-05-sync.md` links to `[[bob]]` but `people/bob.md` does not exist. Create stub or fix link.
- `initiatives/ai-initiative.md` links to `[[old-decision]]` but `decisions/old-decision.md` does not exist. Decision was renamed to `decisions/new-decision.md` — update link.
```

## 3. Stale Raw Detection

### What It Is

Raw notes that are `Unprocessed` for more than 30 days. They accumulate in the inbox and create noise.

### How to Detect

```bash
# Find Raw notes >30 days old with status: Unprocessed
find Raw -name "*.md" -mtime +30 -exec grep -l "status: Unprocessed" {} \;
```

### What to Do

For each stale Raw:
1. Ask the user: process, mark as `Stale`, or delete.
2. If the user says process, follow the Raw processing procedure.
3. If the user says mark Stale, update status and append to maintenance log.
4. If the user says delete, require explicit confirmation and append to maintenance log.

### Maintenance Log Entry

```markdown
## YYYY-MM-DD
### Health Check: Stale Raw
- `Raw/2026-04-old-meeting.md` — >30 days unprocessed. Marked as Stale per user request.
```

## 4. Empty Note Detection

### What It Is

Notes with no body content (only frontmatter) or nearly empty (just a title). These are usually placeholders that were never filled in.

### How to Detect

```bash
# Find notes with no body (only frontmatter and whitespace)
find . -name "*.md" -exec awk '/^---$/ {f=!f; next} f {next} NF {exit 1}' {} \; -print

# Find notes with body shorter than 100 characters (excluding frontmatter)
# This is a heuristic — adjust threshold as needed
```

### What to Do

For each empty note:
1. Check if it is a placeholder that should be filled. If yes, flag it in the maintenance log.
2. If it is obsolete, mark as `Archived`.
3. If it is a type definition or view file, ignore (these are expected to be short).

### Maintenance Log Entry

```markdown
## YYYY-MM-DD
### Health Check: Empty Notes
- `research/placeholder.md` — empty body. Flagged for user to fill in.
- `daily/2026-05-01.md` — empty body. Marked as Archived.
```

## 5. Missing Field Detection

### What It Is

Notes that are missing required frontmatter fields for their type.

### How to Detect

```bash
# Check for notes missing type:
find . -name "*.md" -exec grep -L "^type:" {} \;

# Check for Meeting notes missing attendees:
find . -name "*.md" -exec grep -l "type: Meeting" {} \; | xargs grep -L "attendees:"

# Check for Initiative notes missing owner:
find . -name "*.md" -exec grep -l "type: Initiative" {} \; | xargs grep -L "owner:"
```

### What to Do

For each note with missing fields:
1. Add the missing fields if they are inferable from the content.
2. If not inferable, flag the note in the maintenance log for the user to fix.

### Maintenance Log Entry

```markdown
## YYYY-MM-DD
### Health Check: Missing Fields
- `meetings/data/2026-05-sync.md` — type: Meeting but missing `attendees`. Flagged for user.
- `initiatives/new-initiative.md` — type: Initiative but missing `owner`. Added `owner: "[[alice]]"` from meeting context.
```

## Health Check Procedure

### Weekly Health Check

```
1. Detect orphans: find notes with no incoming links.
2. Detect dead links: find wikilinks pointing to non-existent notes.
3. Detect stale Raw: find Raw >30 days unprocessed.
4. Detect empty notes: find notes with no body.
5. Detect missing fields: find notes missing required frontmatter.
6. Report: list all issues with severity and suggested fix.
7. Ask user: fix all, fix selected, or just flag.
8. Record in maintenance log.
```

### On-Demand Health Check

The user can ask "check vault health" at any time. Run all five checks and report.

### Automated Health Check

Run the health check automatically during maintenance:
- After processing Raw notes
- After generating summaries
- After batch imports

### Subagent Invocation

For large vaults or complex health checks, invoke the health-checker subagent:

```
Agent: "check vault health"
1. Spawn subagent: `references/orchestration/subagents/health-checker.md`
2. Provide vault path.
3. Subagent runs diagnostics in isolation.
4. Subagent returns structured health report.
5. Main agent presents findings and asks user for action.
```

## Health Check Rules

1. **Never delete without confirmation.** Even empty notes should be flagged, not deleted.
2. **Prioritize by severity.** Fix dead links first (high), then missing fields (high), then orphans (medium), then stale Raw (medium), then empty notes (low).
3. **Record everything.** Every health check is recorded in the maintenance log.
4. **Suggest, don't assume.** For orphans, suggest related notes. For dead links, suggest fixes. The human decides.

## Health Check Report Template

```markdown
## YYYY-MM-DD
### Health Check

**Orphans:** 3
- `research/topic-a.md` — suggest link from `initiatives/related.md`
- `people/old-contractor.md` — suggest archive
- `features/old-feature.md` — suggest link from `initiatives/parent.md`

**Dead Links:** 2
- `meetings/data/2026-05-sync.md` → `[[bob]]` (bob.md does not exist)
- `initiatives/ai.md` → `[[old-decision]]` (old-decision.md does not exist)

**Stale Raw:** 1
- `Raw/2026-04-old.md` — >30 days unprocessed

**Empty Notes:** 0

**Missing Fields:** 1
- `meetings/data/2026-05-sync.md` — missing `attendees`
```
