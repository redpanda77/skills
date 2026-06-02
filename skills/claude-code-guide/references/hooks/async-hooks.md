---
source_urls:
  - https://code.claude.com/docs/en/hooks#run-hooks-in-the-background
  - https://code.claude.com/docs/en/hooks#configure-an-async-hook
  - https://code.claude.com/docs/en/hooks#how-async-hooks-execute
  - https://code.claude.com/docs/en/hooks#limitations
last_reviewed: 2026-05-13
---

# Async hooks

## Purpose

Long-running work (tests, deploys, large linters) can run **without blocking** Claude by setting **`"async": true`** on a **`type: "command"`** hook.

Async hooks **cannot** deny tool calls or return blocking decisions — by the time output arrives, the triggering action has already proceeded.

## Configuration

- Set **`async`: true** on the command handler.
- Optional **`asyncRewake`**: background run; exit code **2** can wake Claude with stderr/stdout as a system reminder (see official doc).

## Execution model

Claude Code starts the process and continues immediately. The hook still receives the **same stdin JSON** as synchronous hooks.

When the process exits, **`systemMessage`** / **`additionalContext`** in JSON output may be delivered on the **next** user turn (see reference for idle-session behavior and **`asyncRewake`** exception).

## Limitations (official)

- Only **`command`** hooks support `async` — not prompt hooks.
- **No blocking / permission decisions** from async handlers.
- **No deduplication** across repeated firings — each run is a separate background process.

Full list: [Limitations](https://code.claude.com/docs/en/hooks#limitations) under async section.
