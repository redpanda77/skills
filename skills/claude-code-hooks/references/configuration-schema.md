---
source_urls:
  - https://code.claude.com/docs/en/hooks#configuration
  - https://code.claude.com/docs/en/settings#hook-configuration
  - https://code.claude.com/docs/en/plugins
  - https://code.claude.com/docs/en/plugins-reference#hooks
last_reviewed: 2026-05-13
---

# Configuration schema and hook locations

## Nesting model

Hooks config nests in three levels:

1. **Hook event** — e.g. `PreToolUse`, `PostToolUse`, `Stop`
2. **Matcher group** — filters when the group runs
3. **Hook handlers** — one or more of `command`, `http`, `mcp_tool`, `prompt`, `agent`

See [Configuration](https://code.claude.com/docs/en/hooks#configuration) and [How a hook resolves](https://code.claude.com/docs/en/hooks#how-a-hook-resolves).

## Where hooks are defined (scopes)

| Location | Scope | Shareable |
| --- | --- | --- |
| `~/.claude/settings.json` | All projects | Machine-local |
| `.claude/settings.json` | Single project | Yes (commit) |
| `.claude/settings.local.json` | Single project | No (gitignored) |
| Managed policy | Org-wide | Admin-controlled |
| Plugin `hooks/hooks.json` | When plugin enabled | Bundled with plugin |
| Skill / agent frontmatter | While component active | In skill/agent file |

Details on settings precedence: [Settings](https://code.claude.com/docs/en/settings). Hook-specific settings notes: [Hook configuration](https://code.claude.com/docs/en/settings#hook-configuration).

Enterprise: `allowManagedHooksOnly` can restrict user/project/plugin hooks; managed and force-enabled plugin hooks follow admin policy (see official hooks page).

## Plugins

Plugins ship hooks in **`hooks/hooks.json`** with the same inner `hooks` object shape as settings. Optional top-level `description` in that file is supported.

Plugin script paths often use **`${CLAUDE_PLUGIN_ROOT}`** and **`${CLAUDE_PLUGIN_DATA}`** — see [Reference scripts by path](https://code.claude.com/docs/en/hooks#reference-scripts-by-path) and [Plugin components — hooks](https://code.claude.com/docs/en/plugins-reference#hooks).

## Skills and agents

Skills and agents embed a YAML **`hooks:`** key alongside `name` / `description`. The structure matches settings JSON. See `references/hooks-in-skills-and-agents.md`.
