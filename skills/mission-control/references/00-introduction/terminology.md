# Terminology

## Agent
The AI executing work. Claude Code is the agent. The agent is only as good as the harness around it.

## Harness
The complete control system around the agent: intent, context, tools, constraints, feedback, and memory. The harness makes agent work reliable, repeatable, and observable.

## Harness Runtime
The software that executes the harness. Claude Code is the harness runtime. You do not build a custom runtime. You configure Claude Code's native surfaces.

## Intent
What the agent should do. Expressed in `PLAN.md`, task maps, acceptance criteria, and closure contracts.

## Context
What the agent needs to know. Expressed in `CLAUDE.md`, `AGENTS.md`, rules, and docs.

## Tools
What the agent can inspect or operate. Scripts (`done-check.sh`, `validate.sh`), tests, MCP servers, and shell commands.

## Constraints
What the agent must never violate. Hooks (`stop-if-not-done.sh`, `block-dangerous.sh`), permissions, and sandboxing.

## Feedback
How the agent knows whether it succeeded. Tests, judge subagents, CI, and validation scripts.

## Judge
A subagent that evaluates qualitative quality. The judge is a `.md` file in `.claude/agents/` with YAML frontmatter. It scores principles independently (0.0–1.0). The judge is the sole authority for content quality, naturalness, semantic fit, and intent satisfaction.

## Validator
A deterministic script that checks mechanical facts: tests pass, files exist, schema is valid, no tampering. Validators do NOT judge quality.

## Principle
A single, falsifiable statement that captures one dimension of quality. 5-10 principles per judge. Each principle is scored independently.

## Done-check
The script that decides when work is done. `done-check.sh` is the completion authority. It calls all sub-validators and checks judge verdicts. Claude cannot stop until `done-check.sh` passes.

## Hook
A shell script wired to Claude Code events (Stop, PreToolUse, PostToolUse, SessionStart). Hooks enforce constraints. The Stop hook blocks premature exit. The PreToolUse hook blocks dangerous commands.

## Skill
A reusable workflow encoded as a `.md` file with YAML frontmatter. Skills teach Claude specific patterns, domains, or procedures. The system skill is the operating manual for the project.

## Context Pack
A reusable subagent contract placed in `.claude/context-packs/`. Contains read/skip lists and first-principles contracts. Subagents load their pack first.

## Closed Task
A task that has been completed, validated, and regression-protected. Closed tasks are tracked in `CLOSED_TASKS.md` and `validation-manifest.json`. Their tests are re-run by `validate-closed-tasks.sh` to catch regressions.

## Closure Contract
The evidence required to close a task. Defined in `PLAN.md` for each task. Includes: acceptance criteria, tests, invariants, and protected files.

## System Skill
The operating manual skill created for every project. Lives in `.claude/skills/<system-name>/`. Hard gate — do not skip.

## Domain Skill
A skill for a specific domain of work (e.g., React components, lesson drafting, data pipelines). Lives in `.claude/skills/<domain>/`.

## Tier
The harness complexity level:
- **Minimal** (< 30 min): `PLAN.md`, `done-check.sh`, Stop hook
- **Standard** (30 min – 2 hrs): Minimal + regression tracking + sub-validators
- **Strict** (2+ hrs): Standard + judge subagent + principle-based evaluation

## Layout
Where control files live:
- **Inline**: Control files are in the repo (`.claude/`, `done-check.sh`, etc.)
- **External**: Control scripts live outside the repo (`agent-control/` directory)

## Router
The script or skill that decides the workflow. The model runs the router, reads its output, and executes the router's command. The model does not decide the workflow by reasoning.

## State Hierarchy
Judge JSON overrides precheck. Prechecks output `findings[]` only (no `passed`/`score`/`repair_route`).

```
judge exists and passed
  -> judge wins, continue (unless mechanical validator fails)

judge exists and failed
  -> judge wins, route repair from judge repair_route

judge missing/stale/invalid
  -> if precheck shows mechanical issue, route mechanical repair
  -> if qualitative issue, delegate judge FIRST
```
