# Example: Autonomous DevOps Agent

## Classification

```text
A5-R6-D2
```

Derived risk: Critical

## Purpose

Remediates production incidents under strict constraints.

## Scope

- Can monitor production health.
- Can execute predefined remediation workflows.
- Can coordinate approved diagnostic tools or agents.
- Can roll back a known-bad deployment under policy.
- Cannot change approval gates.
- Cannot grant credentials.
- Cannot create persistent agents.
- Cannot perform destructive actions outside approved runbooks.

## Evidence

- Incident record
- Monitoring alert
- Tool-call trace
- Decision log
- Remediation log
- Rollback record
- Human checkpoint policy

## Controls

- Short authority expiration.
- On-call owner required.
- Kill switch required.
- Full audit trail required.
- Periodic review required.
- Any action outside the runbook requires human approval.

