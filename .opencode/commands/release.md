---
description: Assess release readiness, deployment concerns, and operational risk.
---
Route this release request to the appropriate specialist based on the focus.

## Pre-flight: Documentation freshness

Before assessing release readiness, **always run `hero docs check`** to verify that README.md and GETTING-STARTED.md are current. This checks:
- Agent, command, and skill counts match actual files
- Every agent, command, and skill is mentioned in the README
- No stale references to removed or renamed items

If `hero docs check` reports issues, **fix them before proceeding with the release assessment.** Update README.md and GETTING-STARTED.md to reflect the current state of the project. Counts, tables, and reference sections must match what's actually in the repo.

## Routing

Determine the work type from the request:
- Release readiness, versioning, changelog, rollout assessment → delegate to `release-engineer`
- CI/CD, deployment setup, environment, operational changes → delegate to `devops-engineer`
- If both are relevant, start with `release-engineer` for the readiness assessment

Release request: $ARGUMENTS
