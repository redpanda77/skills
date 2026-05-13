# Pattern: Sequential Workflow Orchestration

**Use when:** Multi-step processes in a specific order.

## Characteristics
- Explicit step ordering
- Dependencies between steps
- Validation at each stage
- Rollback instructions for failures

## Structure

```md
## Workflow: [Name]

### Step 1: [Action]
Call MCP tool: `tool_name`
Parameters: param1, param2

### Step 2: [Dependent Action]
Call MCP tool: `next_tool`
Wait for: [condition from Step 1]

### Step 3: [Final Action]
Call MCP tool: `final_tool`
Parameters: [use output from Step 1]

### Validation
Before proceeding, verify:
- [ ] Check 1
- [ ] Check 2

### Error Handling
If [error] occurs:
1. [Rollback step]
2. [Retry logic]
```

## Example

```md
## Workflow: Onboard New Customer

### Step 1: Create Account
Call MCP tool: `create_customer`
Parameters: name, email, company

### Step 2: Setup Payment
Call MCP tool: `setup_payment_method`
Wait for: payment method verification

### Step 3: Create Subscription
Call MCP tool: `create_subscription`
Parameters: plan_id, customer_id (from Step 1)

### Step 4: Send Welcome Email
Call MCP tool: `send_email`
Template: welcome_email_template
```

## Key Techniques

1. **Explicit dependencies:** Reference outputs from previous steps
2. **Validation gates:** Check conditions before proceeding
3. **Clear parameters:** Specify exact parameter names
4. **Rollback paths:** Document how to undo if failures occur
