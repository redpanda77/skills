# Pattern: Iterative Refinement

**Use when:** Output quality improves with iteration.

## Characteristics
- Explicit quality criteria
- Iterative improvement loop
- Validation scripts
- Know when to stop iterating

## Structure

```md
## Workflow: [Name]

### Initial Draft
1. Fetch data / generate initial output
2. Save to temporary location
3. Prepare for review

### Quality Check
1. Run validation: `scripts/check.py`
2. Identify issues against checklist
3. Categorize by severity

### Refinement Loop
1. Address each identified issue
2. Regenerate affected sections
3. Re-validate
4. Repeat until quality threshold met

### Finalization
1. Apply final formatting
2. Generate summary
3. Save final version
4. Cleanup temporary files
```

## Example

```md
## Workflow: Report Generation

### Initial Draft
1. Fetch data via MCP
2. Generate first draft report
3. Save to temporary file

### Quality Check
1. Run validation script: `scripts/check_report.py`
2. Identify issues:
   - Missing sections
   - Inconsistent formatting
   - Data validation errors

### Refinement Loop
1. Address each identified issue
2. Regenerate affected sections
3. Re-validate
4. Repeat until quality threshold met

### Finalization
1. Apply final formatting
2. Generate summary
3. Save final version
```

## Key Techniques

1. **Quality checklist:** Specific criteria to evaluate against
2. **Maximum iterations:** Prevent infinite loops
3. **Delta tracking:** Only regenerate what changed
4. **Progress indicators:** Show improvement between iterations
