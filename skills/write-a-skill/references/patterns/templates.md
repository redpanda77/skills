---
name: skill-template-pattern
description: Template pattern for skill output formatting. Use when the skill must produce output in a consistent, repeatable structure.
---

# Template Pattern

Provide templates for output format. Match the level of strictness to your needs.

## Strict Requirements

For API responses, data formats, or any output where structure must be exact:

```markdown
## Report structure

ALWAYS use this exact template structure:

```markdown
# [Analysis Title]

## Executive summary
[One-paragraph overview of key findings]

## Key findings
- Finding 1 with supporting data
- Finding 2 with supporting data
- Finding 3 with supporting data

## Recommendations
1. Specific actionable recommendation
2. Specific actionable recommendation
```
```

## Flexible Guidance

When adaptation is useful:

```markdown
## Report structure

Here is a sensible default format, but use your best judgment based on the analysis:

```markdown
# [Analysis Title]

## Executive summary
[Overview]

## Key findings
[Adapt sections based on what you discover]

## Recommendations
[Tailor to the specific context]
```

Adjust sections as needed for the specific analysis type.
```

## When to Use

- **Strict:** Data formats, API responses, generated files, structured reports
- **Flexible:** Analysis outputs, summaries, recommendations, creative writing

## Key Techniques

1. **Provide the template first** — Show the structure before the instructions
2. **Use placeholders** — `[Analysis Title]` tells the agent what goes there
3. **Document deviations** — If the agent can adapt, say so explicitly
4. **Include examples** — Pair the template with a concrete example
