# 00 — Introduction

What is Mission Control and why do you need it.

## Files in this folder

- `README.md` — this file (what it is, why you need it)
- `philosophy.md` — the harness mindset (core beliefs)
- `terminology.md` — key terms defined (agent, harness, judge, validator, etc.)
- `why-components.md` — why each component exists (skills, judges, hooks, etc.)

## The Problem

Claude Code is powerful but unreliable without a control system:
- Stops after subtasks and asks "should I continue?"
- Claims completion while tests still fail
- Repeats the same mistakes across sessions
- Makes destructive changes without warning
- Cannot judge whether output is actually good

## The Solution

Mission Control configures Claude Code as a **harness runtime** — a control system that makes agent work reliable, repeatable, and observable.

## What you get

| Without Mission Control | With Mission Control |
|---|---|
| Claude decides when it's done | `done-check.sh` decides when it's done |
| Same mistakes every session | Skills encode patterns; hooks enforce rules |
| No quality feedback | Judge subagent scores against principles |
| Destructive commands unblocked | `block-dangerous.sh` blocks them |
| No state tracking | `state.json` tracks current task across sessions |
| No regression protection | Closed-task validators catch regressions |
| No recovery after crash | `run-agent.sh` resumes with full context |

## How to read this skill

Start here, then read each phase in order:

1. `00-introduction/README.md` — this file (what it is)
2. `00-introduction/philosophy.md` — core mindset (the harness mindset)
3. `00-introduction/terminology.md` — key terms (agent, harness, judge, validator, etc.)
4. `00-introduction/why-components.md` — why each component exists
5. `references/CHECKLIST.md` — the master checklist
6. `01-discover/README.md` — understand your project
7. `02-decide/README.md` — choose the harness design
8. `03-configure/README.md` — build the harness
9. `04-test/README.md` — verify it works
10. `05-operate/README.md` — run it in production

## Key principle

**The agent is only as good as the system around it.**

When the agent fails, the fix is not "prompt harder." The fix is: what capability is missing from the harness? Add docs, add tests, add hooks, add constraints, add feedback loops.
