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

Any `D4` agent should require:

- explicit review
- delegation graph
- inherited-scope record
- approval chain
- revocation path
- renewal limit
- authority expiration

## Classification Guidance

Classify by what the agent is able to delegate, not only by what it usually delegates.

If the agent can create or authorize another agent with persistent authority, classify it as `D4`.

