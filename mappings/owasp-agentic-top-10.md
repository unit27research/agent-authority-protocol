# Mapping: OWASP Agentic Security

Sources:

- https://genai.owasp.org/initiatives/agentic-security-initiative/
- https://genai.owasp.org/resource/aiuc-1-crosswalks-owasp-top-10-for-agentic-applications/

OWASP's agentic security work addresses risks in autonomous and agentic AI systems. ARD can help scope which risks deserve the most attention before deployment.

## ARD Dimensions and Agentic Risk

| ARD Dimension | Related Risk Area |
|---|---|
| Authority | Tool misuse, unsafe action, rogue behavior, excessive agency |
| Reach | Identity and privilege abuse, data exposure, financial/legal/production impact |
| Delegation | Insecure inter-agent communication, cascading failures, authority propagation |

## Use With OWASP Guidance

ARD can help answer:

- Which agents require deeper threat modeling?
- Which agents require stronger logging?
- Which agents need human approval gates?
- Which agents need delegation graph review?
- Which agents should be prohibited from production access?

## Boundary

ARD is not a vulnerability taxonomy and does not replace OWASP guidance. It is a pre-deployment classification layer that can help teams decide which OWASP controls and mitigations are relevant.

