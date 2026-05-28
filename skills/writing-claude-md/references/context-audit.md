---
name: claude-md-context-audit
description: Context audit for instruction files. Use when the user asks to audit, clean up, or unify their CLAUDE.md, AGENTS.md, context.md, and other instruction files that load into context.
---

# Context Audit

## Goal

Find every instruction file that is entering context. Remove duplicated guidance. Resolve conflicting rules. Keep one canonical source of truth. Move path-specific guidance out of global context.

## Files to Audit

- `CLAUDE.md`
- `CLAUDE.local.md`
- `AGENTS.md`
- `agents.md`
- `context.md`
- `.claude/CLAUDE.md`
- `.claude/rules/**/*.md`
- `.claude/agents/*.md`
- Any file imported with `@path`
- Any nested `CLAUDE.md` in subdirectories

## Important Claude Code Behavior

- Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so if `AGENTS.md` is the shared canonical file, `CLAUDE.md` should import it rather than duplicate it.
- `CLAUDE.md` files in the directory hierarchy above the working directory are loaded in full at launch. Subdirectory `CLAUDE.md` files load later when Claude reads files in those subdirectories.
- Imported files using `@path` are expanded into context at launch, so imports help organization but do not reduce context usage.
- `/memory` can show which `CLAUDE.md`, `CLAUDE.local.md`, and rule files are loaded in the current session.

## Audit Checks

- Are `CLAUDE.md`, `AGENTS.md`, and `context.md` saying the same thing?
- Is `CLAUDE.md` importing `AGENTS.md` and then repeating the same rules below it?
- Is `context.md` imported into `CLAUDE.md` even though its content is always loaded elsewhere?
- Are nested `CLAUDE.md` files contradicting root instructions?
- Are broad root rules actually only relevant to `frontend/`, `api/`, `tests/`, or another subtree?
- Are there personal preferences committed into project instructions?
- Are stale migration notes still being loaded globally?
- Are long explanations being loaded when a short rule would work?
- Are rules written as vague advice instead of concrete instructions?

## Cleanup Policy

- Pick one canonical shared instruction file.
- Prefer `AGENTS.md` as the cross-tool canonical file if multiple coding agents read it.
- Keep `CLAUDE.md` as a thin Claude-specific loader:
  - import `@AGENTS.md`
  - add only Claude-specific deltas below it
- Delete or de-import `context.md` if it only duplicates `AGENTS.md`.
- Move local/private rules into `CLAUDE.local.md`.
- Move task-specific workflows into skills.
- Move path-specific rules into `.claude/rules/` with `paths` frontmatter.
- Move specialist behavior into `.claude/agents/*.md`.

## Example Target Shape

```
AGENTS.md                 # canonical shared rules
CLAUDE.md                 # thin Claude loader
CLAUDE.local.md           # private local preferences, gitignored
.claude/rules/            # path-scoped rules
.claude/agents/           # specialized subagents
.claude/skills/           # workflows loaded only when relevant
```

## Example CLAUDE.md

```markdown
@AGENTS.md

## Claude Code only
- Use plan mode before changing files under `src/billing/`.
- Prefer skills for repeatable workflows instead of expanding this file.
```

## Audit Outcome Labels

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

## Core Principle

The root file should explain the repo. Subdirectory rules should explain local conventions. Skills should teach repeatable workflows. Agents should define specialized workers. Anything else is probably unnecessary context.
