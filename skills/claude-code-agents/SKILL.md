---
name: claude-code-agents
description: Use when designing, creating, reviewing, invoking, or debugging Claude Code subagents, agent teams, and the agent system architecture. Covers built-in agents, custom subagents, agent teams, file placement, frontmatter design, and the execution decision tree.
---

# Core Principles

Progressive disclosure. Load only what is needed, when it is needed.
Keep global context small. Push specificity downward into rules, skills, agents, and teams.
Root context is a behavioral contract, not a tutorial. Every line must change behavior.

See `references/principles.md` for the full rationale.

---

# Agent System Model

Five layers, smallest scope first:

1. **Path-scoped rules** (`.claude/rules/`) — passive guidance for specific files
2. **Skills** (`.claude/skills/`) — repeatable workflows loaded on demand
3. **Subagents** (`.claude/agents/`) — specialist workers with isolated context
4. **Agent teams** — multiple independent sessions coordinated by a lead
5. **Hooks/settings** — deterministic enforcement at lifecycle boundaries

See `references/repo-structure.md` for the full layout and `references/execution-decision.md` for the decision tree.

---

# When to Use What

- **Global repo rule** → `AGENTS.md` / `CLAUDE.md`
- **Path-specific passive guidance** → `.claude/rules/*.md` with `paths`
- **Repeatable workflow** → `.claude/skills/<skill>/SKILL.md`
- **Specialist role, isolated context** → `.claude/agents/<agent>.md`
- **Parallel workers that communicate** → agent team (experimental)
- **Hard enforcement at a lifecycle point** → hook (see `claude-code-hooks`)

---

# Reference Files

| Topic | File |
| --- | --- |
| Principles & quality controls | `references/principles.md` |
| Repo structure & file type roles | `references/repo-structure.md` |
| Execution decision tree | `references/execution-decision.md` |
| Subagent overview | `references/subagent-overview.md` |
| Agent teams | `references/agent-teams.md` |
| Coordinator pattern | `references/coordinator.md` |
| Built-in agents | `references/built-in-subagents.md` |
| Custom agent structure | `references/custom-subagent-structure.md` |
| Frontmatter fields | `references/frontmatter-fields.md` |
| Frontmatter design checklist | `references/frontmatter-checklist.md` |
| Invocation & delegation | `references/invocation-and-delegation.md` |
| Tools, permissions, models | `references/tool-permissions-and-models.md` |
| Skills + subagents | `references/skills-and-subagents.md` |
| Foreground/background/worktrees | `references/foreground-background-worktrees.md` |
| Context management | `references/context-management.md` |
| Agent patterns | `references/agent-patterns.md` |
| Composition patterns | `references/agent-composition-patterns.md` |
| Debugging | `references/debugging-subagents.md` |
| Hooks bridge | `references/hooks-in-agents-bridge.md` |

---

# Tooling

- `scripts/validate-agent-frontmatter.py` — structural checks on agent Markdown frontmatter.
- `scripts/lint-agent-description.py` — delegation-description heuristics.
