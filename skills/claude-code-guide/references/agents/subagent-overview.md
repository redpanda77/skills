---
source_urls:
  - https://code.claude.com/docs/en/sub-agents
last_reviewed: 2026-05-13
---

# Subagent Overview

## What They Are

Subagents are specialist workers. They are Markdown files with YAML frontmatter and a body system prompt. They are selected by name/description and executed through the Agent tool with a fresh context. They return results, not their whole working history.

## Why They Exist

Delegate when a side task would **flood the main thread** with search hits, logs, file dumps, or other noise you will not reuse. The subagent absorbs that work and returns a **compact summary** to the parent.

## Practical Flow

```
.claude/agents/security-reviewer.md
        ↓
Claude Code loads agent definitions at session start
        ↓
Main Claude session decides to delegate
        ↓
Agent tool is called with the selected subagent type and task prompt
        ↓
Subagent starts in its own context window
        ↓
Subagent uses its own prompt, model, tools, skills, memory, and permissions
        ↓
Subagent returns a summary/result to the main session
```

## Important Behavior

- Subagents start with fresh isolated context by default.
- They do not see the full parent conversation history.
- They receive a delegation prompt written by Claude.
- They load `CLAUDE.md`, rules, memory, and any preloaded skills.
- They can have restricted tools.
- They can run in foreground or background.
- They **cannot** spawn other subagents.

## When to Use a Subagent

- Verbose intermediate output should stay out of the main window.
- You want tighter tool allowlists/denylists or a different model for that work.
- The same "worker" role repeats and deserves a saved definition.

## When Something Else Fits Better

- **Skills** — reusable instructions or workflows; may run in main context or with `context: fork` (see `skills-and-subagents.md`).
- **Hooks** — deterministic automation at lifecycle or tool boundaries; see `references/hooks`.
- **Main conversation** — quick edits, tight iteration with the user, or shared context across phases.

## Related Product Concepts

- Subagents operate **within one session**. For many independent sessions monitored together, see [background agents](https://code.claude.com/en/agent-view). For coordinated multi-session workers, see [agent teams](https://code.claude.com/en/agent-teams).
