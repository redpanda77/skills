---
name: skill-arguments
description: Reference for skill arguments, variable interpolation, hints, and dynamic context injection. Use when a skill needs to accept user input.
---

# Arguments

Arguments let a skill accept input from the user at invocation time. Declared in frontmatter, referenced in the body.

## Declaration

```yaml
---
name: review-issue
description: Review a GitHub issue and suggest fixes. Use when user asks to "review issue", "check ticket", or "look at bug".
arguments:
  - name: issue_number
    description: The GitHub issue number to review
    required: true
  - name: focus
    description: What aspect to focus on (security, performance, logic)
    required: false
---
```

## Usage in SKILL.md

Arguments are available as named variables in the body:

```markdown
# Review Issue $issue_number

Focus on $focus.

1. Fetch issue $issue_number from GitHub
2. Analyze based on focus: $focus
3. Suggest fixes
```

## Variable Syntax

| Syntax | Meaning | Example |
|--------|---------|---------|
| `$name` | Named argument from frontmatter | `$issue_number` |
| `$0` | Entire user query (raw) | `$0` |
| `$1`, `$2`, ... | Positional arguments | `$1` = first arg |
| `$ARGUMENTS` | All arguments as a single string | `$ARGUMENTS` |

## Environment Variables

Skills can reference environment variables:

```markdown
# Check environment

Run `echo $ENV_VAR` to check the current value.
```

**Note:** Environment variables are read-only from the skill's perspective. The skill cannot set them permanently.

## Dynamic Context Injection

Some platforms support dynamic context injection — pulling in external context at runtime based on the skill's needs.

**Example:** A skill that reviews code might inject:
- The current git diff
- The file tree
- Recent commit messages

This is platform-specific. On Claude Code, the skill is loaded with the current conversation context automatically.

## Best Practices

- **Keep required arguments minimal.** The more required args, the harder the skill is to invoke.
- **Provide defaults in description.** If an arg is optional, explain what happens if omitted.
- **Validate early.** If `$issue_number` is required, check it exists before doing work.
- **Don't leak secrets.** Never pass tokens, keys, or passwords as arguments.

## Common Patterns

### Pass-through to scripts

```markdown
Run the analysis:
```bash
python scripts/analyze.py --issue $issue_number --focus "$focus"
```
```

### Conditional logic based on arguments

```markdown
If $focus is "security":
1. Run security checks
2. Check for secrets

If $focus is "performance":
1. Profile the code
2. Check for N+1 queries
```
