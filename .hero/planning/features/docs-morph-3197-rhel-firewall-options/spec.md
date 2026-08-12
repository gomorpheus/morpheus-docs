---
title: "Add details/documentation around the firewall options for morpheus.rb as well as firewalld/iptables support when installing on RHEL systems"
slug: docs-morph-3197-rhel-firewall-options
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, installation, rhel, firewall, security]
tracker_id: MORPH-3197
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:02:52Z
---
# Add details/documentation around the firewall options for morpheus.rb as well as firewalld/iptables support when installing on RHEL systems

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3197

Jira description (verbatim):

> Customer would like to see more details around the use of the firewall configuration options for the morpheus.rb file as well as the support for firewalld/iptables when installing on RHEL systems.  More details below:
>
> * If you want to use firewalld instead of the default iptables, then you would implement the morpheus.rb file changes mentioned before by adding the following lines to it:
>
> firewall\['enable'\] = false  
> firewall\['ipv4'\] = false
>
> * You would then implement whatever firewall rules you want (see bullet below on ports)
> * If you want to use the default iptables, then you dont need those morpheus.rb file changes mentioned and can implement whatever firewall rules you want(see bullet below on ports).
> * I did some quick testing in my lab on this by adding a rule to iptables then running a reconfigure (as well as rebooting the appliance) and it retained the new rules without issue. That would also apply if you did an upgrade as you are essentially updating the code base, then running a reconfigure to get everything updated properly.
> * In terms of a "Morpheus approved" firewall setup, we don't really have one per se though we do have advice on which ports you will want to open. You can find that list of ports in our docs at the following links:
>
> https://support.hpe.com/hpesc/public/docDisplay?docId=sd00006453en_us&page=GUID-2D8A0A86-2231-4239-AB44-5475B4AE0827.html  
> https://support.hpe.com/hpesc/public/docDisplay?docId=sd00006453en_us&page=GUID-0DB10170-9557-43A8-BF4B-76F2A2C25FBE.html
>
> Customers response to the above:
>
> The provided solution relies on settings that appear to be undocumented features (firewall\['enable'\] and firewall\['ipv4'\]), and as of now, there is no mention in the official HPE or Morpheus documentation describing what the installer does to the system firewall or how to prevent this behavior.
>
> From my perspective, this is not a minor configuration issue but a serious security concern. During installation, Morpheus disables firewalld on RHEL systems and replaces it with iptables configured with an “allow all” rule — effectively leaving the host completely exposed. The fact that this occurs silently and without clear documentation is troubling, especially for a product positioned as an enterprise solution.
>
> I would appreciate clarification on whether HPE plans to:
>
> 1. Document this installer behavior and the relevant configuration options, and
> 2. Address the underlying security implications in future releases.
>
> You can find more details in SF case 5391476167, let me know if you need any more info/have questions.

The repository already discusses RHEL firewalld in `getting_started/installation/singleNode/redhat.rst`, advanced settings in `getting_started/additional/morpheusRb.rst`, and communication ports in `getting_started/functionality/communication.rst`.

## Goal

Document verified installer firewall behavior, supported `morpheus.rb` controls, firewalld/iptables choices, required ports, and safe reconfigure/upgrade expectations for RHEL without presenting lab observations as supported guarantees.

## Kickoff

Clarify supported RHEL firewall behavior and the `morpheus.rb` controls requested by MORPH-3197.

**Status:** planning — Jira evidence and existing firewall pages are identified; engineering confirmation is required.

**Pick up at:** verify installer behavior and both configuration keys with appliance engineering before drafting security guidance.

→ `.hero/planning/features/docs-morph-3197-rhel-firewall-options/spec.md`

**Files:** `getting_started/installation/singleNode/redhat.rst`, `getting_started/additional/morpheusRb.rst`, `getting_started/functionality/communication.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Add one authoritative explanation near RHEL installation, reference the canonical ports table, and add only verified keys to the advanced settings reference. Clearly distinguish Morpheus-managed iptables behavior from customer-managed firewalld policy.

## Changes

1. `getting_started/installation/singleNode/redhat.rst` — Documented the verified RHEL recipe behavior and safe customer-managed firewall choice.
2. `getting_started/additional/morpheusRb.rst` — Documented `firewall['enabled']` (not `enable`) and `firewall['ipv4']` defaults and interaction.
3. `getting_started/functionality/communication.rst` — Added a stable target for the canonical ports table.

## Acceptance Criteria

- WHEN an administrator reviews RHEL installation guidance THE DOCUMENTATION SHALL explain the verified firewall changes performed by installation and reconfigure.
- WHERE customer-managed firewalld is used THE DOCUMENTATION SHALL identify the verified Morpheus controls and direct the administrator to required ports.
- THE DOCUMENTATION SHALL publish only the appliance-confirmed keys `firewall['enabled']` and `firewall['ipv4']` and SHALL explain that both must be false to retain customer-managed firewalld.
- THE DOCUMENTATION SHALL avoid claiming that custom rules survive reconfigure, reboot, or upgrade unless validated by engineering.

## Boundaries

No installer code changes, firewall policy design, product security remediation, or new port requirements. Do not document SF case details beyond the Jira-provided context.

## Risks

- **Blocker:** Installer defaults, key support, and persistence behavior require confirmation from Morpheus appliance engineering.
- The Jira security assertions and lab observations are unverified and must not be converted directly into product guarantees.

## Validation

Obtain engineering sign-off, compare all port references with `communication.rst`, run `make build`, and review rendered RHEL installation and advanced-settings pages for unambiguous warnings and links.
