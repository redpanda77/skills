# Audit Plan

For code quality audits, security reviews, or technical debt assessments.

## Key Characteristics

- **Scope-first**: Define what is being audited before starting
- **Evidence-based**: Every finding must have file paths and evidence
- **Severity classification**: Critical, High, Medium, Low
- **Remediation plan**: Every finding must have a remediation path
- **Verification**: Remediation must be verified before sign-off

## Directory Structure

```
docs/plans/P{NN}-<name>/
├── README.md (or index.md)
├── goal.md
├── methodology.md
├── P{NN}-AUDIT.md              # Full audit findings
├── P{NN}-FINDINGS.md           # Deep audit findings
├── P{NN}-REMEDIATION.md        # Remediation plan
├── P{NN}-DEVIATIONS.md
└── P{NN}-PHASED-APPROACH.md
```

## Goal.md Emphasis

Audit goal.md files must emphasize:

- **Scope boundaries**: What is being audited and what is not
- **Severity classification**: Critical, High, Medium, Low
- **Evidence requirements**: Every finding must have file paths and evidence
- **Remediation path**: Every finding must have a remediation plan
- **Verification**: Remediation must be verified before sign-off

## Audit Structure

```markdown
## Audit Findings

### Critical (Must Fix)

1. **Finding name** — Description with file paths and evidence
   - Severity: Critical
   - Impact: What breaks if not fixed
   - Remediation: How to fix
   - Owner: Which KO or team

### High (Should Fix)

### Medium (Nice to Fix)

### Low (Deferred)
```

## Validation

Audit plans must validate:

- Every finding has a remediation path
- Every remediation has been verified
- `npm run build` passes after remediation
- `npm run test` passes after remediation
- `npm run lint` passes after remediation
- Security scans pass (if applicable)
- Performance benchmarks pass (if applicable)

## Rules

- Scope must be defined before the audit starts
- Every finding must have evidence (file paths, code snippets, screenshots)
- Every finding must have a severity classification
- Every finding must have a remediation path
- Remediation must be verified before sign-off
- Findings must be tracked until remediation is complete
