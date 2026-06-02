---
name: doc-api
description: How to create API.md. Use when documenting internal and external APIs, interfaces, and data models.
---

# Creating API.md

## Overview
API.md documents how the system communicates. Internal APIs, external APIs, and data models. It lives in `docs/API.md`.

## Core Principle
An API is a contract. Every endpoint, every function, every data model must be documented.

## Step-by-Step Creation

### 1. Internal API Layer

```markdown
## Internal API

### Service Layer

| Service | Purpose | Key Methods | Tests |
|---------|---------|-------------|-------|
| `CharacterService` | CRUD for characters | `getAll`, `getById`, `create` | `characterService.test.ts` |
| `AuthService` | Login, signup, session | `login`, `signup`, `verify` | `authService.test.ts` |

### Data Models

```typescript
interface Character {
  id: string;
  hanzi: string;
  pinyin: string;
  meaning: string;
  hskLevel: number;
  strokeCount: number;
}
```

### Error Handling

| Error | Status | Message | When |
|-------|--------|---------|------|
| `NotFoundError` | 404 | "Character not found" | ID does not exist |
| `ValidationError` | 400 | "Invalid input" | Input fails schema |
| `AuthError` | 401 | "Unauthorized" | Invalid token |
```

### 2. External API Integration

```markdown
## External APIs

| API | Purpose | Auth | Rate Limit |
|-----|---------|------|------------|
| OpenAI | Character explanations | API key | 60 RPM |
| DeepL | Translations | API key | 500K chars/month |
| Stripe | Payments | Secret key | N/A |

### Integration Pattern

```
[Service] → [Adapter] → [External API]
```

- All external calls go through an adapter.
- Adapters handle retries, timeouts, and fallbacks.
- Adapters map external responses to internal types.
```

### 3. Contracts

```markdown
## Contracts

### Frontend → Backend

```typescript
// Request
interface CreateCharacterRequest {
  hanzi: string;
  pinyin: string;
  meaning: string;
  hskLevel: number;
}

// Response
interface CreateCharacterResponse {
  character: Character;
  success: boolean;
  error?: string;
}
```

### Backend → Database

```typescript
// Schema
interface CharacterRow {
  id: UUID;
  hanzi: VARCHAR(10);
  pinyin: VARCHAR(50);
  meaning: TEXT;
  hsk_level: INTEGER;
  created_at: TIMESTAMP;
}
```
```

## Verification Checklist
- [ ] Internal services are listed with key methods
- [ ] Data models are defined with types
- [ ] Error handling is documented
- [ ] External APIs are listed with auth and rate limits
- [ ] Integration patterns are explained
- [ ] Contracts are defined for all interfaces
