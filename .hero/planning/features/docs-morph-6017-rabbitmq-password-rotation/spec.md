---
title: "Steps to Update and Apply RabbitMQ User Password on Morpheus Application Nodes"
slug: docs-morph-6017-rabbitmq-password-rotation
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, rabbitmq, security, password-rotation, appliance]
tracker_id: MORPH-6017
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:02:52Z
---
# Steps to Update and Apply RabbitMQ User Password on Morpheus Application Nodes

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-6017

Jira description (verbatim):

> On each application node, you will need to do the following:
>
> 1. Source .profile to get the binaries in your PATH: source /opt/morpheus/embedded/rabbitmq/.profile
> 2. Change the user password: rabbitmqctl change_password queue_user <password>
> 3. Test the authentication: rabbitmqctl authenticate_user queue_user
> 4. Update the password for the user in /etc/morpheus/morpheus-secrets.json
> 5. Reconfigure morpheus so the password is updated in the application configuration files: morpheus-ctl reconfigure
> 6. Restart the morpheus-ui service: morpheus-ctl restart morpheus-ui

RabbitMQ configuration is documented in `getting_started/external_services/rabbitmq.rst`, with appliance commands in `getting_started/maintenance/morpheus-ctl.rst` and secrets context in `getting_started/additional/encryption.rst`.

## Goal

Document an engineering-approved, HA-aware RabbitMQ `queue_user` password rotation procedure with secure secret handling, sequencing, authentication checks, service impact, rollback, and external-RabbitMQ distinctions.

## Kickoff

Turn the Jira command list into a validated, secure, HA-aware RabbitMQ password rotation runbook.

**Status:** planning — related RabbitMQ and control docs exist; ordering and multi-node behavior require testing.

**Pick up at:** test rotation in single-node and 3-node configurations, including rollback after a partial update.

→ `.hero/planning/features/docs-morph-6017-rabbitmq-password-rotation/spec.md`

**Files:** `getting_started/external_services/rabbitmq.rst`, `getting_started/maintenance/morpheus-ctl.rst`, `getting_started/additional/encryption.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Add the procedure to the RabbitMQ service page, split embedded and external deployments, avoid secrets in shell history where possible, and explicitly sequence HA nodes to prevent credential mismatch.

## Changes

1. `getting_started/external_services/rabbitmq.rst` — Documented that reconfigure does not rotate an existing user and replaced the unsafe command sequence with the supported Support-assisted boundary.
2. `getting_started/maintenance/morpheus-ctl.rst` — Clarified that reconfigure is not a general credential-rotation operation.
3. `getting_started/additional/encryption.rst` — Distinguished ENC conversion from service credential rotation and cross-referenced the RabbitMQ limitation.

## Acceptance Criteria

- WHEN an administrator needs to rotate `queue_user` credentials THE DOCUMENTATION SHALL explain that no supported self-service sequence exists and direct the administrator to HPE Support for topology-specific ordering and rollback.
- THE DOCUMENTATION SHALL warn that broker/application credential mismatch interrupts messaging and SHALL not publish an unverified HA sequence.
- THE DOCUMENTATION SHALL explain that reconfigure creates a missing RabbitMQ user but does not update the password of an existing user.
- THE DOCUMENTATION SHALL distinguish embedded from external RabbitMQ and avoid exposing real passwords.

## Boundaries

No password policy change, automated rotation tool, arbitrary `morpheus-secrets.json` editing guidance, or unsupported zero-downtime guarantee.

## Risks

- **Blocker:** Jira commands and ordering need appliance engineering validation, especially for HA.
- Direct secret-file changes and shell arguments can leak credentials or break service connectivity.

## Validation

Execute on single-node and HA systems, test old/new authentication and rollback, review logs without exposing secrets, obtain appliance engineering/security approval, and run `make build`.
