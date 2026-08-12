---
title: "Docs: HKS CNCF Certification"
slug: docs-morph-11395-hks-cncf-certification
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hks, cncf, certification]
tracker_id: MORPH-11395
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:41Z
---
# Docs: HKS CNCF Certification

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11395

The Jira contains no description, version, certification identifier, scope, or approved claim language.

## Goal
Publish a precise HKS CNCF certification statement only after actionable certification evidence is supplied.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11395-hks-cncf-certification/spec.md`; obtain the certificate/version scope, then update `infrastructure/clusters/kubernetes.rst` and the applicable release note.

## Approach
Require an official CNCF listing or certificate, covered HKS/Kubernetes versions, expiration/status, and legal-approved wording before edits.

## Changes
1. Collect certification evidence and approved claim language from the HKS product owner/CNCF record.
2. Add a scoped statement and evidence link to `infrastructure/clusters/kubernetes.rst`.
3. Update the applicable version under `release_notes/` only when the certification effective release is known.

## Acceptance Criteria
- IF no HKS-specific conformance record is bundled THEN THE DOCUMENTATION SHALL explicitly make no CNCF certification claim.
- THE DOCUMENTATION SHALL link to the authoritative CNCF Certified Kubernetes product list for version-specific confirmation.
- THE SYSTEM SHALL avoid implying all HKS or Kubernetes versions are certified.

## Boundaries
No certification application work or unsupported marketing claim.

## Risks
Certification claims are time/version sensitive and may require legal review.

## Validation
Verify the official CNCF record, obtain product/legal approval, render affected pages, and run `make test`.
