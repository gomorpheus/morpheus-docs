---
type: feature
status: delivering
horizon: now
tags: [documentation, migrations, windows, field-feedback]
parent: docs-field-feedback-improvements
---

# Windows VM Migration Conflict Resolution

## Objective

Resolve conflicting information between two Windows VM migration sections in the published docs. The automated migration prep (9.0+) and the legacy manual VirtIO driver install procedure should be consolidated into a single clear narrative.

## Context

Two published doc pages conflict:
- GUID-3A8E263B-7508-4620-A5C6-5372D385F0DB — Automated Windows migration preparation
- GUID-D8021277-53D1-43E9-9799-785A2511910E — Manual/legacy VirtIO driver installation

The second page should not be needed for 9.0+ where automated driver injection handles everything. Both pages existing without clear relationship creates confusion.

## Acceptance Criteria

1. Single authoritative section for Windows VM migration that covers the automated flow as the primary path
2. Manual/legacy approach is clearly marked as fallback-only with a note on when it might be needed
3. No conflicting or duplicated information between sections
4. Clear version applicability (9.0+ uses automated, pre-9.0 may need manual)

## Changes

- `tools/migrations/windows_2022.rst` — Verify it already handles this correctly (it may already be resolved in our local docs)
