---
source_urls:
  - https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields
  - https://code.claude.com/docs/en/sub-agents#control-subagent-capabilities
last_reviewed: 2026-05-13
---

# Tools, permissions, and models

## Tool allowlists and denylists

- **`tools`** — explicit allowlist. Omitted → inherit **all** tools the parent session has (including MCP).
- **`disallowedTools`** — remove tools from inherited or explicit pool.
- **Both set** — `disallowedTools` applied first, then `tools` filters the remainder. A tool in both is removed.

Examples: [Available tools](https://code.claude.com/docs/en/sub-agents#available-tools).

## Spawning other agents from the main thread

When an agent file runs as the **main** session (`--agent` / `agent` setting), its `tools` may include **`Agent`**:

- `Agent` — may spawn any subagent type.
- `Agent(worker, researcher)` — **allowlist** of spawnable types.
- Omitting `Agent` entirely — **cannot** spawn subagents.

**Note:** In recent versions the **Task** tool was renamed to **Agent**; `Task(...)` may still appear as an alias in older configs.

This **does not apply** inside a subagent definition — subagents cannot nest subagents.

## Permission modes (`permissionMode`)

Controls how permission prompts behave for that agent. Modes include `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`.

**Cautions:**

- Parent `bypassPermissions` / `acceptEdits` can **override** child modes.
- Parent **auto mode** forces the subagent into the same classifier behavior; child `permissionMode` may be ignored.

Full table: [Permission modes](https://code.claude.com/docs/en/sub-agents#permission-modes).

## MCP scoping (`mcpServers`)

Attach MCP servers **only** to a subagent — useful to keep heavy tool schemas out of the main conversation. Supports **inline** server definitions or **string references** to already-configured servers.

## Model choice

Use **Haiku** for wide shallow search, **Sonnet** for balanced implementation/review, **Opus** for hardest reasoning — tune to cost/latency. Use **`inherit`** when the parent model should decide.

See also: `frontmatter-fields.md` for resolution order and `effort`.
