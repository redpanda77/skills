---
source_urls:
  - https://code.claude.com/docs/en/sub-agents#work-with-subagents
last_reviewed: 2026-05-13
---

# Invocation and delegation

## Automatic delegation

Claude chooses subagents using:

- the **user’s task text**,
- each subagent’s **`description`** (primary signal),
- **current context** (what is already loaded vs what still needs discovery).

**Tip:** phrases like **“use proactively”** in `description` can encourage delegation when appropriate — still keep the description truthful and specific.

Official: [Understand automatic delegation](https://code.claude.com/docs/en/sub-agents#understand-automatic-delegation).

## Explicit invocation (escalation ladder)

1. **Natural language** — name the agent (“use the test-runner subagent…”). Claude usually honors it when it fits.
2. **@-mention** — pick `@"agent-name (agent)"` from typeahead to **force** that agent for the task framing.
3. **Session as agent** — `claude --agent <name>` or `"agent": "<name>"` in `.claude/settings.json` so the **main thread** uses that definition’s prompt, tools, and model.

For plugin agents, `--agent` may need the **scoped** plugin name (see docs).

## Why descriptions matter

The `description` field is not marketing copy — it is the **router**. Ambiguous descriptions cause missed delegations or wrong agent choice. Use `checklists/delegation-description-checklist.md`.

## Chaining

Subagents **cannot** spawn subagents. Multi-step flows chain from the **main** conversation: researcher → implementer → reviewer, each returning a summary for the parent to route.

## Denying specific agents

Use `permissions.deny` with `Agent(<name>)` or CLI `--disallowedTools` patterns — see [Disable specific subagents](https://code.claude.com/docs/en/sub-agents#disable-specific-subagents).
