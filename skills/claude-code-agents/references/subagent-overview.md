---
source_urls:
  - https://code.claude.com/docs/en/sub-agents
last_reviewed: 2026-05-13
---

# Subagent overview

Subagents are specialized assistants for specific task types. Each runs in **its own context** with a **custom system prompt**, **tool access**, and **permissions** separate from the main conversation.

## Why they exist

Delegate when a side task would **flood the main thread** with search hits, logs, file dumps, or other noise you will not reuse. The subagent absorbs that work and returns a **compact summary** to the parent.

Official framing: [Create custom subagents](https://code.claude.com/docs/en/sub-agents).

## When to use a subagent

- Verbose intermediate output should stay out of the main window.
- You want **tighter tool allowlists/denylists** or a different **model** for that work.
- The same “worker” role repeats and deserves a saved definition.

## When something else fits better

- **Skills** — reusable instructions or workflows; may run in main context or with `context: fork` (see `skills-and-subagents.md`).
- **Hooks** — deterministic automation at lifecycle or tool boundaries; see `claude-code-hooks`.
- **Main conversation** — quick edits, tight iteration with the user, or shared context across phases.

## Related product concepts

- Subagents operate **within one session**. For many independent sessions monitored together, see [background agents](https://code.claude.com/en/agent-view). For coordinated multi-session workers, see [agent teams](https://code.claude.com/en/agent-teams).
