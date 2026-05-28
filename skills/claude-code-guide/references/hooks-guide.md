---
source_urls:
  - https://code.claude.com/docs/en/hooks-guide
  - https://code.claude.com/docs/en/hooks
related_skills:
  - claude-code-hooks
last_reviewed: 2026-05-13
---

# Hooks guide (orientation)

Hooks run **deterministic** code at lifecycle points: format on save, block dangerous commands, notify when input is needed, inject session context, audit config changes, etc. They can be **command**, **http**, **mcp_tool**, **prompt**, or **agent** handlers.

## First hook pattern

1. Add a `hooks` object to a **settings** file (`~/.claude/settings.json`, `.claude/settings.json`, …) or to **skill / subagent** frontmatter for scoped hooks.
2. Verify with **`/hooks`** (read-only browser).
3. Exercise the event (e.g., trigger `Notification` by causing a permission prompt).

## Guide vs reference

- **This page (guide):** workflows, common recipes, mental model.
- **Hooks reference:** complete event list, stdin/stdout JSON schemas, async behavior, exit codes.
- **This repo:** use **`claude-code-hooks`** for deep authoring, matchers, security, fixtures, and debugging.

## Relationship to permissions

`PreToolUse` hooks can **extend** permissions with dynamic checks (see subagent read-only SQL example in subagents doc). Prompt/hooks still do not replace org managed policy where deployed.

Official: [Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide) and [Hooks reference](https://code.claude.com/docs/en/hooks).
