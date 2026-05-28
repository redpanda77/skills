---
name: skill-examples-pattern
description: Examples pattern for showing input/output pairs. Use when output quality depends on seeing concrete examples.
---

# Examples Pattern

For skills where output quality depends on seeing examples, provide input/output pairs just like in regular prompting.

## Structure

```markdown
## [Output Type] Format

Generate [output type] following these examples:

**Example 1:**
Input: [User input or scenario]
Output:
```
[Exact expected output]
```

**Example 2:**
Input: [Different scenario]
Output:
```
[Exact expected output]
```

**Example 3:**
Input: [Edge case scenario]
Output:
```
[Exact expected output]
```

Follow this style: [style description with specific rules].
```

## When to Use

- Output format is nuanced (commit messages, PR descriptions, documentation)
- Style matters more than structure (tone, terminology, level of detail)
- Edge cases are common (error messages, fallback outputs)
- The agent needs to understand the "voice" of the output

## Key Techniques

1. **Provide 3–5 examples** — Cover common, edge, and complex cases
2. **Show the full output** — Don't truncate; the agent needs to see the complete format
3. **Label the input clearly** — The agent should know what triggered each output
4. **Document the style rules** — After examples, explain the pattern the agent should follow
5. **Include negative examples** — Show what NOT to do if common mistakes are predictable

## Anti-Patterns

- **Too few examples** — One example is not enough for the agent to infer the pattern
- **Too many examples** — More than 5 examples can be overwhelming; move to a reference file
- **Inconsistent examples** — Examples that contradict each other confuse the agent
- **Abstract examples** — "Example 1: [some input]" without concrete content is useless
