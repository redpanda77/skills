---
name: mission-control
description: Configure Claude Code as a harness runtime for reliable, repeatable agent execution. Use when setting up control systems around agents — instructions, validation, constraints, feedback, and memory. Triggers on "mission control", "harness setup", "agent infrastructure", "stop hook", "done-check", "judge subagent", or "autonomous loop".
---

# Mission Control

Meta-skill for configuring Claude Code as a harness runtime.

## The checklist

Execute `references/CHECKLIST.md`. It is the single source of truth for the setup process. Every task must be completed without leaving things out.

## Quick start

1. Read `references/00-introduction/README.md` — what this is and why you need it
2. Read `references/00-introduction/system-components.md` — the core components and data flow
3. Read `references/CHECKLIST.md` — the master checklist
4. Follow the checklist in order. Do not skip steps.

## What this is

A harness is the control system around an agent that makes its work reliable, repeatable, and observable.

| Layer | Output |
|---|---|
| Intent | `PLAN.md`, `AGENTS.md` |
| Context | `CLAUDE.md`, docs |
| Tools | `done-check.sh`, `validate.sh` |
| Constraints | `.claude/hooks/`, `.claude/settings.json` |
| Feedback | `.claude/agents/`, CI |
| Memory | `.claude/skills/`, `state.json` |

## When to use

- New project: "Set up mission control for this repo"
- Broken system: "The agent keeps making the same mistakes"
- Multi-step work: Projects needing multiple agents, validation, or regression tracking
- Adding rigor: "I need a judge for quality" or "regression tracking"

Do NOT use for single tasks ("write a function", "fix this bug").

## Core principles

- Scripts are the completion authority. `done-check.sh` decides when work is done.
- Scripts = deterministic only. Judge = qualitative only. No overlap.
- The judge is always a subagent. Never a script.
- Always invoke `writing-claude-md` to write `CLAUDE.md`. Never write it directly.
- Always create a system skill. Hard gate.
- Stop hook blocks premature exit. Claude cannot stop until `done-check.sh` passes.

## Quick reference

| Tier | Adds |
|---|---|
| 1 — Minimal | `PLAN.md`, `done-check.sh`, Stop hook |
| 2 — Standard | Tier 1 + regression tracking + sub-validators |
| 3 — Strict | Tier 2 + judge subagent + principle-based evaluation |

## Key references

- `references/CHECKLIST.md` — master checklist
- `references/PREFLIGHT.md` — preflight health check before every session
- `references/00-introduction/README.md` — introduction
- `references/00-introduction/system-components.md` — the core components and data flow
- `references/00-introduction/system-architecture/` — detailed breakdown of each component
- `references/01-discover/README.md` — discover phase
- `references/02-decide/README.md` — decide phase
- `references/03-configure/README.md` — configure phase
- `references/04-test/README.md` — test phase
- `references/05-operate/README.md` — operate phase
- `references/06-context-packs/README.md` — context pack discipline and scope boundaries
- `references/07-agents/README.md` — agent design, frontmatter, invocation, and manifest
