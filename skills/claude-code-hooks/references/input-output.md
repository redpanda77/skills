---
source_urls:
  - https://code.claude.com/docs/en/hooks#hook-input-and-output
  - https://code.claude.com/docs/en/hooks#json-output
  - https://code.claude.com/docs/en/hooks#exit-code-output
  - https://code.claude.com/docs/en/hooks#decision-control
last_reviewed: 2026-05-13
---

# Hook input and output

## Input

- **Command hooks:** full event JSON on **stdin**
- **HTTP hooks:** same JSON as **POST body**

Common fields (plus event-specific fields) are documented under [Common input fields](https://code.claude.com/docs/en/hooks#common-input-fields). Tool events include `tool_name` and `tool_input`. Subagent context adds `agent_id` / `agent_type` where applicable.

## Exit codes (command hooks)

| Code | Meaning |
| --- | --- |
| **0** | Success — stdout may contain JSON decisions (parsed only on exit 0) |
| **2** | Blocking error — stderr surfaces to Claude; semantics depend on event |

Full matrix: [Exit code output](https://code.claude.com/docs/en/hooks#exit-code-output) and [Exit code 2 behavior per event](https://code.claude.com/docs/en/hooks#exit-code-2-behavior-per-event).

## JSON output (high level)

Responses may include universal fields such as `continue`, `systemMessage`, and `suppressOutput`, plus event-specific structures.

- Many tool-control decisions use **`hookSpecificOutput`** with **`hookEventName`** set to the firing event.
- **`PreToolUse`** uses `permissionDecision` / `permissionDecisionReason` (and related advanced fields).
- Some events use top-level **`decision`: `"block"`** with **`reason`**.

Authoritative tables: [JSON output](https://code.claude.com/docs/en/hooks#json-output) and [Decision control](https://code.claude.com/docs/en/hooks#decision-control).

## `additionalContext`

`additionalContext` inside `hookSpecificOutput` injects a **system reminder** for Claude on the next model request (see official doc for per-event placement and the **10,000 character** overflow behavior).

## HTTP hooks

Non-2xx responses and connection failures are generally **non-blocking** unless the response body encodes an explicit deny/block per the reference.
