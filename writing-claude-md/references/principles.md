# Principles

## CLAUDE.md is a behavioral contract, not documentation

- README is for humans. CLAUDE.md is for an agent.
- README informs. CLAUDE.md governs.
- Every line must change agent behavior. If removing it changes nothing, delete it.

## Instruction budget

- Frontier thinking models follow ~150–200 instructions reliably.
- Claude Code's system prompt already uses ~50 slots.
- Effective remaining budget: 100–150 slots shared across CLAUDE.md, skills, plugins, user messages.
- Smaller models decay **exponentially** as instruction count rises; large thinking models decay linearly.
- Position bias: LLMs attend most to the **beginning** (system + CLAUDE.md top) and **end** (most recent user message). Middle gets less attention.
- Adherence decay is **uniform** as count rises — more rules makes every rule weaker.

## Recommended length

| Scope | Target |
|------|--------|
| Global (`~/.claude/CLAUDE.md`) | < 30 lines |
| Project root | 60–120 lines |
| Monorepo root | < 80 lines |
| Package-level nested | 30–60 lines |
| Mature/well-auto-memorized repo | ~14 lines |

## Three-layer hierarchy

| Layer | Path | Owner | Scope |
|------|------|-------|-------|
| Global | `~/.claude/CLAUDE.md` | You | Every project on your machine |
| Project | `.claude/CLAUDE.md` or root `CLAUDE.md` | Team (in git) | This repo |
| Local | `CLAUDE.local.md` | You (gitignored) | This repo, this developer |

Enterprise variant: Layer 1 (org-wide, security/compliance, platform team) → Layer 2 (service-level, service team) → Layer 3 (developer-local). Higher layers win in conflicts. Document the policy in the org-wide root.

## How Claude Code loads CLAUDE.md

- Walks up the directory tree from cwd to repo root, **concatenating** every `CLAUDE.md` found.
- Files lower in the tree (closer to cwd) read later — soft weight to later instructions, but don't rely on it.
- Subdirectory files load **on demand** when Claude reads/edits files in that subtree.
- `@imports` (`@foo.md`) are **expanded inline** — same context cost as pasting.
- `/compact` compresses the conversation summary but **re-reads all instruction files fresh**.
- `/memory` shows exactly which instruction files are loaded right now — primary debugging tool.
- Auto-memory: Claude records inferred conventions at `~/.claude/projects/<project>/memory/`. After a few sessions, `/memory` and prune duplicates from CLAUDE.md.

## Five sections that actually matter

Every effective CLAUDE.md covers exactly these:

1. **Critical commands** — build, test, lint, typecheck, migrate. Highest-value section.
2. **Architecture map** — top-level folders and purpose. One line each. Not a directory listing.
3. **Hard rules** — negative + positive imperatives. Under 15 rules. Each must prevent a specific mistake.
4. **Workflow preferences** — minimal changes, ask before big edits, separate commits, ask between approaches.
5. **Human-approval / Out-of-scope** — what requires explicit confirmation, what to never touch.

## Writing style

- **Imperatives** ("Run X", "Never do Y"), not prose ("we generally try…").
- **Verifiable commands** over descriptions.
- **Negative rules** are as important as positive ones.
- **`IMPORTANT`** / **`YOU MUST`** — sparingly, on the truly critical rules only.
- **Testable** — you should be able to verify adherence in code review.

## What CLAUDE.md is not

- Not a linter (use Biome, ESLint, Ruff, gofmt — wire a Stop hook if needed).
- Not enforcement (CI is enforcement).
- Not a place for secrets, design docs, ADRs, or stale architecture.
- Not auto-generated — `/init` produces bloated files that miss what matters.
