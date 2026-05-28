---
source_urls:
  - https://code.claude.com/docs/en/hooks#matcher-patterns
  - https://code.claude.com/docs/en/hooks#match-mcp-tools
  - https://code.claude.com/docs/en/settings#permission-rule-syntax
last_reviewed: 2026-05-13
---

# Matchers and `if`

## Matcher semantics

The `matcher` field filters when a matcher group runs. Evaluation rules (from the official reference):

| Matcher value | Interpreted as |
| --- | --- |
| `"*"`, `""`, or omitted | Match all |
| Only letters, digits, `_`, and the ASCII pipe | Exact match or pipe-separated alternates (e.g. a matcher value like `Edit` or `Write` using the pipe separator between literals) |
| Contains any other character | **JavaScript regex** |

**`FileChanged`** does **not** follow the generic matcher rules for watch lists — see the dedicated [FileChanged](https://code.claude.com/docs/en/hooks#filechanged) section.

Each event matches `matcher` against a **different input field** (tool name, notification type, agent type, etc.). A table mapping **event → matcher meaning → examples** is in [Matcher patterns](https://code.claude.com/docs/en/hooks#matcher-patterns).

### Events that ignore matchers

These events **do not support matchers**; if present, `matcher` is **silently ignored**:

`UserPromptSubmit`, `PostToolBatch`, `Stop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`, `WorktreeCreate`, `WorktreeRemove`, `CwdChanged`

## `if` (tool events only)

On **`PreToolUse`**, **`PostToolUse`**, **`PostToolUseFailure`**, **`PermissionRequest`**, and **`PermissionDenied`**, each handler may set **`if`** to a single [permission rule](https://code.claude.com/docs/en/permissions) string combining tool name and arguments, e.g.:

- `"Bash(git *)"`
- `"Edit(*.ts)"`

Rules beyond one condition require **multiple handler entries** (no `&&` / `||` in a single `if`).

For Bash, matching applies per **parsed subcommand** after stripping leading `VAR=value` assignments. If the command is too complex to parse, the hook **runs** (fail-open for parsing).

## MCP tool names

MCP tools appear as normal tool names in tool events, typically:

`mcp__<server>__<tool>`

To match all tools on a server, use a **regex** with `.*` (e.g. `mcp__memory__.*`). A plain `mcp__memory` (letters + underscores only) is treated as an **exact** string and will not match real tool names.

Details: [Match MCP tools](https://code.claude.com/docs/en/hooks#match-mcp-tools).
