Two-Node Clusters with a Witness
================================

.. versionadded:: 9.0

A two-node HVM cluster can use an HPE Shared File System (GFS2) datastore when a Distributed Worker provides an independent quorum vote. This topology is available for HVM layout 1.3 or later and applies wherever HVM is included, including HPE VM Essentials, HPE Morpheus Enterprise Software, and HPE Morpheus Advanced Software.

The witness is a quorum-only member. It does not run VMs, mount the GFS2 datastore, or become an HVM compute Host. Deploy it outside the failure domain shared by the two HVM Hosts. For vote math and Quorum panel fields, see :doc:`architecture`.

Topology
--------

The logical quorum has three members:

- HVM Host 1
- HVM Host 2
- One Distributed Worker witness

The two Hosts communicate with each other on the Agent quorum network. Each Host must also resolve, reach, and trust the HTTPS Worker URL. |morpheus| derives the witness endpoint as ``<Worker URL>/witness/<cluster UUID>/quorum``.

.. important:: The Worker's outbound connection to the |morpheus| appliance does not prove that the HVM Hosts can reach the witness. Validate the Host-to-Worker path independently.

Prerequisites
-------------

- |morpheus| Manager 9.0 or later
- An HVM layout 1.3 or later cluster with exactly two compatible Hosts
- Static management addresses and Host-to-Host connectivity on TCP 7443
- Shared block storage, such as iSCSI or Fibre Channel, visible to both Hosts
- One Distributed Worker outside the two-Host failure domain
- A stable Worker URL whose DNS name, route, firewall port, and certificate chain are valid from both Hosts
- Enough capacity on either Host to run the workloads that must remain available while the other Host is offline

The Worker URL can terminate TLS directly on the Worker or through a supported reverse proxy or load balancer. Preserve the ``/witness/<cluster UUID>/quorum`` path when a proxy is used. The external HTTPS port is the port in the configured Worker URL; do not assume the Worker's internal application port is exposed directly.

Deployment
----------

1. Create the two-Host HVM cluster using :doc:`building_clusters`. Do not add the GFS2 datastore yet. Do not select a witness during initial cluster create.
2. Deploy and register a Distributed Worker using :ref:`hvm-witness-deployment`.
3. From both HVM Hosts, verify DNS resolution and TLS connectivity to the Worker URL.
4. Navigate to |InfClu|, open the cluster, click :guilabel:`Edit`, select the Distributed Worker in the **Witness** field, and save the cluster.
5. Add the shared block-storage target to both Hosts and confirm both Hosts resolve the same stable multipath device. See :doc:`storage_operations`.
6. Create the HPE Shared File System (GFS2) datastore and select one reliable datastore as the **Heartbeat Target**.
7. Open the cluster **Summary** tab and verify the Quorum panel.

The Manager sends Agent quorum information only after a GFS2 datastore exists. The selected Worker may therefore appear active as a Distributed Worker before it appears as an HVM quorum member. Adding the GFS2 datastore activates the three-member Agent quorum workflow.

.. warning:: Do not place production workloads on a new GFS2 datastore until all three quorum members are reachable and the Quorum panel reports a healthy state.

.. _hvm-witness-deployment:

Witness Deployment
------------------

1. Navigate to |AdmIntDis| and create a Distributed Worker configuration.
2. Set **Worker URL** to the stable client-facing HTTPS URL for the Worker.
3. Save the API key.
4. Install and configure the Worker using the package or container procedure in :doc:`/administration/integrations/workers`.
5. Confirm the Worker is active in |AdmIntDis|.
6. From each HVM Host, verify the configured DNS name and TLS path. For example:

   .. code-block:: bash

      getent hosts witness.example.com
      curl --head https://witness.example.com

Do not use ``--insecure`` for production validation. If a reverse proxy or load balancer fronts the Worker, also confirm it preserves the witness path and does not require interactive authentication.

After the cluster UUID is available on the cluster detail page, verify the generated witness path from each Host:

.. code-block:: bash

   curl --head https://witness.example.com/witness/<cluster UUID>/quorum

Replace ``witness.example.com`` with the host in the configured Worker URL. Do not use ``--insecure``.

Quorum Validation
-----------------

After adding the GFS2 datastore, open |InfClu|, select the cluster, and expand the **Summary** Quorum panel. Confirm:

- Quorum status is **ACHIEVED**
- Nodes configured: 3 (two Hosts plus the witness)
- Both Hosts are online and reachable
- The Witness row is present and reachable
- There is no **Sites** row
- The Host table is a flat list, not grouped by site
- The Designated Coordinator is one of the two Hosts
- GFS2 lockspaces are **OK**, not **WAIT FENCING**
- The selected heartbeat datastore is healthy on both Hosts

Corosync supplies membership information to DLM but does not decide Agent quorum for layout 1.3 or later. A two-node cluster can show ``Quorate: No`` in ``corosync-quorumtool`` while the Agent Quorum panel correctly reports **ACHIEVED**. Use the Agent quorum state as the operational authority.

Failure and Maintenance Behavior
--------------------------------

.. list-table::
   :header-rows: 1
   :widths: 35 30 35

   * - Condition
     - Available votes
     - Expected behavior
   * - Both Hosts and witness reachable
     - 3 of 3
     - Normal operation
   * - One Host unavailable; witness reachable
     - 2 of 3
     - The surviving Host retains quorum; eligible VMs can recover after the heartbeat failure threshold
   * - Witness unavailable; both Hosts reachable
     - 2 of 3
     - The cluster retains quorum, but no Host may be taken offline until witness service is restored
   * - One Host and the witness unavailable
     - 1 of 3
     - The remaining Host cannot retain quorum and protects shared storage by fencing
   * - Host-to-Host partition
     - Depends on witness reachability
     - The Host that can reach the witness can form 2 of 3 votes; the other Host cannot retain quorum
   * - |morpheus| Manager unavailable
     - Unchanged
     - Agent and witness quorum continue independently; UI management is unavailable until the Manager returns

Host unreachability is detected after 60 seconds. Eligible VM recovery on the surviving Host follows the 140-second heartbeat failure threshold and requires the witness to remain reachable. Do not treat these timeouts as the same interval.

For planned Host maintenance, confirm the witness and the other Host are healthy before entering maintenance mode. Do not maintain a Host and the witness at the same time. Restore all three members before beginning maintenance on the second Host.

Troubleshooting
---------------

- **Worker active but witness unreachable:** The Worker can reach the Manager, but one or both Hosts cannot reach the Worker URL. Correct DNS, routing, firewall, proxy, or certificate trust.
- **Witness absent from the Quorum panel:** Confirm the Worker is selected on the cluster and a GFS2 datastore exists. The Manager sends Agent quorum information only after GFS2 exists. Allow the cluster refresh to propagate updated quorum information.
- **Sites row on a two-node cluster:** Site Groups were created. Stop and treat this as a stretch misconfiguration. Remove the Site Groups or follow :doc:`stretch_clusters` only if you intended to convert the topology.
- **Wrong witness URL:** Set **Worker URL** to the client-facing Worker endpoint, not the |morpheus| appliance URL. Verify the generated ``/witness/<cluster UUID>/quorum`` route through any proxy.
- **Certificate error:** Serve a complete certificate chain trusted by both HVM Hosts. Do not bypass certificate validation.
- **GFS2 lockspace waiting for fencing:** Do not issue manual fence acknowledgements until the unreachable Host is physically isolated from shared storage. Follow :doc:`troubleshooting` or contact HPE Support.
- **Witness lost during Host maintenance:** Stop the maintenance operation if possible and restore either the witness or the Host before making another member unavailable.

Limitations
-----------

- A two-node cluster has less compute and maintenance capacity than a three-node cluster.
- The witness is required for Host-failure tolerance; two Hosts without the witness cannot tolerate either Host becoming unavailable.
- This topology is not a stretch cluster. It does not use Site Groups or the ``siteWitness`` designation. Do not create Site Groups on a two-node GFS2 cluster; adding them switches the witness classification to stretch ``siteWitness``. Site Groups are created from the Host-VM Groups tab; see :doc:`host_vm_groups`.
- The witness does not replace shared-storage redundancy, multipathing, backups, or sufficient capacity on the surviving Host.
- Configure one heartbeat target. If it becomes unhealthy, restore it or select another healthy GFS2 datastore before relying on automatic VM recovery.

For multi-site HVM clusters with site groups, see :doc:`stretch_clusters`.
