# Evidence Requirements

Evidence requirements should scale with the ARD classification.

| Classification Pattern | Evidence Required |
|---|---|
| A0-A1 / R0-R1 / D0 | Basic logs and source references |
| A2 / R1-R2 / D0-D1 | Draft artifact, human review record, version history |
| A3 / R2-R4 / D0-D1 | Tool-call trace, approval record, action receipt |
| A4 / R2-R4 / D1-D2 | Runtime logs, policy decision log, exception log, rollback path |
| A5 / R4-R6 / D1-D3 | Full audit trail, human checkpoint policy, incident path, periodic review |
| A6 or D4 | Delegation graph, inherited scopes, approval chain, revocation path, authority expiration |

## Minimum Evidence Record

Every deployed agent should have:

- owner
- purpose
- ARD classification
- tool and system list
- data access list
- approval status
- review cadence
- revocation path

## High-Risk Evidence

Any agent classified as `High`, `Critical`, or `Extreme` should have:

- tool-call logs
- decision logs
- approval records
- error logs
- exception logs
- rollback plan
- incident owner
- authority expiration

## Delegation Evidence

Any `D3` or `D4` agent should have:

- delegation graph
- delegator identity
- delegate identity
- authority granted
- scope limits
- expiration date
- revocation method
- approval chain

