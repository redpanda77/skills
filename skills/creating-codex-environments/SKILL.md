---
name: creating-codex-environments
description: Scaffolds local Codex configuration, custom agents, hooks, and skills. Use when setting up Codex for a repo, creating .codex/agents, .codex/hooks, or .agents/skills. Do not use for Claude Code or Claude Desktop setup.
---

**NEVER** use `.claude/` paths for Codex. Codex uses `.codex/` for agents/hooks/config and `.agents/` for skills.

**CRITICAL PATH RULES:**
- Skills → `.agents/skills/<name>/SKILL.md`
- Agents → `.codex/agents/<name>.toml`
- Hooks → `.codex/hooks.json` + `.codex/hooks/`
- Config → `.codex/config.toml`

**STOP:** Read existing `.codex/` and `.agents/` files before writing. Do not overwrite without asking.

## Workflow

1. **Detect state.** Check if `.codex/` and `.agents/` exist. Read `references/local-file-structure.md` for the full layout map.
2. **Determine scope.** If unclear, ask: `full`, `agents-only`, `hooks-only`, `skills-only`, or `audit`.
3. **Create directories.** `mkdir -p .codex/agents .codex/hooks .agents/skills`
4. **Write config.** If missing, create `.codex/config.toml`:
   ```toml
   [agents]
   max_threads = 6
   max_depth = 1
   [features]
   hooks = true
   ```
5. **Create agents.** Write `.codex/agents/<name>.toml` with required fields: `name`, `description`, `developer_instructions`. Read `references/agent-templates.md` for examples.
6. **Create hooks.** Write `.codex/hooks.json` and scripts in `.codex/hooks/`. Read `references/hook-templates.md` for schema and examples.
7. **Create skills.** Write `.agents/skills/<name>/SKILL.md` with frontmatter. Read `references/skill-templates.md` for templates.
8. **Validate.** Run `find .codex .agents -type f` and confirm layout matches the rules above.

**NEVER** write `CLAUDE.md`, `.claude/skills/`, or Claude-style agent definitions in a Codex environment.
