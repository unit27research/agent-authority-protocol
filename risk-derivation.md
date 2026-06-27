# Risk Derivation

Risk is derived from the ARD classification.

The score is not intended to be a precise quantitative risk model. It is a first-pass review band that helps determine the level of evidence, approval, and monitoring required before deployment.

## Suggested Risk Bands

Each row below is an escalation trigger. Use the highest row triggered by Authority, Reach, or Delegation. Reach and Delegation can raise the band, and neither should lower the band implied by Authority.

| Escalation Trigger | Risk Band |
|---|---|
| All of A0-A1, R0-R1, and D0 | Minimal |
| Any A2, R2, or D1, absent a higher trigger | Low |
| Any A3, R3, or D2, absent a higher trigger | Moderate |
| Any A4, R4, or D3, absent a higher trigger | High |
| Any A5, R5, R6, or D4, absent a higher trigger | Critical |
| Any A6, or R6 with D4 | Extreme |

## Dominance Rule

The highest-risk dimension should dominate the review process.

A low-autonomy agent with legal, financial, production, or delegation reach may still require high-risk controls.

## Examples

| Agent | Classification | Derived Risk |
|---|---:|---|
| Read-only research agent | `A1-R0-D0` | Minimal |
| LinkedIn content drafter | `A2-R1-D0` | Low |
| Customer support responder | `A4-R3-D1` | High |
| GitHub coding agent with PR approval | `A3-R6-D1` | Critical |
| Autonomous DevOps agent | `A5-R6-D2` | Critical |
| Agent factory with financial authority | `A6-R4-D4` | Extreme |
| Agent factory with production authority | `A6-R6-D4` | Extreme |

## Control Escalation

Controls should increase when any of the following are true:

- the agent can write to a system of record
- the agent can communicate with customers or the public
- the agent can affect money, contracts, compliance, or production systems
- the agent can invoke or coordinate other agents
- the agent can create new agents
- the agent can modify scopes, credentials, approvals, or policies
