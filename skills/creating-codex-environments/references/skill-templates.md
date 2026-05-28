# Skill Templates

## Folder Structure

```text
my-skill/
  SKILL.md          # Required. Core workflow.
  scripts/          # Optional. Deterministic helpers.
  references/       # Optional. Deep docs, schemas.
  assets/           # Optional. Templates, images.
  agents/
    openai.yaml     # Optional. UI metadata.
```

## Minimal SKILL.md

```markdown
---
name: pr-review
description: Use when reviewing a branch or diff against main for correctness, security, regressions, and missing tests.
---
Role: senior maintainer review.
Inputs: base branch (default main), current diff, touched files.
Steps:
1. Inspect the diff.
2. Map affected execution paths.
3. Identify correctness, security, regression, and test risks.
4. Ignore style-only issues unless they hide a real defect.
5. Return findings by severity.
Output: summary, findings by severity, missing tests, suggested validation.
Do not edit files.
```

## With Scripts

```markdown
---
name: dependency-audit
description: Use when auditing a dependency update or lockfile change.
---
Workflow:
1. Inspect changed dependency files.
2. Read references/audit-checklist.md.
3. Run scripts/changed_packages.sh.
4. Identify production impact and required tests.
5. Do not update dependencies unless explicitly asked.
Output: packages affected, risk level, evidence, recommended validation.
```

## Progressive Disclosure Rules

| Level | File | When Loaded | Content |
|-------|------|-------------|---------|
| 1 | Frontmatter | Always | Name + description under 1024 chars |
| 2 | SKILL.md body | When triggered | Core workflow under 100 lines |
| 3 | References | When needed | Deep docs, schemas, examples |
| 4 | Scripts | When called | Deterministic operations |

## SKILL.md Frontmatter

```yaml
---
name: skill-name              # kebab-case, max 64 chars
  description: What it does. Use when [triggers].
---
```

## Enabling and Disabling

Add to `~/.codex/config.toml`:

```toml
[[skills.config]]
path = "/absolute/path/to/skill/SKILL.md"
enabled = false
```

## Common Mistakes

- Writing skills in `.codex/` instead of `.agents/skills/`.
- Putting long examples in SKILL.md instead of `references/`.
- Missing `description` trigger phrases for auto-invocation.
- Including secrets or time-sensitive data in frontmatter.
