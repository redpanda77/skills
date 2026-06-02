# docs/ Directory Layout

Standard layout for in-repo knowledge base.

```
docs/
├── index.md                    # Catalog of all docs in this directory
├── TECH_STACK.md             # Core tech, dependencies, auth, DB
├── GETTING_STARTED.md        # How to run the codebase locally
├── ARCHITECTURE.md           # Domain map, package layering, data flow
├── STRUCTURE.md              # Directory structure and principles
├── CONVENTIONS.md            # Code conventions, linting, patterns
├── TESTING.md                # Test strategy, tools, how to run
├── DEVELOPMENT.md            # Dev workflow, how to make changes
├── API.md                    # Internal/external APIs, data models
├── DATABASE.md               # Schema, migrations, data flow
├── DEPLOYMENT.md             # How it runs, how to deploy
├── TROUBLESHOOTING.md        # Common issues and fixes
├── DESIGN.md                 # Design system inventory: tokens, typography, components
├── design-docs/
│   ├── index.md
│   ├── core-beliefs.md
│   └── [feature]-design.md
├── plans/
│   ├── README.md             # Registry of all plans (managed by writing-plans)
│   └── P{NN}-<name>/         # Individual plan directories
├── generated/
│   └── db-schema.md          # Auto-generated docs (not hand-written)
├── product-specs/
│   ├── index.md
│   ├── new-user-onboarding.md
│   └── [feature]-spec.md
└── references/
    ├── design-system.md
    └── [tool]-reference.md
```

AGENTS.md (repo root) — Short map under 100 lines. Only pointers.

## Rules

- `index.md` exists in every subdirectory that has more than 2 files.
- `generated/` is for machine-produced docs; do not hand-edit.
- `plans/` is managed by `writing-plans`; do not create plan files directly.
- Every doc must be reachable from `docs/index.md` or `AGENTS.md`.
