---
name: agent-system-principles
description: Core principles and quality controls for the agent system architecture. Use when setting up or auditing the instruction file hierarchy.
---

# Agent System Principles

## The Model

The clean architecture is layered:

- **Root context** — shared repo rules (`AGENTS.md`, `CLAUDE.md`)
- **Path-scoped rules** — local conventions only when relevant (`.claude/rules/`)
- **Skills** — reusable workflows loaded on demand (`.claude/skills/`)
- **Subagents** — specialist workers inside one session (`.claude/agents/`)
- **Agent teams** — multiple independent sessions coordinated by a lead
- **Hooks/settings** — enforcement, permissions, and experimental flags

## The Key Principle

Do not put everything into root context. Root context should be small and global. Path-specific rules should live near the paths they affect. Workflows should become skills. Specialist behavior should become agents. Parallel coordination should become an agent team.

Claude Code treats `CLAUDE.md` as persistent context, not hard enforcement. Long files consume context and reduce adherence.

## Quality Controls

- Use root context only for repo-wide rules.
- Use path-scoped rules to avoid irrelevant context.
- Use skills for long or rare workflows.
- Use agents for specialized roles.
- Use teams only when parallelism is worth the coordination/token cost.
- Start teams with review/research before implementation.
- Assign file ownership before parallel edits.
- Use plan approval for risky team implementation.
- Use hooks for hard enforcement.
- Run `/memory` during audits to see which files are loaded.

## Compact Teaching Summary

| Layer | Analogy | Content |
|-------|---------|---------|
| `AGENTS.md` / `CLAUDE.md` | Shared repo constitution | Project purpose, architecture, commands, global rules |
| `.claude/rules/` | Local laws for specific paths | Path-scoped conventions |
| `.claude/skills/` | Reusable procedures | Workflows, playbooks, checklists |
| `.claude/agents/` | Specialist workers | Roles with toolsets, models, and output contracts |
| Agent teams | Independent sessions collaborating | Parallel review, research, or implementation |
| Hooks/settings | Enforcement | Lifecycle guardrails, permissions, runtime behavior |

## Core Principle

The root file should explain the repo. Subdirectory rules should explain local conventions. Skills should teach repeatable workflows. Agents should define specialized workers. Anything else is probably unnecessary context.
