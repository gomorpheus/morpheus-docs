---
title: "OKTA/SAML role attribute mapping limitation in Morpheus/VME"
slug: docs-morph-3258-okta-saml-role-mapping-limit
type: feature
status: completed
horizon: now
size: small
tags: [documentation, okta, saml, identity-management, rbac]
tracker_id: MORPH-3258
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:31Z
---
# OKTA/SAML role attribute mapping limitation in Morpheus/VME

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3258

Jira description (verbatim):

> In Morpheus/VME, users cannot map multiple roles from the identity source using space- or comma-separated values in the role attribute. This limitation can restrict effective role-based access control in some environments. Document this limitation

Current role mapping is documented in `integration_guides/IdentityManagement/okta.rst` and `saml.rst`, with adjacent role semantics in `administration/roles/role_permissions.rst`.

## Goal

Document the verified role-attribute cardinality and delimiter limitation for Okta/SAML, its effect on role assignment, and supported configuration alternatives without implying an unsupported workaround.

## Kickoff

Clarify the verified Okta/SAML role-attribute mapping limitation and supported alternatives.

**Status:** planning — relevant identity pages exist; behavior across generic SAML and Okta needs confirmation.

**Pick up at:** test single and multiple attribute values using space and comma delimiters on a supported release.

→ `.hero/planning/features/docs-morph-3258-okta-saml-role-mapping-limit/spec.md`

**Files:** `integration_guides/IdentityManagement/okta.rst`, `integration_guides/IdentityManagement/saml.rst`, `administration/roles/role_permissions.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Add a focused limitation note beside role mapping configuration on both applicable provider pages, using identical terminology and a supported alternative only if validated.

## Changes

1. `integration_guides/IdentityManagement/okta.rst` — Scoped the limitation to Okta applications using SAML SSO.
2. `integration_guides/IdentityManagement/saml.rst` — Documented exact per-value equality and the multi-value assertion alternative.

## Acceptance Criteria

- WHEN an administrator configures role attributes THE DOCUMENTATION SHALL state whether multiple values and space/comma delimiters are supported.
- IF a supported alternative exists THEN THE DOCUMENTATION SHALL describe it and its tradeoffs.
- THE DOCUMENTATION SHALL scope the limitation by identity-source type and version when behavior differs.

## Boundaries

No RBAC feature change, custom assertion transformation tutorial, or claim that multiple roles are impossible through every mapping mechanism.

## Risks

- The Jira claim may apply differently to Okta-specific and generic SAML integrations.
- Incorrect guidance could grant too much or too little access.

## Validation

Test representative assertions and resulting user roles, obtain identity engineering review, run `make build`, and compare notes across both rendered guides.
