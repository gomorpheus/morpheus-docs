---
title: "Javascript version interpreter details for automation tasks listing"
slug: docs-morph-5613-javascript-task-runtime
type: feature
status: completed
horizon: now
size: small
tags: [documentation, automation, javascript, tasks]
tracker_id: MORPH-5613
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:31Z
---
# Javascript version interpreter details for automation tasks listing

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-5613

Jira description (verbatim):

> Can we please add details about the Javascript version and interpreter on our Morpheus nodes which are used for automation tasks?

JavaScript Tasks are listed in `library/automation/tasks.rst`; execution permissions are described in `administration/roles/role_permissions.rst`. The repository does not state an interpreter or ECMAScript version.

## Goal

Document the verified JavaScript Task runtime/interpreter, version discovery method, supported language/API boundaries, execution location, and upgrade/version caveats.

## Kickoff

Add verified JavaScript runtime and interpreter details to the automation Tasks reference.

**Status:** planning — the task type is documented but runtime identity and version are absent and unverified.

**Pick up at:** ask automation engineering for the runtime contract and confirm it on each currently supported appliance release.

→ `.hero/planning/features/docs-morph-5613-javascript-task-runtime/spec.md`

**Files:** `library/automation/tasks.rst`, `administration/roles/role_permissions.rst`, `getting_started/additional/logback.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Add a runtime note directly to the JavaScript Task listing. Prefer a product-supported runtime contract and safe detection method over incidental package inspection.

## Changes

1. `library/automation/tasks.rst` — Documented the embedded GraalJS Community runtime, application-node execution, host-access boundary, pinned source version, and release validation guidance.

## Acceptance Criteria

- WHEN a user selects a JavaScript Task THE DOCUMENTATION SHALL identify the runtime/interpreter and where it executes.
- THE DOCUMENTATION SHALL explain whether runtime versions vary by Morpheus release and how to verify the supported version safely.
- IF no stable runtime contract exists THEN THE DOCUMENTATION SHALL state that scripts must target the documented compatibility baseline rather than invent a version.

## Boundaries

No runtime upgrade, JavaScript tutorial, Node.js assumption, or API compatibility promise beyond engineering approval.

## Risks

- **Blocker:** Runtime identity, version, and compatibility policy require automation engineering confirmation.
- The implementation may not be Node.js despite user expectations.

## Validation

Run representative syntax/features in a JavaScript Task on supported releases, verify the documented detection method, obtain engineering review, and run `make build`.
