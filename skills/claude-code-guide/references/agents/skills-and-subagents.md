---
source_urls:
  - https://code.claude.com/docs/en/skills#run-skills-in-a-subagent
  - https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents
last_reviewed: 2026-05-13
---

# Skills and Subagents

There are **two valid compositions**. Users often confuse them — pick based on **what owns the task**.

## 1. Skill with `context: fork`

Use this when the **skill itself** is an executable workflow that should run in **isolation**.

**Examples:**
- deep code research
- PR summary
- dependency audit
- architecture map

**Division of labor:**
- The **skill** defines the task steps and success criteria.
- The **selected agent** defines the execution environment (tools, model, permissions).

```yaml
---
name: context-audit
description: Audit Claude Code context files and recommend cleanup.
context: fork
agent: Explore
---
Audit the repository instruction system.
Check:
- CLAUDE.md
- AGENTS.md
- context.md
- .claude/rules/
- .claude/agents/
- .claude/skills/
Return:
- duplicated instructions
- conflicting instructions
- stale instructions
- what should move to root, rule, skill, agent, or local memory
```

Use this when the workflow may read many files or produce noisy intermediate output.

Official: [Run skills in a subagent](https://code.claude.com/docs/en/skills#run-skills-in-a-subagent).

## 2. Subagent with `skills:`

Use this when the **subagent** is the worker and needs **reference material** injected up front.

**Examples:**
- API implementer with `api-conventions`
- security reviewer with `security-checklist`
- database agent with `sql-style-guide`

**Division of labor:**
- The **subagent body** defines role, process, and return format.
- The **skills** provide durable domain knowledge (full skill content is injected at startup).

```yaml
---
name: api-reviewer
description: Reviews API routes for validation, errors, permissions, and contract consistency.
tools: Read, Glob, Grep
skills:
  - api-conventions
  - error-handling
---
You are an API reviewer. Use the preloaded skills as the review standard.
```

Use this for stable specialist knowledge.

Official: [Preload skills into subagents](https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents).

## Nuances

- Preloading is **not** the same as banning other skills: unless `Skill` is removed from tools or disallowed, the agent may still discover/invoke other skills at runtime.
- Skills with `disable-model-invocation: true` **cannot** be preloaded.
- Missing or disabled listed skills are **skipped** with a debug-log warning.

## Rule of Thumb

| User need | Prefer |
| --- | --- |
| Repeatable workflow / slash-style procedure | **Skill** + optional `context: fork` |
| Specialized recurring **role** with optional playbooks | **Subagent** + optional `skills:` |

## Mental Model

Both compositions share the same underlying "inject content into an isolated worker" machinery — what differs is **which artifact is the spine of the work** (skill vs agent prompt).
