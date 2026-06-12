# Authority Classes

Authority describes what decisions or actions an agent may perform.

| Class | Name | Description | Example |
|---|---|---|---|
| A0 | Observer | Read-only. Cannot recommend, draft, modify, or act. | Log viewer, read-only research monitor |
| A1 | Advisor | Can analyze and recommend. Human decides and executes. | Research assistant, policy recommendation agent |
| A2 | Drafter | Can create artifacts for human review. Cannot publish, send, merge, or execute. | Email drafter, report generator |
| A3 | Approval-Gated Operator | Can prepare and execute actions only after explicit human approval. | Support refund agent requiring approval |
| A4 | Bounded Autonomous Operator | Can execute predefined workflows independently within strict limits. | Ticket triage agent, calendar scheduling agent |
| A5 | Autonomous Decision Maker | Can make bounded operational decisions with material external or business impact. | Pricing adjustment agent, production remediation agent |
| A6 | Delegating Authority | Can assign tasks, invoke agents, create agents, or grant authority to other agents. | Agent orchestrator, agent factory |

## Important Distinction

`A6` is not simply more autonomous. It is qualitatively different because the agent can expand the effective authority surface by directing or empowering other agents.

## Classification Guidance

Assign the highest authority class the agent can reach in normal operation.

Do not classify an agent by its intended average behavior if it has permissions or tools that allow higher-authority behavior.

