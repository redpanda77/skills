---
source_urls:
  - https://code.claude.com/docs/en/env-vars
last_reviewed: 2026-05-13
---

# Environment variables (orientation)

Set variables in the shell before `claude`, or persist via `settings.json` → `"env": { "NAME": "value" }` for team rollout.

## Categories (non-exhaustive)

| Area | Examples (names drift — verify official table) |
| --- | --- |
| Auth / routing | `ANTHROPIC_API_KEY`, `ANTHROPIC_BASE_URL`, cloud provider vars |
| Model defaults | `ANTHROPIC_DEFAULT_SONNET_MODEL`, … |
| Context / compaction | `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`, `CLAUDE_CODE_AUTO_COMPACT_WINDOW` |
| UX / TUI | `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN`, accessibility toggles |
| Agents / teams | `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`, fork subagent flags |
| Channels / preview | channel-related toggles paired with `--channels` |
| Debugging | `CLAUDE_CODE_DEBUG_LOGS_DIR`, `--debug` categories |

## Reading strategy

The official page is a **long single table** — search by keyword (`HOOK`, `MCP`, `FORK`, `BACKGROUND`). When advising users, quote the **exact** variable name and link the official row.

Official: [Environment variables](https://code.claude.com/docs/en/env-vars).
