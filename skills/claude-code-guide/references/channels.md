---
source_urls:
  - https://code.claude.com/docs/en/channels
last_reviewed: 2026-05-13
---

# Channels (research preview)

**Channels** let an MCP-style server **push events** into an already-running Claude Code session (CI alerts, chat bridges, webhooks). They are **research preview**, require a **minimum Claude Code version**, Anthropic auth, and org policy may need explicit enablement.

## Mental model

- Install/configure channel plugins (Telegram, Discord, iMessage, fakechat demo).
- Launch Claude Code with **`--channels`** selecting which plugin servers to attach.
- Pair / allowlist senders per official security guidance — inbound chat is untrusted input.

## vs other integrations

Channels deliver into the **local session you have open**. Contrast with cloud-only flows or polling integrations — see official **How channels compare**.

## Building custom channels

See **`channels-reference.md`** for the MCP capability declaration, notification payload, reply tools, sender gating, and permission relay.

During preview, unlisted custom channels may require **`--dangerously-load-development-channels`** for local testing.

Official: [Push events into a running session with channels](https://code.claude.com/docs/en/channels).
