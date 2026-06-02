---
name: agent-execution-and-design
description: How the Agent tool executes internally, design practices to combat LLM laziness, and frontmatter description best practices for reliable delegation.
---

# Agent Execution and Design

## How the Agent tool executes

When Claude Code decides to delegate, it emits an `Agent` tool call. The internal payload looks like this:

```json
{
  "tool_name": "Agent",
  "tool_input": {
    "description": "Investigate React rerenders",
    "prompt": "Find why Dashboard rerenders 40 times"
  }
}
```

The `description` field is what the subagent sees as its task framing. The `prompt` is the full instruction passed to the subagent. In telemetry, hook payloads, and traces, the tool name is `Agent`, not `Task` (the legacy name was removed in Claude Code v2.1.63+).

### Execution lifecycle

1. **Routing** — Claude compares the user's request against every loaded agent's `description`.
2. **Decision** — If a description matches strongly enough, Claude emits an `Agent` tool call instead of handling the task directly.
3. **Spawn** — A new isolated session starts with the subagent's frontmatter + body as its system prompt.
4. **Run** — The subagent executes with its own toolset, model, and permission mode.
5. **Return** — Results flow back to the parent session. Subagents cannot spawn further subagents.

## Why the LLM is lazy and how to fix it

The most common failure mode is not broken agents — it is **Claude choosing to answer directly instead of delegating**. This happens when:

- The `description` is too generic or reads like marketing copy.
- The agent name is vague (`helper`, `expert`).
- The parent session has contradictory instructions that say "handle things yourself."
- The task seems small enough that Claude thinks direct handling is faster.

### Anti-laziness patterns

**1. Description is the router — make it specific**

Bad (Claude answers directly):

```yaml
description: Frontend engineer
```

Good (Claude routes reliably):

```yaml
description: |
  Use this agent when debugging React rendering,
  React Query cache issues, hydration problems,
  or component performance regressions.
```

Use the formula: `Use this agent when [trigger/task] involving [domain/files/risk], especially [specific cases].`

**2. Add "use proactively" when appropriate**

Phrases like `Use proactively when...` or `Always invoke this agent before...` increase delegation probability. Do not lie — only use them if the agent truly should be the default for that class of work.

**3. Enforce delegation in CLAUDE.md**

If an agent must be consulted for a specific domain, add a hard rule in the root instructions:

```md
For React bugs, ALWAYS invoke the react-debugger agent
before proposing a fix.
```

**4. Use @-mention for guaranteed delegation**

If automatic routing is still inconsistent, invoke the agent explicitly with `@"agent-name (agent)"` from the typeahead. This bypasses the router and forces that agent.

**5. Split overloaded agents**

One agent with a broad description competes against itself. Split into narrow agents:

- `react-debugger` — React-specific issues
- `api-reviewer` — Backend route review
- `test-runner` — Test execution and diagnosis

## Frontmatter description best practices

The `description` field is the single most important signal for delegation. Treat it as a routing prompt, not a bio.

| Anti-pattern | Fix |
|--------------|-----|
| `Helps with backend code.` | `Use when reviewing backend API routes, request validation, authorization checks, database writes, transactions, and error handling.` |
| `Security expert` | `Use proactively when reviewing authentication, authorization, secrets, input validation, dependency risk, or privileged operations.` |
| `A helpful agent` | `Use when implementing backend API routes, service-layer changes, database writes, validation, and error handling.` |

### Checklist for a strong description

- [ ] Starts with `Use when...` or `Use proactively when...`
- [ ] Lists concrete triggers (files, tasks, risks)
- [ ] Mentions specific cases, not broad domains
- [ ] Does not contradict the agent's body prompt
- [ ] Is unique relative to other agents in the project

## Verification

If you suspect an agent is never being invoked:

1. **Ask Claude** `What subagents are available?` — If it cannot list them, discovery is failing.
2. **Check logs** — Look for `tool_name: "Agent"` in verbose transcripts or hook payloads.
3. **Test @-mention** — Force the agent manually to confirm it works when routed.
4. **Audit the description** — Run it through the heuristics in `scripts/lint-agent-description.py`.

## Summary

- The `Agent` tool is the internal mechanism. The `description` is the external routing signal.
- Laziness is a design problem, not a model problem. Fix it with specific descriptions, root-level enforcement, and narrow agent scopes.
- If automatic delegation fails, escalate from natural language → @-mention → `--agent` session.
