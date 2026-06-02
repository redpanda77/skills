# API

## Internal API

### Service Layer

| Service | Purpose | Key Methods | Tests |
|---------|---------|-------------|-------|

### Data Models

```typescript
interface <Model> {
  <field>: <type>;
}
```

### Error Handling

| Error | Status | Message | When |
|-------|--------|---------|------|

## External APIs

| API | Purpose | Auth | Rate Limit |
|-----|---------|------|------------|

### Integration Pattern

```
[Service] → [Adapter] → [External API]
```

## Contracts

### Request

```typescript
interface <Request> {
  <field>: <type>;
}
```

### Response

```typescript
interface <Response> {
  <field>: <type>;
}
```
