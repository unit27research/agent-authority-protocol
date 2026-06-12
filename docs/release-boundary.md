# Release Boundary

Agent Authority Protocol is released as a Unit27 public protocol package.

## Release Shape

```text
SOURCE_STATUS: PUBLIC_PACKAGE
ACCESS_STATUS: CLEARED_FOR_EXTERNAL_USE
UNIT27_POSITION: ADJACENT_AUTHORITY_CLASSIFICATION_PROTOCOL
PRIMARY_SURFACE: AGENT_AUTHORITY_REVIEW
```

The repository is intended for public orientation, review, and practical use.

Controlled Unit27 materials, private registry notes, unpublished protocol diagrams, and internal research notes remain outside this source package.

## What This Release Includes

- Authority-Reach-Delegation model
- `A#-R#-D#` classification format
- authority classes
- reach classes
- delegation classes
- derived risk bands
- Agent Authority Dossier template
- evidence requirements
- risk scorecard YAML
- delegation chain schema
- example agent classifications
- related-work mapping
- public claim boundaries

## What This Release Does Not Include

- official standards status
- legal or compliance opinion
- runtime enforcement
- IAM integration
- agent authentication
- API authorization
- production certification
- internal Unit27 registry materials

## Where It Fits

Agent Authority Protocol sits beside the Unit27 public field-kit chain as an adjacent protocol.

It can be used before an agent receives:

- tool access
- credential routing
- repository write access
- customer-facing communication rights
- financial, legal, compliance, or production reach
- delegation rights over other agents

## Release Standard

Before public release:

1. Run `python3 scripts/verify_public_release.py`.
2. Confirm all public claims remain inside `docs/claim-boundaries.md`.
3. Confirm `prior-art-and-related-work.md` names adjacent work.
4. Confirm YAML examples parse.
5. Confirm example dossiers cover common agent types.
6. Confirm no public copy claims official standard status, adoption, safety outcomes, or compliance effect.

