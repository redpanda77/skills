---
source_urls:
  - https://code.claude.com/docs/en/hooks#security-considerations
  - https://code.claude.com/docs/en/hooks#command-hook-fields
last_reviewed: 2026-05-13
---

# Security considerations

## Disclaimer (official)

**Command hooks run with your user account’s full permissions.** They can read, modify, or delete any files your user can. Treat hook commands like privileged automation: review, version, and test them.

Source: [Security considerations](https://code.claude.com/docs/en/hooks#security-considerations).

## Practices called out in the reference

- **Validate and sanitize** all inputs from the JSON payload; never trust fields blindly.
- **Quote shell variables:** `"$VAR"` not `$VAR`.
- **Block path traversal** (e.g. reject `..` where paths are interpreted as filesystem locations).
- **Prefer absolute paths** for scripts; combine with **`${CLAUDE_PROJECT_DIR}`** / **`${CLAUDE_PLUGIN_ROOT}`** placeholders. In exec form, placeholders substitute without shell quoting risk; in shell form, wrap in double quotes.
- **Avoid touching secrets** — skip `.env`, keys, `.git/` objects unless you have a deliberate, audited reason.

## Command hook mechanics (security-relevant)

Understand **exec form** (`command` + `args`) vs **shell form** (`command` string only). Exec form avoids shell injection for structured arguments; shell form is required for pipes/`&&` but needs careful quoting.

Windows note: `.cmd` / `.bat` shims often require **shell form** or invoking **`node`** on a `.js` file in exec form — see [Exec form and shell form](https://code.claude.com/docs/en/hooks#exec-form-and-shell-form).

## Timeouts

Set explicit **`timeout`** values for handlers that contact the network or run expensive work, so a stuck hook does not hang the session indefinitely (defaults described in [Command hook fields](https://code.claude.com/docs/en/hooks#command-hook-fields)).
