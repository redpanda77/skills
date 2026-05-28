# Frontmatter

YAML frontmatter is the configuration block at the top of every `.md` file that Claude Code loads as a skill, agent, or command. The harness parses it to decide how to run the file.

## Syntax

```yaml
---
name: agent-name
description: What it does. Use when [specific triggers].
---
```

## Required fields

| Field | Applies to | Purpose |
|-------|-----------|---------|
| `name` | Skills, agents, commands | Kebab-case identifier. Used in `Agent` tool calls and `/` commands. |
| `description` | Skills, agents, commands | Trigger text. Claude uses this to decide when to load the skill or invoke the agent. Must include "Use when..." |

## Optional fields

| Field | Applies to | Purpose |
|-------|-----------|---------|
| `tools` | Agents | List of allowed tools: `["Read", "Write", "Bash", "Agent"]` |
| `disallowedTools` | Agents | List of forbidden tools: `["Edit"]` |
| `model` | Agents | Model override: `claude-sonnet-4-6` |
| `permissionMode` | Agents | `suggest` or `autoEdit` |
| `mcpServers` | Agents | MCP servers to load: `["server-name"]` |
| `hooks` | Agents | Hooks to apply: `["stop-if-not-done"]` |
| `skills` | Agents, subagents | Skills to inject into the agent's context |
| `memory` | Agents | Memory files to load |
| `background` | Agents | Run as background task: `true` or `false` |
| `isolation` | Agents | Worktree isolation: `worktree` |

## Skills

```yaml
---
name: my-system
 description: Operating manual for this project. Use when starting a new session or when asked about project conventions.
---
```

Skills live in `.claude/skills/<name>/SKILL.md` or `~/.claude/skills/<name>/SKILL.md`.

The `description` is the only thing Claude sees when deciding to load the skill. Make it specific and trigger-rich.

## Agents

```yaml
---
name: judge-dialogue
 description: Evaluates dialogue quality. Use when closing dialogue tasks.
 skills:
   - mission-control
   - dialogue-principles
 tools: ["Read", "Write", "Bash"]
 disallowedTools: ["Agent", "Edit"]
 model: claude-sonnet-4-6
---
```

Agents live in `.claude/agents/<name>.md`.

Use `skills:` to inject domain knowledge. Use `tools:` and `disallowedTools:` to bound the agent's capabilities.

## Commands

```yaml
---
 description: Run the full closure workflow for a task. Verifies acceptance criteria, runs validation, updates tracking files, commits.
---
```

Commands live in `.claude/commands/<name>.md`.

Commands are thin shims — they load the system skill and follow its procedure. The `description` is what the user sees when they type `/`.

## Reference

For complete frontmatter specification, validation rules, and anti-patterns:
- Invoke `write-a-skill` — see its "Step 2: Validate Frontmatter" section
- `references/GUIDE.md` in `write-a-skill` — full technical reference

## Rules

- `name` must be kebab-case. No underscores or camelCase.
- `description` must include "Use when..." triggers. This is how Claude decides to load it.
- `skills:` is the primary way to give subagents durable domain knowledge. The subagent body defines *how* to work; the skill defines *what* to know.
- Keep the markdown body focused. The frontmatter is the contract; the body is the instructions.
