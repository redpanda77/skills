---
name: claude-code-hooks
description: Use when designing, reviewing, implementing, or debugging Claude Code hooks, including settings hooks, plugin hooks, skill-scoped hooks, and agent-scoped hooks. Use for hook lifecycle, events, matchers, security, async hooks, prompt/agent hooks, or the /hooks debugging workflow.
---

# Claude Code Hooks

Use this skill to design, review, implement, and debug Claude Code hooks. Hooks are deterministic automation points in Claude Code. They can be configured in settings files, plugins, skills, or agents.

Keep `SKILL.md` focused; deep material lives under `references/`, `examples/`, and `scripts/` (per [Skills](https://code.claude.com/docs/en/skills) guidance — aim for under 500 lines in `SKILL.md`). Primary sources: [Hooks reference](https://code.claude.com/docs/en/hooks), [Hooks guide](https://code.claude.com/docs/en/hooks-guide), [Skills](https://code.claude.com/docs/en/skills#add-supporting-files).

## First decision

Before writing a hook, decide **where** it belongs:

| Location | When to use |
| --- | --- |
| User settings (`~/.claude/settings.json`) | Across all projects on this machine |
| Project settings (`.claude/settings.json`) | One repository, shareable with the team |
| Local settings (`.claude/settings.local.json`) | Personal, uncommitted overrides |
| Managed policy settings | Organization-wide, admin-controlled |
| Plugin `hooks/hooks.json` | Reusable bundles distributed with a plugin |
| **Skill or agent frontmatter** | Only while that skill or subagent is active; cleaned up when it finishes |

See `references/hooks-in-skills-and-agents.md` for skill-scoped and agent-scoped hooks (same JSON shape as settings hooks; subagent `Stop` → `SubagentStop`).

## Workflow

1. Identify the goal (block, allow, log, inject context, notify, etc.).
2. Choose the hook **location** (table above).
3. Choose the **hook event** (`references/hook-events.md`).
4. Choose the **narrowest matcher** (and `if` for tool arguments when needed).
5. Choose the handler type: `command`, `http`, `mcp_tool`, `prompt`, or `agent`.
6. Define expected **input** and **output** for that event.
7. Add blocking or decision behavior only where the event supports it.
8. Test with **fixture payloads** (`tests/fixtures/`, `tests/test-hooks.sh`).
9. Apply the **security** checklist (`references/security.md`).

## Skill-scoped hooks (optional)

This skill is **reference-first**: there is **no** `hooks:` block in this `SKILL.md` frontmatter. That avoids broad matchers (e.g. `PreToolUse` + `"*"`) firing on every tool use while the skill is active.

When building a **hands-on** hook-authoring skill, you may add one or two narrow hooks (for example `PreToolUse` + `Write|Edit` + a validate script). Document tradeoffs in `references/hooks-in-skills-and-agents.md`.

## Supporting references

| Topic | File |
| --- | --- |
| Lifecycle and resolution | `references/hook-lifecycle.md` |
| Event catalog | `references/hook-events.md` |
| Skill and agent hooks | `references/hooks-in-skills-and-agents.md` |
| Configuration and locations | `references/configuration-schema.md` |
| Matchers and `if` | `references/matchers-and-if.md` |
| Input / output / decisions | `references/input-output.md` |
| Security | `references/security.md` |
| Async hooks | `references/async-hooks.md` |
| Prompt and agent hooks | `references/prompt-and-agent-hooks.md` |
| Debugging | `references/debugging.md` |
| Patterns (guide) | `references/patterns.md` |

## Examples and tooling

- JSON and YAML samples: `examples/`
- Validators and dev helpers: `scripts/` (run from repo root or skill root; hooks should use stable paths such as `${CLAUDE_PROJECT_DIR}` or exec form with `args`)
- Fixtures and smoke test: `tests/`
