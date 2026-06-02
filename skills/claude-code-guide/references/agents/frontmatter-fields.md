---
name: agent-frontmatter-fields
description: Deep dive into every agent frontmatter field. Use when writing or reviewing a subagent definition.
---

# Agent Frontmatter Fields

Only **`name`** and **`description`** are required. The Markdown body is the agent's system prompt. Subagent files are loaded at session start, so manual edits usually require restarting Claude Code unless the agent was created through `/agents`.

## 1. Identity and Delegation

### `name`

Required. Stable identifier. Hooks receive this as `agent_type`. Use lowercase words with hyphens.

Good: `security-reviewer`, `test-runner`, `api-reviewer`
Bad: `helper`, `expert`, `agent1`

The filename should match the name to avoid confusion.

### `description`

Required. The most important field for automatic delegation. Claude uses it to decide when to send work to the agent.

Weak: `description: Helps with backend code.`

Strong: `description: Use when reviewing backend API routes, request validation, authorization checks, database writes, transactions, and error handling.`

Use this formula: `Use when [trigger/task] involving [domain/files/risk], especially [specific cases].`

## 2. Capability Fields

### `tools`

Optional allowlist. If omitted, the agent inherits all tools available in the main conversation. `Agent`, `AskUserQuestion`, `EnterPlanMode`, `ScheduleWakeup`, and `WaitForMcpServers` are not available to subagents even if listed.

Read-only reviewer: `tools: Read, Glob, Grep`
Reviewer that may run commands: `tools: Read, Glob, Grep, Bash`
Implementation agent: `tools: Read, Glob, Grep, Bash, Edit, Write`

When an agent runs as the main thread via `claude --agent`, you can restrict spawnable subagents:

```yaml
tools: Agent(security-reviewer, test-runner), Read, Glob, Grep, Bash
```

Subagents cannot spawn other subagents, so `Agent(...)` syntax has no effect inside a normal delegated subagent.

### `disallowedTools`

Optional denylist. Applied to inherited or explicit tool set. If both `tools` and `disallowedTools` are set, `disallowedTools` is applied first, then `tools` filters the remainder. A tool in both is removed.

```yaml
disallowedTools: Write, Edit
```

Use `tools` for strict allowlists. Use `disallowedTools` for inheritance minus a few dangerous tools.

## 3. Permission Fields

### `permissionMode`

Optional. Supported values: `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`.

| Mode | Use |
|------|-----|
| `plan` | Read-only exploration |
| `acceptEdits` | Auto-accept file edits and common filesystem commands |
| `dontAsk` | Fail closed if approval needed |
| `bypassPermissions` | Skip prompts entirely — use with caution |
| `default` | Standard permission prompts |
| `auto` | Classifier-reviewed commands |

Parent session modes can override the subagent. If the parent uses `bypassPermissions` or `acceptEdits`, that takes precedence. If the parent uses `auto`, the subagent inherits `auto` and ignores its own `permissionMode`.

## 4. Model and Reasoning

### `model`

Optional. Aliases: `haiku`, `sonnet`, `opus`, `inherit` (default if omitted). Or a full model ID like `claude-sonnet-4-6`.

Resolution order:
1. `CLAUDE_CODE_SUBAGENT_MODEL` env variable
2. Per-invocation `model` parameter from the delegator
3. Definition frontmatter `model`
4. Main conversation model

| Model | Use |
|-------|-----|
| `haiku` | Cheap search or first-pass review |
| `sonnet` | Normal specialist work |
| `opus` | Hard architecture/security reasoning |
| `inherit` | Follow parent session |

Pick the cheapest model that can do the job reliably.

### `effort`

Optional. Overrides session effort: `low`, `medium`, `high`, `xhigh`, `max`.

| Level | Use |
|-------|-----|
| `low` | Fast triage |
| `medium` | Normal review |
| `high` | Deep audit |

Do not blindly set every agent to `max`. It increases cost and latency.

## 5. Runtime Control

### `maxTurns`

Optional. Caps the number of agentic turns before the subagent stops.

| Default | Use |
|---------|-----|
| 5 | Quick reviewer |
| 8 | Test diagnosis |
| 12 | Deep audit |

Set `maxTurns` when the agent has a bounded job. Leave it unset only for roles that legitimately need open-ended exploration.

### `background`

Optional. Forces the agent to run as a background task.

Use for: long test runs, broad codebase audits, dependency analysis, slow research.
Avoid for: tasks needing immediate approval, risky edits, operations where you want to watch each step.

### `isolation`

Optional. `worktree` runs the subagent in a temporary git worktree.

Use for: risky implementation, competing solutions, experiments, migrations.
Do not use when the agent must inspect uncommitted parent-session changes.

## 6. Skill and Knowledge

### `skills`

Optional. Preloads full skill content into the subagent's context at startup.

```yaml
skills:
  - api-conventions
  - error-handling-patterns
```

Use when: the agent always needs that knowledge, the skill is stable reference material.
Do not use when: the workflow is rarely needed, the skill is long and bloats context, the agent can invoke it on demand.

You cannot preload skills that set `disable-model-invocation: true`. Missing or disabled skills are skipped with a warning.

## 7. Persistent Memory

### `memory`

Optional. Enables persistent memory for the subagent.

| Scope | Path | Use |
|-------|------|-----|
| `user` | `~/.claude/agent-memory/<agent-name>/` | Personal reusable knowledge across projects |
| `project` | `.claude/agent-memory/<agent-name>/` | Project-specific, shareable |
| `local` | `.claude/agent-memory-local/<agent-name>/` | Project-specific, not committed |

Use `project` for agents that accumulate project-specific knowledge: code reviewers, context auditors, test-runners.

When memory is enabled, Claude Code includes memory-management instructions, injects the first 200 lines or 25KB of `MEMORY.md`, and automatically enables `Read`, `Write`, and `Edit` so the subagent can manage its memory files.

## 8. MCP

### `mcpServers`

Optional. Gives the subagent MCP servers.

String reference (reuse configured server):
```yaml
mcpServers:
  - github
```

Inline definition (keep out of parent context):
```yaml
mcpServers:
  - playwright:
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
```

Use inline when: only this agent needs the server, the MCP tool descriptions are large, the parent should not have access.
Use a reference when: the server is already configured, the parent and agent should share it.

Plugin subagents ignore `mcpServers` for security reasons.

## 9. Hooks

### `hooks`

Optional. Defines lifecycle or tool hooks scoped to this subagent.

```yaml
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly-query.sh"
```

Frontmatter hooks run only while that subagent is active and are cleaned up when it finishes.

Use hooks for enforcement. Use prompts for guidance.

Plugin subagents ignore hooks for security reasons.

## 10. UI and Main Session

### `color`

Optional. UI display color.

| Agent | Suggested Color |
|-------|----------------|
| security-reviewer | red |
| test-runner | green |
| frontend-reviewer | cyan |
| backend-reviewer | blue |
| performance-reviewer | orange |
| coordinator | purple |
| context-auditor | yellow |

### `initialPrompt`

Optional. Only relevant when the agent runs as the main session via `--agent` or the `agent` setting.

```yaml
initialPrompt: "Audit the repository instruction system and produce a cleanup plan."
```

Auto-submitted as the first user turn. Commands and skills are processed. Prepended to any user-provided prompt.

Use for: default auditor sessions, dedicated review shells, project-specific coordinator sessions.
Do not use for ordinary subagents unless you run them with `claude --agent`.

## 11. Agent-Team Compatibility

When a subagent definition is used as a teammate type, not all frontmatter behaves the same.

**Normal subagent execution:** all fields apply.
**Agent-team teammate execution:** `tools`, `model`, `body` apply; `skills` and `mcpServers` frontmatter do not.

Teammates load skills and MCP servers like regular sessions. They start with the lead's permission settings.

## 12. Full Examples

### Strict reviewer

```yaml
---
name: security-reviewer
description: Use proactively when reviewing authentication, authorization, secrets, input validation, dependency risk, or privileged operations.
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
model: sonnet
permissionMode: plan
maxTurns: 10
skills:
  - security-review-patterns
memory: project
background: true
color: red
---
You are a security reviewer for this repository.
Review for:
- authentication flaws
- authorization bypasses
- secrets exposure
- unsafe input handling
- injection risks
- insecure dependencies
- missing validation around privileged operations
Do not edit files.
Return:
- severity
- affected file path
- issue
- reasoning
- suggested fix
```

### Implementation worker

```yaml
---
name: backend-implementer
description: Use when implementing backend API routes, service-layer changes, database writes, validation, and error handling.
tools: Read, Glob, Grep, Bash, Edit, Write
model: sonnet
permissionMode: acceptEdits
maxTurns: 12
skills:
  - api-conventions
  - error-handling-patterns
memory: project
isolation: worktree
color: blue
---
You are a backend implementation agent.
Before editing:
1. Inspect existing route, service, and test patterns.
2. Identify the smallest safe change.
3. Explain the implementation plan.
When editing:
- follow the preloaded API conventions
- preserve existing behavior unless explicitly changing it
- add or update targeted tests
- avoid broad refactors
Return:
- files changed
- behavior changed
- tests run
- risks or follow-ups
```

### Coordinator

```yaml
---
name: coordinator
description: Use as the main session agent for complex repo work that requires choosing between direct edits, skills, subagents, and agent teams.
tools: Agent(security-reviewer, test-runner, frontend-reviewer, backend-reviewer), Read, Glob, Grep, Bash
model: sonnet
effort: high
color: purple
initialPrompt: "Classify the task, decide whether to work directly or delegate, and keep global context small."
---
You are the repository coordination agent.
Classify every task:
1. Small local change → handle directly.
2. Repeatable workflow → invoke or recommend a skill.
3. Specialist review → delegate to a subagent.
4. Parallel independent work → propose an agent team.
5. Risky edits → require a plan before implementation.
Avoid parallel edits to the same file.
Use review/research teams before implementation teams.
Prefer path-scoped rules and skills over expanding root context.
```
