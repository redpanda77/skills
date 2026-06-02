---
name: combination-patterns
description: Patterns for combining multiple thinking models when a single model is insufficient. Reference when the problem is complex or high-stakes.
---

# Model Combination Patterns

## When to Combine Models

Use multiple models when:
- Problem spans multiple types
- Single model leaves blind spots
- Stakes are very high
- Time allows deeper analysis

## Combination Patterns

### Sequential
Use Model A to narrow the problem, then Model B to decide.

| Situation | Sequence | Example |
|-----------|----------|---------|
| High-stakes decision | Reversibility → Pre-mortem → Opportunity Cost | Check if reversible, imagine failure, then weigh trade-offs |
| Innovation under constraints | First Principles → TRIZ → Effectuation | Strip to fundamentals, resolve contradictions, use existing means |
| Career decision | Five Whys (past) → Circle of Competence (present) → Regret Minimization (future) | Diagnose, assess, project |

### Parallel
Use Model A and Model B independently, then compare results.

| Situation | Models | Example |
|-----------|--------|---------|
| Validating strategy | Red Team + Steel-manning + Second-Order | Attack, defend, and forecast simultaneously |
| Evaluating a proposal | Pre-mortem + Opportunity Cost + Lindy Effect | Check failure modes, trade-offs, and durability |

### Nested
Use Model A at macro level, Model B at micro level.

| Situation | Models | Example |
|-----------|--------|---------|
| System diagnosis | Cynefin (macro) → Theory of Constraints (meso) → OODA (micro) | Classify domain, find bottleneck, act rapidly |
| Architecture decision | Systems Thinking (macro) → First Principles (micro) | Understand interconnections, then challenge assumptions |

### Temporal
Use different models for different time horizons.

| Situation | Models | Example |
|-----------|--------|---------|
| Long-term planning | Cynefin (now) → Second-Order (near) → Regret Minimization (far) | Classify current state, predict consequences, project to future self |

### Adversarial
Use models that deliberately contradict each other.

| Situation | Models | Example |
|-----------|--------|---------|
| Stress-testing a plan | Red Team + Pre-mortem + Steel-manning | Attack, imagine failure, and argue the strongest opposing view |

## Combination Template

```markdown
# Model Combination: [Problem]

## Problem
[Description]

## Selected Models
| Model | Role | Why |
|-------|------|-----|
| [Model A] | [Narrow/Decide/Attack/etc.] | [Reason] |
| [Model B] | [Narrow/Decide/Attack/etc.] | [Reason] |

## Pattern
[Sequential/Parallel/Nested/Temporal/Adversarial]

## Application
1. [Apply Model A]
2. [Apply Model B]
3. [Synthesize results]

## Verification
- [ ] Each model was applied independently
- [ ] Results were synthesized, not averaged
- [ ] Conflicts between models were resolved explicitly
- [ ] Final recommendation addresses all problem dimensions
```
