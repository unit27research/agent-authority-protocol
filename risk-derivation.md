# Risk Derivation

Risk is derived from the ARD classification.

The score is not intended to be a precise quantitative risk model. It is a first-pass review band that helps determine the level of evidence, approval, and monitoring required before deployment.

## Suggested Risk Bands

| Pattern | Risk Band |
|---|---|
| A0-A1 with R0-R1 and D0 | Minimal |
| A1-A2 with R1-R2 and D0-D1 | Low |
| A3-A4 with R2-R3 or D1-D2 | Moderate |
| A4-A5 with R3-R5 or D2-D3 | High |
| A5-A6 with R5-R6 or D3-D4 | Critical |
| Any A6-R6-D4 | Extreme |

## Dominance Rule

The highest-risk dimension should dominate the review process.

A low-autonomy agent with legal, financial, production, or delegation reach may still require high-risk controls.

## Examples

| Agent | Classification | Derived Risk |
|---|---:|---|
| Read-only research agent | `A1-R0-D0` | Minimal |
| LinkedIn content drafter | `A2-R1-D0` | Low |
| Customer support responder | `A4-R3-D1` | Moderate to High |
| GitHub coding agent with PR approval | `A3-R6-D1` | High |
| Autonomous DevOps agent | `A5-R6-D2` | Critical |
| Agent factory with financial authority | `A6-R4-D4` | Critical |
| Agent factory with production authority | `A6-R6-D4` | Extreme |

## Control Escalation

Controls should increase when any of the following are true:

- the agent can write to a system of record
- the agent can communicate with customers or the public
- the agent can affect money, contracts, compliance, or production systems
- the agent can invoke or coordinate other agents
- the agent can create new agents
- the agent can modify scopes, credentials, approvals, or policies

