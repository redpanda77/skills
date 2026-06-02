---
name: testing-thinking-frameworks
description: Testing guide for the thinking-frameworks skill. Reference when validating the skill before shipping or after adding new methodologies.
---

# Testing Thinking Frameworks

## Triggering Tests

### Should Trigger

Test these queries to verify the skill loads correctly:

- "Help me analyze why this system is slow"
- "I need to decide between these two architectures"
- "What mental model should I use for this problem?"
- "Apply first principles to this design decision"
- "Use systems thinking to understand this bug"

### Should NOT Trigger

Test these queries to verify the skill does NOT load:

- "What is the weather today?" (simple factual lookup)
- "Write a hello world program" (no analysis needed)
- "Fix this typo" (no structured thinking needed)
- "What is 2+2?" (no framework needed)

## Functional Tests

### Test 1: Route to Five Whys Plus

**Query:** "Help me debug why the API is returning 500 errors"

**Expected:**
- Domain identified as Coding/Debugging
- Problem type identified as Diagnose
- Routed to `references/methodologies/12-five-whys-plus.md`
- Verification checklist applied

### Test 2: Route to First Principles

**Query:** "I need to redesign our auth system from scratch"

**Expected:**
- Domain identified as Architecture
- Problem type identified as Create
- Routed to `references/methodologies/11-first-principles.md`
- Process steps followed

### Test 3: Invoke Grill-Me for Vague Problem

**Query:** "I have a problem with my code"

**Expected:**
- Skill recognizes the problem is vague
- Invokes `grill` before routing
- After grilling, routes to appropriate methodology

### Test 4: Combine Models

**Query:** "We need to decide whether to rewrite our monolith as microservices"

**Expected:**
- Domain identified as Architecture
- Problem type identified as Decide
- Primary model: Reversibility
- Secondary models: Second-Order Thinking, Opportunity Cost
- Combination pattern: Sequential

### Test 5: Fallback for Unknown Domain

**Query:** "Help me think about this philosophical problem"

**Expected:**
- Domain not clearly in table
- Falls back to `first-principles` or `systems-thinking`
- Applies the methodology

## Edge Case Tests

| Scenario | Input | Expected Behavior |
|----------|-------|-------------------|
| Missing domain | "I need help" | Ask user to clarify domain |
| Missing methodology file | Route to `99-nonexistent.md` | Fall back to `socratic` questioning |
| Invalid problem type | "Make this better" | Default to `diagnose` for technical, `decide` for strategic |
| Grill-me unavailable | User denies permission | Proceed directly, ask clarifying questions manually |

## Validation Script

Run the validation script to check all methodology files:

```bash
cd /Users/gonzalocasajus/Documents/GitHub/skills/skills/applying-thinking-frameworks
python3 scripts/validate-methodologies.py
```

Expected: 0 errors, warnings are acceptable for key question counts.

## After Adding a New Methodology

1. Create the methodology file in `references/methodologies/`
2. Update `references/router/domain-problem-matrix.md`
3. Run `python3 scripts/validate-methodologies.py`
4. Test with a query that should route to the new methodology
5. Verify the methodology loads and produces correct output

## Performance Checklist

- [ ] Skill loads on relevant queries (3+ tests)
- [ ] Skill does NOT load on unrelated queries (3+ tests)
- [ ] Core workflow completes successfully
- [ ] Error handling works for common failures
- [ ] Edge cases handled (missing input, vague problem, missing file)
- [ ] No secrets in any file
- [ ] Under line target for scope (SKILL.md < 100 lines)
- [ ] Negative rules included
- [ ] References are one level deep
- [ ] No README.md inside skill folder
- [ ] No time-sensitive data
