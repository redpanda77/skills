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

Official: [Preload skills into subagents](https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents).

### Nuances

- Preloading is **not** the same as banning other skills: unless `Skill` is removed from tools or disallowed, the agent may still discover/invoke other skills at runtime.
- Skills with `disable-model-invocation: true` **cannot** be preloaded (same eligibility as invocable skills).
- Missing or disabled listed skills are **skipped** with a debug-log warning.

## Rule of thumb

| User need | Prefer |
| --- | --- |
| Repeatable workflow / slash-style procedure | **Skill** + optional `context: fork` |
| Specialized recurring **role** with optional playbooks | **Subagent** + optional `skills:` |

## Mental model

Both compositions share the same underlying “inject content into an isolated worker” machinery — what differs is **which artifact is the spine of the work** (skill vs agent prompt).
