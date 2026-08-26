---
title: "Guest Customization Compatibility Matrix"
type: feature
status: planning
---

## Description

The cloud coverage page (integration_guides/Clouds/cloudCoverage/cloudCoverage.rst) lacks a Guest Customization section showing which clouds support which guest OS customization methods. Customer feedback indicates the current docs inconsistently mention guest customization support — sometimes only VMware is mentioned, elsewhere HVM and SCVMM are noted as compatible. A clear matrix table is needed.

## Changes

- `integration_guides/Clouds/cloudCoverage/cloudCoverage.rst` — Add Guest Customization compatibility matrix table

## Acceptance Criteria

- New "Guest Customization" table added to the cloud coverage feature matrix
- Table columns cover: Linux cloud-init, Windows Sysprep/Unattend, Force Guest Customization, Cloudbase-Init
- All actively supported clouds have accurate entries
- Cross-references from cloud-specific pages where guest customization is mentioned inconsistently
