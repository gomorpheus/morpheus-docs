---
title: "Documentation update request: Correct usage of \"allLabels\" parameter in Networks API"
slug: docs-morph-9115-networks-api-alllabels
type: feature
status: completed
horizon: now
size: small
tags: [documentation, api, networks, labels]
tracker_id: MORPH-9115
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:32Z
---

# Documentation update request: Correct usage of "allLabels" parameter in Networks API

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9115

Exact Jira description (delivery source requirement):

> When using the **"allLabels"** filter to retrieve networks that should match all the provided labels, the API is not returning the expected results. For example, when filtering with: `allLabels: ENV.NIT, SERVICE.LNX_AP_WLS` the API is returning an empty list instead of the expected networks.  
>   
> However, when using an **“allFilter”** with the following format it’s working fine.  
> `?allLabels=ENV.NIT&allLabels=SERVICE.LNX_AP_WLS`
>
>   
> This needs to be updated clearily in our documentation to how we can use multiple Label with **“allLabels”** and filter the networks.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9115 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9115-networks-api-alllabels/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `infrastructure/networks/networks.rst`
- `infrastructure/networks/network.rst`
- `infrastructure/networks/network_scopes.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Document repeated allLabels query parameters with an encoded request example and distinguish match-all behavior from other label filters.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. `infrastructure/networks/networks.rst` — Added repeated-parameter match-all API guidance and example.
2. `infrastructure/networks/network.rst` — Added a cross-reference to the canonical API guidance.
3. `infrastructure/networks/network_scopes.rst` — Distinguished scopes from Labels and linked the canonical guidance.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9115
- IF a reported behavior cannot be reproduced or confirmed THEN THE DOCUMENTATION SHALL omit it or label the supported limitation using approved product wording
- THE DOCUMENTATION SHALL use current repository navigation, terminology, formatting, and cross-references across every changed file
- THE DOCUMENTATION SHALL preserve the Jira-requested correction while avoiding unsupported timing, compatibility, security, or operational guarantees
- WHEN the documentation build and link checks run THE SYSTEM SHALL complete without new warnings or broken internal references caused by these changes

## Boundaries

- Do not change product code, API behavior, UI behavior, or release support policy.
- Do not broaden this issue into a general rewrite of adjacent documentation.
- Do not add inaccessible Jira media to the repository or reconstruct screenshots from descriptions.
- Do not publish commands, defaults, compatibility claims, or destructive operations until an authoritative owner verifies them.

## Risks

- Verify the Networks API contract and identify the generated API-reference source; no API specification file was located in the documentation repository search.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
