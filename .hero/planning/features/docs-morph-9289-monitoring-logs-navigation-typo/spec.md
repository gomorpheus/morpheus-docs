---
title: "The \"Monitoring->Overview->Logs\" section requires Configuration & Typo update"
slug: docs-morph-9289-monitoring-logs-navigation-typo
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, monitoring, logging, navigation]
tracker_id: MORPH-9289
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:32Z
---

# The "Monitoring->Overview->Logs" section requires Configuration & Typo update

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9289

Exact Jira description (delivery source requirement):

> 1. 
>
> On the HPE Support page for "HPE Morpheus Enterprise Software Documentation":  
> [https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007510en_us&page=GUID-8E6A77CF-6AED-4725-BD4B-566E2FA357DB.html](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007510en_us&page=GUID-8E6A77CF-6AED-4725-BD4B-566E2FA357DB.html)
>
> The "Configuration" section reads:
>
> ```
> Configuration
> Logging configuration can be setup in the Administration > Settings > Logs section.
> ```
>
> However, this logging section has been moved to:
>
> ```
> Administration->Settings->Monitoring->Logging Settings	
> ```
>
> 2. 
>
> On the same HPE Support page, under section "Activity Log", Procedure Step #6 reads:
>
> ```
> Once you see the ASCI art show up you will be able to log back into the User Interface.
> ```
>
> "ASCI" should be "ASCII".

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9289 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9289-monitoring-logs-navigation-typo/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `monitoring/logs.rst`
- `administration/settings/logs.rst`
- `operations/activity.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Correct the Logging Settings navigation path and the ASCI/ASCII typo, checking nearby cross-references for the same stale path.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. `monitoring/logs.rst` — Corrected the Monitoring > Logging Settings path and ASCII typo.
2. `administration/settings/logs.rst` — Added the current Settings navigation path.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9289
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

- Confirm the navigation path for each maintained product/version variant before applying a global wording change.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
