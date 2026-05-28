---
name: skill-subagents
description: Reference for agent integration, context fork, skill preload, and path restrictions in subagents. Use when a skill delegates work to other agents.
---

# Subagents

Skills can delegate work to subagents — isolated agent instances that run with their own context, skills, and permissions.

## When to Use Subagents

- **Parallel work:** Multiple independent tasks that can run simultaneously
- **Isolation:** Dangerous or untrusted work that should not affect the main context
- **Specialization:** A task that needs a different skill set or model
- **Resource limits:** Long-running work that might exhaust the main context window

## Context Fork

Run a subagent in an isolated copy of the repository.

```yaml
# In SKILL.md or subagent frontmatter
context: fork
```

**What it does:**
- Creates a temporary git worktree
- The subagent works in isolation from the main session
- Changes are only applied back if explicitly requested

**When to use:**
- Code review (read-only analysis)
- Experimental changes (try something, discard if it fails)
- Dangerous operations (destructive changes that need validation)

**When NOT to use:**
- Simple, sequential tasks (overhead not worth it)
- Tasks that need the main session's live state

## Skill Preload

Preload skills into a subagent so it can use them.

```yaml
---
name: parent-skill
description: ...
---

## Step 3: Delegate Analysis

Launch a subagent with the security-review skill preloaded:
```

Or in the subagent's own frontmatter:
```yaml
---
name: security-reviewer
description: ...
skills:
  - security-audit
  - code-quality
---
```

**Why preload:** Subagents don't inherit the parent agent's skills by default. Preload what the subagent needs.

## Paths

Restrict which files a subagent can access.

```yaml
---
name: api-reviewer
description: ...
paths:
  - src/api/
  - tests/api/
---
```

**Why restrict:** Reduces context window usage, prevents accidental changes to unrelated files, improves security.

## Subagent Frontmatter

Subagents can have their own frontmatter with these fields:

```yaml
---
name: subagent-task
description: Specific task for this subagent
context: fork          # or none
skills:
  - skill-a
  - skill-b
paths:
  - src/
  - docs/
allowed-tools:
  - Read
  - Bash
---
```

## Delegation Patterns

### Parallel Research

Launch multiple subagents simultaneously, each with a different focus:

```markdown
## Step 2: Research

Launch 3 subagents in parallel:
1. Agent with `security-review` skill — check for vulnerabilities
2. Agent with `performance` skill — check for bottlenecks
3. Agent with `accessibility` skill — check a11y issues

Wait for all results, then synthesize.
```

### Review-Implement-Test

```markdown
## Step 1: Review
Subagent with `code-reviewer` skill reviews the PR.

## Step 2: Implement
If review finds issues, subagent with `refactor` skill fixes them.

## Step 3: Test
Subagent with `test-runner` skill validates the changes.
```

## Best Practices

- **Keep subagents focused.** A subagent should have one clear task. Don't give it a 10-step workflow.
- **Preload only necessary skills.** Each skill consumes context window.
- **Use paths aggressively.** Restrict file access to only what's needed.
- **Document the delegation.** The user should understand why work is being handed off.
- **Handle subagent failures.** If a subagent fails, the parent skill should decide whether to retry, skip, or escalate.
