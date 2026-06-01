# Feature Plan

For adding new functionality, APIs, or user-facing features.

## Key Characteristics

- **Requirements first**: Define acceptance criteria before implementation
- **API contract before implementation**: Types and interfaces before logic
- **User-facing acceptance criteria**: What the user must see/experience
- **Rollout strategy**: How the feature is deployed and monitored

## Tools and Enforcement

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **Requirements analysis** | User stories, acceptance criteria, edge cases | Phase 00 — before design |
| **Design system** | Component patterns, token usage, accessibility | Phase 01 — before implementation |
| **API contract** | Type definitions, request/response shapes, error handling | Phase 01 — before backend logic |
| **Test framework** | Unit tests, integration tests, E2E tests | Phase 04 — after implementation |
| **Feature flags** | Gradual rollout, A/B testing, kill switches | Phase 05 — rollout |
| **Monitoring** | Error tracking, performance metrics, user analytics | Phase 05 — after rollout |
| **GitNexus** | Impact analysis, dependency mapping, API consumers | Phase 01 — before API changes |
| **TypeScript** | Type checking, API contract validation | After every phase |
| **Lighthouse** | Accessibility, performance, SEO | Phase 04 — before release |
| **Storybook** | Component documentation, visual testing | Phase 01 — design system |
| **Playwright/Cypress** | E2E tests, user flow validation | Phase 04 — testing |

### Requirements Analysis

The audit must document:

| Category | What to Document | Example |
|---|---|---|
| **User stories** | Who, what, why | "As a user, I want to switch themes so that I can use the app at night" |
| **Acceptance criteria** | Given/when/then | "Given the user is on Settings, when they tap Dark Mode, then the app switches to dark" |
| **Edge cases** | Unusual conditions | "System theme changes while app is open" |
| **Non-goals** | Explicitly out of scope | "No new theme families (warm, cool, high-contrast)" |
| **Dependencies** | Other features or systems | "Requires next-themes 0.4.x" |
| **Performance** | Load time, bundle size | "Theme switch must be <100ms" |
| **Accessibility** | Screen reader, keyboard, contrast | "Theme switch must work with screen reader" |
| **Mobile constraints** | Touch targets, safe areas, orientation | "Settings toggle must be 44pt minimum" |

### API Contract Audit

```bash
# Find existing API patterns
ls -la app/api/

# Check existing type definitions
rg "export interface" app/ --type ts | head -20

# Check existing request/response patterns
rg "export async function" app/api/ --type ts | head -20

# Check error handling patterns
rg "try {" app/api/ --type ts | wc -l
rg "catch" app/api/ --type ts | wc -l

# Check API consumers
rg "fetch\(" app/ --type tsx | wc -l
rg "useSWR\|useQuery\|useMutation" app/ --type tsx | wc -l
```

### Design System Audit

```bash
# Find similar existing features
rg "similar-feature" app/ --type tsx | head -20

# Check component reuse
rg "import.*ui/" app/features/ --type tsx | head -20

# Check accessibility patterns
rg "aria-" app/ --type tsx | wc -l
rg "role=" app/ --type tsx | wc -l

# Check mobile patterns
rg "safe-area" app/ --type tsx | wc -l
rg "touch-action" app/ --type tsx | wc -l
rg "max-w-\[" app/ --type tsx | wc -l
```

## Directory Structure

```
docs/plans/P{NN}-<name>/
├── README.md (or index.md)
├── goal.md
├── methodology.md
├── P{NN}-REQUIREMENTS.md       # Functional requirements
├── P{NN}-DESIGN.md             # Design and UX
├── P{NN}-API-CONTRACT.md       # API types and interfaces
├── P{NN}-DEVIATIONS.md
├── P{NN}-PHASED-APPROACH.md
└── plans/
    ├── P{NN}-00-requirements.md
    ├── P{NN}-01-design.md
    ├── P{NN}-02-core-implementation.md
    ├── P{NN}-03-integration.md
    ├── P{NN}-04-testing.md
    ├── P{NN}-05-rollout.md
```

## Goal.md Emphasis

Feature goal.md files must emphasize:

- **User-facing acceptance criteria**: What the user must see/experience
- **API contract**: Types and interfaces before logic
- **No breaking changes**: Backward compatibility unless explicitly planned
- **Rollout strategy**: Feature flags, gradual rollout, or immediate launch
- **Monitoring**: How to verify the feature works in production

## Phase Structure

Feature phases are sequential but may have parallel workstreams:

```markdown
| Phase | Plan | Status | Primary Outcome | Depends On |
| --- | --- | --- | --- | --- |
| 00 | Requirements | Ready | Functional requirements, acceptance criteria | Product input |
| 01 | Design | Ready | UX design, API contract, data model | P{NN}-00 |
| 02 | Core Implementation | Ready | Backend logic, API endpoints, types | P{NN}-01 |
| 03 | Integration | Ready | Frontend integration, edge cases | P{NN}-02 |
| 04 | Testing | Ready | Unit tests, integration tests, E2E tests | P{NN}-03 |
| 05 | Rollout | Ready | Feature flags, monitoring, gradual launch | P{NN}-04 |
```

## Validation

Feature plans must validate:

- `npm run build` passes
- `npm run test` passes with zero failures
- `npm run lint` passes with zero issues
- Acceptance criteria are met:
  - User-facing behavior matches requirements
  - API contract is implemented correctly
  - Edge cases are handled
- Monitoring and alerting are in place
- Feature flags work correctly (if applicable)

## Rules

- Requirements must be defined before design
- Design must be defined before implementation
- API contract must be defined before backend logic
- Testing must be defined before rollout
- Rollout must be gradual unless explicitly planned for immediate launch
- Monitoring must be in place before the feature is considered complete
