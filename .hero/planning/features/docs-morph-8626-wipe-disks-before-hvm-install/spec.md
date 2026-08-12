---
title: "Wipe disks before installation to avoid checksum error"
slug: docs-morph-8626-wipe-disks-before-hvm-install
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hvm, installation, storage]
tracker_id: MORPH-8626
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---

# Wipe disks before installation to avoid checksum error

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-8626

Exact Jira description (delivery source requirement):

> I was getting a checksum error after entering proxy information according to the documentation. I followed the following steps:
>
> 1. I used URL based mount of the ISO ([http://10.235.0.75/software/VME/v8.0.13_2/HVM_Install_24.04_S5Q83-11038.iso](http://10.235.0.75/software/VME/v8.0.13_2/HVM_Install_24.04_S5Q83-11038.iso)) as recommended by the networking team.
> 2. I follow steps 1-4 in the guide ([https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007332en_us&page=GUID-28F18596-4902-4CD1-83F3-1411430C5534.html#about-this-task-2](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007332en_us&page=GUID-28F18596-4902-4CD1-83F3-1411430C5534.html#about-this-task-2))
> 3. I configure the network based on values provided by the networking team:
>
>     1. Subnet:     10.235.0.0  
>       Mask:       255.255.224.0 - /19  
>       Gateway:    10.235.0.1  
>       Name Servers:     10.227.1.91,16.110.135.51
>     2. Node: 10.235.0.67
>     3. parameters:  
>                       lacp-rate: fast  
>                       mode: 802.3ad  
>                       transmit-hash-policy: layer3+4
>     4. eno5np0: {}2  
>               eno6np1: {}
>     5. We do these steps differently because this system is set up to use LACP Bonds instead of a simple active-backup network bond. This is not covered in the documentation.
>     
> 4. I put in the proxy: [http://hpeproxy.its.hpecorp.net:8080](http://hpeproxy.its.hpecorp.net:8080)
> 5. I get the error as shown attached.
>
> Jamie Reed was able to help me get this working. He flashed the iLO and reset the Disk Raid to clear off the disks. He said it is best practice to wipe the disks before installing and that his team has seen Ubuntu (the HVM ISO is Ubuntu-based) behave unpredicably when it is reinstalled over itself.
>
> He used this guide: [System Erase and Reset | HPE Compute Security Reference Guide](https://portal-iam-ext-pro.it.hpe.com/hpesc/public/docDisplay?docId=a00018320en_us&page=GUID-DA754C35-8FC5-4753-8CA9-6228D66D8FC0.html&docLocale=en_US)
>
> He said he went into the Option F10 (intelligent provisioning) and deleted and created a new raid different from the original. Using the drive wipe (erase) in the BIOS can take some time.
>
> I am hoping that this can be mentioned as a prerequisite or best practice to help customers who may be getting a similar error.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-8626 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-8626-wipe-disks-before-hvm-install/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `getting_started/installation/hvm_host_prep.rst`
- `getting_started/installation/singleNode/hpe_installer.rst`
- `infrastructure/clusters/hvm/troubleshooting.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Add a gated pre-install disk-state check and vendor-neutral remediation guidance, clearly separating destructive erase options from ordinary installation prerequisites.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `getting_started/installation/hvm_host_prep.rst` to carry the primary procedure and verified guidance.
2. Update `getting_started/installation/singleNode/hpe_installer.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `infrastructure/clusters/hvm/troubleshooting.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-8626
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

- The error attachment is unavailable and the causal link to stale disks is unverified. SME confirmation is required before making disk erasure a prerequisite; destructive steps require explicit data-loss warnings.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
