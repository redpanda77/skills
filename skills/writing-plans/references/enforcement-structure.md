# Enforcement Structure

Enforcement documents establish the rules that must be followed throughout a plan and beyond. They are the guardrails that prevent drift.

## Types of Enforcement Documents

| Document | Purpose | When to Write |
|---|---|---|
| `methodology-enforcement.md` | Execution protocol rules | Every plan |
| `tool-enforcement.md` | Tool-specific rules (e.g., GitNexus, Biome, lint) | When tools are used |
| `style-enforcement.md` | Style and formatting rules | When style is relevant |
| `boundary-enforcement.md` | Import boundary and architectural rules | When boundaries are enforced |

## Structure

```markdown
# P{NN} <Tool> Enforcement

## Mandatory Rules

1. **Rule name** — Description and consequence of violation
2. **Rule name** — Description and consequence of violation

## Tool Reference

| Tool | Command | When to Use |
|------|---------|-------------|
| `tool-name` | `command` | Description |

## Consequences

| Violation | Consequence |
|---|---|
| Rule name | What happens when broken |

## Verification

How to verify the rules are being followed.

```bash
# Example verification command
```

## Rules

- Every enforcement document must be linked from the plan index
- Enforcement rules must be verifiable, not aspirational
- Enforcement documents must define consequences for violations
- Enforcement documents must define verification commands
