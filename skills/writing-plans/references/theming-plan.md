# Theming Plan

For migrating colors, design tokens, typography, spacing, or visual systems.

## Key Characteristics

- **Audit first**: Freeze current state before any changes
- **Token taxonomy before components**: Define CSS variables and Tailwind mappings before touching component files
- **Light mode identity is invariant**: Every token change must leave light mode looking identical
- **Surface-by-surface migration**: Start with low-coupling surfaces (tokens, primitives) before high-drift surfaces (features)
- **Never remove without replacement**: Every `dark:` override and inline style must be replaced with a token

## Directory Structure

```
docs/plans/P{NN}-<name>/
├── README.md (or index.md)
├── goal.md
├── methodology.md
├── P{NN}-AUDIT.md              # Current state audit
├── P{NN}-DESIGN.md             # Design system inventory
├── P{NN}-COVERAGE-MAP.md       # Traceability from audit to phases
├── P{NN}-DEVIATIONS.md
├── P{NN}-PHASED-APPROACH.md
└── plans/
    ├── P{NN}-00-audit-baseline.md
    ├── P{NN}-01-theme-contract.md
    ├── P{NN}-02-runtime-infrastructure.md
    ├── P{NN}-03-core-tokens.md
    ├── P{NN}-04-state-primitives.md
    ├── P{NN}-05-app-shell.md
    ├── P{NN}-06-feature-surfaces.md
    ├── P{NN}-07-capacitor-pwa.md
    └── P{NN}-08-guardrails.md
```

## Goal.md Emphasis

Theming goal.md files must emphasize:

- **No visual redesign**: Maintain current colors and styling
- **No breaking changes**: Light mode must look identical before and after
- **Token hierarchy first**: Define the contract before migrating components
- **Dark mode handled at token level**: No `dark:` overrides in component files
- **Mobile constraints preserved**: Safe areas, touch targets, fonts remain

## Phase Structure

Theming phases are sequential and must be executed in order:

```markdown
| Phase | Plan | Status | Primary Outcome | Depends On |
| --- | --- | --- | --- | --- |
| 00 | Audit Baseline | Ready | Freeze scope, inventory, priorities | Existing audit |
| 01 | Theme Contract | Ready | Define token taxonomy, surface taxonomy, state model | P{NN}-00 |
| 02 | Runtime Infrastructure | Ready | Unlock light/dark/system switching | P{NN}-01 |
| 03 | Core Tokens | Ready | Normalize CSS variables, Tailwind mappings, primitives | P{NN}-02 |
| 04 | State Primitives | Ready | Create shared loading, empty, error primitives | P{NN}-03 |
| 05 | App Shell | Ready | Migrate layout, header, container, bottom nav | P{NN}-03, P{NN}-04 |
| 06 | Feature Surfaces | Ready | Migrate home, lists, vocabulary, etc. | P{NN}-05 |
| 07 | Capacitor/PWA | Ready | Splash screen, PWA manifest, status bar | P{NN}-06 |
| 08 | Guardrails | Ready | Add lint rules, drift checks, contribution guidelines | P{NN}-07 |
```

## Validation

Theming plans must validate:

- `npm run build` passes after every phase
- `npm run lint:biome` passes with zero issues
- Light mode visual audit: must match pre-migration state
- Dark mode visual audit: must be legible and consistent
- Token completeness: every new token has both CSS variable and Tailwind mapping
- Raw color check: `grep -r "#[0-9a-fA-F]\{3,6\}"` should show only exceptions
- `dark:` override check: `grep -r "dark:"` should show zero in component files
- Dead CSS file check: listed dead files must not exist

## Rules

- Phases are sequential and must be executed in order
- Phase 00 (audit) must not change any code
- Phase 01 (contract) must not add CSS variables yet
- Phase 02 (infrastructure) must unlock theme switching before changing colors
- Phase 03 (core tokens) must fix primitives before touching feature surfaces
- Phase 06 (features) must be the last surface migration
- Phase 08 (guardrails) must add lint rules and documentation
