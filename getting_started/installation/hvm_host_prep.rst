.. _hvm-host-prep:

Preparing HVM Hosts
-------------------

HVM hosts are the physical (or nested) servers that run the HVM OS and serve as the hypervisor layer managed by |morpheus|. Before deploying the |morpheus| appliance using the HPE Morpheus Manager Installer, you must prepare at least one HVM host.

.. note::

   If you plan to deploy an HVM cluster, repeat the host preparation steps on each host. You only deploy **one** Morpheus Manager VM — after the manager is running, you add additional hosts to the cluster from within the |morpheus| UI (Infrastructure > Clusters).

Obtaining HVM OS 24.04
^^^^^^^^^^^^^^^^^^^^^^

The HVM OS 24.04 ISO is available for download from `HPE My Software Center <https://myenterpriselicense.hpe.com/>`_. Contact your HPE account representative if you need access.

You can boot the ISO from local virtual media, removable media, or a reachable HTTP/HTTPS virtual-media URL when the server management controller supports that method. A URL can remove the workstation and browser from the transfer path, but transfer speed and reliability still depend on the management controller, source server, and network. Verify the downloaded ISO against the checksum published with the release before booting it.

Hardware Requirements
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Component
     - Requirement
   * - **CPU**
     - One or more 64-bit x86 processors, 1.5 GHz minimum. **Intel VT-x** or **AMD-V** must be enabled in BIOS/UEFI. **IOMMU** (Intel VT-d / AMD-Vi) is required for SR-IOV and hardware passthrough features.
   * - **Memory**
     - 4 GB minimum per host. For converged storage Layouts (Ceph), add 4 GB minimum per Ceph data disk. Production clusters typically require 64 GB+ per host.
   * - **OS Disk**
     - 15 GB minimum for the operating system
   * - **Data Disk**
     - 500 GB minimum for testing (converged storage). Production clusters will require significantly more. Do not RAID data disks — multiple disks can be specified during cluster setup and will be pooled by Ceph. Non-converged Layouts use external storage (NFS, iSCSI) instead.
   * - **Network**
     - 10 Gbps NICs are required for converged storage and situations where all traffic runs through the management interface. Static IP addresses are required on all HVM hosts. Enable jumbo frames only when the complete network path is configured for the same MTU.

.. important::

   You must enable **Intel VT-x** (or AMD-V) and **IOMMU** (Intel VT-d or AMD-Vi) in your server's BIOS/UEFI settings before installing HVM OS. Without hardware virtualization extensions, KVM will not function.

Installing HVM OS 24.04
^^^^^^^^^^^^^^^^^^^^^^^^

1. Boot the target server from the HVM OS 24.04 ISO (via USB, iLO virtual media, or PXE)
2. The **Subiquity** installer (same as standard Ubuntu Server) is displayed automatically on boot
3. Follow the guided installation:

   - Select language and keyboard layout
   - Configure network interface with a **static IP address**, netmask, gateway, and DNS
   - Select the OS disk for installation
   - Create a user account with a password (this user will need ``sudo`` privileges)
   - Complete the installation and reboot

4. After reboot, remove the ISO media and verify the host boots into HVM OS

At each transition, confirm the installer still reports the expected target disk and network configuration. Installation duration varies with media delivery, hardware initialization, disk performance, and network access; do not treat elapsed time by itself as proof that installation failed. If the installer reports a checksum, storage, or unknown error, capture the exact message and installer logs before changing media, RAID, or disk state. See :doc:`/infrastructure/clusters/hvm/troubleshooting`.

Post-Install Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HVM OS 24.04 uses **netplan** for network configuration. If you need to adjust networking after installation:

.. warning:: Perform network changes only with working console or out-of-band management (for example, iLO) and during a maintenance window. Do not rely on the SSH session that the change can disconnect. Record the existing configuration, routes, DNS, interface MAC addresses, upstream switch configuration, and a tested rollback path first.

1. Navigate to the netplan configuration directory:

   .. code-block:: bash

      cd /etc/netplan

2. Back up and edit the existing configuration file (the filename varies by installation method). Modify the existing renderer-owned file unless your site standard explicitly uses a separate file; conflicting Netplan definitions for the same interface are unsafe.

   .. code-block:: bash

      sudo nano /etc/netplan/50-cloud-init.yaml
      # or /etc/netplan/00-installer-config.yaml
      # or /etc/netplan/01-netcfg.yaml

   Before editing, identify the intended physical interface by name, MAC address, and link state:

   .. code-block:: bash

      ip -br link
      sudo hvmcli interfaces list --filter ethernet

   ``hvmcli interfaces list`` is read-only and is the same interface inventory source used by current HVM host discovery. Do not configure an interface that is already an uplink, bond member, bridge member, or storage path without accounting for that dependency.

3. Example static IP configuration:

   .. code-block:: yaml

      network:
        version: 2
        ethernets:
          eth0:
            addresses:
              - 192.168.1.100/24
            gateway4: 192.168.1.1
            nameservers:
              addresses:
                - 8.8.8.8
                - 8.8.4.4

4. Validate and apply the configuration from the console or out-of-band session:

   .. code-block:: bash

      sudo netplan try

   ``netplan try`` temporarily applies the configuration and prompts for confirmation. Confirm only after management connectivity, routes, DNS, expected VLAN reachability, and any affected storage path have been tested from a second session. If confirmation is not received, Netplan attempts to roll back after its timeout; console access is still required because rollback cannot recover every external switch, bond, or routing error.

5. Verify what HVM discovers:

   .. code-block:: bash

      ip -br address
      ip route
      sudo hvmcli interfaces list --filter ethernet

6. In |morpheus|, navigate to :menuselection:`Infrastructure --> Clusters`, open the HVM cluster, and run :guilabel:`Actions` > :guilabel:`Refresh`. After the refresh completes, open the host and compare its interface inventory with ``hvmcli interfaces list``. The new interface can then be selected as a per-host Virtual Switch uplink where supported.

If the OS and ``hvmcli`` show the interface but the refreshed host inventory does not, do not edit database records or create a placeholder interface. Save the ``hvmcli`` output and cluster refresh process output, then contact HPE Support. If connectivity fails, do not confirm ``netplan try``; use the console to allow rollback or restore the backed-up Netplan file and retry ``netplan try``.

.. tip::

   Back up your existing Netplan configuration before making changes: ``sudo cp -a /etc/netplan/<file>.yaml /etc/netplan/<file>.yaml.bak``

Verifying Host Readiness
^^^^^^^^^^^^^^^^^^^^^^^^

Before running the HPE Morpheus Manager Installer, confirm:

- **SSH access** — You can connect to the host over SSH (port 22) from your workstation
- **Sudo privileges** — Your user can run ``sudo`` commands without restriction
- **Static IP** — The host has a static IP address that will not change
- **DNS resolution** — The host can resolve external hostnames (or at minimum, the Morpheus appliance hostname once deployed)

Host Firewall Ownership
^^^^^^^^^^^^^^^^^^^^^^^

Firewall state is owned by the installed HVM host image and the site's network policy. The manager implementation does not define one universal UFW, iptables, or nftables ruleset for both vanilla Ubuntu and every HVM Custom ISO release. Do not assume that disabling UFW removes, preserves, or replaces rules created by another firewall backend.

For each deployed host and installer release, record the active firewall service and effective rules, then validate manager, Agent quorum, Corosync, storage, migration, and VM-network connectivity required by the cluster design. Apply only the rules approved for that host release and environment. The product source does not establish the Jira-reported split-brain outcome as a guaranteed result of changing UFW state; if quorum or shared-storage connectivity changes after a firewall modification, restore the approved policy and stop cluster changes until HPE Support or the installer owner reviews the effective rules.

Layout 2.0 Network Design Checklist
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before creating layout 2.0 Virtual Switches, record the traffic types, physical NICs, switch ports, VLANs, IP ranges, and MTU for each host. Use :doc:`/infrastructure/clusters/hvm/virtual_switches` for the configuration procedure.

.. list-table:: Common validated Virtual Switch choices
   :header-rows: 1
   :widths: 22 20 22 36

   * - Requirement
     - Host uplink
     - Upstream port
     - VLAN handling
   * - Simple untagged segment
     - One NIC or Active Backup
     - Access/native network
     - Leave VLAN ID empty; traffic is untagged
   * - Tagged traffic segments
     - One NIC, Active Backup, or LACP
     - Trunk allowing every selected VLAN
     - Set the VLAN ID for each tagged traffic type
   * - Redundant links without switch aggregation
     - Active Backup
     - Access or trunk, consistently configured
     - Tagged or untagged according to the segment
   * - Aggregated links
     - LACP (802.3ad)
     - Both ports in the same compatible LACP group
     - Tagged or untagged according to the segment

The VLAN ID and MTU are optional product inputs. A decoupled design therefore does not require a native VLAN: assign explicit VLAN IDs to each traffic segment and configure the upstream trunk to allow them. Conversely, leave VLAN ID empty only when that segment is intentionally untagged. Values in examples are illustrative; use the addresses and VLAN IDs approved for your environment.

Canonical Deployment Networking Scenarios
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use these numbered scenarios when discussing a deployment design. They replace positional references to figures in earlier deployment material; detailed configuration screens are in :doc:`/infrastructure/clusters/hvm/virtual_switches`.

**Scenario 1 — Redundant links without switch aggregation.** Configure an Active Backup bond. The upstream ports do not form an LACP group. Configure both ports consistently as access ports for one untagged segment or as trunks that allow the required tagged VLANs.

Automatic MII polling, up-delay, and down-delay values for Active Backup bonds are release- and networking-backend-specific and are not guaranteed. From console or out-of-band access, inspect the effective bond configuration after provisioning and configure the required values explicitly with tooling supported by the installed HVM release. Do not assume values from another ISO, release note, or backend, and do not copy undocumented values into Netplan.

**Scenario 2 — Aggregated links.** Configure an LACP (802.3ad) bond only after both upstream ports are in the same compatible LACP group. The upstream configuration and HVM bond must agree before traffic is moved to the bond. Access or trunk behavior and VLAN tagging still follow the selected segment design.

**Scenario 3 — Dedicated storage paths.** For iSCSI on layout 2.0, use one NIC per dedicated Virtual Switch and provide redundancy with iSCSI multipath rather than a network bond. NFS and Live Migration can use a single NIC or a supported bond as described in the traffic-type matrix.

For every scenario, record the selected physical ports, traffic roles, VLAN tagging location, MTU, and IP ranges before installation. Do not copy interface names, addresses, or VLAN IDs from an example.

Network Ports
^^^^^^^^^^^^^

The following ports are required for communication between HVM hosts and the |morpheus| appliance:

.. list-table::
   :header-rows: 1
   :widths: 35 20 20 10 15

   * - Description
     - Source
     - Destination
     - Port
     - Protocol
   * - Agent communication with |morpheus| appliance
     - HVM Host
     - |morpheus| appliance
     - 443
     - TCP
   * - Hypervisor console access
     - |morpheus| appliance
     - HVM Host
     - 7443
     - TCP
   * - Host configuration and management (SSH)
     - |morpheus| appliance
     - HVM Host
     - 22
     - TCP
   * - Inter-host communication (clustered deployments)
     - HVM Host
     - HVM Host
     - 22
     - TCP
   * - SSH access for deployed VMs
     - |morpheus| appliance
     - HVM VMs
     - 22
     - TCP
   * - WinRM HTTP for deployed VMs
     - |morpheus| appliance
     - HVM VMs
     - 5985
     - TCP
   * - WinRM HTTPS for deployed VMs
     - |morpheus| appliance
     - HVM VMs
     - 5986
     - TCP
   * - Ceph Storage
     - HVM Host
     - HVM Host
     - 3300
     - TCP
   * - Ceph Monitor
     - HVM Host
     - HVM Host
     - 6789
     - TCP
   * - Ceph MDS/OSD
     - HVM Host
     - HVM Host
     - 6800-7300
     - TCP
   * - Corosync
     - HVM Host
     - HVM Host
     - 5404-5406
     - UDP

.. note::

   Ceph and Corosync ports are only required for multi-node clusters using converged (HCI) storage. Single-host deployments or clusters using external storage do not require these ports.

Preparing Multiple Hosts
^^^^^^^^^^^^^^^^^^^^^^^^^

If you plan to deploy an HVM cluster:

1. Repeat the HVM OS installation and configuration on **each host** that will be part of the cluster
2. Ensure all hosts can communicate with each other over the ports listed above
3. Use consistent network interface naming across hosts where possible (e.g., ``eth0`` for management, ``eth1`` for storage, ``eth2`` for compute)
4. Deploy the Morpheus Manager VM onto **one** host using the HPE Morpheus Manager Installer
5. After the Morpheus appliance is running, add the remaining hosts to the cluster from within the |morpheus| UI (Infrastructure > Clusters > + ADD CLUSTER)

Next Steps
^^^^^^^^^^

Once your HVM host(s) are prepared and accessible via SSH, proceed to the :doc:`HPE Morpheus Manager Installer </getting_started/installation/singleNode/hpe_installer>` to deploy the |morpheus| appliance.
