# Example: GitHub Coding Agent

## Classification

```text
A3-R6-D1
```

Derived risk: Critical

## Purpose

Edits code and opens pull requests for human review.

## Scope

- Can read repository files.
- Can edit source code.
- Can run tests and linters.
- Can open pull requests.
- Can invoke approved test or review tools.
- Cannot merge without human approval.
- Cannot deploy without human approval.
- Cannot modify secrets or production credentials.

## Evidence

- Commit diff
- Test logs
- Tool-call trace
- Pull request record
- Human approval record
- Approval packet shown to the human reviewer

## Controls

- Branch protection required.
- Human approval required before merge.
- Production deployment requires a separate approval gate.
- Secrets, environment variables, and release settings are out of scope unless explicitly approved.
