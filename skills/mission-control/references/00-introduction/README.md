# 00 — Introduction

What is Mission Control and why do you need it.

## Files in this folder

- `README.md` — this file (what it is, why you need it)
- `philosophy.md` — the harness mindset (core beliefs)
- `terminology.md` — key terms defined (agent, harness, judge, validator, etc.)
- `system-components.md` — the core components and data flow
- `system-architecture/` — detailed breakdown of each component
  - `source-and-graph.md` — the evidence layer
  - `router.md` — orchestration and routing
  - `agents.md` — workers and judges
  - `validation.md` — deterministic checks
  - `state-and-ledger.md` — tracking and manifests
  - `export-and-render.md` — output materialization
  - `hooks.md` — guardrails and constraints
  - `entrypoints.md` — skills and commands

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
4. `00-introduction/system-components.md` — the core components and data flow
5. `00-introduction/system-architecture/` — detailed breakdown of each component
6. `references/CHECKLIST.md` — the master checklist
7. `01-discover/README.md` — understand your project
8. `02-decide/README.md` — choose the harness design
9. `03-configure/README.md` — build the harness
10. `04-test/README.md` — verify it works
11. `05-operate/README.md` — run it in production

## Context Packs and Scope Discipline

A dedicated reference section covers the two disciplines that make or break multi-agent systems:

- `06-context-packs/README.md` — overview of the two principles
- `06-context-packs/typed-context-packs.md` — schema standard and type system
- `06-context-packs/planning-content-boundaries.md` — plan vs canonical content boundaries
- `06-context-packs/input-output-scope.md` — broad vs deep scope rule
- `06-context-packs/validation-and-budgets.md` — hard validation rules and budgets
- `06-context-packs/content-evidence-pattern.md` — row-local evidence, ID alignment, and migration rules

## Key principle

**The agent is only as good as the system around it.**

When the agent fails, the fix is not "prompt harder." The fix is: what capability is missing from the harness? Add docs, add tests, add hooks, add constraints, add feedback loops.
