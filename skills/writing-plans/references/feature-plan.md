# Feature Plan

For adding new functionality, APIs, or user-facing features.

## Key Characteristics

- **Requirements first**: Define acceptance criteria before implementation
- **API contract before implementation**: Types and interfaces before logic
- **User-facing acceptance criteria**: What the user must see/experience
- **Rollout strategy**: How the feature is deployed and monitored

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
