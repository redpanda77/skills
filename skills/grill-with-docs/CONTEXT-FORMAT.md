# CONTEXT.md Format

A `CONTEXT.md` captures the ubiquitous language of a bounded context — the terms domain experts and developers use with shared, precise meaning.

## File structure

```markdown
# [Context Name] Context

One sentence describing the purpose and boundaries of this context.

## Glossary

### Term
Definition. Use precise language. State what distinguishes this term from similar ones.

**Synonyms to avoid:** list any informal names that should not be used
**Related:** [OtherTerm] — explain the relationship

### AnotherTerm
...
```

## Rules

- **One entry per concept.** If two names refer to the same thing, pick the canonical one and redirect the others.
- **Domain-expert language only.** Don't include implementation details (class names, table names, endpoints). If a domain expert wouldn't say it, it doesn't belong here.
- **State the boundary.** If a term means something different in another context, say so. "In the Billing context, 'Account' means the payment entity. In the Ordering context, 'Account' is not used — see Customer."
- **Keep it short.** A glossary entry is 1-3 sentences. If you need more, the term may be doing too much.
- **Update, don't append.** When a term's meaning evolves, rewrite the entry. Don't add a second entry.

## Example

```markdown
# Ordering Context

Handles everything from a customer placing an order to the kitchen confirming receipt.

## Glossary

### Order
A request from a Customer to a Restaurant for one or more Items. An Order exists from the moment it is placed until it is either Completed or Cancelled. It does not include payment — that is handled in the Billing context.

**Related:** [LineItem] — an Order contains one or more LineItems

### LineItem
A single dish selection within an Order, with a quantity and price at time of order. Prices on LineItems are immutable after the Order is confirmed.

### Customer
The person placing the Order. Identified by their profile in the Identity context. In this context, we only care about their delivery address and order history.

**Synonyms to avoid:** user, buyer, end-user

### Restaurant
A merchant registered on the platform. In this context, a Restaurant is a receiver of Orders and a source of menu data. Ownership, contracts, and payments live in separate contexts.
```
