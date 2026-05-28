---
name: skill-feedback-loops-pattern
description: Feedback loops pattern for quality-critical skills. Use when output must meet a standard before proceeding.
---

# Feedback Loops Pattern

Run validator → fix errors → repeat. This pattern greatly improves output quality.

## Structure

```markdown
## [Workflow Name]

1. [Generate draft / do work]
2. **Validate:** [Run validation]
3. If validation fails:
   - Note each issue with specific reference
   - Fix the issue
   - Re-validate
4. **Only proceed when validation passes**
5. [Finalize]
```

## When to Use

- Output quality is critical (code, legal docs, complex reports)
- Errors are costly (deployments, data transformations, financial calculations)
- The task is open-ended and the agent can make mistakes
- Consistency matters across multiple outputs

## Key Techniques

1. **Validation is deterministic** — Use a script when possible, not subjective judgment
2. **Error messages are specific** — "Field 'signature_date' not found. Available fields: customer_name, order_total" helps the agent fix the issue
3. **Maximum iterations** — Prevent infinite loops: "Repeat up to 3 times, then ask the user"
4. **Validate early, not just at the end** — Catch errors before they compound
5. **Create verifiable intermediate outputs** — For batch operations, create a plan file, validate it, then execute

## Example: Plan-Validate-Execute

For complex, destructive operations, use an intermediate plan file:

```markdown
## Batch update workflow

1. **Analyze:** Run `python scripts/analyze.py` to identify changes
2. **Plan:** Create `changes.json` with the exact modifications
3. **Validate:** Run `python scripts/validate_plan.py changes.json`
   - If errors: fix `changes.json` and re-validate
   - Only proceed when validation passes
4. **Execute:** Run `python scripts/apply_changes.py changes.json`
5. **Verify:** Run `python scripts/verify.py` to confirm changes
```

## Example: Content Review Loop

```markdown
## Content review process

1. Draft content following the guidelines in STYLE_GUIDE.md
2. Review against the checklist:
   - Check terminology consistency
   - Verify examples follow the standard format
   - Confirm all required sections are present
3. If issues found:
   - Note each issue with specific section reference
   - Revise the content
   - Review the checklist again
4. Only proceed when all requirements are met
5. Finalize and save
```

## Anti-Patterns

- **Subjective validation** — "Make sure it looks good" is not a validation step
- **Validation at the end only** — Catching errors after all work is done wastes effort
- **No maximum iterations** — The agent can loop forever if not bounded
- **Vague error messages** — "Validation failed" doesn't help the agent fix the issue
