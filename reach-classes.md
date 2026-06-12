# Reach Classes

Reach describes what people, systems, data, or business domains an agent can affect.

This protocol uses Reach instead of Impact because reach can be assessed before deployment. Impact is often only known after an event occurs.

| Class | Name | Description | Example |
|---|---|---|---|
| R0 | Local / No External Effect | No external systems, users, customers, or persistent records affected. | Local summarizer |
| R1 | Internal Content | Can affect internal documents, drafts, notes, or knowledge artifacts. | Internal wiki updater |
| R2 | Internal Systems | Can affect internal workflows, tickets, tasks, or operational systems. | Jira triage agent |
| R3 | Customer-Facing | Can affect customers, users, external communication, or public content. | Support response agent |
| R4 | Financial | Can affect invoices, payments, refunds, pricing, procurement, or budgets. | Invoice review agent |
| R5 | Legal / Compliance | Can affect contracts, regulated records, compliance decisions, or formal attestations. | Contract review agent |
| R6 | Production / Critical Operations | Can affect production systems, deployments, infrastructure, safety-critical operations, or high-impact business continuity. | DevOps remediation agent |

## Classification Guidance

Assign the highest reach class the agent can affect through its tools, credentials, data access, outputs, or workflow placement.

If an agent can affect multiple domains, classify it by the highest-risk domain.

