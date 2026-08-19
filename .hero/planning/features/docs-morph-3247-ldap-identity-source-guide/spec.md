---
title: "Add integration guide for LDAP identity sources"
slug: docs-morph-3247-ldap-identity-source-guide
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, integration-guide, ldap, identity-management]
tracker_id: MORPH-3247
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:31Z
---
# Add integration guide for LDAP identity sources

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3247

Jira description (verbatim):

> We have an active directory integration guide but not one for LDAP. Need to create one.

Identity guide navigation exists in `integration_guides/IdentityManagement/IdentityManagement.rst`, with patterns in `active_directory.rst`, `saml.rst`, and `okta.rst`. A repository search confirmed LDAP references but no dedicated identity-source guide.

## Goal

Create a complete LDAP identity-source integration guide covering prerequisites, connectivity/TLS, field configuration, user/group and role mapping behavior, testing, troubleshooting, and security guidance.

## Kickoff

Add the missing LDAP identity-source integration guide using current identity-management patterns and verified UI fields.

**Status:** planning — adjacent Active Directory, SAML, and Okta guides are available as structural references.

**Pick up at:** capture the current LDAP identity-source form and validate LDAP/LDAPS bind, search, mapping, and login flows.

→ `.hero/planning/features/docs-morph-3247-ldap-identity-source-guide/spec.md`

**Files:** `integration_guides/IdentityManagement/IdentityManagement.rst`, `integration_guides/IdentityManagement/active_directory.rst`, `integration_guides/IdentityManagement/saml.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Create a dedicated RST page matching established integration-guide style. Prefer LDAPS, explain required fields and mapping semantics, and add navigation without duplicating general role documentation.

## Changes

1. `integration_guides/IdentityManagement/ldap.rst` — Added the application-backed LDAP configuration, mapping, security, test, and troubleshooting guide.
2. `integration_guides/IdentityManagement/IdentityManagement.rst` — Added LDAP to the identity-management toctree.

## Acceptance Criteria

- WHEN an administrator configures LDAP THE DOCUMENTATION SHALL cover prerequisites, LDAP/LDAPS connectivity, bind/search fields, user/group mapping, role mapping, testing, and troubleshooting.
- THE DOCUMENTATION SHALL recommend certificate validation and avoid sample production secrets.
- IF a field or mapping behavior is version-dependent THEN THE DOCUMENTATION SHALL scope it explicitly.

## Boundaries

No LDAP server deployment, Active Directory guide rewrite, SAML/OIDC behavior, or identity-source product changes.

## Risks

- Exact LDAP UI fields and role mapping semantics must be captured from a supported current release.
- Insecure TLS or broad bind permissions could be copied into production if examples are careless.

## Validation

Test LDAP and LDAPS with representative user/group mappings, verify least-privilege bind examples, run `make build`, and inspect navigation and rendered field definitions.
