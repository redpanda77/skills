---
name: tolaria-summary-generator
description: Generate summaries with bounded context in a Tolaria vault in isolation. Triggered by "generate summary" or scheduled summary generation. Returns summary + source_evidence to the main agent.
skills:
  - tolaria-wiki
---

# Tolaria Summary Generator Subagent

**Trigger:** "generate summary", "summarize today", "summarize this week", or scheduled summary generation.

For invocation rules and thresholds, see `references/orchestration/subagents.md`.

**Input:** Vault path + summary type (daily/weekly/topic) + date range or topic (provided by main agent).

**Output:** Summary content + `source_evidence` block for the main agent to write.

## Procedure

1. Read `system/VAULT.md` for vault-specific conventions.
2. Check if a summary already exists for the date range / topic.
3. If yes → check freshness:
   - Read `source_evidence` from existing summary.
   - Compare source note hashes to current hashes.
   - If fresh → report "Summary is fresh. No update needed."
   - If stale → proceed to regenerate.
4. Generate a context pack:
   - For daily: today's notes + related topics + related people
   - For weekly: week's notes + related topics + related decisions + rollup of action items
   - For topic: notes matching topic + directly linked notes + notes sharing wikilinks
5. Read the context pack (max 30 notes).
6. Generate summary from context pack.
7. Build `source_evidence` with hashes of all source notes.
8. Return to main agent:
   - Summary content (full markdown)
   - `source_evidence` block
   - Context pack record

## Rules

- Never read the entire vault. Always use a bounded context pack.
- Always check freshness before regenerating.
- Always record `source_evidence` with hashes.
- Never silently overwrite a hand-edited summary. Check for `_edited:` flag. If present, ask the main agent.
- Display the summary to the user and persist it to `summaries/`.
