---
name: user-intent-matrix
description: Domain × intent → reference file mapping for the claude-code-guide router. Load when the user asks a question and you need to route to the right topic.
---

# User Intent Matrix

Map user questions to the right reference file. Use this when the router in `SKILL.md` is ambiguous.

## Product (CLI, Settings, Permissions, Memory)

| Intent | Reference |
| --- | --- |
| CLAUDE.md, auto memory, rules | `references/product/memory.md` |
| Permission modes (shift+tab, plan, auto, bypass) | `references/product/permission-modes.md` |
| allow/deny rules, tool permissions | `references/product/permissions.md` |
| settings.json scopes, managed, local | `references/product/settings.md` |
| CLI flags, `-p`, `--agent` | `references/product/cli-reference.md` |
| Slash commands in REPL | `references/product/commands.md` |
| Environment variables | `references/product/env-vars.md` |
| Tool names for hooks/permissions | `references/product/tools-reference.md` |
| Plugins vs `.claude/` standalone | `references/product/plugins.md` |
| Channels, Telegram, push events | `references/product/channels.md` |

## Agents (Subagents, Teams, Frontmatter, Patterns)

| Intent | Reference |
| --- | --- |
| Skill vs subagent vs hook vs plugin | `references/agents/execution-decision.md` |
| What subagents are, when to use | `references/agents/subagent-overview.md` |
| How to build a custom agent | `references/agents/custom-subagent-structure.md` |
| Frontmatter fields (tools, model, skills, hooks) | `references/agents/frontmatter-fields.md` |
| Agent teams (multiple sessions) | `references/agents/agent-teams.md` |
| Agent patterns (researcher, reviewer, debugger) | `references/agents/agent-patterns.md` |
| Composition patterns (orchestrator, parallel) | `references/agents/agent-composition-patterns.md` |
| Execution model, why Claude avoids delegating | `references/agents/agent-execution-and-design.md` |
| Context management, isolation, transcripts | `references/agents/context-management.md` |
| Foreground/background/worktrees | `references/agents/foreground-background-worktrees.md` |
| Debugging subagents | `references/agents/debugging-subagents.md` |
| Skills + subagents composition | `references/agents/skills-and-subagents.md` |
| Invocation, delegation, @-mention | `references/agents/invocation-and-delegation.md` |
| Built-in agents (Explore, Plan, General-purpose) | `references/agents/built-in-subagents.md` |
| Tool permissions and models | `references/agents/tool-permissions-and-models.md` |
| Coordinator pattern | `references/agents/coordinator.md` |
| Repo structure (`.claude/` layout) | `references/agents/repo-structure.md` |
| Hooks inside agents (bridge) | `references/agents/hooks-in-agents-bridge.md` |
| Principles | `references/agents/principles.md` |

## Hooks (Events, Matchers, Automation, Security)

| Intent | Reference |
| --- | --- |
| Hook lifecycle, how they resolve | `references/hooks/hook-lifecycle.md` |
| Event catalog (SessionStart, PreToolUse, etc.) | `references/hooks/hook-events.md` |
| Hooks in skills and agents | `references/hooks/hooks-in-skills-and-agents.md` |
| Configuration schema, locations | `references/hooks/configuration-schema.md` |
| Matchers and `if` filters | `references/hooks/matchers-and-if.md` |
| Input/output JSON, exit codes | `references/hooks/input-output.md` |
| Security practices | `references/hooks/security.md` |
| Async hooks | `references/hooks/async-hooks.md` |
| Prompt and agent hooks | `references/hooks/prompt-and-agent-hooks.md` |
| Debugging with `/hooks` | `references/hooks/debugging.md` |
| Common patterns | `references/hooks/patterns.md` |

## Checklists

| Intent | Checklist |
| --- | --- |
| Design a new agent | `checklists/agent-design-checklist.md` |
| Write a delegation description | `checklists/delegation-description-checklist.md` |
| Permissions for an agent | `checklists/permissions-checklist.md` |
| When to create an agent vs skill | `checklists/when-to-create-an-agent.md` |
| Anti-patterns | `checklists/anti-patterns.md` |

## Examples

| Intent | Example |
| --- | --- |
| Agent examples (security, reviewer, debugger) | `examples/agents/` |
| Agent composition (parallel, reviewer→implementer) | `examples/compositions/` |
| Skill with fork context | `examples/skills/` |
| Hook settings (block, format, notify, async) | `examples/hooks/` |

## Scripts and Tests

| Intent | Script |
| --- | --- |
| Validate agent frontmatter | `scripts/validate-agent-frontmatter.py` |
| Lint agent description | `scripts/lint-agent-description.py` |
| Validate hook config | `scripts/validate-hook-config.py` |
| Simulate hook input | `scripts/simulate-hook-input.py` |
| Block dangerous bash | `scripts/block-dangerous-bash.sh` |
| Run formatters | `scripts/run-formatters.sh` |
| Log hook payload | `scripts/log-hook-payload.sh` |
| Validate generated hook | `scripts/validate-generated-hook.sh` |
| Test hooks | `tests/test-hooks.sh` |
| Hook fixtures | `tests/fixtures/` |
