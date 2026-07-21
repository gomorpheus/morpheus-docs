---
type: feature
status: delivering
horizon: now
tags: [documentation, windows, image-prep, field-feedback]
parent: docs-field-feedback-improvements
---

# Windows Cloud Guest Customization

## Objective

Document the recommended "cloud guest customization" image preparation approach for Windows VMs. This is the recommended approach but currently has no documentation.

## Acceptance Criteria

1. Explains what cloud guest customization means for Windows (cloudbase-init)
2. Documents image preparation steps (install cloudbase-init, configure, sysprep)
3. Covers what customization options are available at provision time (hostname, network, admin password, domain join, scripts)
4. Documents how this differs from traditional sysprep-only approach
5. Includes a recommended base image preparation checklist

## Changes

- `provisioning/virtual_images/windows_image_prep.rst` (new or expand existing) — Cloud guest customization guide
