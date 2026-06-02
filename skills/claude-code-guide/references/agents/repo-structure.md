---
name: agent-repo-structure
description: Recommended repo structure and role of each file type in the agent system. Use when setting up or reorganizing a project's instruction files.
---

# Recommended Repo Structure

```
repo/
├── AGENTS.md
├── CLAUDE.md
├── CLAUDE.local.md              # gitignored
├── .claude/
│   ├── settings.json
│   ├── agents/
│   │   ├── security-reviewer.md
│   │   ├── test-runner.md
│   │   ├── frontend-reviewer.md
│   │   ├── backend-reviewer.md
│   │   └── coordinator.md
│   ├── rules/
│   │   ├── api.md
│   │   ├── frontend.md
│   │   ├── tests.md
│   │   └── migrations.md
│   └── skills/
│       ├── review-pr/
│       │   └── SKILL.md
│       ├── fix-issue/
│       │   └── SKILL.md
│       ├── add-regression-test/
│       │   └── SKILL.md
│       └── context-audit/
│           └── SKILL.md
```

## Role of Each File Type

### AGENTS.md

Canonical shared instruction file for cross-tool compatibility. Contains only repo-wide rules.

**Put here:**
- Project purpose
- Architecture overview
- Build/test/lint commands
- Global coding standards
- Global security rules
- PR/review expectations
- "Never do this" repo-wide constraints

**Do not put here:** path-specific details, long workflows, or specialist agent behavior.

### CLAUDE.md

Claude Code reads `CLAUDE.md`, not `AGENTS.md`. If `AGENTS.md` is the canonical shared file, make `CLAUDE.md` a thin loader.

```markdown
@AGENTS.md

## Claude Code only
- Prefer skills for repeatable workflows.
- Use path-scoped rules instead of expanding this file.
- Run the context-audit skill if multiple instruction files appear to overlap.
```

### .claude/rules/

Passive instructions that load only for certain files or directories.

```yaml
---
paths:
  - "src/api/**/*.ts"
  - "apps/api/**/*.ts"
---
# API rules
- Validate external input at the boundary.
- Use the standard error response shape.
- Add or update endpoint tests for behavior changes.
```

**Use rules when:** the instruction is always true for a path, but not globally relevant.

### .claude/skills/

Repeatable workflows:
- context audit
- PR review
- issue fixing
- migration generation
- release notes
- regression test creation
- debugging workflow
- codebase exploration workflow

**Use skills when:** the instruction is useful only sometimes, or is long, or has steps/arguments/templates.

### .claude/agents/

Reusable specialist workers:
- security-reviewer
- test-runner
- frontend-reviewer
- backend-reviewer
- performance-reviewer
- context-auditor
- coordinator

**Use agents when:** the behavior is a specialized role, the work should happen in a separate context window, or the agent needs a constrained toolset or preloaded skills.

## Subagent vs Agent Team

| Aspect | Subagent | Agent Team |
|--------|----------|------------|
| Sessions | One | Multiple independent |
| Communication | Reports to main | Teammates message each other |
| Cost | Lower | Higher (each teammate is a full session) |
| Use when | Focused task, only result matters | Parallel exploration, reviewers challenge each other |

Subagents run inside one Claude Code session. Agent teams are multiple independent sessions coordinated by a lead.

## Recommended Starting Agents

```
.claude/agents/
├── coordinator.md
├── context-auditor.md
├── security-reviewer.md
├── test-runner.md
├── frontend-reviewer.md
├── backend-reviewer.md
└── performance-reviewer.md
```

- **coordinator**: breaks work into phases, decides when to use subagents or teams
- **context-auditor**: audits instruction files and recommends cleanup
- **security-reviewer**: read-only security review
- **test-runner**: targeted tests and failure diagnosis
- **frontend-reviewer**: UI, accessibility, state, component boundaries
- **backend-reviewer**: APIs, data validation, transactions, error handling
- **performance-reviewer**: slow queries, expensive loops, caching, render waste
