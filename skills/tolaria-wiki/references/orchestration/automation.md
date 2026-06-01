# Automation — Orchestration Runbook

**When to read this:** Before any batch operation (processing raw notes, generating summaries, running health checks). This is the core mechanism that keeps the agent from getting lost, prevents mistakes, and ensures every operation is traceable.

For configuration, see `references/orchestration/automation-config.md`. For triggers and lifecycle, see `references/orchestration/automation-lifecycle.md`. For subagent invocation rules, see `references/orchestration/subagents.md`.

## The Orchestration Model

Every operation follows this contract:

```text
User Request
  -> Detect Situation (what does the user want?)
  -> Load system/VAULT.md (vault-specific conventions)
  -> Load Skill Reference (the procedure for this operation)
  -> Generate Context Pack (bounded set of relevant notes)
  -> Execute Workflow (deterministic steps + human decisions)
  -> Record in Audit Trail (logs/maintenance-log.md)
  -> Report to User
```

Every step is mandatory. No shortcuts.

## The Three Automation Layers

```text
Deterministic Refresh (auto-run simple commands)
  -> Auto-Process (auto-file unambiguous Raw)
  -> Context Packs (generate bounded context for every operation)
```

## 1. Deterministic Refresh

### What It Is

Automatically execute simple, mechanical commands without human intervention. The agent runs these until they stop producing output, hit a blocker, or reach a completion condition.

### What Qualifies as Deterministic

- Listing unprocessed Raw notes
- Checking for stale summaries
- Generating an index of notes by type
- Finding dead wikilinks
- Checking for empty notes
- Comparing file mtimes for freshness

### What Does NOT Qualify

- Deciding what category a Raw note belongs in
- Deciding which notes to link
- Writing a summary (qualitative synthesis)
- Classifying a note's type
- Deciding if a note is stale (the check is deterministic; the decision to act is human)

### Stop Conditions

Deterministic refresh stops when:
- No more unprocessed Raw notes
- A blocker is found (ambiguous note, missing required field)
- A human decision is needed
- An error occurs

## 2. Auto-Process

### What It Is

Automatically process Raw notes that are unambiguous. A Raw note is unambiguous if:

1. `category:` is a known type
2. The content clearly maps to a single destination type
3. All required fields for the destination type are present or inferable
4. No contradictions or anomalies in the content

### Auto-Process Procedure

```
1. Find all unprocessed Raw notes.
2. For each Raw note:
   a. Check category is known.
   b. Check content maps to single destination type.
   c. Check required fields are present or inferable.
   d. If all pass → auto-process:
      - Create structured note
      - Update Raw status
      - Move Raw to archive
      - Append to maintenance log
   e. If any fail → add to "needs human" list.
3. Report: auto-processed N notes, M need human decision.
```

### When to Stop and Ask

Stop auto-processing and ask the human when:
- Category is unknown or "Other"
- Content could map to multiple destination types
- Required fields are missing and not inferable
- Content is ambiguous or contradictory
- The Raw note is a voice memo or screenshot (no text to analyze)
- The Raw note contains sensitive or confidential material

## 3. Context Packs

### Why Context Packs Are Critical

Without context packs, the agent reads the entire vault. This causes:
- **Context overflow** — the agent gets lost in too many notes
- **Mistakes** — the agent references wrong notes or misses important ones
- **Slow operations** — reading hundreds of notes is slow
- **Inconsistent behavior** — the agent's behavior depends on vault size

The context pack solves this by providing a **bounded, relevant subset** of notes for every operation.

### What They Are

A bounded set of notes that the agent reads to perform an operation. Instead of reading the entire vault, the agent reads a small, relevant subset.

### Context Pack Schema

Every context pack has:

```yaml
---
context_pack_for: "operation name"
generated_at: "YYYY-MM-DDTHH:MM:SS"
input_hashes:
  - note: "[[path/to/note]]"
    hash: "abc123"
index:
  - "[[path/to/note1]]"
  - "[[path/to/note2]]"
notes_included: 5
notes_total: 127
---
```

### Context Pack Types

| Operation | Context Pack Contents | Typical Size |
|-----------|----------------------|--------------|
| Raw processing | Raw note + existing notes of same category + related people + related topics | 5-15 notes |
| Summary generation | Index of relevant notes (date range, direct links, graph proximity) + notes themselves | 10-30 notes |
| Authoring | Note being created + related notes (linked topics, people, decisions) | 3-10 notes |
| Health check | Index of all notes (for orphan detection) + index of all wikilinks (for dead link detection) | 2 indexes |
| Auto-link suggestions | Notes sharing wikilinks with the new note | 5-10 notes |

### How to Generate a Context Pack

```
1. Determine the operation (Raw processing, summary generation, etc.).
2. Generate an index:
   a. For date range: find notes with date in range.
   b. For direct links: find notes linked from/to the target.
   c. For graph proximity: find notes that share wikilinks with the target.
   d. For category: find notes of the same type.
3. Read the notes in the index.
4. Record the context pack in the maintenance log (or ephemeral — see below).
```

### Context Pack Storage

Context packs are ephemeral by default. They are generated on demand and discarded after the operation. For critical operations, record the context pack in the maintenance log:

```markdown
## YYYY-MM-DD
### Context Pack: Daily Summary
- Index: 15 notes (meetings from 2026-05-11)
- Notes read: 15
- Total vault notes: 127
```

### Context Pack Rules

1. **Mandatory.** Every operation that reads multiple notes must use a context pack.
2. **Bounded.** Never read more than 30 notes in a context pack. If the index is larger, filter it.
3. **Hashed.** Record the hashes of input notes for traceability.
4. **Indexed.** Start with an index, then read the notes.

## 4. Auto-Link Suggestions

### What It Is

When creating a new note, suggest related notes based on shared wikilinks.

### How It Works

```
1. Read the new note's wikilinks and relationship keys.
2. Find all notes that link to the same targets.
3. Score by overlap:
   - Direct link (both notes link to same target): high score
   - Shared category: medium score
   - Shared date: low score
4. Suggest top 5 notes to the user.
5. If user confirms, add `related_to:` links.
```

## 5. Summary Context Pack

### What It Is

For summary generation, generate a context pack instead of reading all notes.

### How It Works

```
User: "Summarize today"

Agent:
1. Generate index: find all notes with date=today.
2. Read the notes.
3. Find related topics (from note `related_to:` links).
4. Find related decisions (from note `related_to:` links).
5. Find related people (from note relationship keys).
6. Generate context pack: today's notes + related topics + related decisions + related people.
7. Generate summary from context pack.
8. Record context pack in maintenance log.
```

### Context Pack Size Limits

| Vault Size | Max Notes in Context Pack |
|------------|--------------------------|
| < 50 notes | 15 |
| 50-200 notes | 20 |
| 200-500 notes | 25 |
| > 500 notes | 30 |

If the index exceeds the limit, prioritize by:
1. Direct links (notes linked from the target)
2. Graph proximity (notes sharing wikilinks with the target)
3. Recency (most recent notes)
4. Category relevance (same type as target)

## 6. The Orchestration Contract

The automation system follows a strict contract:

### Before every operation

1. **Load system/VAULT.md** — the vault's conventions
2. **Load the skill reference** — the procedure for this operation
3. **Generate a context pack** — bounded, relevant notes
4. **Verify state** — check for unprocessed Raw, stale summaries, health issues

### During execution

5. **Execute deterministically** — scripts expose evidence, models decide
6. **Stop on ambiguity** — if any step is unclear, stop and ask
7. **Validate output** — check required fields, valid wikilinks, no orphans

### After execution

8. **Record in audit trail** — append to `logs/maintenance-log.md`
9. **Report to user** — what changed, what was untouched, what needs attention
10. **Update system/VAULT.md** if vault conventions changed

### Critical rules

1. **Deterministic only.** Automation never makes qualitative judgments. It exposes evidence; the human or model decides.
2. **Bounded context.** Automation always uses context packs. Never read the entire vault.
3. **Stop on ambiguity.** If any step is unclear, stop and ask the human.
4. **Record in audit trail.** Every automated operation is recorded in the maintenance log.
5. **Human override.** The human can override any automation at any time. See `references/orchestration/automation-lifecycle.md` § "Human Override".
6. **Context packs are mandatory.** Every operation that reads multiple notes must use a context pack. No exceptions.
