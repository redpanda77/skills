# Entrypoints

The operator interface that defines how users invoke the system.

## Purpose

Provide a consistent, documented contract for invoking the pipeline. Without this, the system is invisible and the protocol is inconsistent.

## What it is

- **Skills** — reusable workflow definitions (`.claude/skills/`)
- **Commands** — slash commands that trigger actions (`.claude/commands/`)
- **Operator Contract** — the documented protocol for running the system

## Skills

### Types

- **System skill** — the operating manual for the project. Hard gate; never skip.
- **Domain skill** — a skill for a specific domain (React, data pipelines, curriculum generation)
- **Meta skill** — a skill about the system itself (mission-control, write-a-skill)

### Rules

- Skills teach Claude specific patterns, domains, or procedures
- The system skill is the entrypoint for all project work
- Domain skills are loaded on demand
- Skills are not a replacement for docs; they are the docs, encoded

## Commands

Common commands:

| Command | Purpose |
|---------|---------|
| `/continue` | Advance the pipeline one step |
| `/close-task` | Closure workflow |
| `/run-judge` | Spawn judge subagent |
| `/status` | Show current state |
| `/recovery` | Recover after context loss |
| `/session-start` | Initialize new session |
| `/handoff` | Pass context to next agent |

## The Entrypoint Contract

The user invokes the system via a command. The system:

1. Runs the router
2. Reads the router output
3. Executes exactly one action
4. Reports the next state
5. Stops

The next step executes only on the next invocation. No chaining.

## Failure Mode

If entrypoints are broken:
- No way to invoke the system
- Inconsistent protocol across sessions
- Agents improvise instead of following the contract
- The system is invisible to users

## Repair Authority

- Broken command → fix the command definition
- Broken skill → fix the skill file
- Missing contract → write the operator documentation
