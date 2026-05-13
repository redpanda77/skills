# Pattern: Domain-Specific Intelligence

**Use when:** Your skill adds specialized knowledge beyond tool access.

## Characteristics
- Domain expertise embedded in logic
- Compliance/procedure before action
- Comprehensive documentation
- Clear governance rules

## Structure

```md
## Workflow: [Name] with [Domain] Compliance

### Pre-Action (Domain Checks)
1. Fetch details via MCP
2. Apply domain rules:
   - Check [rule 1]
   - Verify [rule 2]
   - Assess [metric]
3. Document decision rationale

### Processing
IF [domain checks] passed:
  - Call MCP tool with approved parameters
  - Apply monitoring/controls
  - Execute action
ELSE:
  - Flag for review
  - Create exception case
  - Escalate if needed

### Audit Trail
- Log all checks performed
- Record processing decisions
- Generate compliance report
- Store for audit purposes
```

## Example

```md
## Workflow: Payment Processing with Compliance

### Before Processing (Compliance Check)
1. Fetch transaction details via MCP
2. Apply compliance rules:
   - Check sanctions lists
   - Verify jurisdiction allowances
   - Assess risk level
3. Document compliance decision

### Processing
IF compliance passed:
  - Call payment processing MCP tool
  - Apply appropriate fraud checks
  - Process transaction
ELSE:
  - Flag for review
  - Create compliance case
  - Notify compliance team

### Audit Trail
- Log all compliance checks
- Record processing decisions
- Generate audit report
```

## Key Techniques

1. **Rule engine:** Structured checks with clear pass/fail criteria
2. **Documentation:** Every decision recorded with rationale
3. **Human-in-the-loop:** Escalation paths for edge cases
4. **Auditability:** Complete trace of all actions and checks
