---
title: "Migration requirements need updated "
slug: docs-morph-10279-migration-dns-requirement
type: feature
status: completed
horizon: now
size: small
tags: [documentation, migration, hvm, vmware, dns]
tracker_id: MORPH-10279
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:30:03Z
---
# Migration requirements need updated 

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-10279

Migration currently documents connectivity to ESXi hosts but does not explicitly require HVM hosts to resolve ESXi host FQDNs through DNS.

## Goal
State and operationalize the forward-DNS prerequisite before VMware-to-HVM migration begins.

## Kickoff
Deliver `.hero/planning/features/docs-morph-10279-migration-dns-requirement/spec.md`; update `tools/migrations/requirements.rst` and cross-check `tools/migrations/overview.rst`.

## Approach
Add the requirement beside existing source-host connectivity checks, including a preflight validation command and failure symptom.

## Changes
1. `tools/migrations/requirements.rst` — require every participating HVM host to resolve each source ESXi FQDN when ESXi is registered in vCenter by FQDN, provide a `getent hosts` preflight, and keep port connectivity separate.
2. `tools/migrations/overview.rst` — add the DNS prerequisite to the architecture summary and link to the detailed checks.

## Acceptance Criteria
- WHEN an operator prepares a VMware-to-HVM migration THE SYSTEM SHALL require successful ESXi FQDN resolution from every HVM host.
- IF name resolution fails THEN THE SYSTEM SHALL direct the operator to correct DNS/host records before migration.
- THE SYSTEM SHALL distinguish name resolution from network port connectivity.

## Boundaries
No DNS server configuration guide or migration code changes.

## Risks
The requirement may involve short names, reverse DNS, or certificates in addition to forward FQDN lookup; engineering must confirm the exact contract.

## Validation
Technical review by migration engineering, build the affected pages, verify navigation and commands, and run `make test`.

## Delivery Validation

- Jira comment 3270895 from Tyler Boyd confirms that HVM hosts must resolve ESXi FQDNs when ESXi servers are added to vCenter by FQDN, otherwise migration fails.
- `make html` succeeded; the rendered overview links to the rendered requirements page, and the name-resolution and HTTPS connectivity checks render as separate requirements.
- `make test` is unavailable because the Makefile routes it to an unregistered Sphinx `test` builder.
