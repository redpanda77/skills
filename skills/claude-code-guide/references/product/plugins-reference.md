---
source_urls:
  - https://code.claude.com/docs/en/plugins-reference
last_reviewed: 2026-05-13
---

# Plugins reference (orientation)

The reference defines **schemas** for plugin manifests, component layouts, CLI subcommands, versioning, and bundled resources.

## Components a plugin may ship

| Component | Typical location | Notes |
| --- | --- | --- |
| Skills | `skills/<name>/SKILL.md` | namespaced slash commands |
| Commands | `commands/*.md` | simpler than full skills |
| Agents | `agents/*.md` | subject to plugin agent restrictions |
| Hooks | `hooks/hooks.json` | bundled automation |
| MCP / LSP / monitors | per schema | see official sections |

## CLI surface

`claude plugin` (alias `claude plugins`) installs, removes, updates marketplaces, etc. Exact subcommands and flags live in the official **CLI commands reference** section.

## Versioning

`version` in `plugin.json` controls update semantics for marketplace installs; git-only plugins may fall back to commit SHA — see official **Version management**.

Official: [Plugins reference](https://code.claude.com/docs/en/plugins-reference).
