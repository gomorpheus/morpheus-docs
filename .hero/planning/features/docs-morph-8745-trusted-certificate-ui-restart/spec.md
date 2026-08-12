---
title: "Import Trusted certificate procedure needs a correction"
slug: docs-morph-8745-trusted-certificate-ui-restart
type: feature
status: completed
horizon: now
size: small
tags: [documentation, certificates, security, servicenow]
tracker_id: MORPH-8745
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:02:52Z
---

# Import Trusted certificate procedure needs a correction

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-8745

Exact Jira description (delivery source requirement):

> THis issue was reported from Customer environment when they imported ServiceNow certificate following [support.hpe.com/hpesc/public/docDisplay?docId=sd00006453en_us&docLocale=en_US&page=GUID-0BBD18FA-91D0-406A-B004-3F068114DE70.html](http://support.hpe.com/hpesc/public/docDisplay?docId=sd00006453en_us&docLocale=en_US&page=GUID-0BBD18FA-91D0-406A-B004-3F068114DE70.html).
>
> After that when they try to integrate ServiceNow from Morpheus , it was failing with SSL error. 
>
> By checking 'ignore cert verify” integration was successful and this confirms that Morpheus was not able to verify the cert.
>
> From Morpheus node, curl and openssl were able to very the servicenow cert.
>
> Finally team has figure out that Morpheus UI service needs to be restarted. 
>
> Please update this document with addition step to restart the Morpheus UI post the java keytool was imported with cert.
>
> [support.hpe.com/hpesc/public/docDisplay?docId=sd00006453en_us&docLocale=en_US&page=GUID-0BBD18FA-91D0-406A-B004-3F068114DE70.html](http://support.hpe.com/hpesc/public/docDisplay?docId=sd00006453en_us&docLocale=en_US&page=GUID-0BBD18FA-91D0-406A-B004-3F068114DE70.html) 

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-8745 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-8745-trusted-certificate-ui-restart/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `infrastructure/certificates/certificate_management.rst`
- `integration_guides/ITSM/ServiceNow.rst`
- `troubleshooting/SSL_cert_regen.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Update the trusted-certificate procedure with the validated service reload/restart and a verification check, scoped to the affected deployment topology.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. `getting_started/additional/ssl-import.rst` — Corrected the primary trusted-CA procedure, including automatic OpenSSL/JRE import and the required UI restart.
2. `infrastructure/certificates/certificate_management.rst` — Distinguished stored certificate objects from appliance JVM trust and linked the primary procedure.
3. `integration_guides/ITSM/ServiceNow.rst` — Added the trusted-CA cross-reference and rejected permanent certificate-verification bypass.
4. `troubleshooting/SSL_cert_regen.rst` — Distinguished inbound NGINX certificate regeneration from outbound JVM trust.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-8745
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

- Confirm the exact supported command, service impact, HA-node sequence, and versions. The reported UI restart is a customer finding, not yet an authoritative procedure.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
