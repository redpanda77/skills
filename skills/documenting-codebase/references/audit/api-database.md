---
name: audit-api-database
description: Audit subagent guide for analyzing APIs and database. Use when spawning a parallel audit subagent for endpoints, services, and schema.
---

# Audit: API & Database

## Scope
Analyze API routes, service layer, database schema, and external API integrations. Report what endpoints exist, what data models are used, and what external APIs are called.

## Output Format

```markdown
## API & Database Audit

### API Routes
| Route | Method | Purpose | Handler |
|-------|--------|---------|---------|
| [e.g., /api/characters] | [e.g., GET] | [e.g., List characters] | [e.g., characterApi.getAll] |

### Services
| Service | Purpose | Key Methods |
|---------|---------|-------------|
| [e.g., CharacterService] | [e.g., Character CRUD] | [e.g., getAll, getById, create] |

### Data Models
```typescript
interface [Model] {
  [field]: [type];
}
```

### Database Schema
| Table | Purpose | Key Columns |
|-------|---------|-------------|
| [e.g., characters] | [e.g., Store characters] | [e.g., id, hanzi, pinyin] |

### External APIs
| API | Purpose | Auth | Rate Limit |
|-----|---------|------|------------|
| [e.g., OpenAI] | [e.g., AI features] | [e.g., API key] | [e.g., 60 RPM] |

### Error Handling
| Error | Status | When |
|-------|--------|------|
| [e.g., NotFoundError] | [e.g., 404] | [e.g., ID does not exist] |

### Missing / Unclear
- [Anything that should be documented but isn't clear]
```

## Rules
- Find all API routes
- Find all service files
- Find all database schema/migration files
- List all external API calls
- Do NOT write an API.md or DATABASE.md — only produce the audit report
