---
source_urls:
  - https://code.claude.com/docs/en/channels-reference
last_reviewed: 2026-05-13
---

# Channels reference (orientation)

Channels are **MCP servers** that declare the **`claude/channel`** capability and emit **`notifications/claude/channel`** events consumed by Claude Code.

## Authoring checklist (condensed)

1. Use `@modelcontextprotocol/sdk` (Node/Bun/Deno).
2. Implement stdio transport (Claude spawns the server).
3. Declare channel capability so Claude registers listeners.
4. Validate notification payload shape per official **Notification format**.
5. Optionally expose a **reply tool** for two-way bridges.
6. **Gate senders** aggressively — treat inbound text as attacker-controlled.
7. Optional: **relay permission prompts** for trusted paths only.

## Research preview constraints

Custom servers may be off the global allowlist — local iteration uses **`--dangerously-load-development-channels`** (see official warning text).

## Relation to user guide

`channels.md` covers installing Telegram/Discord/etc. This reference covers **implementing** a channel server.

Official: [Channels reference](https://code.claude.com/docs/en/channels-reference).
