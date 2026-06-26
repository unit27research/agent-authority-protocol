# Agent Authority Protocol

`PUBLIC_PACKAGE // AUTHORITY_CLASSIFICATION_PROTOCOL`

An open proposal for classifying delegated authority in AI agents before deployment.

```text
AGENT AUTHORITY PROTOCOL

CLASS: ADJACENT PROTOCOL
UNIT27_POSITION: ADJACENT_AUTHORITY_CLASSIFICATION_PROTOCOL
FUNCTION: Authority-Reach-Delegation Classification
REF_ID: AGENT-AUTHORITY-PROTOCOL
PRIMARY_SURFACE: AGENT_AUTHORITY_REVIEW
```

## Release Status

`SOURCE_STATUS: PUBLIC_PACKAGE`
`ACCESS_STATUS: CLEARED_FOR_EXTERNAL_USE`

This repository is a Unit27 public protocol package: visible, inspectable, and intended for orientation, testing, and practical use. Controlled Unit27 materials remain outside this source package.

It answers one narrow question:

> What authority has actually been delegated to this agent?

AI agents are beginning to receive tools, credentials, memory, workflow access, and autonomy. Identity systems can tell us who an agent is. Access systems can tell us what an agent can technically reach. Security frameworks can help teams detect and mitigate threats.

The Agent Authority Protocol uses the Authority-Reach-Delegation model, or ARD, to describe an agent's authority, reach, and delegation rights before it is deployed.

```text
A#-R#-D#
```

Example:

```text
A3-R4-D1
```

Meaning:

- `A3`: the agent may prepare and execute actions only after explicit human approval
- `R4`: the agent can affect financial systems or decisions
- `D1`: the agent may invoke approved helper agents or tools inside a fixed workflow

## Why This Exists

Existing work addresses agent identity, authorization, autonomy levels, runtime security, risk management, and governance controls. This proposal focuses on a smaller operational gap: a compact pre-deployment classification for the authority, reach, and delegation rights assigned to an AI agent.

The protocol is intended to complement, not replace, IAM, NIST AI RMF, OWASP guidance, ISO/IEC 42001, SOC 2 controls, runtime monitoring, security review, legal review, or compliance review.

It is useful when a team needs to answer:

- What can this agent decide or do?
- What people, systems, data, or domains can it affect?
- Can it invoke, coordinate, create, or empower other agents?
- What evidence should be retained before and after deployment?

## Relation To AI Agent Governance

This project sits inside the broader AI agent governance, agentic AI governance, agent security, and agent control systems conversation.

Its scope is narrower than a governance platform or runtime enforcement toolkit. Agent Authority Protocol focuses on the pre-deployment authority classification step: what the agent may do, what it can affect, and whether authority can move through delegation chains.

Use it before governance, identity, security, or reliability tooling needs to decide which controls apply.

## Where It Fits

Agent Authority Protocol is not part of the Unit27 Field Kit Suite operating sequence yet.

It sits beside that chain as an adjacent authority-classification protocol for agentic work. Use it when a project is about to give an AI agent tools, credentials, workflow access, production reach, external communication rights, or delegation rights.

Recommended placement:

```text
Context prepared -> Knowledge classified -> Agent authority classified -> Handoff written -> Evals run -> Proof recorded -> Claim bounded -> Launch checked
```

It is especially relevant before:

- Handoff Engine work packets become agent execution instructions
- Zero-Env Proxy or other credential boundaries route tool access
- a coding agent receives repository write access
- a support, finance, legal, compliance, or DevOps agent receives operational authority
- any agent can invoke, coordinate, create, or authorize other agents

## Authority-Reach-Delegation (ARD) Model

ARD has three dimensions:

| Dimension | Question |
|---|---|
| Authority | What decisions or actions may the agent perform? |
| Reach | What people, systems, data, or business domains can the agent affect? |
| Delegation | Can the agent invoke, orchestrate, create, or authorize other agents? |

The full classification uses this format:

```text
A#-R#-D#
```

In this project, `ARD classification` refers to this Authority-Reach-Delegation model.

## Why Authority Is The First Axis

The authority classes are the center of the protocol.

Before a team argues about model choice, agent framework, runtime monitoring, or access-control implementation, it should be able to say what authority is being delegated:

- Is the agent only observing?
- Is it advising?
- Is it drafting?
- Is it acting after approval?
- Is it operating autonomously inside bounds?
- Is it making operational decisions?
- Is it able to delegate authority to other agents?

The distinction matters because `A6` is not just more autonomy. It is authority propagation.

## Quick Examples

| Agent | Classification | Derived Risk |
|---|---:|---|
| Read-only research agent | `A1-R0-D0` | Minimal |
| LinkedIn content drafter | `A2-R1-D0` | Low |
| Customer support responder | `A4-R3-D1` | Moderate to High |
| GitHub coding agent with PR approval | `A3-R6-D1` | High |
| Autonomous DevOps agent | `A5-R6-D2` | Critical |
| Agent factory with production authority | `A6-R6-D4` | Extreme |

## Documents

- [Protocol Overview](protocol.md)
- [Authority Classes](authority-classes.md)
- [Reach Classes](reach-classes.md)
- [Delegation Classes](delegation-classes.md)
- [Risk Derivation](risk-derivation.md)
- [Agent Authority Dossier](agent-authority-dossier.md)
- [Evidence Requirements](evidence-requirements.md)
- [Risk Scorecard YAML](risk-scorecard.yaml)
- [Delegation Chain Schema](delegation-chain-schema.yaml)
- [Prior Art and Related Work](prior-art-and-related-work.md)
- [Claim Boundaries](docs/claim-boundaries.md)
- [Release Boundary](docs/release-boundary.md)
- [Boundary Register](u27/BOUNDARY_REGISTER.md)
- [Proof Packet](u27/PROOF_PACKET.md)

## Examples

- [Research Agent](examples/research-agent.md)
- [LinkedIn Content Agent](examples/linkedin-content-agent.md)
- [Customer Support Agent](examples/customer-support-agent.md)
- [GitHub Coding Agent](examples/github-coding-agent.md)
- [Finance Agent](examples/finance-agent.md)
- [Autonomous DevOps Agent](examples/autonomous-devops-agent.md)
- [Agent Factory](examples/agent-factory.md)

## Mappings

- [NIST AI RMF](mappings/nist-ai-rmf.md)
- [NIST Agent Identity and Authorization Concepts](mappings/nist-agent-identity.md)
- [OWASP Agentic Security](mappings/owasp-agentic-top-10.md)
- [SOC 2](mappings/soc2.md)
- [ISO/IEC 42001](mappings/iso-42001.md)

## Status

This is a v0.1 community proposal. It is not an official standard.

## License

MIT. The protocol docs, templates, schemas, examples, and local verifier are released for reuse in documentation, review workflows, and lightweight tooling.

## Verify

Run the public package checks:

```bash
python3 scripts/verify_public_release.py
```

The check verifies required files, YAML parsing, example coverage, Unit27 release status, boundary docs, and forbidden public-claim language.

## Disclaimer

This project is not legal, compliance, security, audit, procurement, insurance, or professional advice. Use it as a classification and documentation aid, not as a substitute for qualified review.

## Contributing

Contributions are welcome, especially:

- clearer class definitions
- real-world example dossiers
- mappings to existing control frameworks
- schema improvements
- evidence requirements for specific agent patterns
