---
name: mission-control
description: Set up a controlled execution system for multi-step Claude Code sessions — PLAN.md task map, done-check.sh authority, hooks, wrapper loop, and optional judge subagent layer. Use when running autonomous agent loops, human-in-the-loop tracking projects, evaluation/analysis pipelines, "controlled run", "long-running task", "track progress across phases", "don't stop until done", or when the user needs Claude to work without stopping prematurely.
---

# Mission Control

Sets up the control infrastructure that makes Claude the worker, not the authority. Completion is decided by scripts — not by Claude saying "I'm done."

Supports three modes:
- **Autonomous loop** — Claude runs continuously; Stop hook blocks early exit; run-agent.sh wrapper
- **Human-in-the-loop tracking** — human reviews between phases; agent recommends `/close-task`; no blocking Stop hook needed
- **Evaluation/analysis** — judge layer or human assessment gate; coverage targets; milestone reviews

## Detect mode

**Setup mode** — run if `PLAN.md` does not exist. Read `references/setup/router.md` — it asks Q0 (project type) and routes to the correct type-specific guide:
- Autonomous loop → `references/setup/autonomous.md`
- Human-in-the-loop / Evaluation → `references/setup/human-in-the-loop.md`

Setup is a **sequential workflow** — each phase gates the next. The system skill (write-a-skill) has a hard checklist gate before setup can complete. Do not skip it.

**Resume mode** — run if `PLAN.md` already exists. Read `references/runtime/resume.md`.

## Core principle

```
PLAN.md                   → task map (context, not enforcement)
.mission-control/         → runtime state: current task, judge verdicts, closure records
done-check.sh             → completion authority (reads state, calls validators)
Stop hook                 → calls done-check.sh; blocks premature stopping
run-agent.sh              → wrapper that survives crashes, sleep, terminal close
.claude/commands/         → local slash commands: /close-task, /run-judge, /mc-status
.claude/agents/           → subagent definitions (judge + any workers)
.claude/skills/           → system skill documenting the implementation
```

The judge is always a **subagent defined as a Markdown file with YAML frontmatter** in `.claude/agents/` — never a shell script calling `claude -p`. The worker invokes `/run-judge`, which @-mentions the judge subagent. The judge returns a JSON verdict; the worker writes it to `.mission-control/judge-verdicts/`. Done-check reads the verdict file; it does not spawn the judge itself.

## Non-negotiable setup rules

1. **Always local** — all files go in the project's `.claude/` directory. Never write to `~/.claude/` (global). Subagents in `.claude/agents/`, skills in `.claude/skills/`, commands in `.claude/commands/`.
2. **Always create a system skill** — after setup, invoke `write-a-skill` to create a skill in `.claude/skills/` that documents the system: what it does, how the subagents work, what files to use, and how to run it. This is the operating manual for the agent running inside the system.
3. **Always invoke `writing-claude-md`** — never write CLAUDE.md directly. Always use the `writing-claude-md` skill to produce it so it follows the behavioral contract format.
4. **Subagents as files** — any subagent (judge or worker) is a `.md` file in `.claude/agents/` with `name`, `description`, `tools`, and `model` frontmatter fields. The description must be specific enough that the agent knows when to delegate to it. Never embed subagent prompts inside slash commands or shell scripts.

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

### Setup (read during new project setup only)
- `references/setup/router.md` — Q0: asks project type, routes to the right guide
- `references/setup/autonomous.md` — full autonomous loop setup (phases 0–9, done-check.sh, run-agent.sh, acceptance criteria, closure contracts)
- `references/setup/human-in-the-loop.md` — human-in-the-loop / evaluation setup (phase gates, milestone gates, scope lock, file-based closure)

### Runtime (read during active sessions)
- `references/runtime/resume.md` — recovery and status check
- `references/runtime/task-design.md` — task design, milestone gates, user corrections protocol
- `references/runtime/state-tracking.md` — .mission-control/ schema, state.json (incl. project_type, scope_locked), judge verdicts, closure records
- `references/runtime/commands.md` — local slash commands: /close-task, /run-judge, /mc-status, /mc-recovery, /handoff; session-start with handoff check; CLAUDE.md design

### Components (read when designing a specific piece)
- `references/components/validation.md` — how to design done-check.sh for your project
- `references/components/hooks.md` — aggressiveness levels, hook→done-check connection, context-warning hook, individual hook reference
- `references/components/judge.md` — judge as subagent, judge types, rubric design, trigger strategy, /run-judge template, wiring into done-check
- `references/components/folder-structure.md` — exact file trees for each tier/layout, what Claude can/cannot edit

### Templates
- `references/templates/shared/` — PLAN.md, state.json, commands, validators, CLAUDE.md templates
- `references/templates/autonomous/` — done-check.sh, run-agent.sh, hooks, prompts (autonomous loop only)
