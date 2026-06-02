---
source_urls:
  - https://code.claude.com/docs/en/hooks#prompt-based-hooks
  - https://code.claude.com/docs/en/hooks#agent-based-hooks
  - https://code.claude.com/docs/en/hooks#prompt-and-agent-hook-fields
last_reviewed: 2026-05-13
---

# Prompt-based and agent-based hooks

## Prompt hooks (`type: "prompt"`)

- Send **`prompt`** text to a Claude model (default: fast/Haiku-class behavior per docs).
- Embed hook JSON using **`$ARGUMENTS`** (or rely on default append behavior if omitted).
- Model returns structured JSON **`{ "ok": true \| false, "reason": "..." }`**.
- **`continueOnBlock`** adjusts whether a block ends the turn or feeds back as continuation for some events — see [Response schema](https://code.claude.com/docs/en/hooks#response-schema).

Not all events support prompt/agent hooks; the reference lists two groups — events that support **all five** handler types vs those limited to `command` / `http` / `mcp_tool`.

## Agent hooks (`type: "agent"`)

- **Experimental** — behavior and config may change; for production, prefer **command hooks** when possible (official guidance).
- Spawn a **subagent** with tools (Read, Grep, Glob, …) to investigate across multiple turns (up to documented turn budget), then return the same **`ok` / `reason`** schema as prompt hooks.

Configuration mirrors prompt hooks (`prompt`, optional `model`, longer default **timeout**).

## When to prefer command hooks

If the decision is a **deterministic** function of stdin JSON (regex, file path rules, allowlist), a command hook is simpler, cheaper, and easier to test than LLM-based hooks.

Use prompt/agent hooks when you need **judgment** over structured criteria that are awkward to encode purely as rules — subject to event support tables in the reference.
