---
name: skill-testing
description: Reference for testing skills — triggering tests, functional tests, edge cases, and iteration signals. Use before shipping a skill.
---

# Testing

Verify a skill works before users depend on it.

## Evaluation-Driven Development

Create evaluations BEFORE writing extensive documentation. This ensures the skill solves real problems rather than documenting imagined ones.

1. **Identify gaps:** Run Claude on representative tasks without a skill. Document specific failures.
2. **Create evaluations:** Build three scenarios that test these gaps.
3. **Establish baseline:** Measure Claude's performance without the skill.
4. **Write minimal instructions:** Create just enough content to address the gaps and pass evaluations.
5. **Iterate:** Execute evaluations, compare against baseline, and refine.

**Evaluation structure:**
```json
{
  "skills": ["skill-name"],
  "query": "Extract all text from this PDF file",
  "files": ["test-files/document.pdf"],
  "expected_behavior": [
    "Successfully reads the file",
    "Extracts text from all pages",
    "Saves to output.txt"
  ]
}
```

## Test with All Models

Test your skill with all models you plan to use it with:
- **Claude Haiku** (fast, economical): Does the skill provide enough guidance?
- **Claude Sonnet** (balanced): Is the skill clear and efficient?
- **Claude Opus** (powerful reasoning): Does the skill avoid over-explaining?

What works for Opus might need more detail for Haiku. Aim for instructions that work well with all models.

## Triggering Tests

Goal: The skill loads at the right times.

### Should Trigger

Test 3–5 queries that should activate the skill:

```
- "[Exact phrase from description]"
- "[Paraphrased version of the trigger]"
- "[Related technical term]"
- "[Domain-specific phrase]"
- "[Implied need — user doesn't know the skill name]"
```

### Should NOT Trigger

Test 3–5 queries that should NOT activate the skill:

```
- "[Adjacent but wrong domain]"
- "[Generic request — should use built-in capability]"
- "[Out of scope variant]"
- "[Unrelated topic]"
```

### How to Test

1. Ask the system: `When would you use the [skill name] skill?`
2. The response should quote the description
3. If the quoted description doesn't match your intent, revise the description
4. Test with actual queries and verify the skill loads

## Functional Tests

Goal: The skill produces correct outputs.

### Test Format

```
Test: [Use case name]
Given: [Input conditions]
When: Skill executes
Then: [Expected outcome]
```

### Example

```
Test: Generate unit tests for a simple function
Given: A Python function with one parameter
When: User asks "write tests for this"
Then:
  - Test file created in tests/
  - Tests cover edge cases (empty input, None, large value)
  - Tests use the project's test framework (pytest)
  - No tests are generated for built-in functions
```

### Edge Cases

Test these scenarios:
- **Missing input:** What if the user doesn't provide a required argument?
- **Invalid input:** What if the input is malformed?
- **Empty result:** What if there's nothing to process?
- **MCP failure:** What if the external service is down?
- **Large input:** What if the input exceeds reasonable size?
- **Permission denied:** What if the skill tries to access a restricted file?

## Iteration Signals

After deploying, watch for these signals:

| Issue | Signal | Fix |
|-------|--------|-----|
| **Undertriggering** | Skill doesn't load when it should | Add more trigger phrases, make description more specific |
| **Overtriggering** | Loads for irrelevant queries | Add negative triggers, narrow description, be more specific |
| **Execution issues** | Skill loads but produces inconsistent results | Improve instructions, add error handling, add validation gates |
| **Context bloat** | Slow responses, degraded quality | Move deep docs to references, reduce SKILL.md size, enable fewer skills |
| **Tool failures** | Common errors not handled | Add troubleshooting section, add retry logic, add fallback paths |

## Performance Comparison

Compare with and without the skill:
- Number of tool calls
- Tokens consumed
- Success rate
- User satisfaction (did they need to correct the agent?)

## Checklist Before Shipping

- [ ] Triggers on relevant queries (3+ tests)
- [ ] Does NOT trigger on unrelated queries (3+ tests)
- [ ] Core workflow completes successfully
- [ ] Error handling works for common failures
- [ ] Edge cases handled (missing input, MCP failure, empty result)
- [ ] No secrets in any file
- [ ] Under line target for scope
- [ ] Negative rules included
- [ ] References are one level deep
- [ ] No README.md inside skill folder
- [ ] No time-sensitive data
