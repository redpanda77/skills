---
source_urls:
  - https://code.claude.com/docs/en/commands
last_reviewed: 2026-05-13
---

# Slash commands (orientation)

Commands are typed at the **start** of a message (`/help`, `/init`, …). Arguments follow the command name.

## Workflow map (abbreviated)

| Phase | Useful commands |
| --- | --- |
| Bootstrap | `/init`, `/memory`, `/mcp`, `/agents`, `/permissions` |
| During work | `/plan`, `/model`, `/effort`, `/context`, `/compact`, `/btw` |
| Parallelism | `/agents`, `/tasks`, `/background`, `/batch` |
| Ship | `/diff`, `/review`, `/security-review`, `/simplify` |
| Recovery | `/rewind`, `/doctor`, `/debug`, `/feedback` |

## Command categories

- **Built-ins** — implemented in the CLI (`/config`, `/hooks`, …).
- **Bundled skills** — behave like user skills; may auto-invoke when relevant (marked in the official all-commands table).

Type `/` in the REPL to see what your build exposes — availability varies by platform, plan, and feature flags.

Official: [Commands](https://code.claude.com/docs/en/commands).
