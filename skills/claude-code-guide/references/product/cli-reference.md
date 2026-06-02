---
source_urls:
  - https://code.claude.com/docs/en/cli-reference
last_reviewed: 2026-05-13
---

# CLI reference (orientation)

`claude --help` may omit some flags — trust the official CLI reference for the full matrix.

## Session shapes

| Invocation | Meaning |
| --- | --- |
| `claude` | interactive REPL |
| `claude "…"` | interactive with initial user text |
| `claude -p "…"` | **print / SDK** mode — non-interactive, exits |
| `claude -c` | continue latest conversation in cwd |
| `claude -r "<id|name>" "…"` | resume specific session |

Piping: `cat log.txt | claude -p "summarize errors"` processes stdin as context.

## Frequently used flags

| Flag | Role |
| --- | --- |
| `--permission-mode` | startup mode (`plan`, `acceptEdits`, …) |
| `--allowedTools` / `--disallowedTools` | session tool gates |
| `--tools` | restrict available tool set |
| `--agent` | run session as a named agent definition |
| `--agents '{…}'` | ephemeral JSON subagent definitions |
| `--mcp-config` / MCP flags | MCP wiring (see MCP doc) |
| `--bare` | faster non-interactive minimal discovery (`CLAUDE_CODE_SIMPLE`) |
| `--bg` | start as background session |
| `--channels …` | attach channel plugins (preview) |
| `--debug` / `--debug-file` | diagnostics |

## Maintenance commands (examples)

`claude update`, `claude install stable`, `claude auth status`, `claude agents` (interactive) vs **piped** `claude agents` listing subagents, `claude project purge` for local state cleanup — see official tables.

Official: [CLI reference](https://code.claude.com/docs/en/cli-reference).
