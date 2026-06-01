# Audit Plan

For code quality audits, security reviews, or technical debt assessments.

## Key Characteristics

- **Scope-first**: Define what is being audited before starting
- **Evidence-based**: Every finding must have file paths and evidence
- **Severity classification**: Critical, High, Medium, Low
- **Remediation plan**: Every finding must have a remediation path
- **Verification**: Remediation must be verified before sign-off

## Tools and Enforcement

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **Security scanner** | Secrets, API keys, hardcoded tokens, vulnerabilities | Phase 00 — initial audit |
| **TypeScript** | Type coverage, `any` usage, `ts-ignore` count | Phase 00 — type safety audit |
| **Lighthouse** | Accessibility, performance, SEO, best practices | Phase 00 — web app audit |
| **npm audit** | Dependency vulnerabilities, outdated packages | Phase 00 — security audit |
| **Test coverage** | Line coverage, branch coverage, missing tests | Phase 00 — test audit |
| **Biome/ESLint** | Code style, lint violations, import order | Phase 00 — style audit |
| **GitNexus** | Dead code, circular dependencies, god interfaces | Phase 00 — structural audit |
| **React Doctor** | React-specific issues, effect rules, hook rules | Phase 00 — React audit |
| **Bundle analyzer** | Bundle size, duplicate dependencies, tree shaking | Phase 00 — performance audit |
| **Accessibility scanner** | ARIA usage, contrast ratios, keyboard navigation | Phase 00 — a11y audit |
| **Performance profiler** | Render times, memory leaks, re-renders | Phase 00 — perf audit |

### Security Audit Commands

```bash
# Find secrets
rg "api_key|apikey|secret|password|token" app/ --type ts --type tsx | grep -v "\.env"

# Check .env files
cat .env.local 2>/dev/null | grep -E "KEY|SECRET|TOKEN|PASS"

# Check package.json for known vulnerable packages
npm audit

# Check for hardcoded URLs
rg "https?://" app/ --type ts --type tsx | grep -v "localhost\|127.0.0.1"
```

### Type Safety Audit Commands

```bash
# Count any usage
rg ": any" app/ --type ts --type tsx | wc -l

# Count ts-ignore
rg "@ts-ignore" app/ --type ts --type tsx | wc -l

# Count ts-expect-error
rg "@ts-expect-error" app/ --type ts --type tsx | wc -l

# Run type check
npx tsc --noEmit

# Check for missing types
rg "as any" app/ --type ts --type tsx | wc -l
```

### Performance Audit Commands

```bash
# Run build and check bundle size
npm run build

# Check for large files
find app/ -name "*.tsx" -size +50k

# Check for unnecessary re-renders
# Use React DevTools Profiler

# Check for memory leaks
# Use Chrome DevTools Memory tab

# Check Core Web Vitals
# Run Lighthouse in Chrome DevTools
```

### Accessibility Audit Commands

```bash
# Find missing alt text
rg "<img" app/ --type tsx | grep -v "alt=" | wc -l

# Find missing ARIA labels
rg "role=" app/ --type tsx | wc -l
rg "aria-" app/ --type tsx | wc -l

# Check form labels
rg "<input" app/ --type tsx | grep -v "label" | wc -l

# Check button accessibility
rg "<button" app/ --type tsx | grep -v "aria-label" | wc -l

# Run Lighthouse accessibility audit
npx lighthouse --only-categories=accessibility
```

### Structural Audit Commands

```bash
# Find dead code
rg "TODO|FIXME|HACK|XXX" app/ --type ts --type tsx | wc -l

# Find commented-out code
rg "^\s*//.*[a-zA-Z]" app/ --type ts --type tsx | wc -l

# Find unused exports
# Use TypeScript compiler or ts-prune
npx ts-prune

# Find large files (god objects)
find app/ -name "*.tsx" -size +50k -exec wc -l {} \;

# Find files with too many imports
rg "^import" app/ --type tsx | sort | uniq -c | sort -rn | head -20

# Check for duplicate code
# Use jscpd or similar
npx jscpd app/
```

### Severity Classification

| Severity | Definition | Examples |
|---|---|---|
| **Critical** | Will cause production failure, data loss, or security breach | Circular dependencies breaking builds, secrets in code, SQL injection |
| **High** | Will cause significant user impact or technical debt | God interfaces (160+ methods), missing error handling, no tests |
| **Medium** | Will cause minor issues or gradual degradation | Dead code, TODOs, naming inconsistencies, missing documentation |
| **Low** | Cosmetic or minor inconvenience | Package name stale, outdated comments, minor formatting issues |

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
