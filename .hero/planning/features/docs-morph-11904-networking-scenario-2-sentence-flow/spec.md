---
title: "Docs: Deployment guide- sentence cutoff between two images. (networking scenario 2)"
slug: docs-morph-11904-networking-scenario-2-sentence-flow
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, hvm, deployment, networking, editorial]
tracker_id: MORPH-11904
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---
# Docs: Deployment guide- sentence cutoff between two images. (networking scenario 2)

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11904

On deployment-guide networking scenario 2, the sentence “As previously, a bond is also created for management traffic. In this example, these bonds are created in an active/passive configuration.” is interrupted/cut off between images.

## Goal
Restore readable sentence and figure flow without changing the scenario's technical meaning.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11904-networking-scenario-2-sentence-flow/spec.md`; locate the GUID-E49D2EF3 source, expected under `getting_started/installation/`, and repair only its scenario-2 markup.

## Approach
Map the public GUID to its local RST source, inspect image directives and surrounding paragraphs, then move/fix the sentence as one intact paragraph.

## Changes
1. Locate the source file under `getting_started/installation/` that publishes GUID-E49D2EF3-8992-451F-AE3F-55E0380448D2.
2. Correct the RST paragraph/image ordering so the supplied active/passive-bond sentence is complete and attached to the intended figure.

## Acceptance Criteria
- WHEN scenario 2 renders THE SYSTEM SHALL display the complete supplied sentence without an image splitting or truncating it.
- THE SYSTEM SHALL preserve the intended image order and active/passive-bond meaning.

## Boundaries
No rewrite of other networking scenarios or image redesign.

## Risks
The public GUID-to-source mapping is not encoded in the Jira payload.

## Validation
Build the affected page, inspect HTML around both images at desktop/mobile widths, and run `make test`.
