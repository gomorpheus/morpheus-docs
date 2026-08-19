---
title: "Morpheus Agent OS Support"
slug: docs-morph-6887-agent-os-support
type: feature
status: completed
horizon: now
size: small
tags: [documentation, agent, operating-systems, support]
tracker_id: MORPH-6887
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:32Z
---
# Morpheus Agent OS Support

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-6887

> Morpheus agent installation is not supported on RHEL 6.  
>   
> RHEL 6 does not include the file `/etc/os-release` (that was introduced in RHEL 7). Our agent install script currently relies on that file to detect the OS, so when you run the standard install command on RHEL 6, the script fails with errors such as `"grep: /etc/os-release: No such file or directory"` and the install does not complete.

## Goal
Correct the canonical Agent OS support page so RHEL 6 is not presented as installable and readers understand the supported boundary without interpreting a script failure as a troubleshooting problem.

## Kickoff
Audit `getting_started/functionality/agent/osSupport.rst` and related Agent navigation in `getting_started/functionality/agent/overview.rst`. Confirm the minimum supported RHEL major version and affected agent architectures with Engineering or Product before editing. Add only the approved support boundary; use the Jira error as explanatory context only if reviewers approve exposing implementation detail. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Correct the existing support table and add a concise unsupported-version note rather than creating a new page.

## Changes
1. `getting_started/functionality/agent/osSupport.rst` — Removed generic/RHEL 6 installable entries, documented the `/etc/os-release` installer boundary, and separated OS recognition from formal package support.

## Delivery Evidence

The canonical page removes RHEL 6 support and states that a minimum supported RHEL version is not established by bundled package metadata. It does not promote runtime recognition to formal support or expose an unapproved implementation explanation.

## Acceptance Criteria
- THE DOCUMENTATION SHALL not list RHEL 6 as supported for Morpheus Agent installation.
- WHEN a reader checks RHEL compatibility THE DOCUMENTATION SHALL show the approved minimum supported version.
- IF the implementation explanation is not approved THEN THE DOCUMENTATION SHALL state only the support boundary and not speculate about internals.

## Boundaries
No installer changes, workaround for RHEL 6, or unsupported backport guidance.

## Risks
The exact minimum remains a documented support-policy unknown rather than an inferred promise.

## Validation
Compare the table with release/support policy, build the Agent pages, and obtain Agent owner approval.
