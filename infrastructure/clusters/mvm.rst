Legacy HVM Clusters
===================

This appendix covers HVM layout 1.2 and earlier. Legacy clusters remain supported, but their provisioning, high-availability, storage, and networking architecture differs from layouts 1.3 and 2.0. For operations that are not listed as Legacy-specific here, use the shared :doc:`HVM cluster guide </infrastructure/clusters/hvm/hvm>`.

.. important:: Confirm the cluster layout on the cluster detail page before using this appendix. Do not use the Pacemaker or Ceph procedures on layouts 1.3 or 2.0.

Legacy Differences
------------------

.. list-table::
   :widths: 25 35 40
   :header-rows: 1

   * - Area
     - Legacy layout
     - Current layouts
   * - Host operating system
     - Ubuntu 22.04
     - HVM OS/Ubuntu 24.04 for layout 1.3; HVM OS 26.04 for layout 2.0
   * - High availability
     - Pacemaker and Corosync
     - |morpheus| Agent quorum, Corosync, and DLM
   * - Cluster diagnostics
     - ``pcs`` and standard Linux commands
     - Agent quorum endpoint, ``corosync-quorumtool``, and ``dlm_tool``
   * - Host networking
     - Open vSwitch (OVS)
     - OVS on layout 1.3; Virtual Switches on layout 2.0
   * - Converged storage
     - Ceph on HCI layouts
     - HPE Clustered Datastores and supported external storage
   * - Host management CLI
     - Standard Linux, ``virsh``, and ``pcs`` commands
     - Standard Linux commands on layout 1.3; ``hvmcli`` on layout 2.0

Legacy Requirements
-------------------

- **Operating System:** Ubuntu 22.04
- **CPU:** One or more 64-bit x86 CPUs with Intel VT or AMD-V enabled
- **Memory:** 4 GB minimum, plus 4 GB per Ceph disk for converged layouts
- **Storage:** A data disk of at least 500 GB for test HCI deployments; production requires additional capacity
- **Networking:** Static Host IP addresses, DNS resolution of the |morpheus| appliance, and access to package repositories
- **Cluster Size:** At least three Hosts for an HCI layout

.. note:: Ubuntu 22.04 uses Netplan. Configure static Host networking before provisioning the cluster. Clustered storage and combined traffic configurations require at least 10 Gbps interfaces with jumbo frames enabled end-to-end.

Legacy Network Ports
--------------------

.. list-table::
   :widths: 45 20 20 15
   :header-rows: 1

   * - Description
     - Source
     - Destination
     - Port
   * - Agent communication
     - HVM Host
     - |morpheus| appliance
     - TCP 443
   * - Host configuration
     - |morpheus| appliance
     - HVM Host
     - TCP 22
   * - Interhost communication
     - HVM Host
     - HVM Host
     - TCP 22
   * - Ceph Monitor
     - HVM Host
     - HVM Host
     - TCP 3300, 6789
   * - Ceph MDS and OSD
     - HVM Host
     - HVM Host
     - TCP 6800-7300

Provisioning a Legacy Cluster
-----------------------------

#. Provision the required Ubuntu 22.04 Hosts and configure static networking.
#. Create or select a |morpheus|-type Cloud for the cluster.
#. Navigate to :menuselection:`Infrastructure --> Clusters` and click :guilabel:`+ Add Cluster`.
#. Select **HVM** and choose the required Legacy HCI or non-HCI layout.
#. Enter each Host's SSH address and credentials for a user with passwordless sudo access.
#. For an HCI layout, select the Ceph data device on each Host.
#. Select the management, storage, and compute interfaces and configure the required compute VLANs.
#. Complete the wizard and monitor the cluster History tab until the KVM, Ceph, OVS, and Pacemaker configuration tasks finish.

.. warning:: Do not reuse the operating-system disk as a Ceph data device. Verify the selected device on every Host before completing the wizard.

Legacy Networking
-----------------

Legacy layouts use OVS bridges and port groups. The compute VLANs selected during cluster provisioning create OVS-backed networks for workloads. For network lifecycle concepts and supported OVS network types, see :doc:`/infrastructure/clusters/hvm/hvm_networks`.

Legacy High Availability
------------------------

Pacemaker manages Legacy cluster resources, fencing, and failover. Use ``pcs status`` to inspect cluster state and ``pcs resource`` to inspect managed resources. Do not apply the agent quorum interpretation from the current :doc:`architecture <hvm/architecture>` or :doc:`troubleshooting <hvm/troubleshooting>` pages to a Legacy cluster.

Before removing a Host or performing maintenance:

#. Confirm Pacemaker and Ceph report a healthy state.
#. Evacuate or stop VMs that cannot migrate.
#. Enter maintenance mode from the Host Actions menu.
#. Complete the maintenance or removal operation.
#. Confirm Pacemaker resources, Ceph placement groups, and workload placement return to a healthy state.

.. warning:: Never remove a Ceph OSD, Monitor, or Host while the Ceph cluster is unhealthy or rebalancing. Contact HPE Support when a failed Host cannot be cleanly evacuated.

Shared Operations
-----------------

The following current guide topics also apply to Legacy clusters unless a page contains a more restrictive layout notice:

- :doc:`Host maintenance <hvm/host_maintenance>`
- :doc:`VM migration <hvm/vm_migration>`
- :doc:`VM placement <hvm/vm_placement>`
- :doc:`Host and VM groups <hvm/host_vm_groups>`
- :doc:`VM compute settings <hvm/vm_compute>`
- :doc:`Hardware passthrough <hardware-passthrough>`
- :doc:`Guest operating system notes <hvm/guest_os_notes>`
- :doc:`Snapshots <hvm/snapshots>`
- :doc:`Console keyboard mappings <hvm/console_keyboards>`

Uploading Multi-Disk QCOW2 Images
---------------------------------

HVM/KVM supports Virtual Images made from multiple QCOW2 disk files. These uploads require a ``metadata.json`` manifest on the same Virtual Image to map each QCOW2 file to its disk size, guest device, order, and boot role. Upload all QCOW2 files before uploading the manifest. Without valid metadata, |morpheus| treats the image as a single-disk image.

For the required manifest format and complete upload procedure, see :ref:`multi-disk-qcow2-images-for-hvm-kvm`.

Upgrading from Legacy
---------------------

Layout 1.3 replaces Pacemaker with the |morpheus| Agent quorum service while retaining Corosync and DLM. Use the supported cluster layout upgrade rather than manually removing Pacemaker. See :doc:`/infrastructure/clusters/hvm/upgrading` for the migration behavior and verification steps.
