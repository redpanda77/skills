---
source_urls:
  - https://code.claude.com/docs/en/hooks#debug-hooks
  - https://code.claude.com/docs/en/hooks#the-hooks-menu
  - https://code.claude.com/docs/en/debug-your-config
last_reviewed: 2026-05-13
---

# Debugging hooks

## `/hooks` menu

Type **`/hooks`** to open a **read-only** browser of configured hooks: events, matchers, handler types, and **source locations** (User, Project, Local, Plugin, Session, Built-in).

You cannot edit from this UI — change settings JSON or ask Claude to apply edits.

Official description: [The `/hooks` menu](https://code.claude.com/docs/en/hooks#the-hooks-menu).

## Debug logs

Hook execution details (matched hooks, exit codes, stdout/stderr) go to the **debug log**.

- Run with **`claude --debug-file <path>`** to pin log location, or
- **`claude --debug`** and read the log under **`~/.claude/debug/`** (exact filename pattern per your install — see [Debug hooks](https://code.claude.com/docs/en/hooks#debug-hooks)).

For verbose matcher logging, set **`CLAUDE_CODE_DEBUG_LOG_LEVEL=verbose`** (see official doc).

## Config-wide troubleshooting

For **`/doctor`**, **`/context`**, precedence issues, and broader configuration mistakes, follow **[Debug your config](https://code.claude.com/docs/en/debug-your-config)**.

## Practical checklist

1. Confirm hook appears under **`/hooks`** with correct source file.
2. Reproduce with minimal matcher (`Edit|Write` etc.) to rule out matcher/`if` issues.
3. Inspect debug log for spawn line, timeout, exit code, and JSON parse errors.
4. For command hooks, run the same script with a saved stdin fixture (`tests/fixtures/` in this skill).
