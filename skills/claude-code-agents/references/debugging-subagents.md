---
source_urls:
  - https://code.claude.com/docs/en/sub-agents#troubleshooting
last_reviewed: 2026-05-13
---

# Debugging subagents

Use this checklist before changing code or filing issues.

## Agent not listed or not loading

- Confirm **file location** and **name collision** precedence (`custom-subagent-structure.md`).
- If edited **on disk outside `/agents`**, **restart the session** so definitions reload.
- Run `claude agents | cat` to see effective sources and overrides.

## Bad or ignored frontmatter

- Validate YAML (indentation, quotes on colons in strings).
- Run `scripts/validate-agent-frontmatter.py` on the markdown file.
- Remember **plugin agents ignore** `hooks`, `mcpServers`, `permissionMode`.

## Delegation never triggers

- Rewrite **`description`** with explicit *when*, *what*, *output* (`checklists/delegation-description-checklist.md`).
- Remove contradictory instructions in the body that shrink the router’s confidence.

## Wrong agent selected

- Split overloaded agents by **narrower descriptions**.
- Prefer @-mention for a one-off guaranteed path.

## Tool denied / background failures

- Background runs **auto-deny** prompts — retry **foreground** or pre-grant permissions.
- Check `tools` / `disallowedTools` and parent **permission mode** interactions.

## “Stale” session or lost context

- Named agents start **fresh** unless you explicitly **resume** / use team message flows (if enabled).
- Inspect `~/.claude/projects/.../subagents/agent-*.jsonl` for transcript truth.

## Hooks inside agents misbehaving

- `Stop` in agent frontmatter maps to **`SubagentStop`** at runtime.
- Project-wide lifecycle belongs in **`SubagentStart` / `SubagentStop`** in settings — see `hooks-in-agents-bridge.md` and `claude-code-hooks`.

For authoritative troubleshooting copy, match the current [Subagents troubleshooting](https://code.claude.com/docs/en/sub-agents#troubleshooting) section in the official docs.
