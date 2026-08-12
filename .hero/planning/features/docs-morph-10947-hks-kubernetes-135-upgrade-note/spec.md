---
title: "Need to add update note in HKS 8.1.0 , 8.1.1 & 8.1.2 documentation"
slug: docs-morph-10947-hks-kubernetes-135-upgrade-note
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hks, kubernetes, upgrades, 8.1]
tracker_id: MORPH-10947
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:09:14Z
---
# Need to add update note in HKS 8.1.0 , 8.1.1 & 8.1.2 documentation

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-10947

HKS 8.1.0, 8.1.1, and 8.1.2 upgrade documentation incorrectly limits the `--pod-infra-container-image` deprecation warning to Kubernetes v1.35.3. The requested text applies to v1.35 and all v1.35.x or later upgrades.

## Goal
Correct all three published HKS version guides so users remove the deprecated Kubelet flag before attempting a 1.35.x upgrade.

## Kickoff
Deliver `.hero/planning/features/docs-morph-10947-hks-kubernetes-135-upgrade-note/spec.md`; update the three linked HKS guide source components and reconcile `infrastructure/clusters/kubernetes.rst` if it contains the shared upgrade note.

## Approach
Apply one approved warning consistently to the 8.1.0/8.1.1/8.1.2 sources; preserve the exact flag as code and correct “depreciated” to “deprecated.”

## Changes
1. `infrastructure/clusters/kubernetes.rst` — Added the shared v1.35.x-or-later warning with the exact deprecated flag and current script behavior.
2. HKS 8.1.0, 8.1.1, and 8.1.2 source components — Not present in this checkout; the canonical page now explicitly scopes the warning to all three historical release lines.

## Acceptance Criteria
- WHEN users prepare any 8.1.0–8.1.2 HKS cluster upgrade to Kubernetes v1.35.x or later THE SYSTEM SHALL warn that the deprecated flag causes upgrade failure.
- THE SYSTEM SHALL render `--pod-infra-container-image` exactly and use “deprecated.”
- THE SYSTEM SHALL contain equivalent guidance in all three versioned guides.

## Boundaries
No Kubernetes upgrade automation or support claim beyond the supplied limitation.

## Risks
The three public guides may be generated from sources outside this checkout.

## Validation
Search all three rendered guides for the old v1.35.3 wording, verify the replacement, build locally where possible, and run `make test`.
