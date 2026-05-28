# Codex vs. Claude Paths

| Concept | Codex | Claude Code |
|---------|-------|-------------|
| Skills | `.agents/skills/<name>/SKILL.md` | `.claude/skills/<name>/SKILL.md` |
| Agents | `.codex/agents/<name>.toml` | `.claude/agents/` or not used |
| Hooks | `.codex/hooks.json` + `.codex/hooks/` | `settings.json` hooks |
| Config | `.codex/config.toml` | `.claude/CLAUDE.md` |
| Custom agent format | TOML | Markdown frontmatter |

## Critical Rules

- **Skills** live under `.agents/skills/`, NEVER `.codex/`.
- **Agents** live under `.codex/agents/`, NEVER `.agents/`.
- **Hooks** are Python scripts referenced by `.codex/hooks.json`, NOT inline JSON in a markdown file.
- **Config** is `.codex/config.toml`, not `CLAUDE.md`.

## Discovery Paths

Codex scans for skills in this order:
1. `repo/.agents/skills/<name>/SKILL.md`
2. `~/.agents/skills/<name>/SKILL.md`
3. `/etc/codex/skills/<name>/SKILL.md`

Custom agents are loaded from:
1. `repo/.codex/agents/<name>.toml`
2. `~/.codex/agents/<name>.toml`

Hooks are loaded from config layers:
1. `repo/.codex/hooks.json`
2. `repo/.codex/config.toml`
3. `~/.codex/hooks.json`
4. `~/.codex/config.toml`
