---
title: "Morpheus Agent and security review - CASE 5401420459"
slug: docs-morph-7646-agent-security-review
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, agent, security, support-case, review]
tracker_id: MORPH-7646
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T16:00:00Z
---
# Morpheus Agent and security review - CASE 5401420459

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7646

> Hello Team, customer is requesting Morpheus Agent security review.
>
> I have pinged Adam Lipscombe and he also confirmed that we do not have such documentation available yet.
>
> Please create such documentation for future use.
>
> You can review case 5401420459 for more details or ping me at any time.

Existing high-level Agent security claims appear in `getting_started/functionality/agent/overview.rst`; a security review must validate and expand them rather than duplicate marketing language.

## Goal
Publish a security-reviewed Agent architecture and operations reference covering trust boundaries, connectivity, privileges, data handled, update lifecycle, controls, and customer responsibilities.

## Kickoff
Obtain and review support case 5401420459 before drafting. Audit `getting_started/functionality/agent/overview.rst`, `getting_started/functionality/agent/osSupport.rst`, `getting_started/requirements/requirements.rst`, and `release_notes/packages.rst`. Build a claim/evidence matrix with Agent Engineering and Security; do not infer encryption, credential storage, privilege, telemetry, package-signing, update, or vulnerability-handling behavior from high-level prose. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions. Exclude customer identifiers.

## Approach
Expand the canonical Agent overview with a security model or add a dedicated child page if the reviewed material cannot remain concise.

## Changes
1. `getting_started/functionality/agent/overview.rst` — Added the outbound control channel, Manager-controlled remote-shell-equivalent trust boundary, command/file capabilities, Linux and HVM privileges, `verifyPeer` behavior, principal paths/processes, package/update boundary, and customer controls.
2. No new page was required; the canonical Agent overview remains the navigation owner.
3. Existing TCP 443 connectivity guidance was retained; package behavior is described without asserting signing or lifecycle guarantees not present in supplied evidence.

## Delivery Evidence

Agent source shows an outbound STOMP control connection, command and file action dispatch, extensive `sudo` operations, configuration at `/etc/morpheus/morpheus-node.yaml`, runtime content under `/opt/morpheus-node`, and certificate-chain verification controlled by `verifyPeer`. Unsupported package-signing, vulnerability-handling, and case-specific claims were excluded.

## Acceptance Criteria
- THE DOCUMENTATION SHALL describe approved Agent trust boundaries, network direction/ports, privileges, data classes, and customer responsibilities.
- THE DOCUMENTATION SHALL describe approved package integrity and update behavior.
- IF a case question lacks publishable evidence THEN THE DOCUMENTATION SHALL exclude the claim and record it for Security review.
- THE DOCUMENTATION SHALL not expose customer-sensitive case data.

## Boundaries
No penetration test, certification, Agent code change, or disclosure of confidential case content.

## Risks
Delivery is blocked because case 5401420459 is unavailable and Security/Engineering review is mandatory.

## Validation
Trace every statement to approved evidence, run security and legal/support review, build docs, and test links/navigation.
