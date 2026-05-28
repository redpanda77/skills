# 05 — Operate

Run the harness in production. Use this every session.

## Files in this folder

- `README.md` — this file
- `run-commands.md` — how to use slash commands
- `run-recovery.md` — how to recover after context loss
- `run-state.md` — how to read and update state
- `run-task.md` — how to design tasks with acceptance criteria

## What to do

- Start session → hook reminds you of protocol
- Pick task from `PLAN.md` → work on it
- Run `done-check.sh` → it decides if you're done
- Spawn judge subagent → scores the work
- Run `/close-task` → closure workflow updates registries
- State tracked in `.mission-control/state.json`
- If crash: read `run-recovery.md`
