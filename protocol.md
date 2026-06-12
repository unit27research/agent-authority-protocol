# Protocol Overview

The Agent Authority Protocol classifies delegated authority in AI agents before deployment.

The protocol uses the Authority-Reach-Delegation model, or ARD.

ARD uses three dimensions:

```text
A#-R#-D#
```

Where:

- `A` means Authority
- `R` means Reach
- `D` means Delegation

The resulting `A#-R#-D#` value is the agent's ARD classification.

## Classification Steps

1. Identify what the agent is intended to do.
2. Identify the strongest action the agent may take.
3. Identify the highest-impact domain the agent can affect.
4. Identify whether the agent can invoke, coordinate, create, or authorize other agents.
5. Assign one class for each ARD dimension.
6. Derive the risk band.
7. Complete an Agent Authority Dossier.
8. Define evidence, review, revocation, and renewal requirements.

## Scope

This protocol is for pre-deployment classification.

It does not:

- authenticate the agent
- authorize API access
- enforce runtime policy
- monitor live behavior
- replace security review
- replace legal, compliance, or audit review

It should help teams scope those reviews before authority is granted.

## Minimal Classification Record

```yaml
agent: ""
classification: A0-R0-D0
derived_risk: Minimal
owner: ""
human_sponsor: ""
approval_status: proposed
expiration_date: ""
```

## Review Principle

The highest-risk dimension should dominate the review process.

A low-autonomy agent with financial, legal, compliance, production, or delegation reach may still require high-risk controls.

## Renewal Principle

Authority should not be permanent by default.

Any agent classified as `A5`, `A6`, `R5`, `R6`, `D3`, or `D4` should have:

- named owner
- explicit expiration date
- revocation path
- evidence retention requirement
- periodic review cadence
