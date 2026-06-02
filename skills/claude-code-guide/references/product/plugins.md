---
source_urls:
  - https://code.claude.com/docs/en/plugins
last_reviewed: 2026-05-13
---

# Plugins (authoring guide)

Plugins package **skills, agents, hooks, MCP servers**, and related components for sharing across projects via marketplaces or local paths.

## Plugins vs standalone `.claude/`

| | Standalone `.claude/` | Plugin directory |
| --- | --- | --- |
| Skill invocation | Short names like `/hello` | Namespaced `/plugin-name:hello` |
| Sharing | copy git repo | versioned distribution |
| Best for | solo experiments, one repo | teams, community reuse |

Start standalone; **promote to a plugin** when you need namespacing and distribution.

## Manifest

`.claude-plugin/plugin.json` defines `name`, `description`, optional `version`, `author`, and links (`homepage`, `repository`, …). See **`plugins-reference.md`** for the full schema and CLI.

## Local development

`claude` supports loading a plugin from a directory (see official quickstart and CLI reference for `--plugin-dir` style workflows).

## Discover / install

Official discovery doc: **Discover and install plugins** (linked from the plugins page). Use `/plugin` commands in the REPL.

Official: [Create plugins](https://code.claude.com/docs/en/plugins).
