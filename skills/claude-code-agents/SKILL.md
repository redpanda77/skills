---
name: claude-code-agents
description: Use when designing, creating, reviewing, invoking, or debugging Claude Code subagents and agent workflows. Covers built-in agents, custom subagents, delegation descriptions, permissions, models, context isolation, skills in agents, forked skills, and agent composition patterns.
---

# Claude Code Agents and Subagents

Use this skill to help users design, implement, and debug Claude Code subagents.

Do not duplicate hook internals here. For hook lifecycle, matchers, input/output, blocking, and hook security, refer to the existing `claude-code-hooks` skill.

## Related skills

- **`claude-code-guide`** — Claude Code-wide docs map (memory, settings, permissions, CLI, commands, env vars, tools, plugins, channels, hooks guide orientation). Use for “how does X work?” routing; stay in this skill for subagent design, `skills:` vs forked skills, and agent checklists.

## Core decision

Use a subagent when the task should run in an isolated context and return only a summary.

**Good fits:**

- codebase research across many files
- noisy test/debug investigation
- security or performance review
- specialized review roles
- constrained database or infrastructure investigation
- parallel exploration
- work that needs different tools, model, or permissions

**Poor fits:**

- a short answer in the main conversation
- reusable instructions with no isolated task
- one-off project conventions
- deterministic automation that must run every time
- workflows that are better represented as a skill

## Decide what to create

1. Use a built-in agent if `Explore`, `Plan`, or `general-purpose` is sufficient.
2. Create a custom subagent when the same role repeats across tasks.
3. Use a skill with `context: fork` when the reusable workflow itself should run in isolation.
4. Use a subagent with `skills:` when the agent needs reusable reference material preloaded.
5. Use the hooks skill only when the agent needs lifecycle guardrails or project-level agent events.

## Agent design workflow

1. Identify the agent’s role.
2. Define when Claude should delegate to it.
3. Choose tools and disallowed tools.
4. Choose model and reasoning effort.
5. Decide whether it should run in foreground, background, or worktree isolation.
6. Decide whether it needs preloaded skills.
7. Write the system prompt body.
8. Add examples only if they improve delegation or behavior.
9. Validate frontmatter (`scripts/validate-agent-frontmatter.py`).
10. Test with explicit invocation and automatic delegation.

## Reference files

| Topic | File |
| --- | --- |
| Overview | `references/subagent-overview.md` |
| Built-ins | `references/built-in-subagents.md` |
| File format | `references/custom-subagent-structure.md` |
| Frontmatter | `references/frontmatter-fields.md` |
| Delegation | `references/invocation-and-delegation.md` |
| Tools/models/permissions | `references/tool-permissions-and-models.md` |
| Foreground/background/worktrees | `references/foreground-background-worktrees.md` |
| Context | `references/context-management.md` |
| Skills + subagents | `references/skills-and-subagents.md` |
| Agent patterns | `references/agent-patterns.md` |
| Composition patterns | `references/agent-composition-patterns.md` |
| Debugging | `references/debugging-subagents.md` |
| Hooks bridge | `references/hooks-in-agents-bridge.md` |

## Tooling

- `scripts/validate-agent-frontmatter.py` — structural checks on agent Markdown frontmatter.
- `scripts/lint-agent-description.py` — delegation-description heuristics.

## Architecture with other skills

- **`claude-code-hooks/`** — canonical for hooks (lifecycle, matchers, I/O, blocking, safety).
- **`claude-code-agents/`** — canonical for subagents and agent patterns; defers to hooks for scoped or project-level `SubagentStart` / `SubagentStop`.
- **Domain skills** — API conventions, review checklists, testing standards, migration playbooks.
- **Custom agents** — specialized workers that may preload domain skills via `skills:`.
