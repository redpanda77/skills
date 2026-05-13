# Launchpad Workflow

## How the system works

```
.plan/
├── CONTEXT.md                  ← domain vocabulary (written by /grill-with-docs)
├── active.md                   ← what's in focus right now
├── features/
│   ├── _archive/               ← completed features land here
│   └── [feature-name]/
│       ├── prd.md
│       ├── tasks.md
│       └── handoffs/
│           └── YYYY-MM-DD.md
```

`active.md` is the glue. Every command reads it first so Claude always knows where to pick up without scanning the full tree.

## Command reference

| Command | What it does |
|---------|-------------|
| `/start` | Load active feature context, confirm today's task |
| `/grill-me` | Interview before building — decisions saved to handoff |
| `/grill-with-docs` | Build or update `.plan/CONTEXT.md` domain vocabulary |
| `/write-a-prd` | Draft a PRD for a feature, saved to `.plan/features/[name]/prd.md` |
| `/prd-to-tasks` | Break a PRD into session-sized tasks with testable done-criteria |
| `/task-done` | Mark a task complete, update counter, prompt for next step |
| `/handoff` | Write a session handoff to `.plan/features/[name]/handoffs/YYYY-MM-DD.md` |
| `/switch-feature` | Change active feature in `active.md` |
| `/complete-feature` | Archive a finished feature, activate the next queued one |

## Typical flow for a new feature

```
/grill-with-docs   →  .plan/CONTEXT.md (once, or when domain evolves)
/grill-me          →  decisions captured before coding starts
/write-a-prd       →  .plan/features/auth/prd.md
/prd-to-tasks      →  .plan/features/auth/tasks.md + active.md updated
                   →  consider: does any task warrant a dedicated skill? (/write-a-skill)

every session:
/start             →  orient to active feature
[work]
/task-done         →  mark checkbox, update counter
/handoff           →  .plan/features/auth/handoffs/YYYY-MM-DD.md

feature done:
/complete-feature  →  archive, activate next
```

## Skills vs commands

**Global skills** (available in every project, invoked as `/skill-name`):
- `grill-me`, `grill-with-docs`, `write-a-skill`, `writing-claude-md`, `handoff`

**Project commands** (local to this project, in `.claude/commands/`):
- Everything else above — they know about this project's `.plan/` structure

## When to use write-a-skill

After `/prd-to-tasks`, ask: does any task represent a repeatable, multi-step workflow that will recur across sessions or projects? If yes, that task is a skill candidate. Invoke `write-a-skill` to build it before starting the implementation. The skill then becomes the implementation guide.

Examples of good skill candidates:
- A data pipeline that runs in multiple features
- An API integration pattern used across endpoints
- A testing or validation workflow specific to this domain
