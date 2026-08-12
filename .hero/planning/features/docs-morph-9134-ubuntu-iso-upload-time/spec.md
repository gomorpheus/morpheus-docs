---
title: "Uploading Ubuntu ISO Load Time"
slug: docs-morph-9134-ubuntu-iso-upload-time
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, linux, iso]
tracker_id: MORPH-9134
jira_status: New
parent: docs-morph-3266-enhancements
relates-to:
  - docs-morph-8604-hvm-iso-local-vs-url
  - docs-morph-9204-windows-iso-upload-time
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---

# Uploading Ubuntu ISO Load Time

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9134

Exact Jira description (delivery source requirement):

> I am following the documentation “Configuring Linux Images for Use with HVM Clusters”
>
> You can see step 1 says: 
>
> ![](blob:https://media.staging.atl-paas.net/?type=file&localId=28daa46c1661&id=761310fb-5132-44d8-8b1d-06be3fb60600&&collection=&height=578&occurrenceKey=null&width=1176&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
> Because of this, I went to [ubuntu.com/downloads/desktop](http://ubuntu.com/downloads/desktop)
>
> ![](blob:https://media.staging.atl-paas.net/?type=file&localId=908a8f8bb070&id=f702d23d-a9f7-475f-86c9-bd367aaadc02&&collection=&height=946&occurrenceKey=null&width=1850&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
> And I downloaded 24.0.4 to my local downloads folder. I then dragged and dropped into the “Drop Files Here” according to step 2. This loading screen to 2 hours to complete. I have a stable network connection and went through the HPE VPN. The networking team noted that they expected this to take a long time. 
>
> Either this should be changed to a download method that is faster or the documentation should note that the wait times are extremely long. I tried to do this yesterday but because I let my screen time out it got stuck and never finished: 
>
> ![](blob:https://media.staging.atl-paas.net/?type=file&localId=0f942887c1e2&id=699571d8-2d07-4d42-8053-913f7553d370&&collection=&height=753&occurrenceKey=null&width=1750&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
> (This was not a refresh issue, I refreshed multiple times and logged in again twice). If the user has to not have their screen time out it cannot take 2 hours for a download to occur. This will lead to a lot of frustration.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9134 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9134-ubuntu-iso-upload-time/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `library/virtual_images/virtual_images.rst`
- `infrastructure/clusters/hvm/guest_os_notes.rst`
- `getting_started/installation/singleNode/hpe_installer.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Clarify supported Ubuntu ISO acquisition/upload methods, browser-session expectations, progress checks, and recovery from stalled uploads without asserting a fixed duration.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `library/virtual_images/virtual_images.rst` to carry the primary procedure and verified guidance.
2. Update `infrastructure/clusters/hvm/guest_os_notes.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `getting_started/installation/singleNode/hpe_installer.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9134
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

- All Jira screenshots are inaccessible and the two-hour timing is anecdotal. Validate supported alternate upload methods and session-timeout behavior.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
