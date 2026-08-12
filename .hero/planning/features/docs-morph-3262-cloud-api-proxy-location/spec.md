---
title: "Proxies Cloud Communication settings section"
slug: docs-morph-3262-cloud-api-proxy-location
type: feature
status: completed
horizon: now
size: small
tags: [documentation, proxies, clouds, ui-navigation]
tracker_id: MORPH-3262
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:30:03Z
---
# Proxies Cloud Communication settings section

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3262

Jira description (verbatim):

> Product Name(s) (e.g. Morpheus Enterprise, VM Essentials, PCBE, PCAI)
> * Morpheus Documents
>
> Build Number / Service(s) Version
> • 8.0.10
>
> Test Environment
> •
>
> Bug Description
> * Docs reference proxy settings in Advanced options. Proxies now have a dedicated section in the cloud settings under connection options.
>
> Steps to Reproduce
> - [Proxies | HPE Morpheus Enterprise Software Documentation v8.0.10](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00006774en_us&docLocale=en_US&page=GUID-56ECA7C7-DCE4-423D-B8E1-A429E9132E3E.html#ariaid-title4)
>
> Attachments - Relevant logs, screenshots, recordings, etc.
>
> ## Cloud Communication
>
> When morpheus needs to connect to various cloud APIs to issue provisioning commands or to sync in existing environments, we need to ensure that those api endpoints are accessible by the appliance. In some cases the appliance may be behind a proxy when it comes to public cloud access like Azure and AWS. To configure the cloud integration to utilize a proxy, when adding or editing a cloud there is a setting called “API Proxy” under “Advanced Options”. This is where the proxy of choice can be selected to instruct the Provisioning engine how to communicate with the public cloud. Simply adjust this setting and the cloud should start being able to receive/issue instructions.
>
> Note: This is now under a dedicated section **Connection Options >> API Proxy**.
>
> https://d.pr/i/a6OhBq
>
> This should be pretty obvious, but I had an instance where this field didn't appear right away after first creating the proxy setting.
>
> User Impact
> * Low, only an issue in my case because the Connection Options didn’t appear immediately after creating a proxy. Could not find setting as outlined in current docs.
>
> Frequency of Occurrence
> •
>
> Workaround
> •
>
> Priority: P3

Both `getting_started/additional/proxies.rst` and `infrastructure/networks/proxies.rst` currently say API Proxy is under Advanced Options.

## Goal

Update all proxy guidance to the current cloud edit navigation, explain when Connection Options/API Proxy becomes available, and preserve distinctions among API, provisioning, and appliance proxies.

## Kickoff

Correct stale API Proxy navigation from Advanced Options to Connection Options and verify field visibility behavior.

**Status:** planning — two stale local pages were found; the linked screenshot is external and not verified.

**Pick up at:** reproduce cloud edit after creating a proxy and capture the current field label and refresh requirements.

→ `.hero/planning/features/docs-morph-3262-cloud-api-proxy-location/spec.md`

**Files:** `getting_started/additional/proxies.rst`, `infrastructure/networks/proxies.rst`, `administration/integrations/workers.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Correct both duplicated proxy pages consistently and add a short visibility note only if reproducible. Keep API Proxy distinct from Provisioning Proxy and Worker settings.

## Changes

1. `getting_started/additional/proxies.rst` — use `Connection Options > API Proxy`, document the source-verified visibility condition, and distinguish API Proxy from workload proxy settings.
2. `infrastructure/networks/proxies.rst` — apply the same correction and distinctions.
3. `administration/integrations/workers.rst` — reviewed; no conflicting path exists, so no content change was made.

## Acceptance Criteria

- WHEN a user edits a compatible Cloud THE DOCUMENTATION SHALL direct them to `Connection Options > API Proxy`.
- THE DOCUMENTATION SHALL distinguish API Proxy from Provisioning Proxy and Worker selection.
- IF delayed field visibility is reproducible THEN THE DOCUMENTATION SHALL provide the verified refresh action; otherwise it SHALL not speculate.

## Boundaries

No proxy product changes, screenshot replacement without current assets, or broad rewrite of proxy configuration.

## Risks

- The external screenshot is not part of saved Jira output and may be stale.
- Field visibility may differ by Cloud type or permissions.

## Validation

Verify navigation on representative Clouds and roles, search for stale “API Proxy under Advanced Options” text, run `make build`, and inspect rendered links.

## Delivery Validation

- Product source: `morpheus-ui/grails-app/views/admin/siteZone/_form.gsp` and `wizard/_form.gsp` place **API Proxy** beneath the **Connection Options** legend; `MorphTagLib.hasProxiesOrWorkers` renders that section when a Tenant-visible Proxy or owned Distributed Worker exists.
- Repository search found no remaining RST statement placing API Proxy under Advanced Options.
- `make html` succeeded and rendered both updated pages. Existing repository warnings remain; none point to these edits.
- `make test` is unavailable because the Makefile routes it to an unregistered Sphinx `test` builder.
