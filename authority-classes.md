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
| A6 | Delegating Authority | Can decide who or what may act next by determining, granting, changing, or propagating authority for other agents or actors. | Authority-granting supervisor, agent factory |

## Important Distinction

`A6` is not simply more autonomous. It is qualitatively different because the agent has discretionary authority over the actor set. It can decide who or what may act next, alter scope, grant credentials, change another actor's authority, or carry authority forward through another actor.

Ordinary helper invocation and fixed orchestration do not make an agent `A6` by themselves. Those patterns usually belong on the Delegation axis as `D1` or `D2` unless the first agent can change another actor's authority.

## Classification Guidance

Assign the highest authority class the agent can reach in normal operation.

Do not classify an agent by its intended average behavior if it has permissions or tools that allow higher-authority behavior.
