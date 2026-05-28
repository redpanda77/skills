---
name: skill-design-pattern
description: Design interview for determining skill type, scope, and information architecture before scaffolding. Use when user wants to create a skill and the type or content structure is not obvious.
---

# Skill Design Interview

Run this interview before scaffolding any skill. It determines what type of skill is needed, what information it must contain, and how to structure it for the agent.

## When to Use

Always. Before writing a single line of SKILL.md, run the design interview. The output is a design decision that prevents the most common skill failure: building the wrong thing with the right packaging.

## The Interview

Ask 6-8 questions. Use `AskUserQuestion` for each. Single-choice for architecture/type decisions. Multi-select for features. Always include a free-text fallback as the last option.

### 1. What is the agent's primary job when this skill is loaded?

Options:
- Execute a procedure (step-by-step workflow)
- Make a decision (choose between options, evaluate trade-offs)
- Avoid a mistake (prevent common errors, apply guardrails)
- Look up facts (find reference information, schemas, rules)
- Understand a system (build a mental model for reasoning)
- Fix a problem (diagnose and remediate)

### 2. What does the agent currently get wrong about this topic?

The most important question. What mistakes does the agent make when this skill is NOT loaded? These become the negative rules and critical guardrails.

- What wrong assumptions does it make?
- What common patterns does it apply that don't fit here?
- What does it omit or forget?

### 3. What is the minimum information the agent needs to be correct 80% of the time?

Forces the progressive disclosure decision. Not "everything we know" but "what's critical for the first 100 lines."

- What are the 3-5 most important things?
- What can be moved to references?
- What does the agent already know from the codebase or tooling?

### 4. What are the 3 most common scenarios where this skill should be consulted?

Determines the triggering description and test cases. If you can't name 3 scenarios, the skill is too vague.

### 5. How does the agent know when it has succeeded?

Success criteria for the skill itself. What does "done" look like?

- Correct output?
- Correct decision?
- Correctly avoided mistake?
- Correctly followed convention?

### 6. What is the one thing most likely to make this skill fail?

Risk assessment. Common failures:
- Too much information (agent ignores it)
- Too little information (agent guesses wrong)
- Wrong structure (reference info in SKILL.md, workflow in references)
- Wrong trigger (never loads or loads on everything)

### 7. What is explicitly out of scope?

What should this skill NOT do? Define boundaries to prevent bloat.

## Determine Skill Type

Based on the answers, select the primary type:

| Primary Answer to Q1 | Type | Pattern |
|------|------|---------|
| Execute a procedure | **Workflow** | Sequential, Iterative, Conditional, Feedback Loops |
| Make a decision | **Decision Framework** | Context-Aware, Conditional Workflow |
| Avoid a mistake | **Guardrails** | Domain-Specific (rule-focused) |
| Look up facts | **Reference Domain** | Reference structure (see below) |
| Understand a system | **Principles of Operation** | Conceptual structure (see below) |
| Fix a problem | **Troubleshooting** | Diagnostic structure (see below) |

Skills can be hybrid. A Principles of Operation skill might include Decision Framework rules. A Workflow skill might include Reference Domain lookups. But the primary type determines the scaffolding.

## Map to Progressive Disclosure

After determining type, map content to the three levels:

### Level 1: Frontmatter
- What 2-3 trigger phrases load this skill? (from Q4)
- What is the one-line description of what the agent does? (from Q1)

### Level 2: SKILL.md
- What are the critical rules the agent must not break? (from Q2)
- What is the core workflow or decision tree? (from Q1)
- What are the success criteria? (from Q5)

### Level 3: References
- What detailed schemas, examples, or deep docs are needed? (from Q3)
- What are the edge cases and exceptions? (from Q6)
- What background information supports the core workflow? (from Q3)

## Output: Skill Design Document

After the interview, write a brief design document:

```markdown
## Skill Design: <name>

### Type: <primary type> [<hybrid if applicable>]

### Agent's Job: <answer to Q1>

### Critical Negative Rules (from Q2):
- NEVER <rule 1>
- NEVER <rule 2>

### Progressive Disclosure Map:
- **Frontmatter:** <triggers>
- **SKILL.md:** <core content>
- **References:** <deep content>

### Scenarios (from Q4):
1. <scenario 1>
2. <scenario 2>
3. <scenario 3>

### Success Criteria (from Q5):
- <criteria>

### Out of Scope (from Q7):
- <boundary>

### Risks (from Q6):
- <risk>
```

Only proceed to scaffolding after the user confirms this design.

## Reference Structure: Non-Workflow Skills

For skills that are not primarily workflows, use these reference structures.

### Decision Framework

```markdown
### Decision Tree

1. Assess the situation:
   - [Condition A]? → <criteria and outcome>
   - [Condition B]? → <criteria and outcome>
   - [Condition C]? → <criteria and outcome>
   - Else: <default outcome>

2. Evaluate trade-offs:
   - [Option X]: <pros, cons, when to choose>
   - [Option Y]: <pros, cons, when to choose>

3. Document the decision:
   - Why this was chosen
   - What was considered
   - Override option if applicable
```

### Principles of Operation

```markdown
### System Overview
What it does, what it doesn't do, key constraints.

### Core Abstractions
The fundamental entities and how they relate.

### Interaction Patterns
How components communicate, common sequences.

### Design Principles
Trade-offs, invariants, what to preserve vs. what can change.

### Common Pitfalls
Mistakes that violate the architecture.
```

### Reference Domain

```markdown
### Global Rules
Rules that always apply.

### Context-Specific Rules
Rules that apply when [condition].

### Exceptions
Unless [condition], then [different rule].

### Examples
Good vs. bad examples for each rule.
```

### Troubleshooting

```markdown
### Symptom Map
- [Symptom A] → [Likely cause] → [Diagnostic step]
- [Symptom B] → [Likely cause] → [Diagnostic step]

### Diagnostic Flow
1. Check [thing]
2. If [result], check [next thing]
3. If [other result], check [other thing]

### Remediation
- [Cause A]: [Fix]
- [Cause B]: [Fix]
```
