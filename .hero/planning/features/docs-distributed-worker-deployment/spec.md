---
title: "Distributed Worker Package and Container Deployment"
slug: docs-distributed-worker-deployment
type: feature
status: in-review
size: small
horizon: now
priority: high
tags: [distributed-worker, docker, tls, installation]
parent: docs-distributed-worker-guide
depends-on: [docs-distributed-worker-capabilities]
created: 2026-07-30
claimed_by: mcp-agent
claimed_at: 2026-07-30T11:00:55-04:00
---

# Distributed Worker Package and Container Deployment

## Context

Package instructions live on the Distributed Worker and legacy VDI pages, while container instructions are buried in `tools/vdi_pools.rst` and Docker Hub. The examples do not consistently explain Worker-only, gateway-only, and combined key configurations.

## Goal

Provide current, role-aware package and container deployment procedures with explicit connectivity, port, TLS, key, URL, health, and upgrade requirements.

## Approach

Make `administration/integrations/workers.rst` canonical for runtime deployment. Retain concise VDI task links elsewhere and remove or redirect stale duplicate commands. Verify every container variable against the checked-out Docker entrypoint and link to `morpheusdata/morpheus-worker` without treating Docker Hub prose as the sole source of truth.

## Changes

1. Reconcile package operating system, CPU, memory, storage, repository, certificate trust, and connectivity requirements with the current supported release.
2. Document Worker-only, gateway-only, and combined package configuration examples using `worker_url`, `appliance_url`, `worker_key`, and `apikey`.
3. Add container examples for the `morpheusdata/morpheus-worker` image using `MORPHEUS_URL`, `MORPHEUS_WORKER_KEY`, optional `MORPHEUS_KEY`, and HTTP or HTTPS listener choices.
4. Document self-signed development TLS, PKCS#12 configuration using `MORPHEUS_SSL_ALIAS` and `MORPHEUS_SSL_PASSWORD`, and production certificate or load-balancer termination guidance.
5. Document published ports, Manager/browser/Host reachability by role, logs or health checks, version pinning, upgrades, and HA deployment.
6. Consolidate or redirect duplicate Docker and package content in `tools/vdi_pools.rst` and `infrastructure/vdi/gateways.rst`.

## Acceptance Criteria

- THE DOCUMENTATION SHALL provide separate Worker-only, gateway-only, and combined-role package and container examples.
- THE DOCUMENTATION SHALL explain every required and optional Worker container environment variable.
- THE DOCUMENTATION SHALL distinguish outbound Manager connectivity from inbound gateway or witness reachability.
- THE DOCUMENTATION SHALL document production TLS and certificate trust requirements without recommending self-signed TLS for production.
- THE DOCUMENTATION SHALL use a confirmed supported image tag strategy and link to `morpheusdata/morpheus-worker`.
- THE DOCUMENTATION SHALL include startup, health, log, upgrade, and HA validation steps.

## Boundaries

- Do not publish image build or release-maintainer instructions from the Worker README.
- Do not document in-development plugin classloader or reverse proxy console capabilities as available.

## Risks

- Docker Hub's `latest` tag can drift from the Manager release; production guidance must be version-aware.
- Package and container listener defaults differ, particularly around 443, 8080, and 8443.
- Existing OS support tables are stale and inconsistent and require release-owner confirmation.

## Validation

- Compare commands and variables with `Dockerfile`, `docker-run-worker.sh`, `application.yml`, and `WorkerConfig.groovy`.
- Validate package options against the current package template or release artifact owner.
- Run the documentation build and manually inspect command wrapping and substitutions.

## Delivery

- Added separate package and container examples for Worker-only, gateway-only, and combined modes.
- Documented `MORPHEUS_URL`, `MORPHEUS_WORKER_KEY`, `MORPHEUS_KEY`, self-signed test TLS, PKCS#12 production TLS, and outbound proxy configuration.
- Added package and container health, logs, upgrade, and HA guidance; distinguished outbound Manager connectivity from inbound gateway and witness paths.
- Pinned examples to the confirmed `9.0.2` tag and documented Docker Hub maintenance visibility plus the requirement to match an approved Manager release.
- All six acceptance criteria pass against `Dockerfile`, `docker-run-worker.sh`, `WorkerConfig.groovy`, Docker Hub information, and rendered HTML.

## Kickoff

Consolidates supported Worker package and container deployment for worker, gateway, and combined modes.

**Status:** in-review - package and container guidance is implemented and validated.

**Pick up at:** review release-support wording and approve the canonical deployment procedures.

→ `.hero/planning/features/docs-distributed-worker-deployment/spec.md`

**Files:** `administration/integrations/workers.rst`, `tools/vdi_pools.rst`, `infrastructure/vdi/gateways.rst`, `../morpheus-worker/docker-run-worker.sh`, `../morpheus-worker/Dockerfile`
