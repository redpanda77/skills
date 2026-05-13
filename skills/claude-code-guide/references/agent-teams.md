---
source_urls:
  - https://code.claude.com/docs/en/agent-teams
last_reviewed: 2026-05-13
---

# Agent teams (experimental)

Agent teams coordinate **multiple Claude Code sessions** with a **lead** and **teammates**, shared task lists, and (when enabled) direct teammate messaging. They are **disabled by default**.

## Enable

Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in the environment or under `env` in `settings.json` (see official doc for version minimums and limitations).

## vs subagents

| | Subagents | Agent teams |
| --- | --- | --- |
| Processes | One session | Multiple sessions / contexts |
| Communication | Worker → parent only | Teammates can message each other |
| Cost / complexity | Lower | Higher coordination + token use |

Prefer **subagents** for focused side tasks with a single parent orchestrator. Prefer **agent teams** when parallel workers must **debate** or **coordinate** independently.

## Practical notes

- Expect experimental limitations around resumption, shutdown, and task coordination — read upstream **Limitations**.
- Subagent definitions can inform teammate behavior in some flows — see official cross-links.

Official: [Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams).
