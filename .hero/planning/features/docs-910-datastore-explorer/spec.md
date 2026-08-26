---
title: "9.1.0 Docs: Datastore Explorer"
slug: docs-910-datastore-explorer
type: feature
status: planning
horizon: now
tags: [9.1.0, docs]
priority: 1
jira: MORPH-3181
---

# 9.1.0 Docs: Datastore Explorer

## Summary

Document the new Datastore Explorer feature that adds clickable detail views to datastores in Infrastructure → Clusters → Datastores and Infrastructure → Storage → Data Stores, including VM inventory, volume usage, and a file browser for file-type datastores.

## Acceptance Criteria

1. Document how to access the Datastore detail view from both Infrastructure → Clusters → Datastores and Infrastructure → Storage → Data Stores list views.
2. Document the VM/Instance Inventory tab showing VMs stored on the datastore with name, power state, owner/tenant, and allocated storage.
3. Document the Volume Usage tab listing all storage volumes with name, size, associated VM, volume type, and aggregate used/free capacity.
4. Document the File Browser tab (conditional on `diskType == 'file'`): directory navigation, file upload, download, and delete operations. Note that directories can only be deleted, not added/downloaded.
5. Document permissions: `infrastructure-storage` read for the detail view, `infrastructure-storage-browser` read/full for the file browser tab.
6. Document the API extension: `GET /api/datastores/:id` returning volumes, vms, and stats.
7. Note agent dependency: download requires the latest morpheus-agent.

## Sources

- Jira: MORPH-3181
- PR: morpheus-ui #4150, #4153
