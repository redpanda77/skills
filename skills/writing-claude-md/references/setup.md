# Setup procedure

The full procedure for setting up CLAUDE.md in a new (or existing) project. Bias toward **autonomous discovery** — ask the user only what cannot be inferred.

## Step 1 — Discover

Run these commands and read the output before asking anything:

```bash
ls -la                                  # see top-level
test -f package.json && cat package.json | head -50
test -f pyproject.toml && cat pyproject.toml | head -40
test -f Cargo.toml && cat Cargo.toml | head -30
test -f go.mod && cat go.mod | head -10
test -f README.md && head -60 README.md
test -f CLAUDE.md && cat CLAUDE.md
test -f AGENTS.md && cat AGENTS.md
test -d .git && git log --oneline -5 2>/dev/null
```

Use the project-type signals table in this file to classify.

## Step 2 — Classify use case

| Signal | Likely use case |
|--------|-----------------|
| `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `*.gemspec` | `coding-single` |
| Above + `packages/`, `apps/`, workspaces field, `pnpm-workspace.yaml`, Nx/Turbo | `coding-monorepo` |
| `chapters/`, `manuscript.md`, `_drafts/`, `.obsidian/`, lots of `.md` + few code files | `writing` |
| `notes/`, `meetings/`, `research/`, `daily/`, vault-shaped Markdown | `research` or `pm` |
| `initiatives/`, `summaries/`, `decisions/` | `pm` |
| `campaigns/`, `copy/`, `assets/`, brand guidelines | `marketing` |
| Mix of code + content folders | `mixed` |
| Empty or near-empty directory | **Ask** — it's a new project |

If signals are ambiguous, **ask one AskUserQuestion**:

> What is this project primarily about?
>
> - Coding project (single app/package) (Recommended)
> - Coding monorepo (multiple packages)
> - Writing (book, blog, content)
> - Research / knowledge base
> - Product management / notes
> - Marketing / brand
> - Mixed (code + content)
> - Other

## Step 3 — Interview (only what's needed)

Use the question bank in `asking.md`. **Skip every question discovery already answered.** Never ask:

- The stack if you found `package.json` / `pyproject.toml` / etc.
- The build/test command if you found it in `scripts:` or `Makefile`.
- The project name if you found it in `package.json` or the dir name.
- Top-level folders if you can `ls`.

**Do ask** for things only the user knows:

- Hard rules / "never do this" rules specific to their project
- Folders to never touch
- Actions requiring human approval
- Voice / tone (writing, marketing)
- Audience (writing, marketing, PM)
- Tribal-knowledge constraints

Cap at **5 questions** per setup session. If you need more, do a second pass after writing v0.

## Step 4 — Decide on nested files

Apply `nested-decisions.md`. Propose nested locations as an AskUserQuestion with `multiSelect: true`:

> I recommend nested CLAUDE.md files in these locations. Select all that apply:
>
> - `lib/auth/` — auth conventions (Recommended)
> - `app/api/` — API handler conventions (Recommended)
> - `infra/` — Terraform + approval rules
> - `packages/ml-workers/` — Python conventions
> - None — keep everything in the root

## Step 5 — Choose the layer

Default to **root `CLAUDE.md`** for project context. Ask only if the user's situation is unusual:

- Personal-only rules → `CLAUDE.local.md` + gitignore.
- `.claude/` already exists with other config → `.claude/CLAUDE.md`.
- Multi-tool repo → write `AGENTS.md` first, then thin `CLAUDE.md` with `@AGENTS.md`. See `cross-tool.md`.

## Step 6 — Draft

Use the matching template from `use-cases.md`. Fill in real values from discovery + interview. Use [[high-impact-lines]] as building blocks where applicable.

## Step 7 — Length check

| Use case | Target |
|----------|--------|
| `coding-single` | 60–120 lines |
| `coding-monorepo` root | < 80 lines (rest in nested) |
| `writing` | 40–80 lines |
| `research` / `pm` | 40–80 lines |
| `marketing` | 40–80 lines |
| `mixed` | 60–100 lines |

Over budget → run `compression.md` before showing the user.

## Step 8 — Write

Use the Write tool. List every file created.

## Step 9 — Follow-ups

Always end with a brief follow-up list:

- [ ] Add `CLAUDE.local.md` to `.gitignore` (if a git repo)
- [ ] Add CLAUDE.md review checkbox to PR template (coding only)
- [ ] Schedule a 30-min quarterly prune
- [ ] Run `/memory` after a few sessions to find duplicates
- [ ] If multi-tool: extract canonical `AGENTS.md` (see `cross-tool.md`)

## Step 10 — Manage / iterate

When the user says "add this to CLAUDE.md" or "Claude keeps doing X, fix it":

1. Read the current file.
2. Identify which section the new rule belongs in (Hard Rules, Workflow, Out-of-Scope).
3. Check for contradiction with existing rules.
4. Append in imperative form.
5. Re-run length check; compress if over target.
