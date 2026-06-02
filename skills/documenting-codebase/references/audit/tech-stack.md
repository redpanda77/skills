---
name: audit-tech-stack
description: Audit subagent guide for analyzing the tech stack. Use when spawning a parallel audit subagent for dependencies, frameworks, and tools.
---

# Audit: Tech Stack

## Scope
Analyze `package.json`, `requirements.txt`, `Cargo.toml`, `go.mod`, `Dockerfile`, `.github/workflows/`, and any config files. Report what technologies are used and why.

## Output Format

```markdown
## Tech Stack Audit

### Core Framework
- Language: [e.g., TypeScript 5.2]
- Framework: [e.g., Next.js 14 App Router]
- Runtime: [e.g., Node.js 18]
- Package Manager: [e.g., pnpm 8]

### Database & Storage
- [e.g., PostgreSQL 15 via Neon]
- [e.g., Redis via Upstash]
- [e.g., Cloudflare R2 for files]

### Auth
- [e.g., NextAuth.js with Google OAuth]
- [e.g., bcrypt for passwords]

### UI & Styling
- [e.g., Tailwind CSS 3.4]
- [e.g., shadcn/ui components]
- [e.g., Framer Motion for animations]

### State & Data Fetching
- [e.g., React Query for server state]
- [e.g., Zustand for client state]
- [e.g., React Hook Form + Zod for forms]

### Testing
- [e.g., Vitest for unit tests]
- [e.g., Playwright for E2E]
- [e.g., MSW for API mocking]

### External APIs
- [e.g., OpenAI for AI features]
- [e.g., Stripe for payments]

### DevOps
- [e.g., Vercel for hosting]
- [e.g., GitHub Actions for CI/CD]
- [e.g., Sentry for error tracking]

### Key Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| [name] | [version] | [purpose] |

### Config Files
| File | Purpose |
|------|---------|
| [e.g., biome.json] | [e.g., Linting and formatting] |
| [e.g., tsconfig.json] | [e.g., TypeScript config] |

### Missing / Unclear
- [Anything that should be documented but isn't clear from the codebase]
```

## Rules
- Read `package.json` and all dependency files
- Read `Dockerfile` and `.github/workflows/` for CI/CD stack
- List every significant dependency with its purpose
- Flag anything that is unclear or missing
- Do NOT write a TECH_STACK.md — only produce the audit report
