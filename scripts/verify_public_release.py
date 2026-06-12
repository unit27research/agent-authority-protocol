#!/usr/bin/env python3
"""Verify the public release surface for the Agent Authority Protocol draft."""

from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "protocol.md",
    "authority-classes.md",
    "reach-classes.md",
    "delegation-classes.md",
    "risk-derivation.md",
    "agent-authority-dossier.md",
    "evidence-requirements.md",
    "risk-scorecard.yaml",
    "delegation-chain-schema.yaml",
    "prior-art-and-related-work.md",
    "docs/claim-boundaries.md",
    "docs/release-boundary.md",
    "u27/BOUNDARY_REGISTER.md",
    "u27/PROOF_PACKET.md",
    "LICENSE",
    ".github/workflows/ci.yml",
    "requirements-dev.txt",
]

REQUIRED_EXAMPLES = [
    "examples/research-agent.md",
    "examples/linkedin-content-agent.md",
    "examples/customer-support-agent.md",
    "examples/github-coding-agent.md",
    "examples/finance-agent.md",
    "examples/autonomous-devops-agent.md",
    "examples/agent-factory.md",
]

FORBIDDEN_PHRASES = [
    "first AI agent authority standard",
    "official standard",
    "makes agent deployment safe",
    "certifies an AI agent",
    "solves agent governance",
    "enterprise-ready",
    "market-validated",
]

CLAIM_BOUNDARY_FILES = {
    Path("docs/claim-boundaries.md"),
}

LINE_LEVEL_ALLOWED_CONTEXTS = [
    "not an official standard",
    "official standards status",
    "no public copy claims official standard status",
    "enterprise-ready or market-validated",
]


def fail(message: str) -> None:
    print(f"FAIL {message}")
    sys.exit(1)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check_required_files() -> None:
    missing = [path for path in REQUIRED_FILES + REQUIRED_EXAMPLES if not (ROOT / path).exists()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")


def check_yaml() -> None:
    required_keys = {
        "risk-scorecard.yaml": {
            "protocol",
            "model",
            "model_abbreviation",
            "classification",
            "derived_risk",
            "agent",
            "controls",
            "evidence",
        },
        "delegation-chain-schema.yaml": {
            "protocol",
            "schema",
            "model",
            "model_abbreviation",
            "root_principal",
            "agent",
            "delegated_authority",
            "delegation_chain",
            "revocation",
        },
    }
    for path, keys in required_keys.items():
        with (ROOT / path).open("r", encoding="utf-8") as handle:
            parsed = yaml.safe_load(handle)
        if not isinstance(parsed, dict):
            fail(f"{path} did not parse to a mapping")
        missing = sorted(keys - set(parsed.keys()))
        if missing:
            fail(f"{path} missing YAML keys: {', '.join(missing)}")


def check_release_status() -> None:
    readme = read("README.md")
    for token in [
        "SOURCE_STATUS: PUBLIC_PACKAGE",
        "ACCESS_STATUS: CLEARED_FOR_EXTERNAL_USE",
        "UNIT27_POSITION: ADJACENT_AUTHORITY_CLASSIFICATION_PROTOCOL",
        "Authority-Reach-Delegation",
        "A#-R#-D#",
    ]:
        if token not in readme:
            fail(f"README missing release token: {token}")


def check_forbidden_claims() -> None:
    markdown_paths = sorted(ROOT.rglob("*.md"))
    for path in markdown_paths:
        rel = path.relative_to(ROOT)
        if rel in CLAIM_BOUNDARY_FILES:
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            lower = line.lower()
            if any(context in lower for context in LINE_LEVEL_ALLOWED_CONTEXTS):
                continue
            for phrase in FORBIDDEN_PHRASES:
                if phrase.lower() in lower:
                    fail(f"forbidden public-claim phrase in {rel}:{line_number}: {phrase}")


def main() -> None:
    check_required_files()
    check_yaml()
    check_release_status()
    check_forbidden_claims()
    print("PASS public release surface verified")


if __name__ == "__main__":
    main()
