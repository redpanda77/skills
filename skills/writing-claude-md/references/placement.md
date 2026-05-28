---
name: claude-md-placement
description: Root vs subdirectory placement checklist for CLAUDE.md rules. Use when deciding where a rule belongs — root, subdirectory, skill, agent, or local file.
---

# Root vs Subdirectory Placement Checklist

## Put in Root AGENTS.md / Root CLAUDE.md Only If

- The rule applies to the entire repository.
- Every developer and every agent needs it.
- It is stable across most tasks.
- It affects architecture, safety, build, test, release, or repo-wide conventions.
- Violating it would be costly anywhere in the repo.

## Good Root-Level Content

- Project purpose
- Repo architecture overview
- Package manager
- Build command
- Test command
- Lint command
- Formatting command
- Branch / PR conventions
- Global naming conventions
- Security constraints
- "Never do this" rules
- Cross-cutting dependency rules

## Do Not Put in Root If

- The rule applies only to one package.
- The rule applies only to one framework.
- The rule applies only to tests.
- The rule applies only to generated code.
- The rule applies only during deployment.
- The rule is a long tutorial.
- The rule is useful only for rare tasks.
- The rule is already obvious from nearby files.
- The rule changes frequently.

## Put in Subdirectory CLAUDE.md or Path-Scoped Rules If

- The instruction only matters inside that subtree.
- The repo is a monorepo.
- Different packages have different conventions.
- Frontend and backend use different patterns.
- Tests have their own helpers and fixtures.
- API routes have their own validation/error conventions.
- Database migrations have special safety rules.
- Generated files have special edit restrictions.

## Path-Scoped Rules

Claude Code supports `.claude/rules/` files with `paths` frontmatter so rules only load when Claude works with matching files.

```yaml
---
paths:
  - "src/api/**/*.ts"
---
# API rules
- Validate all external input at the boundary.
- Use the standard error response shape.
- Add or update endpoint tests for behavior changes.
```

### Use `.claude/rules/` When

- The rule is passive guidance.
- The rule is file-path-specific.
- The rule should load only when matching files are touched.
- The rule is still project documentation, not an executable workflow.

### Use a Skill When

- The guidance is task-specific.
- The workflow should load on demand.
- The instruction is long.
- The user or Claude should invoke it only when relevant.
- The workflow has steps, arguments, templates, or scripts.

Claude's docs explicitly recommend skills for task-specific instructions that do not need to stay in context all the time.

### Use an Agent When

- The behavior is a specialized role.
- The work should happen in a separate context window.
- The agent needs a constrained toolset.
- The agent should preload specific skills.
- The agent has its own review, debugging, research, or planning behavior.

Subagents are Markdown files with YAML frontmatter and a body system prompt; they can also preload skills into their context with the `skills` field.

## What Goes in an Agent File

An agent file (`.claude/agents/<name>.md`) defines a **specialized worker** with its own behavior, toolset, and context. It is not a catch-all for complex rules.

### Put in an Agent File

- **Specialized role definition** — "You are a security reviewer. Focus on injection, auth, and secrets."
- **Constrained toolset** — `allowed-tools: [Read, Bash]` only
- **Preloaded skills** — `skills: [security-audit, code-quality]`
- **Context fork** — `context: fork` for isolated work
- **Path restrictions** — `paths: [src/api/]` so the agent only sees relevant files
- **Review behavior** — specific checklists, quality gates, pass/fail criteria
- **Debugging behavior** — systematic troubleshooting steps for a domain
- **Research behavior** — how to gather sources, evaluate claims, cite evidence
- **Planning behavior** — how to break down tasks, estimate, sequence work

### Do NOT Put in an Agent File

- **General repo rules** — those belong in `AGENTS.md` or `CLAUDE.md`
- **File-path-specific guidance** — use `.claude/rules/*.md` instead
- **Repeatable workflows** — use skills under `.claude/skills/` instead
- **Personal preferences** — use `CLAUDE.local.md` instead
- **Commands that change repo state** — agents should review/plan, not execute irreversible actions
- **Long tutorials** — agents need concise instructions, not explanations

### Example Agent File

```yaml
---
name: security-reviewer
context: fork
paths:
  - src/api/
  - src/auth/
allowed-tools:
  - Read
  - Bash
skills:
  - security-audit
---

## Security Review

1. Check all input validation points for injection risks
2. Verify auth middleware is applied to every route
3. Search for hardcoded secrets or tokens
4. Run `scripts/security-scan.sh`
5. Report findings as a checklist with severity

## Output Format

- **CRITICAL:** Must fix before merge
- **WARNING:** Should fix in this PR
- **INFO:** Note for future
```

## Decision Tree

- Does this apply to every task in the repo?
  - **Yes** → root AGENTS.md / CLAUDE.md
  - **No** → continue
- Does this apply to a specific path or file type?
  - **Yes** → `.claude/rules/*.md` with paths
  - **No** → continue
- Is this a repeatable workflow?
  - **Yes** → skill
  - **No** → continue
- Is this a specialized role or worker?
  - **Yes** → `.claude/agents/<name>.md`
  - **No** → keep it out of always-loaded context
- Is this personal and not team-wide?
  - **Yes** → `CLAUDE.local.md` or user-level memory
  - **No** → project-shared file

## Core Principle

The root file should explain the repo. Subdirectory rules should explain local conventions. Skills should teach repeatable workflows. Agents should define specialized workers. Anything else is probably unnecessary context.
