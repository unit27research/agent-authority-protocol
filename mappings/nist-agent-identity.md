# Mapping: Agent Identity and Authorization Concepts

The Agent Authority Protocol does not authenticate agents or authorize API calls.

It can support identity and authorization work by documenting the authority that should be represented in identity, access, and audit systems.

## Concepts

| Concept | ARD Support |
|---|---|
| Agent identity | Records the agent name, version, owner, sponsor, runtime, and framework |
| Authentication | Identifies which agent is being reviewed before credentials are issued |
| Authorization | Records what actions, systems, and data classes the agent should be allowed to access |
| Auditability | Defines evidence, logging, approval, and retention requirements |
| Non-repudiation | Supports clear records of owner, approval, action receipt, and delegation chain |
| Lifecycle management | Records deployment status, review cadence, expiration, and revocation path |
| Least privilege | Helps compare the agent's purpose against its authority, reach, and delegation rights |

## Boundary

ARD should be used before technical access is granted.

Identity and authorization systems should enforce the resulting scopes. ARD does not enforce them by itself.

