---
name: writing-claude-md
description: Write, audit, or compress a CLAUDE.md / AGENTS.md instruction file for a coding agent. Use when the user asks to create, write, draft, generate, review, audit, compress, refactor, or improve a CLAUDE.md, AGENTS.md, copilot-instructions.md, .cursor/rules, or .windsurfrules file — or asks how to make Claude Code follow their conventions, what to put in CLAUDE.md, or why their CLAUDE.md is being ignored.
---

# Core Principles

Progressive disclosure is the most critical principle. Load only what is needed, when it is needed.
- **Level 1:** Frontmatter — name + description. Always loaded.
- **Level 2:** SKILL.md — core workflow. Loaded when triggered. Under 100 lines.
- **Level 3:** References — deep docs. Loaded only when needed.

CLAUDE.md is a behavioral contract, not documentation. Every line must change agent behavior or be deleted.
Less is more. Target 60–120 lines for a project file, under 30 for global, under 80 for monorepo root.
Imperatives over prose. Verifiable commands over descriptions.
High-priority rules first. Security, irreversibility, and out-of-scope rules in the first 40 lines.
IMPORTANT / YOU MUST sparingly. Reserve for the one or two truly critical rules.
Negative rules matter. Without explicit "nevers," the agent picks the most common pattern.
Don't duplicate the linter, the CI, or auto-memory. Delete anything tooling already enforces.
No secrets. Ever. Not in CLAUDE.md, not in CLAUDE.local.md.

See references/principles.md for full rationale.

---

# When Asked to Write, Audit, or Compress a CLAUDE.md

Do not write anything before reading the reference for the step you are on. Use the checklist in references/process.md. Mark each item as done before proceeding.

## 1. Determine Task

- **Create / Setup** → See references/setup.md
- **Audit existing file** → See references/checklist.md + references/anti-patterns.md
- **Compress bloated** → See references/compression.md
- **Multi-tool setup** → See references/cross-tool.md
- **Context audit** → See references/context-audit.md

## 2. Discover Project Context

Read autonomously before asking the user. See references/setup.md for the full procedure.
- `ls -la` the root
- Detect project type by signal files (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, etc.)
- Read existing `CLAUDE.md`, `AGENTS.md`, `README.md`, top-level folder names
- If `CONTEXT.md` exists, read it — CLAUDE.md must reference it, never contradict its terms
- Run `/memory` if available to see what Claude has already learned

## 3. Classify Use Case

Pick one. See references/use-cases.md for full templates per type:
- **coding-single** — one app/package
- **coding-monorepo** — multiple packages, nested files needed
- **writing** — book, blog, content, brand voice
- **research** — knowledge base, notes vault
- **pm** — product management, meeting notes, initiatives
- **marketing** — campaigns, copy, brand
- **mixed** — repo combines code + content

If signals are ambiguous, ask **one** question to confirm.

## 4. Decide Structure

- **Layer:** Global vs Project vs Local (see references/principles.md)
- **Placement:** Run the decision tree in references/placement.md to decide what goes in root vs subdirectory vs skill vs agent vs local
- **Nested files:** Run the decision tree in references/nested-decisions.md
- **Project-local skills:** If a cluster of rules applies to 2+ distinct scenarios, extract to a skill (see references/local-skills.md). Delegate to `write-a-skill` for the how.

## 5. Draft Content

Fill the relevant use-case template from references/use-cases.md. Only cover the 5 sections that matter. See references/categories.md for what to include, what to exclude, and where to put it.
1. Critical commands — build, test, lint, typecheck
2. Architecture map — top-level folders and purpose
3. Hard rules — negative + positive imperatives, under 15 rules
4. Workflow preferences — minimal changes, ask before big edits
5. Human-approval / Out-of-scope — what requires explicit confirmation

## 6. Apply Principles

- Every line prevents a specific mistake
- Imperatives over prose
- High-priority rules in first 40 lines
- Negative rules included
- No secrets anywhere
- Don't duplicate linter, CI, or auto-memory
- Use `@imports` for linked docs (see references/principles.md)
- See references/categories.md for the full include/exclude list

## 7. Validate Length

- Project: 60–120 lines
- Global: under 30 lines
- Monorepo root: under 80 lines
- If over, run compression (see references/compression.md)

## 8. Test & Deliver

See references/testing.md for the before/after test.
- File path written
- Line count
- One-paragraph rationale for any unusual rule
- Suggested follow-ups: add `CLAUDE.local.md` to `.gitignore`, add review checkbox to PR template, schedule quarterly pruning
