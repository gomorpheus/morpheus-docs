---
title: "Update HPE VME Agent Installation documentation to include guidance regarding Cortex and antivirus/security applications potentially blocking agent installation."
slug: docs-morph-11565-agent-security-software-interference
type: feature
status: completed
horizon: now
size: small
tags: [documentation, agents, security-software, troubleshooting, vme]
tracker_id: MORPH-11565
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T16:00:00Z
---
# Update HPE VME Agent Installation documentation to include guidance regarding Cortex and antivirus/security applications potentially blocking agent installation.

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11565

A VME 8.1.1 Agent installation failed while Cortex endpoint security was active and succeeded after it was disabled. Customers need guidance that Cortex or similar endpoint protection can block installation, reachability checks, or communication, with safe allowlisting/exclusion guidance.

## Goal
Add security-conscious troubleshooting guidance that prioritizes approved allowlisting and limits any temporary disablement advice.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11565-agent-security-software-interference/spec.md`; update `getting_started/functionality/agent/agentInstallation.rst` and `troubleshooting/Morpheus_Agent.rst`.

## Approach
Identify Agent binaries, scripts, endpoints, ports, and log evidence that security teams can permit; frame disabling protection as controlled, temporary, policy-approved diagnosis only.

## Changes
1. `getting_started/functionality/agent/agentInstallation.rst` — Added a security-conscious EDR/antivirus prerequisite covering script delivery, package installation, startup, TCP 443/websocket communication, and upgrades.
2. `troubleshooting/Morpheus_Agent.rst` — Added staged symptoms, evidence collection, targeted allowlisting, retry/verification, and tightly controlled temporary-disablement guidance.
3. Existing Appliance URL/TCP 443 requirements are referenced in context rather than introducing a duplicate endpoint list.

## Acceptance Criteria
- WHEN Agent installation or communication is blocked THE SYSTEM SHALL identify endpoint protection as a possible cause and show how to gather evidence.
- WHEN remediation is needed THE SYSTEM SHALL recommend product/vendor-approved exclusions or allowlisting before disablement.
- IF temporary disablement is mentioned THEN THE SYSTEM SHALL require security-policy approval, minimal duration, and immediate re-enable/verification.
- THE SYSTEM SHALL NOT prescribe broad permanent antivirus exclusions.

## Boundaries
No vendor-specific Cortex administration procedure or weakening of customer security controls.

## Risks
Unsafe wording could encourage disabling protection in production; paths/endpoints vary by platform/version.

## Validation
Security and Agent engineering review, reproduce with a controlled policy block, render notes, and run `make test`.
