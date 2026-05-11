# Workflow Automation Deep Dive

Workflow Automation skills turn AI from a "task rabbit" into a reliable, methodical worker by forcing strict Standard Operating Procedures (SOPs).

## The Core Mechanism: State and Validation

A true workflow skill doesn't just list steps - it manages task state and implements validation gates.

**Instead of:** "Do A, B, and C"

**Say:**
1. "Do A"
2. "Stop. Evaluate output of A against this checklist"
3. "If A passes, move to B. If A fails, redo A"

This forces Chain of Thought reasoning, breaking complex deliverables into manageable, verifiable chunks.

---

## The Two Master Patterns

### Pattern A: Sequential Orchestration (The Assembly Line)

**Use when:** Process must happen in strict chronological order with dependencies between steps.

**How it works:** Complete Step 1 → store output → use that exact output as input for Step 2.

**Real-World Example (Sprint Planning):**

```
Step 1: Fetch
→ Pull last 5 closed tickets from Jira via MCP

Step 2: Analyze
→ Calculate team's average completion time

Step 3: Draft
→ Look at backlog, propose 5 new tickets fitting that time frame

Step 4: Execute
→ Create those 5 tickets in Jira
```

**The Secret Sauce:** Explicit dependency mapping.

Your SKILL.md must clearly state:
```
In Step 3, you MUST use the exact ID numbers generated in Step 1.
```

### Pattern B: Iterative Refinement (The Editor)

**Use when:** Task requires high quality, polish, or accuracy (writing code, legal docs, complex reports).

**How it works:** Loop through creation → self-critique → correction until standard is met.

**Real-World Example (Code Review):**

```
Step 1: Draft
→ Generate initial Python script

Step 2: Test
→ Run script using bundled validate.py tool

Step 3: Refine Loop
→ If test throws error:
  - Read the error
  - Rewrite broken function
  - Test again

Step 4: Finalize
→ Only present code once tests pass
```

**The Secret Sauce:** Explicit quality criteria.

Tell the AI exactly when to stop:
```
Repeat until validate.py returns exit code 0.
```

---

## Best Practices for Workflow Skills

### 1. Be Dictatorial with Headers

Use aggressive formatting to make steps undeniable:

```md
### Phase 1: Data Gathering
[Instructions...]

🛑 CRITICAL GATE: Do not proceed to Phase 2 until you have collected at least 3 sources.

### Phase 2: Synthesis
[Instructions...]
```

### 2. Include Fallback Logic

AI models panic when things go wrong. Give them escape hatches:

```md
If the API times out on Step 2:
1. Do not apologize to the user
2. Wait 5 seconds
3. Attempt the call one more time
4. If it fails again, ask user if they want to proceed with cached data
```

### 3. Use Code for Hard Checks (Deterministic Validation)

Language models are bad at checking their own work subjectively.

**Don't ask AI to:** "Check the CSV format is correct"

**Instead:** Bundle a validation script:

```python
# scripts/validate_csv.py
import csv
import sys

def validate(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        required = ['id', 'name', 'date']
        if not all(col in reader.fieldnames for col in required):
            print("Missing required columns")
            sys.exit(1)
    print("Valid")
    sys.exit(0)

if __name__ == "__main__":
    validate(sys.argv[1])
```

Then in SKILL.md:
```md
Before finalizing, run:
```bash
python scripts/validate_csv.py {output_file}
```

Only proceed if exit code is 0.
```

**Why this works:** Code is deterministic; AI interpretation is not.

---

## Validation Gate Patterns

### Simple Checklist Gate
```md
### Step 2: Validate
Before proceeding, verify:
- [ ] At least 3 sources collected
- [ ] All dates within last 30 days
- [ ] No duplicate entries
```

### Conditional Gate
```md
### Step 3: Quality Check
Run validation script. If output contains "ERROR":
→ Go back to Step 2 and fix issues
→ Re-run validation
→ Only proceed when validation passes
```

### Timeout Gate
```md
### Step 4: API Call
Attempt API call. If no response in 10 seconds:
1. Log timeout
2. Retry once after 5 second delay
3. If still no response, use cached data and notify user
```

---

## State Management Techniques

### In-Memory State
```md
Track these variables throughout:
- `sources_collected`: Count of valid sources
- `retry_count`: Number of API attempts
- `last_valid_output`: Most recent successful result
```

### File-Based State
```md
After each phase, write state to `temp/state.json`:
{
  "current_phase": 2,
  "completed_steps": ["fetch", "analyze"],
  "outputs": {
    "fetch": [...],
    "analyze": {...}
  }
}
```

### Checkpoint Pattern
```md
After completing Phase 1:
1. Write checkpoint to `temp/checkpoint_1.json`
2. If workflow fails later, can resume from checkpoint
3. Always verify checkpoint exists before starting Phase 2
```

---

## Anti-Patterns to Avoid

❌ **Vague steps:** "Analyze the data"
✅ **Specific steps:** "Calculate average order value from the CSV and store in variable `aov`"

❌ **Implicit dependencies:** "Use the data from earlier"
✅ **Explicit dependencies:** "Use the `ticket_ids` list generated in Step 1"

❌ **Subjective quality checks:** "Make sure it looks good"
✅ **Objective quality checks:** "Verify all JSON keys match schema in `references/schema.json`"

❌ **No failure handling:** "Call the API"
✅ **Failure handling:** "Call the API. If 404: log and skip. If 500: retry once. If 429: wait 60s and retry."

---

## Summary

Workflow automation is **programming with natural language**, where the AI acts as both compiler and execution engine.

**Key ingredients:**
1. State management (track where you are)
2. Validation gates (verify before proceeding)
3. Explicit dependencies (exact inputs/outputs)
4. Deterministic checks (code, not subjective judgment)
5. Fallback logic (escape hatches for failures)
