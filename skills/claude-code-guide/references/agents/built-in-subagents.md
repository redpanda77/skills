---
source_urls:
  - https://code.claude.com/docs/en/sub-agents#built-in-subagents
last_reviewed: 2026-05-13
---

# Built-in subagents

Claude Code ships built-in subagents. Claude may delegate to them automatically when the task matches their role. They **inherit the parent session’s permissions** with **additional tool restrictions** where documented.

## Explore

- **Model:** Haiku (fast).
- **Tools:** Read-oriented; **no Write/Edit**.
- **Use for:** discovery, search, understanding codepaths without mutating files.
- **Thoroughness:** parent may pass a level (`quick`, `medium`, `very thorough`).

## Plan

- **Model:** inherits from main conversation.
- **Tools:** read-only; **no Write/Edit**.
- **Use for:** research while [plan mode](https://code.claude.com/en/permission-modes#analyze-before-you-edit-with-plan-mode) is active — gathers context before a plan is shown.
- **Note:** avoids infinite nesting (subagents do not spawn subagents); Plan covers research inside plan mode.

## General-purpose

- **Model:** inherits.
- **Tools:** full tool set available to the session.
- **Use for:** multi-step work that needs both exploration and edits, or dependent steps.

## Other helpers

Typically invoked automatically:

| Agent | Model | When used |
| --- | --- | --- |
| `statusline-setup` | Sonnet | `/statusline` setup |
| `claude-code-guide` | Haiku | questions about Claude Code itself |

## Custom vs built-in

Prefer built-ins when they already match the job. Add a **custom subagent** when you need a **stable name**, **domain prompt**, **preload skills**, **hooks**, **MCP scoping**, **permissionMode**, or **tool policy** the built-ins do not provide.
