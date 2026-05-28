# Slash Commands

Local commands in `.claude/commands/` that the worker invokes by name.

## Core commands

| Command | When |
|---------|------|
| `/session-start` | Start of every session |
| `/mc-status` | Progress check |
| `/mc-recovery` | After crash or context loss |
| `/handoff` | Ending a long session |
| `/log-decision` | Before any deviation |
| `/close-task` | Closure workflow |
| `/run-judge` | Spawn judge (if enabled) |

Each command is a `.md` file with YAML frontmatter. Use `write-a-skill` for detailed structure.

## Rules

- Commands are thin shims — the system skill owns the logic
- `/close-task` loads the system skill and follows its close-task procedure
- `/run-judge` spawns the judge subagent via the `Agent` tool
- Always invoke `write-a-skill` to create commands. Never write them manually.
