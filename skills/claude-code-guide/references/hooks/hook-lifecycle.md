---
source_urls:
  - https://code.claude.com/docs/en/hooks#hook-lifecycle
  - https://code.claude.com/docs/en/hooks-guide
  - https://code.claude.com/docs/en/hooks#how-a-hook-resolves
last_reviewed: 2026-05-13
---

# Hook lifecycle

Hooks fire at defined points in a Claude Code session. When an event fires and a **matcher** matches, Claude Code passes **JSON context** to your handler:

- **Command hooks:** JSON on **stdin**
- **HTTP hooks:** JSON as the **POST body**

Your handler can inspect the payload, run side effects, and optionally return a **decision** (depending on the event).

## Cadence

Events fall into broad cadences:

1. **Once per session** — e.g. `SessionStart`, `SessionEnd`
2. **Once per turn** — e.g. `UserPromptSubmit`, `Stop`, `StopFailure` (see reference for exact semantics per event)
3. **Per tool call** in the agentic loop — e.g. `PreToolUse`, `PostToolUse`

Use the official [Hook events](https://code.claude.com/docs/en/hooks#hook-events) table for the authoritative “when it fires” list.

## How a hook resolves (mental model)

1. **Event fires** — e.g. `PreToolUse` for an upcoming tool call.
2. **Matcher group** — optional filter on tool name, notification type, agent type, etc., depending on the event.
3. **`if` (tool events)** — optional permission-rule filter on tool name + arguments; avoids spawning handlers when the matcher is broad.
4. **Handlers run** — command, HTTP, MCP tool, prompt, or agent; may run in parallel where documented; deduplication rules apply for identical handlers.
5. **Claude Code applies stdout / HTTP body / exit code** per the event’s supported decision fields.

Walkthrough with a blocking Bash example: [How a hook resolves](https://code.claude.com/docs/en/hooks#how-a-hook-resolves).

## Guide vs reference

- **Patterns and tutorials:** [Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)
- **Exact schemas and edge cases:** [Hooks reference](https://code.claude.com/docs/en/hooks)
