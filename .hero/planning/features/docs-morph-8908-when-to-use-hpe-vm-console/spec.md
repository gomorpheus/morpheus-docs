---
title: "When to configure the HVM host using hpe-vm console"
slug: docs-morph-8908-when-to-use-hpe-vm-console
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, networking, console]
tracker_id: MORPH-8908
jira_status: New
parent: docs-morph-3266-enhancements
relates-to:
  - docs-morph-8909-hpe-vm-console-unsaved-changes
  - docs-morph-8910-hpe-vm-console-exit-display
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---

# When to configure the HVM host using hpe-vm console

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-8908

Exact Jira description (delivery source requirement):

> I finished installing the HVM hosts and was confused at if using the Configuring the HVM host using hpe-vm console was required for me, especially because I’d already gone through setting up time zone with the last steps in Installing HVM OS on host servers document and I had already configured the network. I am using a LACP set up instead of the suggested active backup networking setup (the networking team has said LACP is more stable which is why I am using that, I don’t know why it’s recommended to use a different set up if the networking team is not testing on it).
>
> ‌
>
> I asked the team if I should use the Configuring the HVM host using the hpe-vm console and I had to just check that LACP rate was fast which was already configured when creating a bond.
>
> ‌
>
> I think there should be more in the About this task section about when the document applies and that most steps only apply to active backup setups. I think it should be explicit how it’s different than the previous document’s configuration steps to avoid confusion.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-8908 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-8908-when-to-use-hpe-vm-console/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `getting_started/installation/hvm_host_prep.rst`
- `tools/hvmcli/getting_started.rst`
- `tools/hvmcli/network.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Add applicability and handoff guidance explaining when post-install console configuration is required, especially for active-backup versus LACP configurations.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `getting_started/installation/hvm_host_prep.rst` to carry the primary procedure and verified guidance.
2. Update `tools/hvmcli/getting_started.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `tools/hvmcli/network.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-8908
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

- Validate supported bond modes and whether the named hpe-vm console content has moved to hvmcli before asserting workflow differences.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
