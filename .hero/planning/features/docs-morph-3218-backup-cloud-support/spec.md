---
title: "Backup Integration should clearly state what clouds they support"
slug: docs-morph-3218-backup-cloud-support
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, backups, integrations, compatibility]
tracker_id: MORPH-3218
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:09:14Z
---
# Backup Integration should clearly state what clouds they support

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3218

Jira description (verbatim):

> Many backup integrations do not state what clouds they work with or are not very clear. I put together a list from what is currently in the documentation and what I could get from Tommy.
>
> **Cohesity - VMware**
> * Not stated in docs
>
> **Commvault - VMware, OpenStack**
> * States it works with OpenStack in the docs but tommy was not confident that it does. Should be tested.
>
> **Veeam - VMware, Hyper-V, SCVMM, VCD**
> * Does not state SCVMM
>
> **Rubrik - VMware**
> * Stated in docs
>
> **Zerto - VMware**
> * Says “such as VMware vCenter Clouds”. Not very clear it only works with VMware.
>
> **Avamar - (I think just VMware)**
> * Tommy was not sure on this
> * Not stated in docs
>
> I think each should have a section called “Clouds supported” and a bullet list of what clouds they work with as many people assume its all clouds.

Existing pages already state support for some providers, including Commvault, Veeam, and Rubrik; uncertain Jira claims require validation.

## Goal

Give every listed backup integration a consistent, product-approved “Supported Clouds” section that distinguishes backup support from storage or replication capabilities.

## Kickoff

Standardize supported-cloud declarations across Cohesity, Commvault, Veeam, Rubrik, Zerto, and Avamar integration pages.

**Status:** planning — current pages were located; Commvault OpenStack, Veeam SCVMM, Cohesity, Zerto, and Avamar claims need approval.

**Pick up at:** obtain the current compatibility matrix from backup integration owners before editing prose.

→ `.hero/planning/features/docs-morph-3218-backup-cloud-support/spec.md`

**Files:** `backups/integrations/commvault.rst`, `backups/integrations/veeam.rst`, `backups/integrations/cohesity.rst`, `backups/integrations/avamar.rst`, `backups/integrations/zerto.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Use identical section structure on each provider page and preserve existing supported-cloud statements until contradicted by an approved matrix or successful product test.

## Changes

1. `backups/integrations/commvault.rst` — Added the proven VMware and OpenStack Supported Clouds list.
2. `backups/integrations/veeam.rst` — Added the proven VMware, Hyper-V, SCVMM, and vCloud Director Supported Clouds list.
3. `backups/integrations/rubrik.rst` — Made the existing VMware-only support explicit in the common section format.
4. `backups/integrations/avamar.rst` — Added the proven VMware Supported Clouds list.
5. `integration_guides/Backups/veeam.rst` — Kept the duplicate Veeam guide consistent for SCVMM support.
6. `backups/integrations/cohesity.rst` and `backups/integrations/zerto.rst` — Added Supported Clouds boundaries stating that exact compatibility is not established in bundled metadata; distinguished Cohesity S3 storage from backup and Zerto replication from backup.

## Acceptance Criteria

- THE DOCUMENTATION SHALL include an explicit Supported Clouds section for all six named integrations.
- WHEN support differs by backup, replication, or storage feature THE DOCUMENTATION SHALL distinguish those capabilities.
- IF a Jira-listed cloud cannot be confirmed THEN THE DOCUMENTATION SHALL omit it or label it unsupported; uncertainty SHALL not be published as support.

## Boundaries

No compatibility expansion, plugin testing implementation, or claims for integrations not named in Jira.

## Risks

- **Blocker:** Commvault OpenStack, Veeam SCVMM, Cohesity, Zerto-only-VMware, and Avamar support require owner confirmation.
- Published compatibility claims affect customer architecture decisions.

## Validation

Secure provider-owner sign-off, compare every list with current product behavior, run `make build`, and inspect all six rendered pages for consistency.
