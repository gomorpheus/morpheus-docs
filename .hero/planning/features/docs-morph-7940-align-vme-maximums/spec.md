---
title: "Align maximums in documentation with Maximums Guide"
slug: docs-morph-7940-align-vme-maximums
type: feature
status: completed
horizon: now
size: small
tags: [documentation, vme, maximums, installation, correction]
tracker_id: MORPH-7940
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
depends-on: [docs-morph-7243-vme-maximums-guide]
completed_at: 2026-08-03T15:23:31Z
---
# Align maximums in documentation with Maximums Guide

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7940

> The current doc mentions maximum clusters per manager depending on the size selected at installation. Please remove the numbers leaving only the guidance and point to the maximums guide: https://psnow.ext.hpe.com/doc/a00157488enw (Still a bit unclear, but at least we’re removing the perceived limitations)

The likely repository target is `getting_started/installation/singleNode/hpe_installer.rst`, which contains Manager size guidance. MORPH-7243 separately requests a canonical Maximums Guide.

## Goal
Remove stale or misleading cluster-count numbers from Manager sizing guidance and point readers to the approved canonical Maximums Guide while retaining useful qualitative selection guidance.

## Kickoff
Wait for `docs-morph-7243-vme-maximums-guide` or confirm that the approved PSNow document remains the canonical destination. Audit `getting_started/installation/singleNode/hpe_installer.rst` and search all RST files for manager-size and cluster-count claims. Obtain Product wording for the qualitative size guidance; Jira itself says the replacement remains unclear, so do not improvise it. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Replace duplicated numeric maxima with concise guidance and a durable canonical reference. Correct all matching claims in the same scope.

## Changes
1. `getting_started/installation/singleNode/hpe_installer.rst` — Clarify that Manager sizing profiles do not establish fixed HVM cluster counts, retain the available profile options, and direct readers to workload-specific sizing review.
2. `getting_started/installation/singleNode/hpe_installer.rst` — Link Manager sizing guidance to the completed canonical `infrastructure/clusters/hvm/maximums.rst` guide.
3. `getting_started/requirements/capacity_planning.rst` — Remove fixed supported-workload counts and the stale 32 GB node maximum, preserve qualitative architecture and scaling guidance, and link to the canonical guide.
4. Repository-wide RST audit — Check Manager sizing, managed-host, managed-object, and maximum-cluster claims for contradictory fixed VME values; no additional stale fixed Manager or HVM cluster-count maxima were found.
5. `.hero/planning/features/docs-morph-7940-align-vme-maximums/spec.md` — Record delivered files, audit results, and satisfied acceptance criteria.

## Acceptance Criteria
- [x] WHEN a reader selects a VME Manager size THE DOCUMENTATION SHALL provide approved qualitative guidance without stale hard-coded cluster maxima.
- [x] THE DOCUMENTATION SHALL link to the approved canonical Maximums Guide.
- [x] IF the local maximums page is not yet approved THEN THE DOCUMENTATION SHALL not link to an unfinished source. (The dependency is completed and the local guide is in navigation.)
- [x] THE DOCUMENTATION SHALL contain no conflicting maximum-cluster values in the audited scope.

## Boundaries
No change to installer size options or maximum values.

## Risks
Blocked on MORPH-7243 or explicit Product confirmation of the external canonical guide and replacement wording.

## Validation
Search repository RST files for old Manager sizing and cluster-count values, verify the local canonical link, build the documentation, and inspect the rendered installer and capacity-planning pages.
