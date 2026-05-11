---
name: mission-control
description: Set up a controlled execution system for long-running Claude Code sessions — PLAN.md task map, done-check.sh authority, hooks, wrapper loop, and optional judge subagent layer. Use when running autonomous multi-step tasks, setting up "agent loop", "controlled run", "long-running task", "Claude should keep going", "don't stop until done", or when the user needs Claude to work without stopping prematurely.
---

# Mission Control

Sets up the control infrastructure that makes Claude the worker, not the authority. Completion is decided by scripts — not by Claude saying "I'm done."

## Detect mode

**Setup mode** — run if `PLAN.md` does not exist. Read `references/setup.md`.

**Resume mode** — run if `PLAN.md` already exists. Read `references/resume.md`.

## Core principle

```
PLAN.md                   → task map (context, not enforcement)
.mission-control/         → runtime state: current task, judge verdicts, closure records
done-check.sh             → completion authority (reads state, calls validators)
Stop hook                 → calls done-check.sh; blocks premature stopping
run-agent.sh              → wrapper that survives crashes, sleep, terminal close
.claude/commands/         → local slash commands: /close-task, /run-judge, /mc-status
```

The judge is always a **subagent** spawned via the Agent tool — never a shell script calling `claude -p`. The worker invokes `/run-judge`, the judge subagent returns a JSON verdict, and the worker writes it to `.mission-control/judge-verdicts/`. Done-check reads the verdict file; it does not spawn the judge itself.

## Tiers

| Tier | Good for | What you get |
|------|----------|--------------|
| **1 — Minimal** | < 30 min, low risk | PLAN.md + done-check.sh + Stop hook + run-agent.sh + local skills |
| **2 — Standard** | 30 min – 2 hrs, partial tests | Tier 1 + regression tracking + anti-gaming hooks + sub-validators |
| **3 — Strict** | 2+ hrs, production risk | Tier 2 + judge subagent + private rubric + isolated agent-control/ |

## Hook aggressiveness levels

| Level | Hooks | Use when |
|-------|-------|---------|
| **Low** | Stop only | Short tasks, trust Claude's judgment |
| **Medium** | Stop + block-dangerous + session-reminder | Most tasks > 30 min |
| **High** | Medium + protect-control-files + post-edit-reminder | Long tasks, Claude writing tests |

## References

- `references/setup.md` — full guided setup (9 phases, AskUserQuestion throughout)
- `references/resume.md` — recovery and status check
- `references/validation-design.md` — how to design done-check.sh for your project
- `references/hooks.md` — aggressiveness levels, hook→done-check connection, individual hook reference
- `references/folder-structure.md` — exact file trees for each tier/layout, what Claude can/cannot edit
- `references/task-design.md` — how to write good tasks, acceptance criteria, closure contracts
- `references/state-tracking.md` — .mission-control/ schema, state.json, judge verdicts, closure records
- `references/local-skills.md` — local slash commands written during setup: /close-task, /run-judge, /mc-status, /mc-recovery; CLAUDE.md design
- `references/judge.md` — judge as subagent, judge types, rubric design, trigger strategy, /run-judge template, wiring into done-check
- `references/templates/` — all script templates
