---
source_urls:
  - https://code.claude.com/docs/en/tools-reference
last_reviewed: 2026-05-13
---

# Tools reference (orientation)

Tool names are stable strings used in:

- `permissions.allow` / `deny` / `ask`
- subagent `tools` / `disallowedTools`
- hook matchers (`PreToolUse`, …)

## Core built-ins (abbreviated)

| Tool | Role | Usually prompts |
| --- | --- | --- |
| `Read` / `Glob` / `Grep` | inspect repo | no |
| `Edit` / `Write` / `NotebookEdit` | mutate files | yes |
| `Bash` / `PowerShell` | run commands | yes |
| `WebFetch` / `WebSearch` | external info | yes |
| `Agent` | spawn subagent | no (delegation policy still applies) |
| `Skill` | run a skill workflow | yes |
| `Task*` / `TodoWrite` | task tracking | varies by generation |

MCP servers add more tools (often prefixed). `ToolSearch` appears when MCP tool search is enabled.

## Configure without renaming tools

Use permissions + hooks to constrain **how** tools may be used (prefix allowlists, validators).

Official: [Tools reference](https://code.claude.com/docs/en/tools-reference).
