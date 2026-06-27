# Example: Finance Agent

## Classification

```text
A3-R4-D0
```

Derived risk: High

## Purpose

Reviews invoices and prepares payment recommendations.

## Scope

- Can read invoices, purchase orders, and vendor records.
- Can compare invoice data against approved records.
- Can draft payment recommendations.
- Cannot release funds.
- Cannot approve vendors.
- Cannot change bank details.
- Cannot invoke other agents.

## Evidence

- Invoice record
- Source documents reviewed
- Recommendation artifact
- Approval packet shown to the human reviewer
- Approval record
- Exception log

## Controls

- Human approval required before payment.
- Bank detail changes are prohibited.
- Vendor onboarding remains outside the agent's authority.
- Exceptions route to finance owner.
