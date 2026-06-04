---
type: initiative
slug: docs-gap-analysis-9
status: active
horizon: now
title: "Documentation Gap Analysis & Sprint Plan (9.0.0)"
tags: [9.0.0, meta, planning]
---

# Documentation Gap Analysis — 9.0.0

## Executive Summary

Code audit of `morpheus-ui` (1,615 services) against current docs reveals **~85 significant documentation gaps** across all sections. These range from entirely missing feature surfaces (AI/MCP) to undocumented sub-features of existing pages.

## Sprint Plan (Priority Order)

| Sprint | Focus | Priority | Gaps | Effort |
|--------|-------|----------|------|--------|
| 1 | AI/LLM & MCP | CRITICAL | 6 | 5 new pages |
| 2 | Networking & Security | HIGH | 16 | 12 new pages, 5 expansions |
| 3 | Storage, LBs & Infra Ops | HIGH | 18 | 8 new pages, 10 expansions |
| 4 | Kubernetes, Containers & VDI | HIGH | 12 | 7 new pages, 3 expansions |
| 5 | Operations, Costing & Approvals | MEDIUM | 15 | 5 new pages, 8 expansions |
| 6 | Certificates, DNS, SCM & Provisioning | MEDIUM | 18 | 8 new pages, 10 expansions |

## Top 10 Most Impactful Gaps

1. **AI/LLM/MCP** — Entirely new feature surface, zero docs
2. **NSX-T Integration Guide** — Major networking product, no guide
3. **Kubernetes Jobs/Helm upgrades** — Key K8s lifecycle, undocumented
4. **Network Security Servers** — Full security subsystem, no docs
5. **BMC Remedy Approvals** — Enterprise approval integration, no docs
6. **VDI Apps & Gateways** — Critical for VDI deployments
7. **A10/Avi Load Balancers** — Enterprise LB integrations, no guides
8. **HPE 3PAR/Primera Storage** — HPE's own storage, no guide
9. **Certificate Management** — Core trust feature, undocumented
10. **PowerVC Cloud** — IBM Power integration, no guide

## Methodology

Each section was audited by comparing:
- RST file content (what's documented)
- Controller classes (what's exposed in UI)
- Service classes (what capabilities exist)
- Seed data (what types/options are registered)

Gaps were classified by operator impact — internal implementation details were excluded.
