---
type: feature
status: delivering
horizon: now
tags: [documentation, storage, hvm, field-feedback]
parent: docs-field-feedback-improvements
---

# FC Storage Connection

## Objective

Document Fibre Channel storage connectivity for HVM clusters.

## Acceptance Criteria

1. Covers FC zoning requirements for HVM hosts
2. Documents multipath configuration (multipathd setup)
3. Explains LUN presentation and discovery on HVM hosts
4. Documents datastore creation from FC LUNs in Morpheus
5. Includes prerequisites (HBA firmware, driver versions, switch configuration)

## Changes

- `infrastructure/clusters/hvm/storage_operations.rst` — Add FC storage connection section (or new file)
