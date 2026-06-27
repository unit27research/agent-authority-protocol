# Delegation Classes

Delegation describes whether an agent can invoke, coordinate, create, or authorize other agents.

| Class | Name | Description | Example |
|---|---|---|---|
| D0 | No Delegation | Cannot call, invoke, create, or direct other agents. | Standalone drafter |
| D1 | Approved Invocation | May invoke pre-approved agents or tools within a fixed workflow. | Coding agent invoking test agent |
| D2 | Agent Orchestration | May coordinate multiple approved agents within a defined workflow. | Research orchestrator |
| D3 | Temporary Agent Creation | May create temporary agents for bounded tasks, without granting persistent authority. | Multi-step project agent spawning task agents |
| D4 | Authority Delegation | May assign authority, pass credentials, modify scopes, or authorize other agents. | Agent factory, autonomous manager agent |

## Important Distinction

`D4` is the highest-risk delegation class because it allows authority to propagate.

`A6` and `D4` are related without being identical. `D4` describes a delegation path in which authority can propagate, including approval-gated or policy-bound propagation. `A6` describes discretionary authority over the actor set. If an agent can choose another actor's scope, credentials, persistence, or action rights, the deployment has entered `A6` territory.

Any `D4` agent should require:

- explicit review
- delegation graph
- inherited-scope record
- approval chain
- revocation path
- renewal limit
- authority expiration

## Classification Guidance

Classify by the highest delegation path the agent is able to use, rather than by its usual behavior.

If the agent can create or authorize another agent with persistent authority, classify the delegation path as `D4`. If the agent can also decide the new actor's authority without a fixed approval gate, classify the Authority axis as `A6`.
