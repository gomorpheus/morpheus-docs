---
title: "The Guide items lack sufficient detail, impacting operations."
slug: docs-morph-11025-ui-field-reference-gaps
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, ui-reference, policies, instances, storage]
tracker_id: MORPH-11025
jira_status: New
parent: docs-morph-3266-enhancements
relates-to: [docs-morph-11027-ui-field-reference-gaps]
created: 2026-08-03
completed_at: 2026-08-03T18:00:00Z
---
# The Guide items lack sufficient detail, impacting operations.

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11025

Customer feedback identifies missing explanations for Naming Policy **Auto Resolve Conflicts**, **Max Virtual Servers** versus **Max VMs**, instance **Port** and **QEMU Arguments**, and datastore **Image Target**. The Jira's sample explanations are proposals, not authoritative behavior.

## Goal
Provide accurate field-level reference content at each relevant workflow so operators can predict consequences before saving or provisioning.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11025-ui-field-reference-gaps/spec.md`; update `administration/policies/policies.rst`, `provisioning/instances/creating_instances.rst`, `infrastructure/clusters/hvm/vm_advanced_options.rst`, and the verified datastore source.

## Approach
Validate every field against current UI and engineering behavior, then extend existing topical pages rather than create a duplicate all-UI encyclopedia.

## Changes
1. `administration/policies/policies.rst` — Clarified naming conflict behavior and load-balancer virtual server versus managed VM quotas.
2. `provisioning/instances/creating_instances.rst` — Added the HVM QEMU Arguments provisioning/reconfigure cross-reference and disambiguated contextual Port fields. Application seeds identify the MySQL Existing-layout service port and the Windows server WinRM connection port; there is no universal Instance Port field.
3. `infrastructure/clusters/hvm/vm_advanced_options.rst` — Reconciled QEMU storage, tokenization, lifecycle, and warning behavior.
4. `infrastructure/storage/data_stores.rst` — Documented Image Target capability and local-appliance fallback.

## Acceptance Criteria
- WHEN users configure Naming or quota policies THE SYSTEM SHALL explain each named field's operational outcome and failure behavior.
- WHEN users configure an Instance THE SYSTEM SHALL explain that Port is contextual, identify the application-backed MySQL and Windows connection examples, and state that it does not open or publish a guest endpoint.
- WHEN users configure an HVM VM THE SYSTEM SHALL explain QEMU Arguments, including lifecycle applicability and startup risk.
- WHEN users edit a datastore THE SYSTEM SHALL explain Image Target using engineering-verified behavior.
- THE SYSTEM SHALL avoid presenting Jira sample text as fact without verification.

## Boundaries
No exhaustive reference for every UI field and no UI product changes.

## Risks
Fields can vary by cloud/layout; generic wording could be incorrect outside HVM.

## Validation
Field-by-field application-source review, rendered-page inspection, link checks, search for duplicate/conflicting definitions, and `make build`.
