---
title: "Document the 'Allow-List' CS Required URLs behind on-premise proxy"
slug: docs-morph-7982-central-service-allow-list
type: feature
status: completed
horizon: now
size: small
tags: [documentation, proxy, central-service, connectivity, security]
tracker_id: MORPH-7982
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:41Z
---
# Document the 'Allow-List' CS Required URLs behind on-premise proxy

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7982

> With releasing central-service, on prem morpheus appliances need to allow central service Greenlake URLs and also the HPE RDA URL to Morpheus Proxy. Central service URLs: tunnel-eu1.data.cloud.hpe.com, tunnel-jp1.data.cloud.hpe.com, tunnel-uae1.data.cloud.hpe.com, tunnel-uk1.data.cloud.hpe.com, tunnel-us1.data.cloud.hpe.com. RDA URL: https://midway.ext.hpe.com. The suggested target is the Internet Connectivity (optional) section.

The repository’s Internet Connectivity list is in `getting_started/requirements/requirements.rst`; proxy configuration is covered by `getting_started/additional/proxies.rst` and `administration/settings/proxy.rst`.

## Goal
Add a security-reviewed, version-scoped allow-list entry for Central Service tunnel regions and RDA connectivity, including protocol, port, direction, purpose, and conditions under which each endpoint is required.

## Kickoff
Audit `getting_started/requirements/requirements.rst`, `getting_started/additional/proxies.rst`, and `administration/settings/proxy.rst`. Obtain the authoritative Central Service/RDA endpoint registry, HTTPS/WSS protocols, ports, outbound direction, DNS wildcard policy, regional selection behavior, release floor, and whether `midway.ext.hpe.com` is customer-facing and stable. Jira’s host list alone is insufficient for firewall guidance. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Extend the canonical connectivity table and cross-link proxy setup, avoiding repeated endpoint lists.

## Changes
1. Add approved endpoint rows and qualifiers to the Internet Connectivity table in `getting_started/requirements/requirements.rst`.
2. Add a concise allow-list cross-reference and proxy-routing considerations to `getting_started/additional/proxies.rst`.
3. Audit `administration/settings/proxy.rst` for the correct configuration path and link to canonical requirements.

## Acceptance Criteria
- WHEN the applicable Central Service or Remote Data Access feature is enabled THE DOCUMENTATION SHALL list the proven ``midway.ext.hpe.com`` outbound HTTPS/TCP 443 requirement.
- THE DOCUMENTATION SHALL distinguish optional feature connectivity from baseline appliance requirements.
- IF a proposed tunnel endpoint is not proven stable and customer-facing THEN THE DOCUMENTATION SHALL not publish it and SHALL direct the reader to the current HPE endpoint registry.
- THE DOCUMENTATION SHALL maintain one canonical endpoint list.

## Boundaries
No proxy implementation, firewall rule automation, or inferred wildcard/domain policy.

## Risks
Incorrect endpoint guidance can break service or expose unnecessary egress. Delivery is blocked pending Central Service, RDA, networking, and security approval.

## Validation
Test documented egress through an on-prem proxy, verify DNS/TLS connectivity for each applicable region, build docs, and obtain service-owner sign-off.
