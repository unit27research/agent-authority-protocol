# Example: Customer Support Agent

## Classification

```text
A4-R3-D1
```

Derived risk: High

## Purpose

Responds to common customer support requests within approved categories.

## Scope

- Can read customer support tickets.
- Can retrieve approved help-center content.
- Can respond to customers for predefined issue categories.
- Can invoke approved retrieval or policy-checking tools.
- Cannot issue refunds without approval.
- Cannot change account ownership.
- Cannot modify legal or billing records.

## Evidence

- Ticket record
- Tool-call trace
- Response log
- Policy source used
- Escalation record
- Exception log

## Controls

- Human review required for refunds, account changes, complaints, legal threats, or safety-sensitive content.
- Unsupported issue categories route to human support.
- Response logs retained for review.
