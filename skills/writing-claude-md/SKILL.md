---
name: writing-claude-md
description: Write, audit, or compress a CLAUDE.md / AGENTS.md instruction file for a coding agent. Use when the user asks to create, write, draft, generate, review, audit, compress, refactor, or improve a CLAUDE.md, AGENTS.md, copilot-instructions.md, .cursor/rules, or .windsurfrules file — or asks how to make Claude Code follow their conventions, what to put in CLAUDE.md, or why their CLAUDE.md is being ignored.
---

# Writing CLAUDE.md / AGENTS.md

You are helping the user produce a high-signal instruction file for a coding agent. CLAUDE.md is a **behavioral contract**, not documentation — every line must change agent behavior or be deleted.

The bundled knowledge base for this skill lives in `references/` next to this file. Read those files for deep references; this file is the working procedure.

## Core principles (apply to every output)

1. **Less is more.** Target 60–120 lines for a project file, under 30 for global, under 80 for monorepo root. Every line must prevent a specific mistake.
2. **Imperatives over prose.** "Run `pnpm test` before marking ready" beats "make sure tests pass."
3. **Verifiable commands over descriptions.** Commands can be executed and checked; descriptions can't.
4. **High-priority rules first.** Security, irreversibility, and out-of-scope rules in the first 40 lines.
5. **`IMPORTANT` / `YOU MUST` sparingly.** Reserve for the one or two truly critical rules. If everything is important, nothing is.
6. **Negative rules matter.** Without explicit "nevers," the agent picks the most common pattern it knows — which may not be yours.
7. **Don't duplicate the linter, the CI, or auto-memory.** Delete anything tooling already enforces or that the agent infers from one session in the repo.
8. **No secrets. Ever.** Not in CLAUDE.md, not in CLAUDE.local.md.

See `references/principles.md` for the full rationale.

## Workflows

### A. Setup / Create a new CLAUDE.md

Use the structured setup procedure in `references/setup.md`. The short version:

1. **Discover.** Read the directory autonomously (do not ask the user yet):
   - `ls -la` the root.
   - Detect project type by signal files (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `.git`, `next.config.*`, `Dockerfile`, etc.). Absence of any of these → likely a **non-code** project (writing, research, PM, marketing).
   - Read existing `CLAUDE.md`, `AGENTS.md`, `README.md`, `package.json` scripts, top-level folder names.
   - **If `CONTEXT.md` exists**, read it. The CLAUDE.md you write must reference it (`@CONTEXT.md` import or an explicit "read CONTEXT.md at session start" rule) so domain vocabulary is always loaded. Never author a CLAUDE.md that uses different terms than those defined in CONTEXT.md.
   - Run `/memory` if available to see what Claude has already auto-learned.
2. **Classify the use case.** Pick one (see `references/use-cases.md` for full template per type):
   - `coding-single` — one app/package.
   - `coding-monorepo` — multiple packages, nested files needed.
   - `writing` — book, blog, content, brand voice.
   - `research` — knowledge base, notes vault (e.g., Tolaria-style).
   - `pm` — product management, meeting notes, initiatives.
   - `marketing` — campaigns, copy, brand.
   - `mixed` — repo combines code + content.
   If the signals are ambiguous, ask **one** AskUserQuestion to confirm.
3. **Interview — only what cannot be inferred.** Use `AskUserQuestion` for every clarifying question — never plain text (see `references/asking.md`). One question per decision, multi-select where natural, always with a recommended option marked `(Recommended)`, always include a free-text fallback as the last option. Skip every question the discovery step already answered.
4. **Decide on nested files.** Run the nested-file decision tree in `references/nested-decisions.md`. Propose locations as an AskUserQuestion if any are recommended; let the user confirm.
5. **Pick the layer.** Root `CLAUDE.md` vs `.claude/CLAUDE.md` vs `CLAUDE.local.md` — ask only if ambiguous.
6. **Draft using the use-case template** from `references/use-cases.md`. Fill the relevant sections.
7. **Length check.** Use the target for the chosen use case. If over, run compression before showing.
8. **Write file(s).** Output to the directory. If multiple files (root + nested), list them all.
9. **Follow-ups.** Suggest gitignore additions for `CLAUDE.local.md`, PR template checkbox (coding), quarterly review reminder. If the project has no `CONTEXT.md`, suggest running `/grill-with-docs` to create one — the CLAUDE.md you just wrote will be stronger once domain vocabulary is captured.

### B. Audit an existing CLAUDE.md

1. **Read the file.** Note line count.
2. **Run the 10-point checklist** in `references/checklist.md`.
3. **Flag anti-patterns** using `references/anti-patterns.md`. Common findings:
   - Personality instructions ("be a senior engineer")
   - Style rules a linter already enforces
   - Contradictory rules
   - Stale architecture descriptions
   - Mixed personal preferences with team standards
   - Generic copy-paste content with no project specifics
4. **Score signal-to-noise.** For every line, ask: "If I remove this, would Claude make a specific mistake?" If no → flag for deletion.
5. **Identify extraction candidates.** Apply the 2-of-N test in `references/local-skills.md` to find clusters that should become project-local skills under `.claude/skills/`.
6. **Produce a report** with: line count, checklist results, suggested deletions (quoted), suggested additions (with reasoning), suggested skill extractions, and a proposed compressed version.

### C. Compress a bloated CLAUDE.md

Run the three-pass framework in `references/compression.md`:

1. **Pass 1 — Deduplication.** Merge duplicate rules, delete rules the linter/CI/auto-memory handle.
2. **Pass 2 — Prose → commands.** Replace every "make sure X" with a runnable command.
3. **Pass 3 — Split.** Anything folder-specific moves to a nested `CLAUDE.md`. **Anything that is deep reference content gets extracted to a project-local skill** under `.claude/skills/` — see `references/local-skills.md` for the 2-of-N extraction test. Root must be scannable in 90 seconds.

CLAUDE.md must reference any project-local skill it spawns in a `## Project-local skills` section so Claude knows the skill exists.

**Do NOT author the extracted skill inline.** Delegate to `write-a-skill` (preferred), `skill-creator`, or `plugin-dev:skill-development`. See the handoff procedure in `references/local-skills.md`. Read those skills' content only when actually authoring, not during audit/compression.

Then run the **before/after test** in `references/testing.md` if the user wants validation.

### D. Build a multi-tool unified setup

When the user uses Claude Code + Codex/Copilot/Cursor/Windsurf:

1. Create a canonical `AGENTS.md` (tool-agnostic).
2. `CLAUDE.md` starts with `@AGENTS.md` then adds Claude-specific behavior.
3. Stub adapters for other tools, each referencing `AGENTS.md`.
4. Recommend a CI check that verifies core rules appear in every adapter.

Details: `references/cross-tool.md`.

## What NOT to do

- **Do not auto-generate via `/init`-style enumeration.** A good CLAUDE.md is hand-crafted. Auto-generated files are bloated and miss the rules that actually matter.
- **Do not include code style rules** a linter enforces. See `references/anti-patterns.md`.
- **Do not include secrets, tokens, or env-specific values** — even in `CLAUDE.local.md`.
- **Do not paste design docs or ADRs** in full. Summarize the rule in two sentences; link the doc.
- **Do not write `IMPORTANT:` on more than two rules.**
- **Do not invent commands.** Ask the user; never guess `pnpm test` vs `npm test`.
- **Do not author project-local skills inline.** When extraction is needed, delegate to `write-a-skill` / `skill-creator` / `plugin-dev:skill-development`. This skill decides *whether* and *what* to extract; the skill-authoring skills decide *how* to build it. Read them only when actually authoring.

## After producing output

End with:
- File path written
- Line count
- One-paragraph rationale for any unusual rule
- Suggested follow-ups: add `CLAUDE.local.md` to `.gitignore`, add CLAUDE.md review checkbox to PR template, schedule quarterly pruning.

## References

- `references/setup.md` — full setup procedure: discover → classify → interview → nested → write
- `references/use-cases.md` — templates per use case (coding, writing, research, PM, marketing, mixed)
- `references/asking.md` — how to use AskUserQuestion well in this skill
- `references/nested-decisions.md` — when to create nested CLAUDE.md, where, and what goes in them
- `references/local-skills.md` — **whether** and **what** to extract into project-local skills (the **how** is delegated to `write-a-skill` / `skill-creator`)
- `references/principles.md` — full principles, instruction budget, three-layer hierarchy, loading mechanics
- `references/template.md` — production-ready coding template + 14-line compressed variant
- `references/checklist.md` — 10-point audit checklist
- `references/anti-patterns.md` — what to refuse / flag
- `references/compression.md` — three-pass compression framework
- `references/cross-tool.md` — AGENTS.md + adapters for Codex/Copilot/Cursor/Windsurf
- `references/testing.md` — how to verify adherence
- `references/high-impact-lines.md` — copy-paste high-leverage rules
