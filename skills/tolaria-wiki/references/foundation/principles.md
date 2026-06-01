# Tolaria Wiki Core Principles

**When to read this:** When you need to resolve a conflict or ambiguity about how the vault should behave. These principles govern every workflow, decision, and automation. They are non-negotiable.

## 1. The vault is a graph, not a folder hierarchy

Folders are for human browsing. The real structure is the graph formed by `[[wikilinks]]`, `type:` relationships, and shared references. A note's position in the folder tree is secondary to its position in the graph.

## 2. State is derived from the vault, not from agent memory

The agent reads the vault to determine what exists, what's unprocessed, what's stale. Never assume state from conversation context. Re-read indexes before acting.

## 3. Every note has a type and a lifecycle

Every note has a `type:` and a `status:` that defines its current lifecycle stage. Types are not tags — they define the note's schema, required fields, and valid state transitions.

## 4. Raw sources are immutable. The wiki is a maintained layer

Raw notes (transcripts, pastes, screenshots) are source material. They are never edited after creation. Structured notes, summaries, and cross-links are a generated layer built on top of Raw. If a Raw is wrong, file a new Raw — don't edit the old one.

## 5. Cross-linking is the primary navigation mechanism

The graph is navigated via `[[wikilinks]]`. Every new note should link to at least one existing note. Orphaned notes (no incoming or outgoing links) are a smell — flag them in health checks.

## 6. Context is bounded

The agent never reads the entire vault to perform an operation. It reads an index, then a bounded context pack of relevant notes. This is the only scalable approach.

## 7. Automation is deterministic

Scripts and automation steps expose evidence (lists, counts, hashes). They do not make qualitative judgments. A script can say "these 5 notes share the tag `AI`"; it cannot say "these 5 notes are about AI." That decision belongs to a model or a human.

## 8. Quality is evaluated at every step

Every note creation, every Raw processing, every summary generation has a quality gate: required fields present, wikilinks valid, no orphans created, source traceability recorded.

## 9. The audit trail is append-only

Every operation is recorded in `logs/maintenance-log.md` or a receipt. History is never rewritten. If a summary is regenerated, the old one is preserved (or its receipt is).

## 10. Human curates, LLM maintains

The human decides what goes into the vault, what the vault is for, and what "good" means. The LLM files notes, cross-links, generates summaries, maintains the log, and flags health issues. The human approves; the LLM executes.

## 11. Never delete, only archive

Notes are append-only. If a note is obsolete, change its status to `Archived` or `Stale`. Move it to an `archive/` subfolder. Deletion is only for accidental duplicates or sensitive material — and only with explicit confirmation.

## 12. Confidentiality is opt-out, not opt-in

Material is confidential by default unless explicitly marked otherwise. The human sets the confidentiality policy; the LLM enforces it.
