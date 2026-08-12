---
title: "The Guide items lack sufficient detail, impacting operations."
slug: docs-morph-11027-ui-field-reference-gaps
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, duplicate, ui-reference]
tracker_id: MORPH-11027
jira_status: New
parent: docs-morph-3266-enhancements
relates-to: [docs-morph-11025-ui-field-reference-gaps]
created: 2026-08-03
completed_at: 2026-08-03T14:31:32Z
---
# The Guide items lack sufficient detail, impacting operations.

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11027

The summary and description are exact duplicates of MORPH-11025, covering Auto Resolve Conflicts, Max Virtual Servers versus Max VMs, Port, QEMU Arguments, and Image Target.

## Goal
Resolve this duplicate without creating a second, conflicting documentation implementation.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11027-ui-field-reference-gaps/spec.md`; verify duplication against `docs-morph-11025-ui-field-reference-gaps/spec.md` and make no documentation edits independently.

## Approach
Treat MORPH-11025 as the implementation-bearing request; link and close/resolve this Jira according to tracker policy after confirming no hidden attachments add scope.

## Changes
1. Compared full MORPH-11027 and MORPH-11025 records; descriptions are identical and neither has attachments. MORPH-11027 adds no implementation scope.
2. Linked MORPH-11027 as a duplicate of MORPH-11025 in Jira; no independent docs source was changed.

## Acceptance Criteria
- WHEN both Jira records are reviewed THE SYSTEM SHALL identify MORPH-11025 as the single implementation source.
- IF MORPH-11027 contains unique evidence THEN THE SYSTEM SHALL merge it into the MORPH-11025 spec before resolving duplication.
- THE SYSTEM SHALL NOT produce duplicate guide text.

## Boundaries
No documentation implementation independent of MORPH-11025.

## Risks
Attachments not present in the JSON payload could contain distinct scope.

## Validation
Compare full Jira records, verify the relation, and confirm only MORPH-11025 drives documentation changes.
