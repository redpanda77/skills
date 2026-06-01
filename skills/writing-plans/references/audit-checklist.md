# Audit Checklist by Plan Type

Every plan type has a specific set of things that must be audited before writing KOs. This checklist documents what to look for, what tools to use, and what evidence to collect.

## Reorganization Plan Audit

### What to Audit

| Category | What to Look For | Evidence | Tool |
|---|---|---|---|
| **Dumping grounds** | Root directories with >50 files and no clear ownership | `ls -la`, `find . -type f | wc -l` | `find`, `ls` |
| **Empty directories** | Directories with zero files | `find . -type d -empty` | `find` |
| **Dead code** | Files with zero consumers, orphan backups, `.new` files | `gitnexus_impact`, `rg "filename"` | GitNexus, `rg` |
| **Barrel files** | `export *` patterns | `grep -r "export \\*"` | `grep` |
| **Circular dependencies** | Cross-import cycles between directories | `gitnexus_cypher` circular query | GitNexus |
| **Import boundaries** | Cross-feature imports, infrastructure-to-feature imports | `rg "from.*features/"`, `rg "from.*infrastructure/"` | `rg` |
| **Route safety** | Next.js route files in wrong directories | `find -name "page.tsx" -o -name "layout.tsx"` | `find` |
| **Mixed ownership** | Files with imports from 3+ unrelated domains | `gitnexus_context` | GitNexus |
| **Naming inconsistency** | kebab vs camel vs Pascal vs snake | `ls` inspection | Manual |
| **Context placement** | `createContext` calls scattered across files | `rg "createContext"` | `rg` |

### Audit Output

- `P{NN}-AUDIT.md` — Inclusion decision table (what KOs to include vs skip)
- `P{NN}-FINDINGS.md` — Deep audit findings with severity classification
- `P{NN}-diagram.md` — Target directory tree and import rules

### Example Commands

```bash
# Count files per directory
find . -maxdepth 2 -type d | sort | while read dir; do echo "$dir: $(find "$dir" -type f | wc -l)"; done

# Find barrel files
find . -name "index.ts" -o -name "index.tsx" | xargs grep -l "export \\*" 2>/dev/null

# Find circular dependencies
# gitnexus_cypher query:
# MATCH (a:File)-[r:CodeRelation {type: 'IMPORTS'}]->(b:File),
#       (b)-[r2:CodeRelation {type: 'IMPORTS'}]->(a)
# RETURN a.filePath, b.filePath

# Find cross-directory imports
rg "from.*@/components/" app/ --type ts --type tsx
rg "from.*@/lib/" app/ --type ts --type tsx

# Find empty directories
find . -type d -empty
```

## Theming Plan Audit

### What to Audit

| Category | What to Look For | Evidence | Tool |
|---|---|---|---|
| **Raw colors** | Hex, rgb, rgba values in component files | `grep -r "#" --include="*.tsx"`, `grep -r "rgba?"` | `grep`, `rg` |
| **dark: overrides** | Tailwind dark mode overrides | `grep -r "dark:" --include="*.tsx"` | `grep`, `rg` |
| **Inline styles** | `style={{ color: "#..." }}` | `grep -r "style={{" --include="*.tsx"` | `grep`, `rg` |
| **CSS files** | Hardcoded colors in CSS | `grep -r "#" --include="*.css"` | `grep` |
| **Theme lock** | `forcedTheme`, `enableSystem={false}` | `grep -r "forcedTheme"` | `grep` |
| **Status bar** | iOS/Android status bar configuration | `grep -r "status-bar"`, `grep -r "backgroundColor"` | `grep` |
| **PWA manifest** | Hardcoded colors in manifest | `cat public/manifest.json` | `cat` |
| **Splash screen** | Hardcoded splash screen colors | `grep -r "backgroundColor" capacitor.config.ts` | `grep` |
| **Token completeness** | Missing CSS variables or Tailwind mappings | `grep -r "var(--" --include="*.tsx"`, `grep -r "bg-" --include="*.tsx"` | `grep` |
| **Duplicate sources** | Same colors defined in multiple files | Manual comparison | Manual |
| **Ionic integration** | Ionic dark mode palette, inline styles | `grep -r "@ionic"`, `grep -r "style="` | `grep` |
| **Animation colors** | Hex/rgb in SVG, canvas, animations | `grep -r "#" --include="*.tsx"` in animation files | `grep` |
| **Typography** | Font overrides, `!important` font rules | `grep -r "font-family" --include="*.css"` | `grep` |
| **Safe areas** | Hardcoded safe-area values | `grep -r "safe-area" --include="*.css"` | `grep` |

### Audit Output

- `P{NN}-AUDIT.md` — Surface taxonomy table with drift counts per surface
- `P{NN}-DESIGN.md` — Design system inventory (tokens, typography, spacing, elevation)
- `P{NN}-COVERAGE-MAP.md` — Traceability from audit findings to phases

### Example Commands

```bash
# Count raw colors by directory
for dir in app components styles; do
  echo "$dir: $(grep -r "#[0-9a-fA-F]\{3,6\}" "$dir" --include="*.tsx" --include="*.css" | wc -l)"
done

# Count dark: overrides
rg "dark:" --include="*.tsx" | wc -l

# Count inline styles with hex
rg "style=\{\{.*#" --include="*.tsx" | wc -l

# Find all CSS files
find . -name "*.css" | sort

# Check theme lock
grep -r "forcedTheme" app/ --include="*.tsx"

# Check PWA manifest colors
cat public/manifest.json | grep -E "background_color|theme_color"

# Check Ionic dark mode
grep -r "@ionic/react/css/palettes" app/ --include="*.css"
```

## Feature Plan Audit

### What to Audit

| Category | What to Look For | Evidence | Tool |
|---|---|---|---|
| **Existing code** | Similar features, reusable components | `gitnexus_query`, `rg` | GitNexus, `rg` |
| **API patterns** | Existing API route patterns, response shapes | `ls app/api/`, `cat existing/route.ts` | `ls`, `cat` |
| **Type definitions** | Existing types, interfaces, schemas | `rg "interface.*Feature"`, `rg "type.*Feature"` | `rg` |
| **State management** | Existing stores, contexts, reducers | `rg "createContext"`, `rg "useStore"` | `rg` |
| **Tests** | Existing test patterns, coverage gaps | `find . -name "*.test.ts"`, `find . -name "*.spec.ts"` | `find` |
| **Dependencies** | External libraries, peer dependencies | `cat package.json` | `cat` |
| **Authentication** | Auth requirements, protected routes | `rg "auth"`, `rg "middleware"` | `rg` |
| **Performance** | Existing performance patterns, lazy loading | `rg "lazy"`, `rg "dynamic"` | `rg` |
| **Accessibility** | Existing a11y patterns, ARIA usage | `rg "aria-"`, `rg "role="` | `rg` |
| **Mobile constraints** | Safe areas, touch targets, responsive | `rg "safe-area"`, `rg "touch-action"` | `rg` |

### Audit Output

- `P{NN}-REQUIREMENTS.md` — Functional requirements and acceptance criteria
- `P{NN}-DESIGN.md` — UX design and wireframes
- `P{NN}-API-CONTRACT.md` — API types, interfaces, request/response shapes

### Example Commands

```bash
# Find similar features
rg "similar-feature-name" app/ --type ts --type tsx

# Check existing API routes
ls -la app/api/

# Check existing types
rg "export interface" app/ --type ts | head -20

# Check existing tests
find . -name "*.test.ts" -o -name "*.test.tsx" | sort

# Check package.json dependencies
cat package.json | jq '.dependencies'

# Check auth patterns
rg "auth" app/ --type ts --type tsx | head -20

# Check lazy loading
rg "lazy" app/ --type ts --type tsx | head -20
```

## Audit/Remediation Plan Audit

### What to Audit

| Category | What to Look For | Evidence | Tool |
|---|---|---|---|
| **Security** | Secrets, API keys, hardcoded tokens | `grep -r "api_key"`, `grep -r "secret"`, `grep -r "password"` | `grep`, `rg` |
| **Type safety** | `any` usage, `ts-ignore`, missing types | `grep -r "any" --include="*.ts"`, `grep -r "@ts-ignore"` | `grep` |
| **Error handling** | Uncaught exceptions, missing try/catch | `grep -r "console.error"`, `grep -r "throw"` | `grep` |
| **Performance** | Large bundles, unnecessary re-renders | `npm run build` output, `webpack-bundle-analyzer` | Build tools |
| **Dead code** | Unused exports, commented code, TODOs | `gitnexus_impact`, `grep -r "TODO"`, `grep -r "FIXME"` | GitNexus, `grep` |
| **Accessibility** | Missing alt text, low contrast, no ARIA | `rg "alt="`, `rg "aria-"`, Lighthouse | `rg`, Lighthouse |
| **Tests** | Missing tests, low coverage, skipped tests | `find . -name "*.test.*"`, `cat coverage/report` | `find`, `cat` |
| **Documentation** | Missing README, outdated docs, broken links | `find . -name "README.md"`, `grep -r "TODO.*doc"` | `find` |
| **Dependencies** | Outdated packages, security vulnerabilities | `npm audit`, `npm outdated` | `npm` |
| **Code style** | Inconsistent formatting, lint violations | `npm run lint`, `npx biome check` | Lint tools |

### Audit Output

- `P{NN}-AUDIT.md` — Full audit findings with severity classification
- `P{NN}-FINDINGS.md` — Deep audit findings with file paths and evidence
- `P{NN}-REMEDIATION.md` — Remediation plan with owner and timeline

### Example Commands

```bash
# Find secrets
rg "api_key|apikey|secret|password|token" app/ --type ts --type tsx | grep -v "\.env"

# Find any usage
rg ": any" app/ --type ts --type tsx | wc -l

# Find TODOs
rg "TODO|FIXME|HACK|XXX" app/ --type ts --type tsx | wc -l

# Find missing alt text
rg "<img" app/ --type tsx | grep -v "alt=" | wc -l

# Check test coverage
npm run test -- --coverage

# Check security
npm audit

# Check outdated packages
npm outdated

# Check lint
npm run lint

# Run type check
npx tsc --noEmit
```

## Rules

- Every plan must have an audit before KOs are written
- The audit must use the appropriate tools for the plan type
- The audit must produce evidence (file paths, code snippets, command output)
- The audit must classify findings by severity (Critical, High, Medium, Low)
- The audit must be reproducible — another agent should get the same results
