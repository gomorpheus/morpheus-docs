.. _hvm-host-prep:

Preparing HVM Hosts
-------------------

HVM hosts are the physical (or nested) servers that run the HVM OS and serve as the hypervisor layer managed by |morpheus|. Before deploying the |morpheus| appliance using the HPE Morpheus Manager Installer, you must prepare at least one HVM host.

.. note::

   If you plan to deploy an HVM cluster, repeat the host preparation steps on each host. You only deploy **one** Morpheus Manager VM — after the manager is running, you add additional hosts to the cluster from within the |morpheus| UI (Infrastructure > Clusters).

Obtaining HVM OS 24.04
^^^^^^^^^^^^^^^^^^^^^^

The HVM OS 24.04 ISO is available for download from `HPE My Software Center <https://myenterpriselicense.hpe.com/>`_. Contact your HPE account representative if you need access.

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
     - 10 Gbps NICs with jumbo frames enabled are required for converged storage and situations where all traffic runs through the management interface. Static IP addresses are required on all HVM hosts.

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

Post-Install Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HVM OS 24.04 uses **netplan** for network configuration. If you need to adjust networking after installation you can manually edit **netplan** configuration files or use the provided **hpe-vm** TUI.

Using the hpe-vm TUI
""""""""""""""""""""

1. Log in to the HVM host using the user account created during installation

2. Run the **hpe-vm** command to launch the TUI:

   .. code-block:: bash

      sudo hpe-vm

3. Navigate to **Network Configuration**

  .. image:: /images/hpe-vm/hpe-vm.png
      :alt: hpe-vm TUI
      :align: center

4. Select the network interface to configure and set a static IP address, netmask, gateway, and DNS servers

  .. image:: /images/hpe-vm/interface-selection.png
      :alt: Interface selection in hpe-vm TUI
      :align: center

Editing Netplan Configuration Files
"""""""""""""""""""""""""""""""""""

1. Navigate to the netplan configuration directory:

   .. code-block:: bash

      cd /etc/netplan

2. Edit the existing configuration file (the filename varies by installation method):

   .. code-block:: bash

      sudo nano /etc/netplan/50-cloud-init.yaml
      # or /etc/netplan/00-installer-config.yaml
      # or /etc/netplan/01-netcfg.yaml

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

4. Validate and apply the configuration:

   .. code-block:: bash

      sudo netplan try

   The ``try`` command validates the configuration and applies it. If invalid, it automatically rolls back after 120 seconds.

.. tip::

   Back up your existing netplan configuration before making changes: ``cp /etc/netplan/<file>.yaml /etc/netplan/<file>.yaml.bak``

Verifying Host Readiness
^^^^^^^^^^^^^^^^^^^^^^^^

Before running the HPE Morpheus Manager Installer, confirm:

- **SSH access** — You can connect to the host over SSH (port 22) from your workstation
- **Sudo privileges** — Your user can run ``sudo`` commands without restriction
- **Static IP** — The host has a static IP address that will not change
- **DNS resolution** — The host can resolve external hostnames (or at minimum, the Morpheus appliance hostname once deployed)

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
