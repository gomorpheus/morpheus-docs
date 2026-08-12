---
title: "UBS- Environments Concept in HPE VM Essentials – Limited Documentation and Unclear Functional Usage"
slug: docs-morph-10111-vme-environments-concept
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vme, environments, rbac]
tracker_id: MORPH-10111
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:32Z
---

# UBS- Environments Concept in HPE VM Essentials – Limited Documentation and Unclear Functional Usage

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-10111

Exact Jira description (delivery source requirement):

> The current documentation for the _Environments_ concept in HPE VM Essentials is limited and does not clearly explain its intended purpose or usage.
>
> * **Unclear Functional Role**
>
>     * It is not clear whether _Environments_ influence:
>     
>         * VM placement
>         * Policies or configurations
>         * Operational behavior within the platform
>         
>     * No clear examples or workflows are provided in the documentation.
>     
> * **RBAC / Access Control Ambiguity**
>
>     * There is no documented mechanism to apply Role-Based Access Control (RBAC) using _Environments_.
>     * It is unclear whether _Environments_ are intended to be used for logical isolation or access segmentation.
>     
>
> Kindly provide clarity on the following:
>
> * What are the **intended use cases** of the _Environments_ feature?
> * Does _Environment_ have any **functional impact** on system behavior, policies, or VM lifecycle?
> * Are there plans to support:
>
>     * Filtering and grouping based on Environment
>     * RBAC integration using Environment
>     
> * If currently informational only, can this be explicitly documented?
>

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-10111 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-10111-vme-environments-concept/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `administration/settings/environments.rst`
- `provisioning/instances/creating_instances.rst`
- `administration/roles/role_permissions.rst`
- `getting_started/guides/instance_tabs.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Expand the Environments concept page with verified purpose, lifecycle effects, filtering/grouping behavior, RBAC limitations, and concrete workflows; explicitly label informational-only behavior where applicable.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. `administration/settings/environments.rst` — Documented InstanceContextType purpose, metadata effects, required selection, and non-RBAC/non-placement boundary.
2. `provisioning/instances/creating_instances.rst` — Documented stored Instance context, filtering, naming-variable use, and RBAC boundary.
3. `administration/roles/role_permissions.rst` — Distinguished Environment administration permission from workload access control.
4. `getting_started/guides/instance_tabs.rst` — Clarified that Environment-based plugin visibility is custom logic, not native RBAC.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-10111
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

- Product ownership must answer the Jira questions about placement, policy, lifecycle, filtering, and RBAC. Until then, those behaviors are unresolved blockers, not documentation facts.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
