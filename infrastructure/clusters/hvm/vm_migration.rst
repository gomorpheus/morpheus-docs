VM Migration & Failover
=======================

Live Migration
--------------

Live migration moves a running VM from one cluster host to another with no downtime to the guest operating system.

Requirements
^^^^^^^^^^^^

- The VM must be running (powered on)
- The VM's storage must reside on a shared datastore (HPE Clustered Datastore or NFS), or every local volume must be mapped to a target datastore. Unmapped local storage cannot be live-migrated
- No host devices (GPU/USB passthrough) are attached to the VM
- The target host must have sufficient available memory
- Network connectivity between source and target hosts
- The VM CPU definition must be supported by both hosts. Named CPU models use exact matching; choose a named model supported by every host on which the VM can run
- VMs using Host Passthrough with nested virtualization enabled are non-migratable

Mixed CPU Hosts
^^^^^^^^^^^^^^^

Before admitting different CPU models to one cluster, configure one exact named CPU model that is supported by every source and destination host, then test a live migration in both directions. Configure the model while creating or editing the cluster using the **CPU Architecture/Model** field. Compatibility is based on that exact common model, not a universal rule to select the processor marketed as "lowest" or oldest.

Do not assume that |morpheus| automatically selects the lowest processor generation. Host Passthrough's migratable setting is not a guarantee that arbitrary physical CPU combinations can live-migrate. If both directions have not been validated, use homogeneous hosts or keep affected VMs on a compatible host set.

Initiating a Live Migration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start a move from any of these locations:

- Instance detail: |ProIns| > select the Instance > :guilabel:`Actions` > :guilabel:`Move`
- Virtual machine detail: |InfComVir| > select the VM > :guilabel:`Actions` > :guilabel:`Move`
- Cluster inventory: |InfClu| > select the cluster > :guilabel:`Virtual Machines` > select the VM > :guilabel:`Actions` > :guilabel:`Move`

The user must have **Infrastructure: Manage Placement** at User or Full.

In the Move dialog:

#. Select the **Target Cluster**. Leave the current cluster selected to move within the same cluster. Choose a different HVM cluster in the same Cloud for a cross-cluster move.
#. Optionally select a **Target Host**. Leave blank to auto-select a host in the target cluster.
#. For a different cluster, map datastores and networks as described in `Moving VMs Between HVM Clusters`_.
#. Optionally enable **CPU Throttling** and set a **Migration Timeout** in seconds (default 6000; range 30–7200).
#. Click :guilabel:`Move`.

.. NOTE:: |morpheus| automatically determines whether to perform a live or cold migration based on the VM's current power state and storage configuration.

What Happens During Live Migration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. A migration lock is acquired to prevent concurrent migrations of the same VM
#. Storage pools are refreshed on the target host to ensure it can access the VM's disks
#. Network preparation ensures the target host has the correct bridge configurations
#. The migration executes, transferring the VM's memory state to the target host
#. Upon completion, the VM's parent host reference is updated in |morpheus|
#. The migration lock is released

Migration Options
^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Option
     - Description
   * - Migration Timeout
     - Maximum time allowed for the migration to complete before it is cancelled
   * - CPU Throttling
     - When enabled, throttles the VM's CPU during migration to help convergence for memory-intensive workloads

Moving VMs Between HVM Clusters
-------------------------------

Use :guilabel:`Actions` > :guilabel:`Move` to relocate a running HVM/KVM VM to another HVM cluster in the same Cloud. Select the destination cluster, optionally a host, then map each disk and NIC to a datastore and network on the target. A powered-on VM is transferred with no guest downtime (live migration). A powered-off VM is relocated cold.

This is not a VMware-to-HVM conversion. For converting VMs from vCenter into HVM, see :doc:`/tools/migrations/overview`.

Move between HVM clusters stays in one |morpheus| Cloud. It does not move VMs between Clouds or between |morpheus| Managers.

Requirements
^^^^^^^^^^^^

In addition to the live-migration requirements above:

- Source and target are HVM clusters in the same Cloud
- The target host is enabled and has enough available memory
- Each mapped target datastore is online and has capacity for the volume
- Each mapped target network has a bridge that exists on the destination host
- Source and target hosts can reach each other so |morpheus| can propagate an SSH key for ``qemu+ssh`` transport
- The VM CPU definition is supported on the destination hosts

When a volume is mapped to a different datastore, |morpheus| copies storage as part of the move. Unmapped volumes are treated as already reachable on the destination (shared storage with the same path). Unmapped networks keep the same bridge name on the target host.

Initiating a Cross-Cluster Move
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Open the Instance or VM detail page and click :guilabel:`Actions` > :guilabel:`Move`.
#. Set **Target Cluster** to the destination HVM cluster.
#. Optionally set **Target Host**. Leave blank to auto-select within that cluster.
#. Under **Datastore Mapping**, map each source volume to a datastore on the destination cluster. The dialog shows the volume size and current datastore.
#. Under **Network Mapping**, map each source NIC to a network or bridge on the destination cluster.
#. Optionally enable **CPU Throttling** and set **Migration Timeout**.
#. Click :guilabel:`Move`.

If the Instance has more than one VM, the dialog states that all VMs in the Instance are migrated to the target.

What Happens During a Cross-Cluster Move
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. |morpheus| validates the target host, storage mappings, and network mappings
#. An SSH key is propagated from the source host to the target host
#. Target storage pools are prepared and refreshed; target bridges are verified
#. Domain XML is rewritten with the mapped disk paths and bridge names
#. The VM is live-migrated if it is powered on, or relocated cold if it is powered off
#. After success, the VM, Instance, and container records are updated to the destination cluster, Cloud resource pool, datastores, and networks

Limitations
^^^^^^^^^^^

- Same-cluster network remapping is not supported. Change networks with Reconfigure, not Move, when the VM stays in the current cluster.
- Linked-clone VMs cannot be storage-migrated. Linked clones on local storage also cannot change hosts.
- VMs with snapshots cannot be storage-migrated. Remove snapshots first.
- VMs with assigned host devices (GPU/USB passthrough) cannot be live-migrated or storage-migrated.
- Multi-attached, read-only, and ISO volumes cannot be included in a storage mapping.
- Local storage without a datastore mapping requires the VM to be powered off.
- VMs that use SR-IOV networks or vGPU assignments are not eligible for live migration. See :doc:`hvm_networks` and :doc:`nvidia_vgpu`.
- The target host must differ from the current host.

Cold Migration
--------------

Cold migration moves a powered-off VM to a different host. This is used when:

- The VM is powered off
- The VM has local storage that cannot be live-migrated
- Live migration failed and the VM was subsequently powered off

For cold migration, the VM's definition is relocated and storage volumes (if local) are copied to the target host.

VM Failover & Heartbeat System
-------------------------------

HVM clusters use a heartbeat-based failure detection and automatic VM recovery system managed by the |morpheus| Agent on each host. This system operates independently of Corosync quorum (see :doc:`troubleshooting` for details on why Corosync quorate state does not affect cluster operation).

Heartbeat Datastores
^^^^^^^^^^^^^^^^^^^^^

Each host in the cluster writes periodic heartbeat files to shared storage. These files serve two purposes: they prove the host is alive and they store the VM definitions needed to recover workloads after a host failure.

**What is written:**

- A ``hb.properties`` file containing the host's hostname, timestamp, memory usage, and IP addresses
- A libvirt domain XML file for each running VM on the host

**Where heartbeats are stored:**

Heartbeat data is written to all configured heartbeat datastore paths for redundancy. The folder structure uses a hash of the agent's API key to identify each host.

**Write interval:**

Heartbeat files are written every **20 seconds** by default. The interval is configurable from the |morpheus| appliance.

Host Failure Detection
^^^^^^^^^^^^^^^^^^^^^^^

The |morpheus| Agent on each host reads heartbeat files from all other hosts in the cluster. A host is considered **offline** when:

- Its heartbeat timestamp is stale for **7 consecutive check cycles** (approximately 140 seconds at the default 20-second interval)
- AND a direct HTTPS ping to the host on port 7443 has also failed

.. NOTE:: During stretch cluster arbitration, the detection threshold is extended to **10 check cycles** (approximately 200 seconds) to avoid premature failover during storage freezes caused by DLM fencing.

The host with the lowest identifier hash among all online hosts is automatically elected as the **recovery coordinator**. This election is deterministic — all nodes independently compute the same coordinator.

Failover Sequence
^^^^^^^^^^^^^^^^^^

When the recovery coordinator detects a host failure, the following sequence occurs:

**Phase 1 — VM Assignment:**

#. The coordinator reads the VM domain XML files from the failed host's heartbeat folder
#. For each VM:

   - **Pinned VMs are skipped** — they are not automatically recovered
   - **VMs with local-only storage are skipped** — they cannot be recovered without shared storage
   - The online host with the **most available free memory** that can accommodate the VM is selected as the target

#. The coordinator copies each VM's definition to the target host's recovery folder on the heartbeat datastore
#. Memory tracking is updated after each assignment to prevent over-committing during batch recovery

**Phase 2 — Cleanup on Failed Host:**

#. The coordinator attempts to reach the failed host via SSH and terminate any remaining VM processes
#. The |morpheus| appliance is notified of the failover via the ``/app/failoverWorkloadPrepare`` message

**Phase 3 — VM Recovery on Target Hosts:**

#. Each host checks its own recovery folder for VM definitions to start
#. Before starting a VM, the host verifies:

   - All shared disk files referenced by the VM are accessible
   - The VM is not already running on another host (confirmed over 3 consecutive checks to prevent duplicate starts)

#. The VM is defined and started, with up to **12 retry attempts** (10 seconds apart) if the initial start fails
#. If the VM uses a software TPM (vTPM), the TPM state is restored from shared storage before startup
#. The |morpheus| appliance is notified via the ``/app/failoverWorkloadStart`` message

**Phase 4 — Failed Host Recovery:**

When the failed host comes back online, it reads its failover record, confirms each VM is running elsewhere, and removes the local VM definitions to prevent conflicts.

APD (All Paths Down) Protection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a host loses connectivity to **all** heartbeat datastore paths, it enters All Paths Down (APD) protection mode:

- An isolation failure counter increments each cycle where writes fail on all paths
- After **6 consecutive failures** (approximately 2 minutes), the host **destroys all running VMs** to protect shared storage from data corruption
- During stretch cluster arbitration, the threshold is extended to **9 consecutive failures**
- Pinned VMs and VMs using local-only storage are exempt from APD shutdown

.. WARNING:: APD protection is a last-resort safety mechanism. When triggered, all non-exempt VMs on the isolated host are forcefully terminated to prevent split-brain storage access. Investigate and resolve storage connectivity issues immediately.

Agent Startup Recovery
^^^^^^^^^^^^^^^^^^^^^^^

When the |morpheus| Agent starts (for example, after a host reboot), it enters a recovery mode for the first several minutes:

- The agent checks its own heartbeat folder for VM definitions that are not currently running
- It attempts to auto-start these VMs (handling the host-reboot scenario where VMs were running before the reboot)
- VMs with inaccessible disks are deferred to the recovery folder for later retry

DLM Fencing Integration
^^^^^^^^^^^^^^^^^^^^^^^^^

HVM clusters use GFS2 with the Distributed Lock Manager (DLM) for shared storage. When a host leaves the cluster, DLM enters a "wait fencing" state that freezes all GFS2 I/O cluster-wide until the departed host is confirmed safely fenced.

The |morpheus| Agent handles DLM fencing automatically:

#. The agent detects that a peer host is unreachable via its connectivity checks (every 20 seconds)
#. Once confirmed unreachable, the agent issues a DLM fence acknowledgement to release the storage freeze
#. A fast-path mechanism can issue the fence acknowledgement within **~20 seconds** for single-host failures, minimizing GFS2 freeze duration
#. For safety, the agent confirms a rebooted host has actually restarted (via boot ID comparison) before acknowledging the fence, preventing split-brain scenarios

When a host **loses quorum** (cannot reach a majority of peers), it self-fences by rebooting to ensure it cannot access shared storage while isolated.

.. NOTE:: During maintenance mode, self-fencing withdraws from GFS2 lockspaces and stops cluster services instead of rebooting, keeping the host available for administrator access.

For detailed failover timelines and scenarios, see :doc:`failure_scenarios`.
