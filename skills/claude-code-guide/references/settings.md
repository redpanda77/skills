---
source_urls:
  - https://code.claude.com/docs/en/settings
last_reviewed: 2026-05-13
---

# Settings

Claude Code configuration is layered **scopes** plus CLI overrides. Use `/config` (alias `/settings`) for the in-app settings UI.

## Scopes (who wins)

Typical precedence (highest first): **managed policy** → **CLI flags** → **local** (`.claude/settings.local.json`) → **project** (`.claude/settings.json`) → **user** (`~/.claude/settings.json`).

Managed sources include server-delivered policy, MDM plist / Windows registry JSON, and file-based `managed-settings.json` (+ optional `managed-settings.d/*.json` merge rules).

## Common file paths

| Feature | User | Project | Local |
| --- | --- | --- | --- |
| Settings JSON | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` |
| Subagents | `~/.claude/agents/` | `.claude/agents/` | — |
| MCP | `~/.claude.json`, etc. | `.mcp.json` | varies |
| CLAUDE.md | `~/.claude/CLAUDE.md` | `CLAUDE.md` or `.claude/CLAUDE.md` | `CLAUDE.local.md` |

Windows resolves `~/.claude` to `%USERPROFILE%\.claude`.

## Practical tips

- Put **team defaults** in project settings; personal experiments in `settings.local.json` (gitignored when created via tooling).
- Large orgs: watch for **managed-only keys** that user/project cannot override — see permissions doc.

Official: [Claude Code settings](https://code.claude.com/docs/en/settings).
