---
title: "[VME version:8.1.0]:\"Cluster Permissions\" section is not having detailed information in HPE Morpheus VME Document"
slug: docs-morph-9608-cluster-permissions-impact
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vme, clusters, permissions]
tracker_id: MORPH-9608
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---

# [VME version:8.1.0]:"Cluster Permissions" section is not having detailed information in HPE Morpheus VME Document

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9608

Exact Jira description (delivery source requirement):

> Setup: PCBE Greenfield VME  
> Agent Version: 3.1.3  
> VME Manager: 8.1.0  
> Storage plugin: 1.9.2
>
> As per the document “[Cluster Permissions | HPE Morpheus VM Essentials Software Documentation v8.1.0](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007520en_us&page=GUID-2581C2D1-AC07-4DE2-B794-20AC25652417.html)[”](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007520en_us&page=GUID-FB7D15CC-A606-42DC-9DBF-27778D20282D.html%E2%80%9D)
>
> “Cluster Permissions” field in VME document just mentioned about the ‘Groups’ and Service Plan' options availability.
>
> But there is no specific information about the change of the permission in this page where will be the impact or in which page it will be impact.
>
> Say Ex, if user select the Service Plan ‘1CPU 2GB’ alone from the list, then what's the impact in Instance Creation page where these Service Plan will list is not mentioned.
>
> Also NO information about ‘Default’ option is documented.  VME Environment: [https://10.157.232.173](https://10.157.232.173/)
>
> **Steps to Reproduce**:
>
> 1.Connect to VME and Go to 'Cluster' > Permission under the Actions
>
> 2. Check ‘Group & Service Plan’ level Permissions available with default option as wel
>

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9608 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9608-cluster-permissions-impact/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `infrastructure/clusters/hvm/building_clusters.rst`
- `administration/roles/role_permissions.rst`
- `provisioning/instances/creating_instances.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Explain Group, Service Plan, and Default cluster permission semantics and show their observable impact on instance-creation choices with a validated example.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `infrastructure/clusters/hvm/building_clusters.rst` to carry the primary procedure and verified guidance.
2. Update `administration/roles/role_permissions.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `provisioning/instances/creating_instances.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9608
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

- Product/RBAC SME confirmation is required for inheritance, Default semantics, precedence, and UI impact; the Jira example is a question, not established behavior.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
