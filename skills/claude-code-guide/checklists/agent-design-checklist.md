# Agent Design Checklist

Use while authoring `.claude/agents/*.md` or user-level agents.

## Role

- [ ] Single clear **role** (one primary job).
- [ ] Success criteria implied by the prompt’s **Return:** section.

## Delegation

- [ ] `description` answers: **when**, **what**, **output**, **exclusions** (`delegation-description-checklist.md`).
- [ ] No contradictory “never use” lines that confuse routing.

## Tools

- [ ] Smallest **tool** set that can complete the job (`permissions-checklist.md`).
- [ ] If read-only, **omit** `Edit`/`Write` and dangerous `Bash` patterns.

## Model and effort

- [ ] `model` chosen for cost/latency vs difficulty (`haiku` search, `sonnet` default deep work).
- [ ] `effort` set only when you truly need an override from session defaults.

## Execution mode

- [ ] Default **foreground vs background** behavior matches risk (background + prompts = auto-deny).
- [ ] `isolation: worktree` when filesystem isolation is required.

## Skills and memory

- [ ] `skills:` lists only **reference** skills the agent should see immediately.
- [ ] `memory:` enabled only when cross-session learning is desired and governance is clear.

## Hooks

- [ ] Agent-scoped hooks are **narrow** matchers (avoid `PreToolUse` + `"*"` unless justified).
- [ ] Project-wide lifecycle uses `SubagentStart`/`SubagentStop` instead of duplicating per file.

## Validation

- [ ] Run `scripts/validate-agent-frontmatter.py` on the file.
- [ ] Run `scripts/lint-agent-description.py` on the file.

## Ship

- [ ] Project agents committed to VCS when team-shared.
- [ ] Plugin limitations documented if copying from plugin templates (`hooks`/`mcpServers`/`permissionMode` stripped).
