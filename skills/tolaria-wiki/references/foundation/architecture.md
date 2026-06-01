# Tolaria Wiki System Architecture

**When to read this:** When you need to understand the full pipeline, layer contracts, or how the vault fits together conceptually. Read this for system design questions, not for day-to-day operations.

## The Pipeline

```text
Raw Sources (external)
  -> Inbox (Raw/)
  -> Structured Notes (meetings, initiatives, decisions, ...)
  -> Cross-linked Graph (wikilinks, relationships, indexes)
  -> Summaries (daily, weekly, topic)
  -> Audit Trail (logs/maintenance-log.md, receipts)
```

Every layer is a transformation. Every transformation leaves a receipt.

## Layers

### Layer 0: Raw Sources

External material: meeting recordings, Slack copies, email forwards, screenshots, voice memos, documents. These are immutable. They enter the vault as Raw notes.

**Contract:**
- Raw notes are never edited after creation.
- Raw notes carry `source:` and `source_type:` frontmatter.
- Raw notes are the ground truth. If a summary contradicts a Raw, the Raw wins.

### Layer 1: Inbox (Raw/)

Unprocessed material. The staging area for the vault.

**Contract:**
- Every Raw note has `status: Unprocessed` on creation.
- The agent checks for unprocessed Raw before any other operation.
- Raw notes older than 30 days are flagged as stale.

**State Machine:**
```text
Unprocessed -> Processing -> Processed
                    |
                    v
                  Stale (abandoned)
```

### Layer 2: Structured Notes

Typed notes with full frontmatter and cross-links. The core of the vault.

**Contract:**
- Every structured note has a `type:` and a `status:`.
- Every structured note links to at least one other note (no orphans).
- Notes are created by processing Raw or by direct authoring.
- Filing follows the folder routing table in `references/operations/types.md`.

**State Machine (Universal):**
```text
Draft -> Active -> In Review -> Completed
  |         |           |
  v         v           v
Blocked   Archived    Archived
```

### Layer 3: Cross-linked Graph

The graph formed by all `[[wikilinks]]`, relationship keys (`attendees`, `owner`, `initiative`, etc.), and shared references.

**Contract:**
- The graph is the source of truth for navigation and relevance.
- Indexes are derived from the graph, not from folder structure.
- The agent uses graph traversal (not just direct links) to find related notes.

### Layer 4: Summaries

Generated notes that synthesize information across multiple structured notes.

**Contract:**
- Every summary carries `source_evidence:` frontmatter listing the source notes and their hashes.
- Summaries are regenerated when source notes change (hash-based freshness).
- Summaries are never hand-edited without an `_edited:` flag. If edited, the agent asks before regenerating.

### Layer 5: Audit Trail

The append-only record of every operation on the vault.

**Contract:**
- Every operation (create, process, import, generate, status change) is recorded.
- The maintenance log is human-readable.
- Receipts (for generated content) are machine-readable.
- History is never rewritten.

## The Router

The tolaria-wiki skill is a router. It detects the user's situation and routes to the correct workflow:

```text
User request
  -> Detect situation (vault exists? Raw unprocessed? Note to create?)
  -> Route to workflow (Setup, Authoring, Maintenance, Lookup)
  -> Load bounded context (index + relevant notes)
  -> Execute workflow
  -> Record in audit trail
  -> Report to user
```

This is the same pattern as mission-control's router, but simpler: no hooks, no judges, no multi-tier validation. Just situation detection → bounded context → execution → audit.

## State Refresh

Before any operation, the agent refreshes state from the vault:

1. **Check for unprocessed Raw:** `grep -l "status: Unprocessed" Raw/*.md`
2. **Check for stale summaries:** Compare `source_evidence` hashes to current note hashes.
3. **Check for health issues:** Orphans, dead links, empty notes (if health check requested).

This is the "state derived from disk, not from memory" principle in practice.

## Bounded Context

Every operation gets a bounded context pack:

- **For Raw processing:** The Raw note + relevant existing notes (same category, same people, same initiatives).
- **For summary generation:** An index of relevant notes (date range, direct links, graph proximity) + the notes themselves.
- **For authoring:** The note being created + related notes (linked initiatives, people, decisions).

Never read the entire vault. Read the index, then the context pack.

## Deterministic Automation

Some operations can be automated without human judgment:

- **Auto-process Raw:** If a Raw note is unambiguous (clear category, clear content, clear destination), auto-process it.
- **Auto-link suggestions:** When creating a note, suggest related notes based on shared wikilinks.
- **Health check:** Find orphans, dead links, stale notes, empty notes.

These are deterministic scripts, not qualitative judgments. They expose evidence; the human or model decides.

## Separation of Concerns

| Concern | Human | LLM |
|---------|-------|-----|
| What goes in | Decides | Executes |
| Vault purpose | Defines | Follows |
| Quality standards | Sets | Enforces |
| Filing notes | Approves | Does |
| Cross-linking | Reviews | Suggests + does |
| Summaries | Reviews | Generates |
| Health issues | Decides | Flags |
| Raw processing | Approves ambiguous | Auto-processes unambiguous |

## What This Is NOT

- Not a compiler operating system (no multi-tier validation, no judge subagents, no repair system).
- Not a router-driven execution system where the router decides every micro-step.
- Not a mission-control system. It is a knowledge vault with a pipeline, principles, and lightweight automation.
