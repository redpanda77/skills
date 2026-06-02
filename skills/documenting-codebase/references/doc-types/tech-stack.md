---
name: doc-tech-stack
description: How to create TECH_STACK.md. Use when documenting the core technologies, dependencies, auth, database, and frameworks used in the codebase.
---

# Creating TECH_STACK.md

## Overview
TECH_STACK.md documents what the codebase is built on. Frameworks, libraries, database, auth, payment, external APIs. It lives in `docs/TECH_STACK.md`.

## Core Principle
A developer should understand the tech stack in 2 minutes. No surprises, no hidden dependencies.

## Step-by-Step Creation

### 1. Core Framework

```markdown
## Core Framework

| Layer | Technology | Version | Why |
|-------|------------|---------|-----|
| Language | TypeScript | 5.2 | Strict typing, modern JS |
| Framework | Next.js | 14 | App Router, SSR, API routes |
| Runtime | Node.js | 18 | LTS, stable |
| Package Manager | pnpm | 8 | Fast, disk efficient |
```

### 2. Database & Storage

```markdown
## Database & Storage

| Component | Technology | Purpose | Notes |
|-----------|------------|---------|-------|
| Database | PostgreSQL | Primary data store | Hosted on Neon |
| ORM | Drizzle | Type-safe queries | Schema in `src/db/schema.ts` |
| Migrations | Drizzle Kit | Schema changes | Run `pnpm migrate` |
| Cache | Redis | Session cache, rate limiting | Hosted on Upstash |
| Files | Cloudflare R2 | User uploads | CDN-backed |
```

### 3. Authentication

```markdown
## Authentication

| Component | Technology | Purpose | Notes |
|-----------|------------|---------|-------|
| Auth library | NextAuth.js | Session management | OAuth + credentials |
| OAuth providers | Google, GitHub | Social login | Configured in `auth.ts` |
| Passwords | bcrypt | Password hashing | 12 rounds |
| Sessions | JWT | Stateless sessions | 7-day expiry |
| 2FA | TOTP | Optional MFA | Via authenticator app |
```

### 4. UI & Styling

```markdown
## UI & Styling

| Component | Technology | Purpose | Notes |
|-----------|------------|---------|-------|
| Styling | Tailwind CSS | Utility-first CSS | Custom tokens in `globals.css` |
| Components | shadcn/ui | Primitive components | Installed via CLI |
| Animation | Framer Motion | Page transitions, gestures | Used sparingly |
| Icons | Lucide | Icon library | Tree-shakeable |
```

### 5. State & Data Fetching

```markdown
## State & Data Fetching

| Component | Technology | Purpose | Notes |
|-----------|------------|---------|-------|
| Server state | React Query | API caching, invalidation | Global config in `providers.tsx` |
| Client state | Zustand | Local state | Per-feature stores |
| Forms | React Hook Form | Form handling | With Zod validation |
| Validation | Zod | Schema validation | Shared schemas in `src/schemas/` |
```

### 6. Testing

```markdown
## Testing

| Component | Technology | Purpose | Notes |
|-----------|------------|---------|-------|
| Unit tests | Vitest | Fast unit tests | With React Testing Library |
| E2E tests | Playwright | Browser automation | Critical paths only |
| Mocking | MSW | API mocking | Used in tests and dev |
| Coverage | v8 | Code coverage | Target: 80% |
```

### 7. External APIs

```markdown
## External APIs

| API | Purpose | Auth | Rate Limit |
|-----|---------|------|------------|
| OpenAI | AI features | API key | 60 RPM |
| Stripe | Payments | Secret key | N/A |
| SendGrid | Email | API key | 100/day |
```

### 8. DevOps

```markdown
## DevOps

| Component | Technology | Purpose | Notes |
|-----------|------------|---------|-------|
| Hosting | Vercel | App deployment | Edge functions |
| CI/CD | GitHub Actions | Test, lint, deploy | Config in `.github/workflows/` |
| Monitoring | Sentry | Error tracking | Source maps enabled |
| Analytics | PostHog | Product analytics | Optional, privacy-focused |
```

## Verification Checklist
- [ ] Every core dependency is listed with version
- [ ] Database, auth, and storage are documented
- [ ] UI stack is documented
- [ ] State management and data fetching are documented
- [ ] Testing tools are documented
- [ ] External APIs are listed with rate limits
- [ ] DevOps stack is documented
