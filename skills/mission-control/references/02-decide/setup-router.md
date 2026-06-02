# Setup Router

Routes to the correct setup guide based on project type.

## Standing rules

- Claude Code is the harness runtime. Configure native surfaces: `CLAUDE.md`, `.claude/rules/`, `.claude/settings.json`, hooks, skills, subagents.
- Always local — every file goes in the project's `.claude/` directory.
- Subagents as files — every subagent is a `.md` file in `.claude/agents/` with YAML frontmatter.
- Invoke `writing-claude-md` for `AGENTS.md` and `CLAUDE.md`. Never write them directly.
- Invoke `write-a-skill` for the system skill. Hard gate — do not skip.
- Invoke `claude-code-guide` for hook design. Never write hooks manually.
- Sequential workflow — each phase gates the next.
- Judges use bounded context packs.
- Judge output is authoritative. No script rewrites it.
- No qualitative heuristics in scripts.

## Q0 — Project type

Ask: "What kind of project is this?"

Options:
- **Autonomous loop** — Claude runs continuously; Stop hook blocks early exit; `done-check.sh` decides when work is done

Save as `PROJECT_TYPE`.

## Harness layers

| Layer | Output |
|-------|--------|
| Intent | `PLAN.md`, `AGENTS.md`, `.claude/skills/` |
| Context | `CLAUDE.md`, `.claude/rules/`, `docs/` |
| Tools | `scripts/agent/`, `done-check.sh` |
| Constraints | `.claude/hooks/`, `.claude/settings.json` |
| Feedback | `.claude/agents/`, `judge-principles.md`, CI |
| Memory | `.mission-control/state.json`, `CLOSED_TASKS.md` |

## State hierarchy

```
Judge JSON (authoritative)
  -> Deterministic Evidence (support)
    -> Router (combines both)
```

Judge wins over precheck. A passed judge with a failed precheck means the judge accepted the evidence. A failed judge with a passed precheck means the judge found a qualitative issue the precheck missed.
