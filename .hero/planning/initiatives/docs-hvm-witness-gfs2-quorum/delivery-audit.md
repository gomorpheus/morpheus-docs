# Delivery audit — docs-hvm-witness-gfs2-quorum

**Audited:** `git diff -- infrastructure/clusters/hvm administration/integrations/workers.rst getting_started/guides/edge_site_management.rst` @ `c54eac065` plus unstaged working tree
**Verdict:** SHIP
**Surface:** noteworthy

Children audited from disk: `docs-hvm-quorum-topology-model`, `docs-hvm-two-node-gfs2-operations`, `docs-hvm-witness-discovery-crosslinks`. Ledger rows are all DONE; each maps to a real RST change. No performative DONE rows.

## Acceptance criteria

### docs-hvm-quorum-topology-model

- [✓] Distinct two-node GFS2 and stretch topologies sharing Distributed Worker and GFS2 activation — `infrastructure/clusters/hvm/architecture.rst:47-79` Witness Topologies table
- [✓] Two-node GFS2 does not use Site Groups or `siteWitness` — table Site Groups / classification rows `architecture.rst:62-70`
- [✓] Agent quorum sent only for layout 1.3+ with GFS2 — `architecture.rst:50` and Activation row `:77-79`
- [✓] Two-node majority is 2 of 3, counting the witness — `architecture.rst:43`
- [✓] Witness common; Sites stretch-only — Quorum panel row `architecture.rst:74-76`
- [✓] Do not copy stretch same-site cross-verification onto two-node — Peer Communication split `architecture.rst:31-32`
- [✓] Site Groups on two-node switch witness to `siteWitness` — warning `architecture.rst:81`

### docs-hvm-two-node-gfs2-operations

- [✓] Assignment, GFS2 activation, and Quorum validation on `two_node_clusters.rst` — Deployment steps 1–7 `:39-47` plus Quorum Validation `:78-93`
- [✓] Expected panel values: 3 members, witness reachable, no Sites — `two_node_clusters.rst:83-91`
- [✓] Timed Host, witness, combined, and partition failures — `failure_scenarios.rst:116-191`
- [✓] Must not use Site Groups or `siteWitness` — Limitations `two_node_clusters.rst:144`
- [✓] Agent quorum authority when Corosync `Quorate: No` — `two_node_clusters.rst:93`
- [✓] Runbook does not require stretch for assignment/validation — Edit path is `|InfClu|` `:42`; Worker install is `:ref:`hvm-witness-deployment`` / `workers.rst`
- [✓] Do not apply alphabetical site-winner to two-node partitions — `failure_scenarios.rst:119` and `:191`

### docs-hvm-witness-discovery-crosslinks

- [✓] Worker assignment links two-node and stretch separately — `administration/integrations/workers.rst:34` and `:316-319`
- [✓] Stretch is not the default generic assignment destination — lone stretch sentence removed; both runbooks listed
- [✓] Site Groups warned as stretch-only — `infrastructure/clusters/hvm/host_vm_groups.rst:53`
- [✓] Troubleshooting marks Sites stretch-only — `troubleshooting.rst:19`
- [✓] Worker URL/TLS warnings remain — `workers.rst:306-314` unchanged except next-step split

### Initiative (`docs-hvm-witness-gfs2-quorum`)

- [✓] Peer topologies sharing Distributed Worker and GFS2 activation — architecture table
- [✓] Two-node GFS2 does not use site groups or `siteWitness` — architecture warning + two-node Limitations
- [✓] Two-node assignment/validation path without stretch procedures — `workers.rst` + `two_node_clusters.rst`
- [✓] Two-node Host/witness/partition failures at stretch-equivalent specificity — four timed tables in `failure_scenarios.rst:121-191` vs stretch Scenario 4 `:85-114`
- [✓] Agent quorum distinguished from Corosync `Quorate` for both topologies — `architecture.rst:45`, `troubleshooting.rst:29`
- [✓] Stretch arbitration/Site Group rules not copied onto two-node — peer split + partition recovery sentence

## Changes

### docs-hvm-quorum-topology-model

- [✓] `architecture.rst` Quorum Algorithm — peer split, 2-of-3 majority, Witness Topologies table, Site Group warning
- [✓] Chooser sentences on `hvm.rst:83-85`, `two_node_clusters.rst:8`, `stretch_clusters.rst:9`
- [✓] Do not retarget `workers.rst` in this spec — left to discovery child (who did retarget it)

### docs-hvm-two-node-gfs2-operations

- [✓] Expand deployment and Quorum Validation — Witness after create; HTTPS `/witness/<cluster UUID>/quorum` without `--insecure` (`two_node_clusters.rst:70-76`)
- [✓] Timing note + maintenance — 60s vs 140s `two_node_clusters.rst:124-126`
- [✓] Replace one-paragraph two-node failures — four timed scenarios `failure_scenarios.rst:116-191`
- [✓] Two-node troubleshooting — GFS2-not-yet and Sites-row items `two_node_clusters.rst:132-133`
- [✓] Site Group limitation warning — links `host_vm_groups` as creation location only `two_node_clusters.rst:144`

### docs-hvm-witness-discovery-crosslinks

- [✓] `workers.rst` Witness Configuration next steps — `:316-319`
- [✓] `host_vm_groups.rst` Site Group bullet — `:53`
- [✓] `troubleshooting.rst` panel list + Corosync note — `:7`, `:19`, `:29`
- [✓] `building_clusters.rst` Witness field + edge guide — `building_clusters.rst:70`, `edge_site_management.rst:74`
- [✓] `hvm.rst` chooser already present from topology child — not re-edited beyond topology bullets

## Open items (if any)

- Initiative Kickoff / Progress: HVM engineering review of two-node vote math, failure matrix, and Site Group exclusion remains before publication — not a ledger PARTIAL; process gate, not a missing doc row — concrete

## Audit notes

- Working-tree RST matches every ledger DONE row. Grep of `stretch_clusters` in the scoped RST files shows paired two-node links on Worker, building, edge, architecture, troubleshooting, and Site Groups. Remaining stretch-only links are topology-specific (stretch host-count, stretch arbitration, two-node “if you meant to convert”).
- Sphinx HTML exists on disk: `/tmp/hvm-docs-check` (architecture/hvm/stretch/two_node), `/tmp/hvm-docs-tables` (workers/building_clusters/hvm; list-tables parsed), `/tmp/hvm-docs-final` (full changed HVM set including failure_scenarios, host_vm_groups, troubleshooting). `/tmp/hvm-docs-check` two-node Limitations HTML is an earlier snapshot; current RST and `/tmp/hvm-docs-final` include the Site Group warning.
- Internal names `witnessOnly` / `site: null` were not published. `siteWitness` appears only where the specs allow it.
- No new files. Diff is scoped to the named RST pages. No SKIPPED/BLOCKED/PARTIAL ledger rows. No downgrades.
