---
name: claude-code-guide
description: Use when answering questions about Claude Code (the CLI tool), Claude Agent SDK, or Claude API. Routes to the right topic — product features, custom agents, hooks, permissions, settings, etc. — based on user intent. Use for orientation and routing; load specialist references for deep implementation detail.
---

# Claude Code Guide

Route to the right topic based on user intent. Three areas: **Product** (CLI, settings, permissions), **Agents** (subagents, teams, frontmatter), **Hooks** (events, matchers, automation).

## Quick Router

| User intent | Topic | Start here |
| --- | --- | --- |
| "What is CLAUDE.md / memory / rules?" | Product | `references/product/memory.md` |
| "Shift+Tab modes / plan / auto / bypass" | Product | `references/product/permission-modes.md` |
| "allow deny Bash(git …) rules" | Product | `references/product/permissions.md` |
| "settings.json scopes / managed / local" | Product | `references/product/settings.md` |
| "claude flags / -p / --agent" | Product | `references/product/cli-reference.md` |
| "/commands in the REPL" | Product | `references/product/commands.md` |
| "CLAUDE_CODE_* env vars" | Product | `references/product/env-vars.md` |
| "Tool names for permissions or hooks" | Product | `references/product/tools-reference.md` |
| "Plugins vs `.claude/` standalone" | Product | `references/product/plugins.md` |
| "Push events into a session" | Product | `references/product/channels.md` |
| "Skill vs subagent vs hook vs plugin?" | Agents | `references/agents/execution-decision.md` |
| "Subagents / Explore / fork" | Agents | `references/agents/subagent-overview.md` |
| "How to build a custom agent" | Agents | `references/agents/custom-subagent-structure.md` |
| "Agent frontmatter fields" | Agents | `references/agents/frontmatter-fields.md` |
| "Multiple sessions as a team" | Agents | `references/agents/agent-teams.md` |
| "Agent patterns and composition" | Agents | `references/agents/agent-patterns.md` |
| "Automate with hooks" | Hooks | `references/hooks/hook-lifecycle.md` |
| "Hook events catalog" | Hooks | `references/hooks/hook-events.md` |
| "Match syntax / if filters" | Hooks | `references/hooks/matchers-and-if.md` |
| "Hook input/output/exit codes" | Hooks | `references/hooks/input-output.md` |
| "Hook security / block commands" | Hooks | `references/hooks/security.md` |
| "Debug hooks / /hooks menu" | Hooks | `references/hooks/debugging.md` |

## Workflow

1. **Identify user intent** — What is the user asking about? (see table above)
2. **Route to topic** — Product, Agents, or Hooks
3. **Load the reference** — Read the corresponding file
4. **Follow the guidance** — Apply the instructions, checklists, or examples
5. **Escalate if needed** — If the reference says "go deeper," load the deeper reference

## When to Combine Topics

- **Agent + Hook**: When building an agent that needs deterministic guardrails (see `references/agents/hooks-in-agents-bridge.md`)
- **Product + Agent**: When setting up project structure for agents (see `references/agents/repo-structure.md`)
- **Product + Hook**: When configuring permissions alongside hooks (see `references/product/permissions.md`)
- **All three**: When designing a complete `.claude/` project setup

## Rules

- Never answer from memory alone — always load the relevant reference.
- If the user question spans multiple topics, load references in parallel.
- If the reference is missing, fall back to the official docs URL in the frontmatter.
- If the user asks for a checklist, load the matching checklist from `checklists/`.
- If the user asks for an example, load from `examples/`.
- Never duplicate deep implementation detail in the router — push it to references.

## Error Handling

- Missing reference: Ask the user to clarify which topic they need.
- Outdated reference: Check the `last_reviewed` date in the frontmatter and warn if stale.
- Conflicting guidance: Prefer the official docs URL over the local reference.
