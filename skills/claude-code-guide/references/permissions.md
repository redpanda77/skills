---
source_urls:
  - https://code.claude.com/docs/en/permissions
last_reviewed: 2026-05-13
---

# Permissions rules

`/permissions` lists effective **allow / ask / deny** rules and their originating file.

## Evaluation order

**Deny → ask → allow.** First match wins; deny always beats allow.

> Rules are enforced by **Claude Code**, not the model. Prompts and `CLAUDE.md` influence intent, not capability.

## Rule syntax

`Tool` or `Tool(specifier)`:

- `Bash` — all shell commands (`Bash(*)` equivalent).
- `Bash(npm test)` — exact command prefix patterns (see official glob and `:*` suffix rules).
- `Read(./.env)` — path-specific reads.
- `WebFetch(domain:example.com)` — domain-scoped fetch.

Wildcards for Bash are powerful and easy to over-broaden — copy examples from the official doc and test with `/permissions`.

## Modes vs rules

Modes (see `permission-modes.md`) set default prompting behavior; rules refine per tool/pattern. `bypassPermissions` skips the permission system (still has catastrophic command circuit breakers).

## Managed policy

Org admins can disable risky modes (`disableBypassPermissionsMode`, `disableAutoMode`) and ship allow/deny baselines.

Official: [Configure permissions](https://code.claude.com/docs/en/permissions).
