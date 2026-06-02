---
name: agent-execution-decision
description: Decision tree for where to place a rule, when to use a skill vs agent vs team, and when to use hooks.
---

# Execution Decision Tree

## Is this global repo knowledge?
- **Yes** → `AGENTS.md` / `CLAUDE.md`
- **No** → continue

## Does this apply to a specific path or file type?
- **Yes** → `.claude/rules/*.md` with `paths`
- **No** → continue

## Is this a repeatable task workflow?
- **Yes** → `.claude/skills/<skill>/SKILL.md`
- **No** → continue

## Is this a specialized role or worker?
- **Yes** → `.claude/agents/<agent>.md`
- **No** → continue

## Does the task need parallel workers who communicate?
- **Yes** → agent team
- **No** → continue

## Does the task need enforcement at a fixed lifecycle event?
- **Yes** → hook (see `references/hooks`)
- **No** → probably unnecessary context

## Subagent vs Skill vs Agent Team

| Need | Prefer |
|------|--------|
| Repeatable workflow / slash-style procedure | **Skill** + optional `context: fork` |
| Specialized recurring **role** with optional playbooks | **Subagent** + optional `skills:` |
| Multiple workers communicating, parallel exploration | **Agent team** |
| Hard enforcement at lifecycle boundary | **Hook** |

## Quick Reference

- **Subagent**: main session → Agent tool → one specialist context → summary returns
- **Agent team**: lead session → multiple Claude Code sessions → shared tasks/messages → synthesized result
- **Skill**: workflow loaded on demand via Skill tool or `skills:` frontmatter
- **Rule**: passive guidance loaded only when matching files are touched

## Quality Controls

- Use root context only for repo-wide rules.
- Use path-scoped rules to avoid irrelevant context.
- Use skills for long or rare workflows.
- Use agents for specialized roles.
- Use teams only when parallelism is worth the cost.
- Start teams with review/research before implementation.
- Assign file ownership before parallel edits.
- Use plan approval for risky team implementation.
- Use hooks for hard enforcement.
