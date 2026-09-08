---
title: HVM Witness Topology Is Site Groups, Not Host Count
type: context
status: active
tags: [hvm, witness, quorum, gfs2, stretch-cluster]
created: 2026-09-04
---

## Context

`StatsService.sendQuorumDetailsToWorker()` and `sendQuorumDetailsToServer()` classify the Distributed Worker witness by Site Group presence, not by host count.

If any `HostVmGroupType.SITE_GROUP` exists, the worker is labeled `site: 'siteWitness'` (stretch). If none exist, it is labeled `site: null` with the source comment `use this for 2 node gfs2 witness`.

Adding Site Groups to a two-Host GFS2 cluster therefore switches it to stretch witness behavior. Agent quorum is sent only when `MvmHostService.shouldSendQuorumInfo()` is true: layout 1.3+ and at least one GFS2 datastore.

Do not document two-node GFS2 using stretch same-site peer or alphabetical site-winner rules. Keep those on `stretch_clusters.rst`.
