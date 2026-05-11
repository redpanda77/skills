---
name: launchpad
description: Set up and run a full project planning system (.plan/ folder, slash commands, CLAUDE.md integration). Use when starting a new project, when the user says "set up the project", "launchpad", "initialize planning", or wants to start working on a feature with full context tracking.
---

Launchpad sets up a `.plan/`-based workflow system for a project and keeps it running across sessions.

## Detect mode

**Setup mode** — run if `.plan/` does not exist in the project root. Read `references/setup.md`.

**Use mode** — run if `.plan/` already exists. Read `references/workflow.md`.

## Global skill checks (both modes)

Before doing anything, verify these global skills exist in `~/.claude/skills/`:
- `grill-me`
- `grill-with-docs`
- `write-a-skill`
- `writing-claude-md`
- `handoff`

If any are missing, list them and tell the user: "These global skills are required. Install them before continuing." Do not proceed until confirmed present or the user explicitly skips.

## References

- `references/setup.md` — full setup procedure
- `references/workflow.md` — day-to-day usage guide
- `references/formats/active.md` — active.md schema
- `references/formats/tasks.md` — tasks.md schema
- `references/formats/prd.md` — PRD structure
- `references/commands/` — source of truth for all project slash commands
