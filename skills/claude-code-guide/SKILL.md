---
name: claude-code-guide
description: Use when answering questions about Claude Code product behavior—memory and CLAUDE.md, permission modes, permissions rules, settings scopes, CLI flags, slash commands, environment variables, tools, plugins, channels, hooks at a guide level, subagents vs agent teams, and where to find official docs. Use for orientation and routing; use specialist skills for deep hook authoring or custom subagent design.
---

# Claude Code guide

This skill is a **router and condensed guide** to Claude Code configuration and extension points. It tracks the official documentation pages listed in `references/doc-index.md`.

**Prefer official docs** for exhaustive tables, UI-specific tabs, and versioned behavior. This repo’s references summarize durable concepts and link outward.

## Specialist skills in this repository

| Topic | Skill |
| --- | --- |
| Hooks (events, matchers, I/O, blocking, `/hooks`, fixtures) | `claude-code-hooks` |
| Subagents (frontmatter, delegation, skills preload, patterns, validators) | `claude-code-agents` |

When the user needs **implementation detail** for hooks or agents, load the specialist skill instead of duplicating it here.

## Route common questions

| User intent | Start here |
| --- | --- |
| “What is CLAUDE.md / memory / rules?” | `references/memory.md` |
| “Shift+Tab modes / plan / auto / bypass” | `references/permission-modes.md` |
| “allow deny Bash(git …) rules” | `references/permissions.md` |
| “settings.json scopes / managed / local” | `references/settings.md` |
| “claude flags / -p / --agent” | `references/cli-reference.md` |
| “/commands in the REPL” | `references/commands.md` |
| “CLAUDE_CODE_* env vars” | `references/env-vars.md` |
| “Tool names for permissions or hooks” | `references/tools-reference.md` |
| “Plugins vs `.claude/` standalone” | `references/plugins.md` + `references/plugins-reference.md` |
| “Push events into a session (Telegram, etc.)” | `references/channels.md` + `references/channels-reference.md` |
| “Automate with hooks (first hook, patterns)” | `references/hooks-guide.md` → then `claude-code-hooks` |
| “Subagents / Explore / fork” | `references/sub-agents.md` → then `claude-code-agents` |
| “Multiple sessions as a team” | `references/agent-teams.md` |

## Principles (short)

- **Instructions ≠ enforcement:** `CLAUDE.md` and auto memory load as **context**; permissions and hooks enforce behavior.
- **Scopes stack:** managed → CLI → local → project → user (see `references/settings.md` for nuance).
- **Modes vs rules:** permission **mode** sets baseline; `permissions.allow` / `deny` / `ask` and `PreToolUse` hooks layer on top (except `bypassPermissions`, which skips the permission layer).
- **Isolation choices:** subagents within one session; agent teams for separate Claude instances; channels for external push events.

## Doc index

See `references/doc-index.md` for the canonical URL → local reference map.
