---
title: "VMware Hypervisor Console Access Failure for Windows 11 VM with TPM in Morpheus"
slug: docs-morph-6016-vmware-tpm-console-privileges
type: feature
status: completed
horizon: now
size: small
tags: [documentation, vmware, windows-11, tpm, permissions, console]
tracker_id: MORPH-6016
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:17:20Z
---
# VMware Hypervisor Console Access Failure for Windows 11 VM with TPM in Morpheus

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-6016

Jira description (verbatim):

> A Windows 11 virtual machine was created in vCenter using the ISO image, with TPM enabled as required for Windows 11 installations. The VM was successfully deployed and discovered within Morpheus.
>
> However, attempts to access the hypervisor console from Morpheus consistently failed.
>
> To resolve this, the following privileges need to be added to the MorpheusRole in vCenter:
>
> Added Privileges (under “Cryptographic Operations”):
>
> * Clone
> * Direct
> * AccessMigrate
>
> Can we update our documentation to reflect the above privileges required for the **MorpheusRole** in vCenter?
>
> I’ve also created a forum post for reference — please find the link below:

The promised forum URL is absent. Existing VMware permissions and console guidance are in `integration_guides/Clouds/vmware/vmware.rst`, `permissions.rst`, and `troubleshooting/Remote_Console.rst`.

## Goal

Document the minimum validated vCenter cryptographic privileges required for Morpheus console access to encrypted/vTPM Windows 11 VMs, with scope, symptoms, and troubleshooting.

## Kickoff

Verify and document vCenter cryptographic privileges needed for console access to Windows 11 vTPM VMs.

**Status:** planning — likely permissions pages are known; the Jira fix and missing forum evidence are unverified.

**Pick up at:** reproduce with the documented MorpheusRole, add privileges individually, and establish the minimum required set.

→ `.hero/planning/features/docs-morph-6016-vmware-tpm-console-privileges/spec.md`

**Files:** `integration_guides/Clouds/vmware/permissions.rst`, `integration_guides/Clouds/vmware/vmware.rst`, `troubleshooting/Remote_Console.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Update the canonical VMware role matrix with least-privilege, task-scoped permissions and add a console troubleshooting symptom. Avoid asserting all three privileges are required until isolated testing confirms them.

## Changes

1. Update `integration_guides/Clouds/vmware/permissions.rst` with approved cryptographic privileges and precise feature scope.
2. Update `integration_guides/Clouds/vmware/vmware.rst` with a cross-reference for vTPM/encrypted VM management.
3. Update `troubleshooting/Remote_Console.rst` with the verified symptom, checks, and least-privilege remediation.

## Acceptance Criteria

- WHEN Morpheus accesses the hypervisor console for an encrypted or vTPM VM THE DOCUMENTATION SHALL list the minimum verified vCenter privileges and where to assign them.
- IF a privilege is required for clone or migration but not console access THEN THE DOCUMENTATION SHALL distinguish that scope.
- THE DOCUMENTATION SHALL not cite the absent forum post or present the Jira list as validated without testing.

## Boundaries

No vCenter role automation, Windows 11 installation guide, HVM TPM guidance, or blanket administrator-role recommendation.

## Risks

- **Blocker:** The forum link is missing and the exact minimum privilege set is unverified.
- Excess privileges weaken least-privilege posture; missing privileges break encrypted VM operations.

## Validation

Test each privilege against console, clone, and migration operations, review with VMware integration/security owners, run `make build`, and inspect the rendered permissions table.
