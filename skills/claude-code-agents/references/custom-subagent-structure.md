---
source_urls:
  - https://code.claude.com/docs/en/sub-agents#quickstart-create-your-first-subagent
  - https://code.claude.com/docs/en/sub-agents#write-subagent-files
  - https://code.claude.com/docs/en/sub-agents#configure-subagents
last_reviewed: 2026-05-13
---

# Custom subagent structure

## File format

Subagents are **Markdown files** with **YAML frontmatter** followed by the **system prompt body** (markdown). Only the subagent definition’s body and injected content shape its behavior — it does **not** receive the full Claude Code system prompt.

Official: [Quickstart](https://code.claude.com/docs/en/sub-agents#quickstart-create-your-first-subagent), [Write subagent files](https://code.claude.com/docs/en/sub-agents#write-subagent-files).

## Where files live (precedence)

Higher priority wins when names collide:

| Location | Scope | Priority |
| --- | --- | --- |
| Managed settings (org) | organization | 1 (highest) |
| `--agents` CLI JSON | current session | 2 |
| `.claude/agents/` | project | 3 |
| `~/.claude/agents/` | all projects (user) | 4 |
| Plugin `agents/` | where plugin enabled | 5 (lowest) |

- **Project agents** (`.claude/agents/`) — team-shareable, repo-specific.
- **User agents** (`~/.claude/agents/`) — personal defaults across repos.
- **CLI `--agents`** — ephemeral JSON; same frontmatter fields as files (`prompt` = file body).

Project agents are discovered by **walking up** from the cwd. Directories added with `--add-dir` grant **file access only**, not configuration discovery — they are **not** scanned for subagents.

## Authoring workflows

1. **`/agents`** — recommended UI for create/edit/delete, running tab, library.
2. **Manual files** — edit markdown on disk; **restart session** to pick up changes made outside `/agents` (definitions created via `/agents` apply immediately).
3. **`claude agents`** — CLI listing (pipe-friendly).

## Plugins and managed agents

- **Plugins:** ship `agents/` with the plugin; see [plugin agents reference](https://code.claude.com/en/plugins-reference#agents).
- **Managed:** org admins deploy markdown under managed settings; same frontmatter as project/user agents.

## Security note (plugins)

Plugin subagents **ignore** `hooks`, `mcpServers`, and `permissionMode` in frontmatter. Copy the agent into `.claude/agents/` or `~/.claude/agents/` if those fields are required, or use session `permissions.allow` / `permissions.deny` where appropriate (session-wide, not per-subagent).
