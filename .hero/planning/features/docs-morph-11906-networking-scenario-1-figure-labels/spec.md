---
title: "Docs: Deployment guide -  Add image figure numbers and description to add clarity when referring to specific image. (networking scenario 1)"
slug: docs-morph-11906-networking-scenario-1-figure-labels
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, deployment, networking, figures]
tracker_id: MORPH-11906
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---
# Docs: Deployment guide -  Add image figure numbers and description to add clarity when referring to specific image. (networking scenario 1)

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11906

Networking scenario 1 repeatedly refers to “below,” “the example below,” and “the similar chart above.” With multiple images, the references are ambiguous. The request is to add figure numbers and descriptions.

## Goal
Give every scenario-1 image a meaningful caption/number and replace positional references with durable figure references.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11906-networking-scenario-1-figure-labels/spec.md`; locate the GUID-2DD9D39D source under `getting_started/installation/` and update its image directives and references.

## Approach
Map the public GUID to RST, inventory all images in order, add descriptive captions/labels using the repository's supported figure pattern, and rewrite only ambiguous references.

## Changes
1. Locate the source file under `getting_started/installation/` that publishes GUID-2DD9D39D-9031-4BB5-A4ED-A0179BEF5259.
2. Convert or augment each scenario-1 image directive with a unique descriptive caption, accessible alt text, and stable label/number supported by the build.
3. Replace “below/above” phrases with the corresponding named/numbered figure references.

## Acceptance Criteria
- WHEN scenario 1 renders THE SYSTEM SHALL show a unique description and unambiguous figure identity for every image.
- WHEN prose refers to an image THE SYSTEM SHALL use its figure identity rather than relative page position.
- THE SYSTEM SHALL preserve image order and technical content.

## Boundaries
No replacement of image assets or renumbering outside the affected page unless generated automatically.

## Risks
Manual numbers can drift; use native generated numbering where the documentation toolchain supports it.

## Validation
Build the page, verify captions/cross-references/alt text and no duplicate labels, then run `make test`.
