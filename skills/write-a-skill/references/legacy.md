---
name: skill-legacy
description: Reference for deprecated commands and migration notes. Use when updating old skills or converting legacy prompts to skill format.
---

# Legacy Commands

Historical ways of adding capabilities to Claude. Prefer the skill format for all new work.

## Deprecated Formats

### Custom Prompts (Pre-Skills)

Before skills, users injected custom prompts via system instructions or user messages.

- **Problem:** Not version controlled, not composable, not portable
- **Migration:** Extract the prompt into a SKILL.md with proper frontmatter

### Slash Commands (Platform-Specific)

Some platforms supported `/command` syntax for custom behavior.

- **Problem:** Platform-specific, not portable, no structured metadata
- **Migration:** Convert to a skill with `name: command-name` and a clear description

### Hardcoded System Prompts

Embedding instructions directly in application code.

- **Problem:** Requires code changes to update, not user-configurable
- **Migration:** Move to a skill file that can be loaded dynamically

## Migration Guide

### From Custom Prompt

**Before:**
```
System prompt: "You are a helpful coding assistant. When reviewing code,
always check for security issues, performance problems, and style violations."
```

**After:**
```yaml
---
name: code-reviewer
description: Reviews code for security, performance, and style issues.
  Use when user asks for "code review", "check this", or "review PR".
---

## Step 1: Security
Check for:
- SQL injection
- XSS vulnerabilities
- Hardcoded secrets

## Step 2: Performance
Check for:
- N+1 queries
- Unnecessary loops
- Memory leaks

## Step 3: Style
Check for:
- Consistency with project conventions
- Type safety
- Error handling
```

### From Slash Command

**Before:**
```
/command: /deploy
Behavior: "Deploy the current branch to staging"
```

**After:**
```yaml
---
name: deploy-to-staging
description: Deploys the current branch to staging environment.
  Use when user says "deploy to staging", "ship to staging", or "stage this branch".
---

## Step 1: Verify
- Check current branch
- Verify no uncommitted changes
- Confirm staging is healthy

## Step 2: Deploy
```bash
git push origin $(git branch --show-current):staging
```

## Step 3: Verify Deployment
- Check staging URL
- Run smoke tests
```

## Why Skills Over Legacy

| Feature | Legacy | Skills |
|---------|--------|--------|
| Version control | ❌ | ✅ |
| Composable | ❌ | ✅ |
| Portable | ❌ | ✅ |
| Auto-trigger | ❌ | ✅ |
| Explicit scope | ❌ | ✅ |
| User-configurable | ❌ | ✅ |
| Structured metadata | ❌ | ✅ |

## Updating Old Skills

If a skill was written for an older platform version:

1. Check for deprecated frontmatter fields
2. Verify tool names match current platform
3. Update references to current file paths
4. Test triggering on current platform
5. Consider adding `disable-model-invocation` if the skill was previously manual-only
