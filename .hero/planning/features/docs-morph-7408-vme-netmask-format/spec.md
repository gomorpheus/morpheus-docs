---
title: "VME deployment guide is not clear on the format to use for the IP netmask"
slug: docs-morph-7408-vme-netmask-format
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, vme, installation, networking, netmask]
tracker_id: MORPH-7408
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:17:20Z
---
# VME deployment guide is not clear on the format to use for the IP netmask

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7408

> There are two representation methods for IP netmasks. One is CIDR (Classless Inter-Domain Routing) Notation (e.g. 172.16.63.0/19) and the other is Dotted Decimal Notation (e.g. 255.255.224.0).
>
> The "Installing the VM Essentials manager" section ... does not mention which method to use. Although there is a screenshot using DDN, the HVM installation uses CIDR and if the customer uses this CIDR with hpe-vm it will be accepted (there is no input validation) but the VME manager will fail to deploy. The documentation should be updated to make it clear that DDN must be used.

`getting_started/installation/singleNode/hpe_installer.rst` already shows a dotted-decimal example; this work makes the requirement explicit.

## Goal
State unambiguously that the VME Manager installer’s netmask input requires dotted-decimal notation and warn that CIDR input may be accepted but causes deployment failure, if Product confirms that behavior.

## Kickoff
Audit `getting_started/installation/singleNode/hpe_installer.rst`, especially prerequisites, field definitions, examples, and troubleshooting. Compare `tools/hvmcli/deploy.rst` only to prevent readers from carrying HVM CLI notation into the Manager installer. Confirm accepted formats and failure behavior with Installer Engineering before publication; then make a narrow correction around every Manager netmask input. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Strengthen the existing field definition and preflight guidance rather than adding a networking primer.

## Changes
1. Update `getting_started/installation/singleNode/hpe_installer.rst` to require dotted-decimal netmask notation and include an approved valid example.
2. Add a warning against CIDR notation and confirmed remediation for a failed deployment.
3. Audit `tools/hvmcli/deploy.rst` for clear command-specific notation without changing HVM behavior.

## Acceptance Criteria
- WHEN a user enters the VME Manager netmask THE DOCUMENTATION SHALL require dotted-decimal notation with a valid example.
- IF CIDR notation is accepted but later fails THEN THE DOCUMENTATION SHALL warn about the confirmed failure before installation.
- THE DOCUMENTATION SHALL distinguish Manager installer input from HVM CLI input.

## Boundaries
No installer validation fix or broad subnetting tutorial.

## Risks
Delivery is blocked until Installer Engineering confirms the accepted format and failure/remediation behavior.

## Validation
Exercise valid and invalid inputs on a supported installer, build the page, and have Installer Engineering review it.
