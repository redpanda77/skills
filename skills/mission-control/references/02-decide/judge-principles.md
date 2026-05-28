# Principle-Based Judging

The judge evaluates against **principles** — 5-10 project-specific qualitative dimensions that define what "good" means.

## What is a principle

A single, falsifiable statement. Not a category. Not a checklist.

**Good:** "Evidence comes before teaching — every new concept appears in context before formal explanation."

**Bad:** "Code is well-structured." (not falsifiable)

## How many

5-10. Fewer than 5 misses dimensions. More than 10 dilutes focus.

## Categories (prompts, not prescriptions)

| Category | Ask yourself |
|----------|-------------|
| Purpose/Intent | Does it achieve what it claims? |
| Naturalness | Is the output native to its domain? |
| Structure/Contract | Does it follow required form? |
| Evidence/Proof | Is every claim backed by something concrete? |
| Progression | Does it respect what came before and prepare for what's next? |
| Audience Fit | Is it designed for the intended consumer? |

## Scoring

Judge evaluates each principle independently (0.0–1.0). Task passes only when every principle >= threshold.

## Verdict format

```json
{
  "task_id": "T002",
  "verdict": "pass",
  "confidence": 0.82,
  "principle_scores": {
    "communicative_purpose_first": 0.91,
    "evidence_before_explanation": 0.75
  },
  "threshold": 0.70,
  "must_fix": [],
  "should_fix": [],
  "evidence": [],
  "concerns": []
}
```

## Multi-judge

When >10 principles, split into domains. Each domain gets its own judge subagent.

- No overlap: each principle lives in exactly one domain
- Independence: judges run independently
- Selective invocation: run only relevant judges per task
- Aggregation: done-check.sh checks all invoked judges

## Rules

- Judge output is authoritative — no script rewrites it
- No Python script pre-packages context for the judge
- Invoke `write-a-skill` for detailed judge design. Never design judges manually.
