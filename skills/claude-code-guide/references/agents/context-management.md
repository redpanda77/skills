---
source_urls:
  - https://code.claude.com/docs/en/sub-agents#manage-subagent-context
  - https://code.claude.com/docs/en/sub-agents#fork-the-current-conversation
last_reviewed: 2026-05-13
---

# Context management

## Isolated vs inherited context

- **Named subagent** — fresh context: definition body (+ preloads), not the full parent transcript.
- **Forked subagent (experimental)** — inherits the **conversation so far** while still keeping tool transcripts out of the main thread; see [Fork the current conversation](https://code.claude.com/docs/en/sub-agents#fork-the-current-conversation). Requires `CLAUDE_CODE_FORK_SUBAGENT=1` and recent Claude Code.

## Resume and transcripts

Each spawn is a **new instance** by default. To continue prior work, ask Claude to **resume** the same agent thread when supported.

Transcripts live under `~/.claude/projects/{project}/{sessionId}/subagents/` as `agent-{id}.jsonl` — useful when debugging “stale” or silent failures.

**Compaction:** subagents compact independently from the main conversation (separate files). Auto-compaction defaults around **95%** capacity; tune with `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`.

## Session and cleanup

Subagent transcripts persist for the session; cleanup follows `cleanupPeriodDays` (default 30 days).

## Cwd and shell state

Subagents start in the parent’s cwd. **`cd` in Bash does not persist** across tool calls nor change the parent cwd — use **`isolation: worktree`** when filesystem isolation matters.

## Agent teams note

When `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, **SendMessage** / teammate flows add additional persistence semantics — see upstream [agent teams](https://code.claude.com/en/agent-teams) docs if you use that mode.
