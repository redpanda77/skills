---
name: claude-md-categories
description: CLAUDE.md content categories. Reference when deciding what to include, what to exclude, where to put it, and how to organize it.
---

# CLAUDE.md Categories

Map content to the right location. If it's not needed every turn, put it in a reference or skill.

## Purpose and Scope

CLAUDE.md is a **behavioral contract**, not documentation.
- README is for humans. CLAUDE.md is for an agent.
- README informs. CLAUDE.md governs.
- Every line must change agent behavior. If removing it changes nothing, delete it.

See `references/principles.md` for the full rationale.

## File Locations

| Location | Owner | Scope | Target Length |
|----------|-------|-------|---------------|
| `~/.claude/CLAUDE.md` | You | Every project on your machine | < 30 lines |
| `.claude/CLAUDE.md` or root `CLAUDE.md` | Team (in git) | This repo | 60–120 lines |
| `CLAUDE.local.md` | You (gitignored) | This repo, this developer | Personal overrides |
| Nested `CLAUDE.md` | Team | Subdirectory / package | 30–60 lines |

Enterprise variant: Layer 1 (org-wide) → Layer 2 (service-level) → Layer 3 (developer-local). Higher layers win in conflicts.

See `references/principles.md` for loading mechanics and `references/nested-decisions.md` for when to nest.

## What to Include

Only include what the agent cannot infer from one session in the repo:

1. **Critical commands** — build, test, lint, typecheck, migrate. Highest-value section.
2. **Architecture map** — top-level folders and purpose. One line each. Not a directory listing.
3. **Hard rules** — negative + positive imperatives. Under 15 rules. Each must prevent a specific mistake. Include **permanent facts / invariants**: constraints from past decisions that are always true regardless of the specific task. If a task conflicts with one, flag it before proceeding.
4. **Workflow preferences** — minimal changes, ask before big edits, separate commits, ask between approaches.
5. **Human-approval / Out-of-scope** — what requires explicit confirmation, what to never touch.

See `references/use-cases.md` for templates per use case and `references/template.md` for a production-ready coding template.

## What to Exclude

Delete anything that does not change agent behavior:

- **Generic advice** — "write clean code", "follow best practices"
- **Obvious language conventions** — things a linter already enforces
- **Long tutorials** — explanations of how things work; the agent already knows
- **File-by-file codebase maps** — the agent can see the file tree
- **Frequently changing information** — version numbers, percentages, dates
- **Documentation better linked elsewhere** — design docs, ADRs, API docs (link them, don't paste)
- **Secrets, tokens, env-specific values** — never in CLAUDE.md or CLAUDE.local.md
- **Personality instructions** — "be a senior engineer", "be helpful"
- **Style rules a linter enforces** — delete anything tooling already handles

See `references/anti-patterns.md` for what to refuse and flag.

## Loading Behavior

- Loaded at **session start** — walks up directory tree from cwd, concatenating every `CLAUDE.md` found.
- Treated as **context**, not hard enforcement — the agent can override with user instructions.
- Survives **compaction** better than chat-only instructions — `/compact` re-reads instruction files fresh.
- Adds to **context budget** — every line competes with conversation history and other skills.
- Files lower in the tree load **later** — soft weight to later instructions, but don't rely on it.
- Subdirectory files load **on demand** when the agent reads/edits files in that subtree.
- `@imports` (`@foo.md`) are **expanded inline** — same context cost as pasting.
- `/memory` shows exactly which instruction files are loaded right now — primary debugging tool.
- Auto-memory records inferred conventions at `~/.claude/projects/<project>/memory/` — after a few sessions, prune duplicates from CLAUDE.md.

See `references/principles.md` for the full loading mechanics.

## Import and Organization

- **@imports** — `@CONTEXT.md` expands inline. Use for domain vocabulary that must always be loaded.
- **Linked docs** — `[reference.md](reference.md)` for deep docs loaded only when needed.
- **Project-level memory files** — `MEMORY.md` for session summaries and decisions. `ERRORS.md` for logging approaches that took >2 attempts: what failed, what worked, what to remember next time. Link from CLAUDE.md, do not paste contents.
- **Split large instructions** — if a section is >20 lines, consider extracting to a reference or skill.
- **Monorepo-specific files** — root CLAUDE.md is high-level; package-level CLAUDE.md is specific.
- **Local personal overrides** — `CLAUDE.local.md` for personal preferences that shouldn't be in git.

See `references/nested-decisions.md` for nested file organization and `references/local-skills.md` for extracting to skills.

## Editing and Maintenance

- **Init** — `/init` produces bloated files. Use as a starting point, then compress aggressively.
- **Memory** — `/memory` shows what Claude has learned. Prune duplicates from CLAUDE.md.
- **Pruning** — Quarterly review. Delete anything the agent now infers automatically.
- **Testing adherence** — Run the before/after test in `references/testing.md`.
- **Keeping it concise** — If a line doesn't prevent a specific mistake, delete it.

See `references/compression.md` for the three-pass compression framework and `references/testing.md` for verification.
