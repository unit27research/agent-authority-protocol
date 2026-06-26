# Prior Art and Related Work

The Agent Authority Protocol is not presented as the first work on AI agent governance, autonomy, delegation, identity, authorization, or security.

It is a lightweight pre-deployment classification proposal built around the Authority-Reach-Delegation model, or ARD. ARD is intended to complement adjacent work.

## NIST AI Risk Management Framework

The NIST AI RMF is a voluntary framework for managing risks to individuals, organizations, and society associated with AI. The Agent Authority Protocol can support AI RMF-style governance by providing a compact pre-deployment record of agent authority, reach, delegation rights, evidence expectations, and review status.

Source: https://www.nist.gov/itl/ai-risk-management-framework

## OWASP Agentic Security Initiative

OWASP's Agentic Security Initiative addresses security risks in autonomous agents and multi-step AI workflows. The OWASP Agentic Applications work covers risks including tool misuse, identity and privilege abuse, insecure inter-agent communication, cascading failures, trust exploitation, and rogue agents.

The Agent Authority Protocol is not a threat taxonomy. It can help teams classify an agent before applying OWASP-style controls and mitigations.

Sources:

- https://genai.owasp.org/initiatives/agentic-security-initiative/
- https://genai.owasp.org/resource/aiuc-1-crosswalks-owasp-top-10-for-agentic-applications/
- https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/

## Microsoft Agent Governance Toolkit

Microsoft's Agent Governance Toolkit addresses a broader AI agent governance surface, including policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous agents.

The Agent Authority Protocol has a narrower role. It can be used before runtime governance tooling to record the agent's Authority-Reach-Delegation classification and identify which authority, reach, delegation, evidence, and review controls should be considered.

Source: https://github.com/microsoft/agent-governance-toolkit

## Autonomy-Level Frameworks

Academic and industry work already classifies AI agents by autonomy level. For example, "Levels of Autonomy for AI Agents" treats autonomy level as a deliberate design decision and describes escalating levels through the user's role in relation to the agent.

The Agent Authority Protocol builds on this general direction, but separates Authority from Reach and Delegation.

Source: https://arxiv.org/abs/2506.12469

## Authenticated Delegation and Authorized AI Agents

"Authenticated Delegation and Authorized AI Agents" proposes authenticated, authorized, and auditable delegation of authority to AI agents, extending identity and access concepts such as OAuth and OIDC.

The Agent Authority Protocol is not an authentication or authorization implementation. It is a pre-deployment classification layer that can help document what authority should be represented in those systems.

Source: https://arxiv.org/abs/2501.09674

## Authorization Propagation and Delegation Chains

Recent research has focused on authorization propagation, recursive delegation, inherited scopes, temporal validity, and verifiable delegation chains in multi-agent systems.

Relevant work includes:

- "Authorization Propagation in Multi-Agent AI Systems"
- "Overlaying Governance: A Compositional Authorization Framework for Delegation and Scope in Agentic AI"
- "SentinelAgent: Intent-Verified Delegation Chains for Securing Federal Multi-Agent AI Systems"

The Agent Authority Protocol treats delegation as one of three classification axes and provides a practical review artifact for early-stage governance.

Sources:

- https://arxiv.org/abs/2605.05440
- https://arxiv.org/abs/2606.03518
- https://arxiv.org/abs/2604.02767

## ISO/IEC 42001

ISO/IEC 42001 is an AI management system standard for establishing, implementing, maintaining, and improving an AI management system.

The Agent Authority Protocol can support ISO/IEC 42001-aligned documentation by making agent authority, reach, delegation, review, and evidence requirements easier to record.

Source: https://www.iso.org/standard/42001

## SOC 2

SOC 2 reports focus on controls relevant to security, availability, processing integrity, confidentiality, or privacy.

The Agent Authority Protocol does not provide SOC 2 compliance. It can provide supporting documentation for agent-related control scoping, especially where agents affect access, change management, operational workflows, evidence retention, or data handling.

Source: https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services

## Gartner-Style Proportional Governance

Public reporting on Gartner research has emphasized that one-size-fits-all agent governance can fail when organizations do not distinguish agent autonomy from access scope.

The Agent Authority Protocol aligns with proportional governance but makes the classification more portable through the ARD model and `A#-R#-D#` notation.

Sources:

- https://www.itpro.com/technology/artificial-intelligence/one-size-fits-all-agent-governance-sets-enterprises-up-to-fail
- https://www.techradar.com/pro/lack-of-ai-governance-could-force-40-percent-of-enterprises-to-roll-back-autonomous-ai-agents-by-2027

## Distinct Contribution

The protocol's distinct contribution is not the discovery of agent authority as a problem.

Its contribution is a small, usable ARD classification packet:

- Authority: what the agent may do
- Reach: what the agent can affect
- Delegation: whether authority can propagate through other agents
- Dossier: what must be documented before deployment
- Evidence requirements: what review artifacts should exist for each risk pattern
