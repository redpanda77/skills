---
source_urls:
  - https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents
  - https://code.claude.com/docs/en/skills
  - https://code.claude.com/docs/en/sub-agents
last_reviewed: 2026-05-13
---

# Hooks in skills and agents

Hooks can be defined directly in a skill’s `SKILL.md` or in a **subagent** definition’s frontmatter. They use the **same configuration shape** as settings-based hooks (event keys → matcher groups → handler objects).

Official summary: these hooks are **scoped to the component’s lifecycle**, run **only while that skill or subagent is active**, and are **cleaned up when the component finishes**. All hook events are supported in that context.

## Use skill or agent frontmatter when

- The hook should **only run while the skill (or subagent) is active**
- The behavior is **part of that component’s workflow** (validation, logging, guardrails specific to the task)
- The hook should **not** be installed globally in user or project settings
- You need **temporary** guardrails, validation, logging, or cleanup tied to that invocation

## Do not use skill/agent frontmatter when

- The hook should apply across **all** Claude Code sessions
- The hook should run even when the **skill is not active**
- The rule is **project policy** or **organization policy** (use project settings, managed settings, or plugins as appropriate)
- The behavior should ship as a **reusable plugin** for many projects (prefer plugin `hooks/hooks.json`)

## Subagents: `Stop` → `SubagentStop`

For subagents, **`Stop` hooks are converted to `SubagentStop`**, because the event that fires when a subagent completes is `SubagentStop`, not `Stop`. Plan matchers and handler logic around **`SubagentStop`** for end-of-subagent automation.

## Where hooks live (full map)

Hooks are loaded from several places; the Claude Code docs list them separately:

| Source | Typical path / mechanism |
| --- | --- |
| User settings | `~/.claude/settings.json` |
| Project settings | `.claude/settings.json` |
| Local (gitignored) | `.claude/settings.local.json` |
| Managed policy | Admin-controlled managed settings |
| Plugin | `hooks/hooks.json` inside the plugin |
| **Skill** | `hooks:` in `SKILL.md` YAML frontmatter |
| **Subagent** | `hooks:` in the agent definition frontmatter |

The in-app **`/hooks`** browser shows configured hooks and their **source** (User, Project, Local, Plugin, Session, Built-in). Skill-defined hooks register for the active session while the component runs.

## `once` (skill frontmatter only)

The hooks reference documents a `once: true` field on handlers: **only honored for hooks declared in skill frontmatter**; ignored in settings files and agent frontmatter. Use it when a hook should run **once per session** and then be removed.

## Good vs bad skill-scoped patterns

**Good (narrow):** `PreToolUse` with matcher `Write|Edit` and a script that validates hook JSON you are authoring — only runs for edits relevant to hook files.

**Reasonable:** `PostToolUse` with the same matcher and a logging script for an internal audit trail.

**Bad (too broad):** `PreToolUse` with matcher `"*"` and a “security” script — runs on **every** tool use while the skill is active; noisy, slow, and easy to get wrong.

**Reference-only skills:** keep **hooks out of frontmatter** and describe patterns here and in `examples/`. Add skill-scoped hooks only when the skill is explicitly a **hands-on hook builder** and the automation adds clear value.

## See also

- [Hooks reference — Hooks in skills and agents](https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents)
- [Skills](https://code.claude.com/docs/en/skills)
- [Subagents](https://code.claude.com/docs/en/sub-agents)
