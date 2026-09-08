# Completion Ledger — docs-hvm-witness-gfs2-quorum

Delivered 2026-09-04 against `../morpheus-ui` `StatsService` Site Group discriminator, `MvmHostService.shouldSendQuorumInfo()`, and `_summaryQuorum.gsp`.

Validation: Sphinx HTML for changed HVM/Worker pages. `workers.rst` and `building_clusters.rst` list-tables parse. Pre-existing repo Sphinx warnings/errors unchanged.

## docs-hvm-quorum-topology-model

### Acceptance Criteria

| # | Criterion | Status | Note |
|---|---|---|---|
| 1 | Distinct two-node GFS2 and stretch topologies sharing Distributed Worker and GFS2 activation | DONE | `architecture.rst` Witness Topologies table |
| 2 | Two-node GFS2 does not use Site Groups or `siteWitness` | DONE | Table Site Groups row + warning |
| 3 | Agent quorum sent only for layout 1.3+ with GFS2 | DONE | Activation rows and intro paragraph |
| 4 | Two-node majority is 2 of 3, counting the witness | DONE | Majority Calculation paragraph |
| 5 | Witness common; Sites stretch-only | DONE | Quorum panel row |
| 6 | Do not copy stretch same-site cross-verification onto two-node | DONE | Peer Communication split |
| 7 | Site Groups on two-node switch witness to `siteWitness` | DONE | warning directive |

### Changes

| # | Item | Status | Note |
|---|---|---|---|
| 1 | `architecture.rst` Quorum Algorithm | DONE | Peer, majority, Witness Topologies, warning |
| 2 | Chooser sentences on `hvm.rst`, `two_node_clusters.rst`, `stretch_clusters.rst` | DONE | |
| 3 | Do not retarget `workers.rst` | DONE | Left to discovery child |

### Exercise-the-feature check

- [x] Rendered `/tmp/hvm-docs-check/infrastructure/clusters/hvm/architecture.html` Witness Topologies heading, 2 of 3 majority, `siteWitness` warning, and working `:doc:` links.

## docs-hvm-two-node-gfs2-operations

### Acceptance Criteria

| # | Criterion | Status | Note |
|---|---|---|---|
| 1 | Assignment, GFS2 activation, Quorum validation on two-node page | DONE | Deployment steps 1–7 and Quorum Validation |
| 2 | Expected panel values: 3 members, witness reachable, no Sites | DONE | Quorum Validation bullets |
| 3 | Timed Host, witness, combined, and partition failures | DONE | `failure_scenarios.rst` |
| 4 | Must not use Site Groups or `siteWitness` | DONE | Limitations |
| 5 | Agent quorum authority when Corosync `Quorate: No` | DONE | Quorum Validation |
| 6 | Runbook does not require stretch for assignment/validation | DONE | Edit path is \|InfClu\|; Worker install still `workers.rst` |
| 7 | Do not apply alphabetical site-winner to two-node partitions | DONE | Partition recovery sentence |

### Changes

| # | Item | Status | Note |
|---|---|---|---|
| 1 | Expand deployment and Quorum Validation | DONE | Witness after create; HTTPS `/witness/<cluster UUID>/quorum` |
| 2 | Timing note + maintenance | DONE | 60s vs 140s |
| 3 | Replace one-paragraph two-node failures | DONE | Four timed scenarios |
| 4 | Two-node troubleshooting | DONE | GFS2-not-yet and Sites-row items |
| 5 | Site Group limitation warning | DONE | Links `host_vm_groups` as creation location only |

### Exercise-the-feature check

- [x] Read rendered two-node Quorum Validation list and `failure_scenarios.rst` four timed tables.

## docs-hvm-witness-discovery-crosslinks

### Acceptance Criteria

| # | Criterion | Status | Note |
|---|---|---|---|
| 1 | Worker assignment links two-node and stretch separately | DONE | `workers.rst` capability cell + lines 316–319 |
| 2 | Stretch is not the default generic assignment destination | DONE | |
| 3 | Site Groups warned as stretch-only | DONE | `host_vm_groups.rst` |
| 4 | Troubleshooting marks Sites stretch-only | DONE | |
| 5 | Worker URL/TLS warnings remain | DONE | Unchanged in Witness Configuration |

### Changes

| # | Item | Status | Note |
|---|---|---|---|
| 1 | `workers.rst` Witness Configuration next steps | DONE | |
| 2 | `host_vm_groups.rst` Site Group bullet | DONE | |
| 3 | `troubleshooting.rst` panel list + Corosync note | DONE | Also \|InfClu\| |
| 4 | `building_clusters.rst` Witness field + edge guide | DONE | |
| 5 | `hvm.rst` chooser already present from topology child | DONE | Not re-edited |

### Exercise-the-feature check

- [x] Confirmed `workers.rst` no longer has a lone stretch assignment sentence. Grep of `stretch_clusters` shows paired two-node links on Worker, building, edge, architecture, troubleshooting, and Site Groups.

### Excellence Bar self-check

Yes — operators can now choose two-node GFS2 without opening stretch, and the discriminator matches `StatsService`.
