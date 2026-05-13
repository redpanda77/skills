---
source_urls:
  - https://code.claude.com/docs/en/features-overview#compare-similar-features
last_reviewed: 2026-05-13
---

# Agent composition patterns

## Orchestrator → researcher → implementer → reviewer

**Main conversation:**

1. states goal and constraints  
2. delegates **research** (Explore or custom)  
3. decides plan / scope  
4. delegates **implementation** (narrow, tool-appropriate)  
5. delegates **review** (read-only reviewer)

Each hop should return **structured summaries** the parent can route onward.

## Parallel reviewers

Spawn separate agents for **security**, **performance**, **tests**, **API compatibility**.

Each returns a **focused** report; parent synthesizes conflicts and priorities.

## Skill-driven fork

Use a skill with `context: fork` for a reusable isolated task.

**Examples:**

- `/deep-research auth middleware`
- `/pr-summary 123`
- `/map-codepath checkout flow`

## Subagent with preloaded skills

Use when the agent needs durable project/domain knowledge without re-discovery.

**Examples:**

- `api-implementer` preloads `api-conventions`
- `db-reviewer` preloads `sql-style-guide`
- `frontend-reviewer` preloads `design-system`

## Agent with hook bridge

Use hooks when you need **lifecycle automation** or **deterministic guardrails**:

- log agent start/stop
- block unsafe tools inside an agent
- enforce read-only behavior beyond tool lists
- run validation after edits

**Do not** re-document hook JSON here — read `claude-code-hooks` and `references/hooks-in-agents-bridge.md`.

## Feature comparison pointer

When users ask “skill vs subagent vs hook vs plugin?”, start from the official comparison: [Compare similar features](https://code.claude.com/docs/en/features-overview#compare-similar-features).
