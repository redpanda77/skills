# Agents Setup

How to write `AGENTS.md`, `CLAUDE.md`, and nested files.

## What this is

- `AGENTS.md` is the primary orchestration contract. It is a map, not a manual (under 120 lines).
- `CLAUDE.md` is the auto-loaded adapter. It is a behavioral contract.
- Nested files in subdirectories are for divergent conventions.

## Rules

- Always invoke `writing-claude-md` to write `AGENTS.md` and `CLAUDE.md`. Never write them directly.
- `AGENTS.md` is the authority. `CLAUDE.md` is the auto-loaded adapter.
- If they conflict, `AGENTS.md` wins.
- Nested files are created only where score >= 2.
- Each nested file is 30–60 lines. Three sections: Conventions, Commands, Hard Rules.
- Do not duplicate root rules. Root rules apply everywhere.
