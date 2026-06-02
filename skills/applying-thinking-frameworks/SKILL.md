---
name: applying-thinking-frameworks
description: Apply structured thinking methodologies to solve problems, make decisions, and analyze systems. Use when user needs root cause analysis, decision-making frameworks, systems thinking, or strategic analysis. Routes to the right mental model based on domain and problem type. Do NOT use for simple factual lookups or tasks that require no structured analysis.
---

# Thinking Frameworks

Route to the right thinking methodology based on domain and problem type.

## Quick Router

| Domain | Diagnose | Decide | Understand | Create | Evaluate | Predict | Optimize |
|--------|----------|--------|------------|--------|----------|---------|----------|
| **Coding/Debugging** | Five Whys Plus, Scientific Method | Reversibility | Systems Thinking, Feedback Loops | First Principles, TRIZ | Red Team, Steel-manning | Probabilistic, Bayesian | Theory of Constraints |
| **Architecture** | Systems Thinking, Five Whys | Reversibility, Opportunity Cost | Systems Thinking, Leverage Points | First Principles, TRIZ | Lindy Effect, Circle of Competence | Fermi Estimation | Theory of Constraints |
| **Product** | Five Whys Plus, Jobs to Be Done | Reversibility, Regret Minimization | Jobs to Be Done, Cynefin | Effectuation, First Principles | Scientific Method, Pre-mortem | Bayesian, Probabilistic | Theory of Constraints |
| **Strategy** | Systems Thinking, Archetypes | Reversibility, Regret Minimization | Cynefin, Feedback Loops | Effectuation, First Principles | Red Team, Pre-mortem | Second-Order Thinking | Leverage Points |
| **Personal** | Five Whys Plus | Regret Minimization, Reversibility | Circle of Competence, Cynefin | Effectuation, First Principles | Pre-mortem, Steel-manning | Probabilistic | Opportunity Cost |
| **Abstract/Analytical** | Scientific Method, Socratic | Bayesian, Probabilistic | Map-Territory, Systems Thinking | Thought Experiment, First Principles | Steel-manning, Occam's Razor | Fermi Estimation | Via Negativa |
| **Risk/Safety** | Five Whys Plus, Pre-mortem | Reversibility, Margin of Safety | Pre-mortem, Red Team | Inversion, Via Negativa | Red Team, Pre-mortem | Bayesian, Probabilistic | Margin of Safety |
| **Innovation** | Scientific Method, Five Whys | Effectuation, Reversibility | Cynefin, Systems Thinking | First Principles, TRIZ | Red Team, Pre-mortem | Second-Order Thinking | Leverage Points |

## Workflow

1. **Identify the domain** — What area is the problem in? (Coding, Architecture, Product, Strategy, Personal, Abstract, Risk, Innovation)
2. **Identify the problem type** — What do you need to do? (Diagnose, Decide, Understand, Create, Evaluate, Predict, Optimize)
3. **Look up the router** — Find the intersection in the table above.
4. **Check if grilling is needed** — Is the problem vague? Do we need to clarify scope? See `references/grill/when-to-grill.md`.
5. **Check if exploration is needed** — Are there documents to read? See `references/exploration/document-exploration.md`.
6. **Load the methodology** — Read the corresponding `references/methodologies/XX-*.md` file.
7. **Apply the methodology** — Follow the process in the reference file.
8. **Verify** — Use the verification checklist in the methodology file.

## When to Combine Models

Use multiple models when:
- Problem spans multiple types
- Single model leaves blind spots
- Stakes are very high
- Time allows deeper analysis

See `references/router/combination-patterns.md` for patterns (Sequential, Parallel, Nested, Temporal).

## Rules

- Never apply a framework without understanding the problem first.
- Always verify the model fits the situation before applying it.
- If the problem is vague, invoke `grill-me` before routing.
- If a plan exists and needs validation, invoke `grill-with-docs`.
- If analysis stalls for 15+ minutes, consider switching models.
- If the domain or problem type is not in the table, default to `first-principles` or `systems-thinking`.
- If the methodology file is missing, fall back to `socratic` questioning to clarify the problem.

## Error Handling

- Missing domain: Ask the user to clarify which domain the problem belongs to.
- Missing methodology file: Use `socratic` questioning as a universal fallback.
- Invalid problem type: Default to `diagnose` for technical problems, `decide` for strategic problems.
- Grill-me or grill-with-docs unavailable: Proceed with the framework directly, but ask clarifying questions manually.
