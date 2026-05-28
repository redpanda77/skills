# Composition: subagent with hooks reference

**Intent:** combine **role isolation** (subagent) with **deterministic enforcement** (hooks).

## Agent-scoped example

Use `hooks:` in the subagent frontmatter when guardrails should exist **only** while that agent runs (validation scripts, linters, command allowlists via `PreToolUse`).

## Project-scoped example

Use `SubagentStart` / `SubagentStop` in settings when **every** spawn of `db-agent` needs shared setup/teardown regardless of which project file defined it.

## Where to read next

- `references/hooks-in-agents-bridge.md` (this repo)
- `skills/claude-code-hooks/` for matchers, stdin JSON, exit codes, `/hooks` debugging

Do not duplicate hook internals in agent prompts — call scripts and keep hook JSON in one place.
