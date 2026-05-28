---
name: agent-teams
description: Agent teams execution model, enabling, and coordination patterns. Use when the user asks about parallel agents, multi-agent collaboration, or team-based review.
---

# Agent Teams

## Execution Model

Subagents and agent teams are related but different.

- **Subagents** run inside one Claude Code session and report back to the main agent.
- **Agent teams** are multiple independent Claude Code sessions coordinated by a lead session.

Teammates have their own context windows, can message each other directly, and coordinate through a shared task list.

## When to Use Teams

Use subagents when:
- The task is focused
- Only the result matters
- No teammate-to-teammate communication is needed
- You want lower token cost

Use agent teams when:
- Multiple workers need to communicate
- The work benefits from parallel exploration
- Reviewers should challenge each other
- Frontend/backend/tests can proceed independently
- Debugging needs competing hypotheses

Agent teams have higher token cost because each teammate is a separate Claude Code instance with its own context. Anthropic recommends starting with 3–5 teammates for most workflows and avoiding same-file edits because parallel editing can overwrite work.

## Enabling Agent Teams

Agent teams are experimental, disabled by default, and require Claude Code v2.1.32 or later.

In `.claude/settings.json` or `~/.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Or in the shell:

```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

## Using Subagent Definitions as Teammate Roles

A strong design pattern: define stable roles once in `.claude/agents/`, then reuse them both as subagents and agent-team teammates.

Example prompt:

```
Create an agent team to review this branch against main.
Spawn three teammates:
- Alice using the security-reviewer agent type to audit auth, secrets, injection, and dependency risk.
- Bob using the test-runner agent type to run targeted tests and identify missing regression coverage.
- Cara using the frontend-reviewer agent type to review UI behavior and accessibility.
Do not edit files.
Each teammate should produce findings with file paths and severity.
Have them message each other if findings overlap.
Wait for all teammates to finish before synthesizing one prioritized report.
```

Claude Code supports referencing a subagent type when spawning a teammate. The teammate uses the subagent definition’s tools allowlist and model, and the definition body is appended to the teammate’s system prompt.

## Important Compatibility Note

When a subagent definition is used as an agent-team teammate type, not all frontmatter behaves the same way.

**Normal subagent execution:**
- `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `isolation`, `color` all apply.

**Agent-team teammate execution:**
- Role body applies as additional instructions
- Tools allowlist applies
- Model applies
- Team communication tools are still available
- `skills` frontmatter does not apply
- `mcpServers` frontmatter does not apply
- Teammate loads normal project/user context like a regular session

Teammates also start with the lead’s permission settings, and you cannot set per-teammate permission modes at spawn time, though modes can be changed after spawning.

## Recommended Pattern

Define stable roles once in `.claude/agents/`, then reuse them both as subagents and agent-team teammates.

```
.claude/agents/
├── security-reviewer.md
├── test-runner.md
├── frontend-reviewer.md
└── backend-reviewer.md
```

## Core Principle

Use teams only when parallelism is worth the coordination/token cost. Start teams with review/research before implementation. Assign file ownership before parallel edits. Avoid same-file edits.
