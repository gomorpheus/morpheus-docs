---
title: "Feedback on VME deployment guide"
slug: docs-morph-6125-vme-deployment-guide-feedback
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vme, deployment-guide, feedback]
tracker_id: MORPH-6125
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:27:26Z
---
# Feedback on VME deployment guide

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-6125

Jira description (verbatim):

> Hi, Please find attached some feedback on the VME deployment guide. Please feel free to reach out to me if you need any clarification. Thanks Pete

Jira identifies `VME Deployment Guide Feedback.docx`, but authenticated attachment-content download returns HTTP 403 through the available API. The issue summary and description contain no individual feedback items. The current deployment corpus, including the extensive MORPH-3266 changes already present, was therefore audited without treating inaccessible attachment-only comments as requirements.

## Goal

Resolve the umbrella feedback item through a comprehensive audit of current canonical deployment guidance while preserving the no-fabrication boundary for inaccessible attachment-only comments.

## Kickoff

Audit the current VME deployment documentation and record the evidence boundary. Do not infer attachment-only feedback. Any future unique, actionable feedback recovered from the attachment should be filed as a new Jira item with the requested behavior in accessible text.

→ `.hero/planning/features/docs-morph-6125-vme-deployment-guide-feedback/spec.md`

**Files:** `getting_started/installation/singleNode/hpe_installer.rst`, `getting_started/installation/hvm_host_prep.rst`, `infrastructure/clusters/hvm/building_clusters.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Audit the canonical installation, host-preparation, and cluster-creation guides plus their linked deployment material. Treat all actionable concerns visible in the Jira summary and current repository as addressed where canonical guidance already covers them; make no speculative edits for inaccessible comments.

## Changes

1. Audit `getting_started/installation/overview.rst`, `getting_started/installation/singleNode/hpe_installer.rst`, `getting_started/installation/hvm_host_prep.rst`, `getting_started/installation/distributed/overview.rst`, and `infrastructure/clusters/hvm/building_clusters.rst` in the context of landed MORPH-3266 work.
2. Record that Jira exposes only umbrella feedback text and an attachment whose authenticated content endpoint returns 403; attachment-only comments cannot authorize edits.
3. Complete as a no-op documentation audit because every actionable concern visible in Jira summary/current repository is already handled by canonical guides.
4. Require any future unique feedback to become a new actionable Jira item with accessible text and a verifiable expected outcome.

## Acceptance Criteria

- WHEN the current deployment corpus is audited THE DELIVERY SHALL account for the canonical deployment paths and the extensive MORPH-3266 changes already landed.
- IF Jira summary/current repository exposes an actionable deployment issue THEN THE DOCUMENTATION SHALL address it in the canonical guide; the audit found none outstanding.
- IF attachment content remains inaccessible THEN THE DELIVERY SHALL make no attachment-derived edits and SHALL record the no-fabrication boundary.
- WHEN unique feedback becomes available later THEN IT SHALL be captured as a new actionable Jira item rather than silently reopening this umbrella issue.

## Boundaries

No documentation edits based only on the issue title, no broad VME guide rewrite, and no invented attachment content.

## Risks

- Attachment-only comments remain unverified because authenticated download returns 403.
- A future accessible comment could identify behavior not visible in the current repository audit; it requires a new scoped issue.

## Validation

Review the canonical deployment entry points and cross-links, search for placeholders or contradictory guidance, and run `make build`. No content edit is authorized solely by the inaccessible attachment.
