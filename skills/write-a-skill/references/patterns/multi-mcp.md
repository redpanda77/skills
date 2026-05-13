# Pattern: Multi-MCP Coordination

**Use when:** Workflows span multiple services.

## Characteristics
- Clear phase separation
- Data passing between MCPs
- Validation before moving to next phase
- Centralized error handling

## Structure

```md
## Workflow: [Name]

### Phase 1: [Service A]
1. Action with Service A MCP
2. Process output
3. Prepare for handoff

### Phase 2: [Service B]
1. Receive data from Phase 1
2. Action with Service B MCP
3. Process output

### Phase 3: [Service C]
1. Receive data from Phase 2
2. Final action
3. Notify/complete
```

## Example

```md
## Workflow: Design-to-Development Handoff

### Phase 1: Design Export (Figma MCP)
1. Export design assets from Figma
2. Generate design specifications
3. Create asset manifest

### Phase 2: Asset Storage (Drive MCP)
1. Create project folder in Drive
2. Upload all assets
3. Generate shareable links

### Phase 3: Task Creation (Linear MCP)
1. Create development tasks
2. Attach asset links to tasks
3. Assign to engineering team

### Phase 4: Notification (Slack MCP)
1. Post handoff summary to #engineering
2. Include asset links and task references
```

## Key Techniques

1. **Data contracts:** Document what each phase expects/produces
2. **Phase gates:** Validate before moving to next service
3. **Error boundaries:** Handle failures per phase
4. **Compensation:** Rollback actions in previous services if later phase fails
