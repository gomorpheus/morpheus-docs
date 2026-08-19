---
title: "Loading ISO from Local Download VS URL"
slug: docs-morph-8604-hvm-iso-local-vs-url
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, installation, iso]
tracker_id: MORPH-8604
jira_status: New
parent: docs-morph-3266-enhancements
relates-to:
  - docs-morph-9134-ubuntu-iso-upload-time
  - docs-morph-9204-windows-iso-upload-time
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---

# Loading ISO from Local Download VS URL

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-8604

Exact Jira description (delivery source requirement):

> The first sentence: Use the HPE-Provided HVM OS ISO to install your hosts. Download **HVM_Install\_\*\*\*\*\*\*.iso** from [My HPE Software Center](https://myenterpriselicense.hpe.com/cwp-ui/product-details/HPE_VME_EVAL/-/sw360_hpe_internal). Does not indicate any difference between downloading locally (saving the ISO to your Downloads folder and uploading from there) vs using a URL([http://10.235.0.75/software/VME/v8.0.13_2/HVM_Install_24.04_S5Q83-11038.iso](http://10.235.0.75/software/VME/v8.0.13_2/HVM_Install_24.04_S5Q83-11038.iso)). When I was using an ILO to test the documentation, uploading from local would take 30 mins-an hour to complete step 3-4. I was told by the networking team to use the URL instead because the other option is extremely slow and not as stable. I think we should note this for customers in the documentation because it took this step from at min 30 mins to 1 min using the URL. It should be noted as an option or have a tip that if it is taking a long time then use the URL version. I also always got an error when I let the screen time out between step 3-4 (attached file) so it’s necessary that this doesn’t take long enough that the customer leaves it to hang.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-8604 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-8604-hvm-iso-local-vs-url/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `getting_started/installation/hvm_host_prep.rst`
- `getting_started/installation/singleNode/hpe_installer.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Clarify supported local-upload and URL-mounted ISO paths, their prerequisites, and troubleshooting guidance without promising unverified transfer times.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `getting_started/installation/hvm_host_prep.rst` to carry the primary procedure and verified guidance.
2. Update `getting_started/installation/singleNode/hpe_installer.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-8604
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

- The attached error is unavailable and the stability/performance comparison is anecdotal; validate supported iLO methods, security constraints, and timeout behavior.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
