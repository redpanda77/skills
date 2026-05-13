---
source_urls:
  - https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields
last_reviewed: 2026-05-13
---

# Supported frontmatter fields

Only **`name`** and **`description`** are required. The markdown **body** is the subagent system prompt.

Official table: [Supported frontmatter fields](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields).

## Field catalog

| Field | Purpose |
| --- | --- |
| `name` | Unique id (`lowercase-with-hyphens`). Hooks receive this as `agent_type`. Filename need not match. |
| `description` | **Delegation trigger** — when Claude should use this agent; be specific. |
| `tools` | Allowlist of tools; omit to inherit all session tools. For preloading skills, use `skills:` not listing `Skill` in tools. |
| `disallowedTools` | Denylist applied to inherited or explicit tool set. |
| `model` | `sonnet`, `opus`, `haiku`, full model id, or `inherit` (default if omitted). |
| `permissionMode` | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`. Ignored for plugin agents. Parent modes can override (see docs). |
| `maxTurns` | Cap agentic turns. |
| `skills` | Skill names to **preload** full content at startup. |
| `mcpServers` | MCP servers scoped to this agent (inline or by reference). Ignored for plugin agents. |
| `hooks` | Hooks scoped to this agent’s lifecycle. Ignored for plugin agents. |
| `memory` | `user`, `project`, or `local` persistent memory; enables memory instructions and caps `MEMORY.md` injection. |
| `background` | `true` to default this definition to background runs. |
| `effort` | Reasoning effort override (`low` … `max`; availability depends on model). |
| `isolation` | `worktree` for isolated git worktree checkout. |
| `color` | UI color (`red`, `blue`, …). |
| `initialPrompt` | When agent runs as **main** session (`--agent` / `agent` setting): auto-first user turn; commands/skills expand. |

## CLI JSON equivalents

`--agents` JSON uses `prompt` for the body; other keys align with frontmatter (`description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `mcpServers`, `hooks`, `maxTurns`, `skills`, `initialPrompt`, `memory`, `effort`, `background`, `isolation`, `color`).

## Model resolution order

When a subagent runs, model is resolved roughly as:

1. `CLAUDE_CODE_SUBAGENT_MODEL` env (if set)
2. Per-invocation `model` parameter from the delegator
3. Definition frontmatter `model`
4. Main conversation model

See [Choose a model](https://code.claude.com/docs/en/sub-agents#choose-a-model).
