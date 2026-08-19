Host Maintenance & Evacuation
==============================

Overview
--------

Host maintenance mode allows administrators to take a host offline for servicing (hardware repair, OS patching, firmware updates) without triggering unnecessary VM failover. When a host enters maintenance mode, |morpheus| evacuates VMs to other cluster hosts via live migration before marking the host offline.

Entering Maintenance Mode
--------------------------

Procedure
^^^^^^^^^

#. Navigate to ``Infrastructure > Clusters > [Cluster] > Hosts``
#. Click the actions menu for the target host
#. Select :guilabel:`Enter Maintenance Mode`
#. |morpheus| begins the automated evacuation process

.. NOTE:: Maintenance mode can also be entered from ``Infrastructure > Clusters > [Cluster] > Hosts > [Host] > Actions > Enter Maintenance Mode``.

Automated Evacuation Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When maintenance mode is initiated, |morpheus| performs the following:

#. **Capacity validation (dry run)** — Before moving any VMs, |morpheus| verifies that remaining hosts have sufficient memory to accommodate all VMs. The system ensures no host exceeds 95% projected memory utilization after receiving migrated VMs. If capacity is insufficient, maintenance mode is refused with an error.

#. **VM iteration** — VMs are processed in descending order by memory allocation (largest VMs first).

#. **Target host selection** — For each VM, |morpheus| selects a target host with the most available memory that can accommodate the VM without exceeding 95% utilization.

#. **Live migration** — Running VMs on shared storage are live-migrated (no downtime). Each migration is retried up to 3 times on failure, with a 15-second pause between attempts.

#. **Cold migration** — Powered-off VMs are cold-moved (XML definition relocated).

#. **Status update** — Once all eligible VMs are evacuated, the host status changes from ``maintenancing`` to ``maintenance``.

VMs Skipped During Evacuation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following VMs are not moved during maintenance evacuation:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - VM Type
     - Reason
   * - Pinned VMs (system servers with ``pinned`` placement strategy)
     - These are explicitly bound to the host and cannot be automatically relocated
   * - Powered-off VMs (when ``movePoweredOff`` is disabled)
     - Powered-off VMs do not consume runtime resources; moving them is optional
   * - VMs with unknown power state
     - Cannot safely determine migration path
   * - VMs with local storage (while powered on)
     - Local storage cannot be live-migrated; VM must be powered off first

.. WARNING:: If pinned VMs exist on the host, they will remain in place during maintenance. Ensure these VMs can tolerate the host being serviced, or manually relocate them before entering maintenance mode.

For permanent decommissioning, maintenance mode is only the evacuation step. Complete the supported cluster removal and post-removal health checks in :doc:`managing_hosts`.

VMs With Local Storage
^^^^^^^^^^^^^^^^^^^^^^^

VMs that have volumes on local datastores cannot be live-migrated. These VMs must be powered off before the host enters maintenance mode. If a running VM has local storage, maintenance mode will report a failure for that VM and continue with the remaining VMs.

To handle VMs with local storage:

#. Power off the VM manually before initiating maintenance mode
#. Or move the VM's storage to a shared datastore before initiating maintenance mode

Capacity Requirements
^^^^^^^^^^^^^^^^^^^^^^

Maintenance mode requires that remaining hosts can absorb the workload:

- Each target host must have available memory greater than the VM's allocated memory
- Projected utilization on the target host must remain below 95%
- If no host has sufficient capacity for a given VM, the operation fails

.. IMPORTANT:: Plan cluster sizing with N+1 capacity to always allow at least one host to enter maintenance. See :doc:`capacity_planning` for sizing guidance.

Exiting Maintenance Mode
--------------------------

Procedure
^^^^^^^^^

#. Navigate to ``Infrastructure > Clusters > [Cluster] > Hosts``
#. Click the actions menu for the host in maintenance
#. Select :guilabel:`Exit Maintenance Mode`

What Happens
^^^^^^^^^^^^

- The host status changes from ``maintenance`` to ``provisioned``
- The host's maintenance mode flag is cleared
- Stat collection and quorum participation resume immediately
- VMs are **not** automatically moved back to the host

.. NOTE:: After exiting maintenance mode, VMs remain on their current hosts. Use Dynamic Placement or manual migration to rebalance workloads if desired.

Planned vs. Unplanned Host Absence
------------------------------------

.. list-table::
   :widths: 25 37 38
   :header-rows: 1

   * - Aspect
     - Planned (Maintenance Mode)
     - Unplanned (Host Failure)
   * - VM evacuation
     - Live migration before host goes offline
     - VMs lost; restarted on surviving hosts after 140s
   * - Quorum impact
     - Host remains a quorum member (maintenance flag)
     - Host becomes unreachable; counted against quorum
   * - Data integrity
     - Clean unmount of shared storage
     - Fencing protects storage; DLM coordinates
   * - VM downtime
     - Zero (live migration)
     - 140+ seconds (failover timeline)
   * - Recovery
     - Exit maintenance mode
     - Host rejoins automatically on reboot

Proper Shutdown Sequence
^^^^^^^^^^^^^^^^^^^^^^^^^

To cleanly shut down a host without triggering failover:

#. Enter maintenance mode (evacuates VMs)
#. Wait for evacuation to complete (host status shows ``maintenance``)
#. Power off or reboot the host for servicing

.. WARNING:: Do NOT power off a host without first entering maintenance mode. An abrupt power-off will be interpreted as a host failure, triggering quorum evaluation and VM failover after 140 seconds.

Re-joining After Maintenance
------------------------------

When a host boots back up after maintenance:

#. The |morpheus| agent starts and reads ``.quorum-nodes`` from ``/opt/morpheus-node``
#. The agent resumes peer-to-peer quorum pinging on port 7443
#. Other cluster agents detect the returning host as reachable
#. Quorum status updates to include the returning host
#. The host is available to receive VMs (via Dynamic Placement, manual migration, or new provisioning)

.. NOTE:: If the host was offline for less than 140 seconds and did not enter maintenance mode, no VM failover occurs. The host simply rejoins the quorum cycle transparently.

Maintenance During Cluster Updates
------------------------------------

When performing rolling cluster updates (see :doc:`upgrading`), |morpheus| automatically enters and exits maintenance mode for each host as part of the update process. A Dynamic Placement lock is acquired during maintenance to prevent resource scheduling from interfering with the update cycle.
