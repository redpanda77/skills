# Doc Templates

Use these templates when creating documentation. Load the relevant template based on the doc type.

## Template Router

| Doc Type | Template | Load When... |
|----------|----------|--------------|
| `TECH_STACK.md` | `tech-stack.md` | Documenting core tech, dependencies, auth, DB |
| `GETTING_STARTED.md` | `getting-started.md` | Documenting how to run the codebase |
| `ARCHITECTURE.md` | `architecture.md` | Documenting domain map, layering, data flow |
| `STRUCTURE.md` | `directory-tree.md` | Documenting directory structure and principles |
| `CONVENTIONS.md` | `conventions.md` | Documenting code conventions, linting, patterns |
| `TESTING.md` | `testing.md` | Documenting test strategy, tools, how to run |
| `DEVELOPMENT.md` | `development.md` | Documenting dev workflow, how to make changes |
| `API.md` | `api.md` | Documenting internal/external APIs, data models |
| `DATABASE.md` | `database.md` | Documenting schema, migrations, data flow |
| `DEPLOYMENT.md` | `deployment.md` | Documenting how it runs, how to deploy |
| `TROUBLESHOOTING.md` | `troubleshooting.md` | Documenting common issues and fixes |
| `AGENTS.md` / `CLAUDE.md` | `agents-map.md` | Writing the short map |

## Checklist Before Using Any Template

- [ ] The corresponding doc-type guide has been loaded (`references/doc-types/*.md`)
- [ ] GitNexus analysis has been run (if available) to verify structure
- [ ] The template is customized with real project data, not copied verbatim
- [ ] All `[placeholders]` have been replaced
