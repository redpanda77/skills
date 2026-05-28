---
name: claude-md-process
description: Full implementation checklist for writing, auditing, or compressing a CLAUDE.md. Reference when the user asks to create, modify, or review a CLAUDE.md.
---

# Implementation Checklist

When user asks to write, audit, or compress a CLAUDE.md, you MUST work through this checklist in order. Do not skip steps. Mark each item as done before proceeding.

## 1. Read & Decide

Before writing anything, read the relevant references and make decisions:

- [ ] **Read `references/principles.md`** — Confirm the 8 core principles apply to this CLAUDE.md
- [ ] **Read `references/setup.md`** — Know the full discovery procedure
- [ ] **Determine task:**
  - Create / Setup → read `references/setup.md` + `references/use-cases.md`
  - Audit existing file → read `references/checklist.md` + `references/anti-patterns.md`
  - Compress bloated → read `references/compression.md`
  - Multi-tool setup → read `references/cross-tool.md`
  - Context audit → read `references/context-audit.md` + `references/placement.md`
- [ ] **Determine scope:**
  - Global (`~/.claude/CLAUDE.md`) → under 30 lines, personal conventions
  - Project (root or `.claude/CLAUDE.md`) → 60–120 lines, team standards
  - Monorepo root → under 80 lines, high-level only
  - Package-level nested → 30–60 lines, package-specific
  - Local (`CLAUDE.local.md`) → personal overrides, gitignored
- [ ] **Determine if CONTEXT.md exists:**
  - If yes → read it, reference it in CLAUDE.md, never contradict its terms
  - If no → suggest running `/grill-with-docs` to create one
- [ ] **Determine if nested files needed:**
  - Run the decision tree in `references/nested-decisions.md`
  - Multi-package repo? → nested CLAUDE.md per package
  - Mixed content? → nested CLAUDE.md per domain
- [ ] **Determine if project-local skills needed:**
  - Does a cluster of rules apply to 2+ distinct scenarios? → read `references/local-skills.md`
  - Delegate to `write-a-skill` for the how

## 2. Discover

Read autonomously before asking the user:

- [ ] **List root directory:** `ls -la` or equivalent
- [ ] **Detect project type:**
  - `package.json` → Node.js / JavaScript
  - `pyproject.toml` / `requirements.txt` → Python
  - `Cargo.toml` → Rust
  - `go.mod` → Go
  - `next.config.*` / `svelte.config.*` → Frontend framework
  - `Dockerfile` / `docker-compose.yml` → Containerized
  - `.git` → Git repo
  - Absence of all above → likely non-code (writing, research, PM, marketing)
- [ ] **Read existing files:**
  - `CLAUDE.md` if exists
  - `AGENTS.md` if exists
  - `README.md` (first 50 lines)
  - `package.json` scripts if exists
  - Top-level folder names
- [ ] **Check for CONTEXT.md:** If exists, read it fully
- [ ] **Run `/memory` if available:** See what Claude has already learned
- [ ] **Infer conventions:** Look at existing code for style, patterns, tooling

## 3. Context Audit (If Task is Context Audit)

If the user asked to audit their instruction files, run the full context audit from `references/context-audit.md` and use the placement decision tree from `references/placement.md`.

### 3a. Find All Instruction Files

- [ ] **List all instruction files:** Search for `CLAUDE.md`, `AGENTS.md`, `context.md`, `CLAUDE.local.md`, `.claude/CLAUDE.md`, `.claude/rules/**/*.md`, `.claude/agents/*.md`, `.claude/skills/**/SKILL.md`, and any file imported with `@path`
- [ ] **Read all files:** Read every instruction file found
- [ ] **Run `/memory` if available:** See what is currently loaded in context

### 3b. Run Audit Checks

- [ ] **Are `CLAUDE.md`, `AGENTS.md`, and `context.md` saying the same thing?**
- [ ] **Is `CLAUDE.md` importing `AGENTS.md` and then repeating the same rules below it?**
- [ ] **Is `context.md` imported into `CLAUDE.md` even though its content is always loaded elsewhere?**
- [ ] **Are nested `CLAUDE.md` files contradicting root instructions?**
- [ ] **Are broad root rules actually only relevant to `frontend/`, `api/`, `tests/`, or another subtree?**
- [ ] **Are there personal preferences committed into project instructions?**
- [ ] **Are stale migration notes still being loaded globally?**
- [ ] **Are long explanations being loaded when a short rule would work?**
- [ ] **Are rules written as vague advice instead of concrete instructions?**

### 3c. Decide Placement for Each Rule

Run the decision tree in `references/placement.md` for every rule:

- [ ] **Does this apply to every task in the repo?**
  - Yes → KEEP ROOT (AGENTS.md / CLAUDE.md)
  - No → continue
- [ ] **Does this apply to a specific path or file type?**
  - Yes → MOVE TO RULE (`.claude/rules/*.md` with paths)
  - No → continue
- [ ] **Is this a repeatable workflow?**
  - Yes → MOVE TO SKILL (`.claude/skills/`)
  - No → continue
- [ ] **Is this a specialized role or worker?**
  - Yes → MOVE TO AGENT (`.claude/agents/<name>.md`)
  - No → continue
- [ ] **Is this personal and not team-wide?**
  - Yes → MOVE TO LOCAL (`CLAUDE.local.md`)
  - No → project-shared file

### 3d. Apply Cleanup Policy

- [ ] **Pick one canonical shared instruction file.** Prefer `AGENTS.md` as the cross-tool canonical file.
- [ ] **Keep `CLAUDE.md` as a thin Claude-specific loader:** import `@AGENTS.md`, add only Claude-specific deltas below it.
- [ ] **Delete or de-import `context.md`** if it only duplicates `AGENTS.md`.
- [ ] **Move local/private rules** into `CLAUDE.local.md`.
- [ ] **Move task-specific workflows** into skills.
- [ ] **Move path-specific rules** into `.claude/rules/` with paths frontmatter.
- [ ] **Move specialist behavior** into `.claude/agents/*.md`.

### 3e. Label Each Outcome

Use these labels in the audit output:

- **KEEP ROOT** — Applies globally.
- **MOVE TO RULE** — Applies only to paths or file types.
- **MOVE TO SKILL** — Task-specific workflow.
- **MOVE TO AGENT** — Specialized role behavior.
- **MOVE TO LOCAL** — Personal/private preference.
- **MERGE INTO AGENTS.md** — Duplicate canonical guidance.
- **DELETE** — Stale, redundant, or obvious.
- **CONFLICT** — Contradicts another instruction.
- **REWRITE** — Too vague or too long.

### 3f. Deliver Audit Report

- [ ] **List all instruction files found** with line counts
- [ ] **Show the target shape** (AGENTS.md → CLAUDE.md → .claude/rules/ → .claude/agents/ → .claude/skills/)
- [ ] **Present each rule with its label** and rationale
- [ ] **Show the proposed canonical `AGENTS.md`** (merged, deduplicated)
- [ ] **Show the proposed thin `CLAUDE.md`** (import + deltas)
- [ ] **Show the proposed `.claude/rules/`** files with paths
- [ ] **Show the proposed skills** to extract (delegate to `write-a-skill` for the how)
- [ ] **Show the proposed agents** to create
- [ ] **Show the proposed `CLAUDE.local.md`** content
- [ ] **List files to delete**
- [ ] **Run `/memory` after changes** to verify reduced context

If the user asked for a **single-file audit** (not a full context audit), skip to Phase 3 below.

---

## 3. Classify

Pick one use case. See `references/use-cases.md` for full templates:

- [ ] **coding-single** — one app/package
- [ ] **coding-monorepo** — multiple packages, nested files needed
- [ ] **writing** — book, blog, content, brand voice
- [ ] **research** — knowledge base, notes vault
- [ ] **pm** — product management, meeting notes, initiatives
- [ ] **marketing** — campaigns, copy, brand
- [ ] **mixed** — repo combines code + content

If ambiguous, ask **one** question to confirm.

## 4. Interview

Only ask what cannot be inferred. See `references/asking.md` for technique.

- [ ] **Critical commands:** What are the build, test, lint, format commands?
- [ ] **Architecture:** What do the top-level folders mean?
- [ ] **Hard rules:** What specific mistakes should the agent avoid?
- [ ] **Workflow:** What workflow preferences? (minimal changes, ask before big edits, etc.)
- [ ] **Out-of-scope:** What requires human approval?
- [ ] **Secrets / env:** Any env-specific values needed? (Never put in CLAUDE.md)

## 5. Draft

Fill the relevant template. Only cover the 5 sections that matter:

- [ ] **Critical commands** — build, test, lint, typecheck, migrate
- [ ] **Architecture map** — top-level folders and purpose, one line each
- [ ] **Hard rules** — negative + positive imperatives, under 15 rules
- [ ] **Workflow preferences** — minimal changes, ask before big edits, separate commits
- [ ] **Human-approval / Out-of-scope** — what requires explicit confirmation, what to never touch

## 6. Apply Principles

- [ ] **Every line prevents a specific mistake** — if removing it changes nothing, delete it
- [ ] **Imperatives over prose** — "Run X" not "we generally try to X"
- [ ] **Verifiable commands** — commands can be executed and checked
- [ ] **High-priority rules first** — security, irreversibility, out-of-scope in first 40 lines
- [ ] **IMPORTANT / YOU MUST sparingly** — reserve for 1–2 truly critical rules
- [ ] **Negative rules included** — explicit "nevers" prevent wrong defaults
- [ ] **No secrets anywhere** — not in CLAUDE.md, not in CLAUDE.local.md
- [ ] **Don't duplicate tooling** — delete anything linter/CI/auto-memory handles
- [ ] **Use `@imports`** — `@CONTEXT.md` or `@reference.md` for linked docs
- [ ] **No generic advice** — delete obvious language conventions, long tutorials, file-by-file maps
- [ ] **No stale info** — remove frequently changing information, version numbers, percentages

## 7. Validate

- [ ] **Line count:**
  - Project: 60–120 lines
  - Global: under 30 lines
  - Monorepo root: under 80 lines
  - Package-level: 30–60 lines
  - Mature repo: ~14 lines
- [ ] **No README.md inside skill folder** — if any skills were created
- [ ] **References one level deep** — no nested `references/sub/dir/file.md`
- [ ] **No XML tags in frontmatter** — if any skills were created
- [ ] **No secrets:** Search for API keys, tokens, passwords, internal URLs
- [ ] **No time-sensitive data:** Remove version numbers, percentages, dates
- [ ] **No generic copy-paste:** Check for personality instructions, obvious conventions, stale architecture
- [ ] **Consistent terminology:** One term per concept throughout
- [ ] **Forward slashes:** All file paths use `/` not `\`
- [ ] **Third person descriptions:** If any skills were created, descriptions are third person
- [ ] **Gerund naming:** If any skills were created, names use gerund form where possible

## 8. Test & Deliver

- [ ] **Before/after test:** If compression, verify adherence improved (see `references/testing.md`)
- [ ] **File path written:** Output to correct directory
- [ ] **Line count reported:** Include in final response
- [ ] **Rationale included:** One paragraph for any unusual rule
- [ ] **Follow-ups suggested:**
  - Add `CLAUDE.local.md` to `.gitignore`
  - Add CLAUDE.md review checkbox to PR template
  - Schedule quarterly pruning
  - If no CONTEXT.md, suggest `/grill-with-docs`
