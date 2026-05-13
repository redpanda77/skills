---
source_urls:
  - https://code.claude.com/docs/en/sub-agents#define-hooks-for-subagents
  - https://code.claude.com/docs/en/hooks
related_skills:
  - claude-code-hooks
last_reviewed: 2026-05-13
---

# Hooks in agents (bridge)

This file is intentionally **small**. Hook mechanics live in **`claude-code-hooks`**.

## Two hook surfaces for agents

### 1. Agent-scoped hooks (`hooks:` in subagent frontmatter)

- Same JSON shape as settings hooks.
- Run **only while that subagent is active**, then **clean up**.
- Use for guardrails **specific to that agent** (validate Bash, lint after `Edit`, audit logging).

Official: [Define hooks for subagents](https://code.claude.com/docs/en/sub-agents#define-hooks-for-subagents).

### 2. Project/session hooks for agent lifecycle

In `settings.json`, respond to:

| Event | Matcher | When |
| --- | --- | --- |
| `SubagentStart` | agent type | subagent begins |
| `SubagentStop` | agent type | subagent completes |

Use for cross-cutting behavior: connect ephemeral resources, telemetry, cleanup — **without** embedding that logic in every agent file.

## `Stop` vs `SubagentStop` in frontmatter

In **subagent frontmatter**, a `Stop` hook is converted to **`SubagentStop`** at runtime (the completing event for subagents). Plan matchers accordingly.

Details also documented in `claude-code-hooks` (`hooks-in-skills-and-agents.md`).

## When to jump to `claude-code-hooks`

Read the hooks skill for:

- full **event catalog** and matcher grammar
- stdin/stdout contracts and **exit codes**
- async hooks, security, debugging with `/hooks`
- `once:` behavior (**skills only**; ignored in agent frontmatter per product rules)

## Minimal decision rule

| Need | Where |
| --- | --- |
| Policy for **one** agent definition | `hooks:` on that agent |
| Policy whenever **any** subagent of type X starts/stops | `SubagentStart` / `SubagentStop` in settings |
| Policy whenever **files edit hooks JSON** | settings or plugin — **not** this skill |
