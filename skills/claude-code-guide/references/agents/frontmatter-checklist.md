---
name: agent-frontmatter-checklist
description: 16-point checklist for designing agent frontmatter. Use when creating or reviewing a subagent definition.
---

# Frontmatter Design Checklist

## Identity
- [ ] Is `name` lowercase, unique, and stable?
- [ ] Does the filename match the name?
- [ ] Does `description` clearly say when to use the agent?

## Capability
- [ ] Should the agent inherit all tools?
- [ ] Should `tools` be a strict allowlist?
- [ ] Should `Write`/`Edit` be denied?
- [ ] Should this agent be allowed to spawn subagents when run as main via `--agent`?

## Permissions
- [ ] Should this agent be read-only `plan` mode?
- [ ] Should edits be auto-accepted with `acceptEdits`?
- [ ] Should permission prompts fail closed with `dontAsk`?
- [ ] Is `bypassPermissions` actually justified?

## Model / Runtime
- [ ] Is the selected model proportional to the task?
- [ ] Should `effort` override the session?
- [ ] Should `maxTurns` cap runaway work?
- [ ] Should this run in the `background`?

## Isolation
- [ ] Does the agent need a temporary `worktree`?
- [ ] Does it need access to parent uncommitted changes?
- [ ] Could parallel edits conflict?

## Knowledge
- [ ] Does it always need specific skills preloaded?
- [ ] Are the preloaded skills model-invocable?
- [ ] Would on-demand skill invocation be cheaper?

## Memory
- [ ] Should the agent remember anything?
- [ ] Is the memory `user`, `project`, or `local`?
- [ ] Is project memory safe to commit?

## MCP / Hooks
- [ ] Does only this agent need a specific MCP server?
- [ ] Should MCP be inline to avoid parent-context bloat?
- [ ] Is a `hook` needed to enforce a rule?

## Agent Teams
- [ ] Will this definition also be used as a teammate type?
- [ ] If yes, remember that `tools`/`model`/`body` apply, but `skills` and `mcpServers` frontmatter do not.

## Teaching Summary

| Field | Purpose |
|-------|---------|
| `name` + `description` | Identity and delegation |
| `tools` + `disallowedTools` | Capability boundary |
| `permissionMode` | Approval behavior |
| `model` + `effort` | Cost/capability tradeoff |
| `maxTurns` + `background` + `isolation` | Runtime behavior |
| `skills` + `memory` | Reusable knowledge |
| `mcpServers` | External capabilities |
| `hooks` | Enforcement |
| `color` | UI clarity |
| `initialPrompt` | Main-session startup behavior |

## The Most Important Rule

Do not write agents as "smart helpers." Write agents as bounded workers with clear triggers, limited tools, explicit permissions, and a predictable output contract.
