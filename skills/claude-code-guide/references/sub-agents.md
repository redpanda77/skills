---
source_urls:
  - https://code.claude.com/docs/en/sub-agents
related_skills:
  - claude-code-agents
last_reviewed: 2026-05-13
---

# Subagents (overview)

Subagents are **isolated workers** inside one session: their own context, system prompt (the markdown body), tool allow/deny lists, optional model override, optional preloaded **skills**, optional **hooks**, optional **worktree isolation**.

Delegate when a side task would **flood** the main conversation with search output, logs, or file dumps you will not reuse — the subagent returns a **summary**.

## Built-ins (high level)

- **Explore** — fast read-only search (Haiku).
- **Plan** — read-only research while plan mode is active.
- **general-purpose** — exploration + edits when the parent needs a capable worker.

## Definitions

Markdown + YAML frontmatter; locations include `.claude/agents/`, `~/.claude/agents/`, plugins, managed settings, or ephemeral `--agents` JSON. Precedence and discovery rules are subtle — see the official **Configure subagents** section.

## Important constraints

- Subagents **cannot spawn subagents**; chain work from the **main** conversation.
- **Plugin agents** ignore `hooks`, `mcpServers`, and `permissionMode` frontmatter — copy to project/user agents if you need those fields.

## Where to go deeper

Use the **`claude-code-agents`** skill in this repo for patterns, `skills:` vs `context: fork`, checklists, and `scripts/validate-agent-frontmatter.py`.

Official: [Create custom subagents](https://code.claude.com/docs/en/sub-agents).
