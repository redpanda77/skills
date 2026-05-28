# 03 — Configure

Build the harness.

## Files in this folder

- `README.md` — this file
- `agents.md` — how to write `AGENTS.md`, `CLAUDE.md`, nested files
- `frontmatter.md` — how to write YAML frontmatter for skills, agents, commands
- `hooks.md` — how to design and install hooks
- `judges.md` — how to create judge subagents
- `skills.md` — how to create system and domain skills
- `validators.md` — how to write validators

## Setup order

1. **Intent** — `agents.md` — write `AGENTS.md`, `CLAUDE.md`, `PLAN.md`
2. **Validation** — `validators.md` — write `done-check.sh`, `validate-*.sh`
3. **Constraints** — `hooks.md` — install hooks
4. **Feedback** — `judges.md` — create judge subagent(s)
5. **Memory** — `skills.md` — create system and domain skills
6. **Commands** — create in `.claude/commands/`

## Next

Read `references/04-test/README.md`
