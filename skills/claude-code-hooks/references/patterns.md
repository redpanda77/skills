---
source_urls:
  - https://code.claude.com/docs/en/hooks-guide
  - https://code.claude.com/docs/en/hooks#how-a-hook-resolves
last_reviewed: 2026-05-13
---

# Patterns (hooks guide)

The **[Hooks guide](https://code.claude.com/docs/en/hooks-guide)** documents copy-pastable patterns, including:

- Desktop / system **notifications** on `Notification`
- **Auto-format** after `Write` / `Edit` on `PostToolUse`
- **Block edits** to protected files (`PreToolUse` / exit code 2 patterns)
- **Re-inject context** after compaction
- **Audit** configuration changes (`ConfigChange`)
- **Reload environment** on `CwdChanged` / `FileChanged`
- **Auto-approve** selective permission prompts

Each pattern includes JSON you merge into the appropriate **settings** file (user, project, or local) or adapt for **plugin** / **skill** frontmatter using the same handler objects.

## Schema truth

Treat the **[Hooks reference](https://code.claude.com/docs/en/hooks)** as the source of truth for **field names**, **per-event decision support**, and **limitation** notes. Use the guide for **intent and examples**, then validate against the reference (and `scripts/validate-hook-config.py` for basic structural checks).

## Related files in this skill

- Examples: `examples/*.json`
- Fixture payloads: `tests/fixtures/*.json`
- Smoke test: `tests/test-hooks.sh`
