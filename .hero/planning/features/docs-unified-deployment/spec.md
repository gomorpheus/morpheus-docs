---
title: "Unified Deployment Documentation"
type: feature
slug: docs-unified-deployment
status: planning
priority: high
horizon: now
parent: unified-docs-merge
---

# Unified Deployment Documentation

## Purpose

Update installation and deployment docs to reflect that all three tiers use the same binary and support the same deployment models. Remove any language suggesting separate installers or deployment paths per tier.

## Scope

- `getting_started/` — installation, system requirements, upgrades
- Remove references to separate VM Essentials installer/appliance
- Clarify that license key determines tier, not install method
- Ensure all supported deployment models (single-node, HA, distributed) are documented as tier-agnostic

## Acceptance Criteria

- [ ] Installation docs make no distinction between tiers for deployment
- [ ] System requirements page is unified (one product)
- [ ] License activation/tier selection documented clearly
- [ ] Upgrade paths documented as tier-agnostic
