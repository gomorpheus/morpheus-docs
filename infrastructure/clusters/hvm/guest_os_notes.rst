Guest Operating System Notes
============================

This page covers OS-specific considerations, recommendations, and behaviors when running virtual machines on HVM clusters.

The HVM controls referenced on this page are selected from **Advanced Options** on the Configure step during provisioning. See :doc:`vm_advanced_options` for field availability and reconfiguration behavior.

Windows Guests
--------------

Cores Per Socket
^^^^^^^^^^^^^^^^

Windows 10 and Windows 11 display only one socket in Task Manager regardless of the actual CPU topology. If your Windows VM has multiple vCPUs and you want the guest to see them as cores within a single socket (rather than multiple single-core sockets), set **Cores Per Socket** equal to the total vCPU count during provisioning.

For example, a VM with 8 vCPUs and Cores Per Socket set to 8 will present as 1 socket with 8 cores. If Cores Per Socket is left at the default (1), Windows sees 8 sockets with 1 core each, which may confuse certain applications and licensing models.

.. NOTE:: Windows Server editions are less affected since they support multi-socket display, but setting Cores Per Socket appropriately is still recommended for licensing clarity (many Windows Server licenses are per-socket).

VirtIO Drivers
^^^^^^^^^^^^^^

Windows does not include VirtIO drivers natively. To achieve optimal I/O performance, VirtIO drivers must be installed during the initial Windows setup:

#. When provisioning a Windows VM from an ISO, enable **Attach VirtIO Drivers** in Advanced Options
#. This mounts the VirtIO driver ISO as a secondary CD-ROM
#. During the Windows "Where do you want to install Windows?" step, click **Load Driver**
#. Browse to the mounted VirtIO ISO and select the appropriate driver for your Windows version (e.g., ``viostor`` for the storage controller)
#. Complete the Windows installation
#. After Windows is installed and you are logged in, navigate to the VirtIO ISO drive in Windows Explorer
#. Right-click ``virtio-win-guest-tools`` and select **Install**
#. Step through the installer — this installs all remaining VirtIO drivers (network, balloon, serial) and the QEMU Guest Agent

.. IMPORTANT:: The QEMU Guest Agent installed by ``virtio-win-guest-tools`` is required for guest customization (Sysprep), graceful shutdown, and |morpheus| agent communication without network access. Always run this installer after the OS is set up.

Hardware Compatibility
^^^^^^^^^^^^^^^^^^^^^^^

- **Modern (Q35)** — Use for Windows 8/Server 2012 and later. Supports PCIe, VirtIO, and modern features.
- **Legacy (i440fx)** — Use for Windows XP, Windows Server 2003, or other guests that cannot load VirtIO drivers. This provides emulated IDE storage and legacy PCI bus.

TPM and Secure Boot
^^^^^^^^^^^^^^^^^^^^

Windows 11 requires both TPM 2.0 and Secure Boot. Enable both **TPM** and **Secure Boot** (which also requires **UEFI**) in Advanced Options when provisioning Windows 11 VMs.

Windows 10 does not require TPM or Secure Boot but supports both for enhanced security features like BitLocker.

Guest Customization (Sysprep)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When cloning a Windows VM or provisioning from a template, |morpheus| runs Sysprep via the QEMU Guest Agent to generalize the image (new SID, hostname, network identity). This requires:

- The VirtIO drivers and QEMU Guest Agent to be installed in the template (``virtioSupported`` must be true)
- The template to have been prepared with ``sysprep /generalize`` (or have the Sysprep utility available)

If the QEMU Guest Agent is not available, guest customization will be skipped and the VM may have identity conflicts.

Hostname Length
^^^^^^^^^^^^^^^

Windows hostnames are automatically truncated to **15 characters** (the NetBIOS limit). If your naming policy generates longer names, be aware that the Windows hostname will differ from the |morpheus| display name.

Agent Communication
^^^^^^^^^^^^^^^^^^^^

|morpheus| communicates with Windows VMs using:

#. **QEMU Guest Agent** (preferred) — works without network connectivity, used for Sysprep, command execution, and file operations
#. **WinRM** (fallback) — requires network connectivity and WinRM to be enabled in the guest

Ensure WinRM is configured with ``winrm quickconfig`` and set to automatic startup in your Windows templates.

Diagnosing Inter-Host Network Throughput
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do not use a nominal 10 Gb NIC speed as a throughput guarantee for a Windows VM. End-to-end results depend on the guest driver and CPU, VM sizing, host load, Virtual Switch and bond configuration, MTU, and every physical link in the path.

Before changing Windows settings:

#. Confirm the VirtIO network driver is installed and current for the supported guest image.
#. Test in both directions with a dedicated throughput tool and multiple streams; record latency, retransmits, guest CPU, and host CPU during the test.
#. Compare same-host and different-host VM results to isolate the virtual/guest path from the physical uplinks.
#. Verify negotiated physical link speed, bond state, switch counters, VLANs, and end-to-end MTU. Resolve drops, errors, or MTU mismatch first.
#. Record the Windows version, VirtIO driver version, HVM release, VM vCPU/memory, test command, and topology so results are repeatable.

As a bounded diagnostic, an administrator can inspect RSS and TCP auto-tuning from an elevated PowerShell session:

.. code-block:: powershell

   Get-NetAdapterRss
   Get-NetAdapterAdvancedProperty -Name "<adapter>"
   netsh int tcp show global

If RSS is disabled and the installed VirtIO driver supports it, test enabling RSS on the specific adapter with ``Enable-NetAdapterRss -Name "<adapter>"`` and repeat the same benchmark. Revert with ``Disable-NetAdapterRss -Name "<adapter>"`` if throughput, CPU use, or stability regresses.

Do not disable checksum or large-send offload, or add ``MaxUserPort`` and ``TcpTimedWaitDelay`` registry values, as a general HVM optimization. Those changes affect guest-wide networking and should be used only for a measured workload under Microsoft and HPE Support direction, with the original adapter and registry values recorded for rollback.

Linux Guests
------------

Cloud-Init
^^^^^^^^^^^

Linux VMs use **cloud-init** by default for guest customization. |morpheus| generates cloud-init configuration (user data, meta data, and network data) and delivers it via an ISO mounted to the VM at boot.

Cloud-init handles:

- Hostname and network configuration
- SSH key injection
- User account creation
- Post-provisioning scripts

.. NOTE:: Ensure your Linux templates have cloud-init installed and configured to look for the ``NoCloud`` datasource.

QEMU Guest Agent
^^^^^^^^^^^^^^^^^

For enhanced management capabilities (graceful shutdown, filesystem freeze for snapshots, live IP reporting), install the QEMU Guest Agent in your Linux templates:

- **Ubuntu/Debian:** ``apt install qemu-guest-agent``
- **RHEL/CentOS:** ``yum install qemu-guest-agent``
- **Enable and start:** ``systemctl enable --now qemu-guest-agent``

The QEMU Guest Agent enables |morpheus| to communicate with the VM even when network-based access (SSH) is unavailable.

VirtIO Drivers
^^^^^^^^^^^^^^

Modern Linux kernels (2.6.25+) include VirtIO drivers natively. No additional driver installation is needed. The **Hardware Compatibility** setting should be left at **Modern (Q35)** for all supported Linux distributions.

For very old Linux distributions (kernel < 2.6.25) that lack VirtIO support, select **Legacy (i440fx)** hardware compatibility.

Cores Per Socket
^^^^^^^^^^^^^^^^

Linux correctly identifies and utilizes multi-socket topologies, so Cores Per Socket configuration is less critical than for Windows. However, for NUMA-aware workloads, aligning Cores Per Socket with the host's physical cores-per-NUMA-node can improve memory locality. See :doc:`vm_compute` for vNUMA configuration.

Template Preparation
^^^^^^^^^^^^^^^^^^^^^

Before converting a Linux VM to a template:

#. Clear cloud-init state: ``sudo cloud-init clean --logs --machine-id``
#. Remove SSH host keys: ``sudo rm -f /etc/ssh/ssh_host_*``
#. Clear machine ID: ``sudo truncate -s 0 /etc/machine-id``
#. Remove persistent network rules if present
#. Power off the VM

General Considerations
----------------------

Power Operations & Shutdown Behavior
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When stopping a VM, |morpheus| performs a **graceful-then-force** shutdown sequence:

#. An ACPI power-button signal is sent to the guest OS, giving it the opportunity to perform a clean shutdown (flush buffers, stop services, sync filesystems)
#. If the guest has not powered off after **10 seconds**, the VM is forcefully terminated

This sequence runs automatically on every Stop Server operation. There is no separate "force only" option at this time — all stops attempt graceful first.

**How ACPI shutdown works with different guest configurations:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Guest Configuration
     - Shutdown Behavior
   * - QEMU Guest Agent installed
     - ACPI signal is sent to the guest OS. The guest agent is **not** used for the shutdown signal itself — shutdown is handled by the guest OS responding to the ACPI power button event. However, the guest agent enables other operations like filesystem freeze before snapshots.
   * - QEMU Guest Agent NOT installed
     - Same ACPI signal is sent. If the guest OS has ACPI support enabled (all modern operating systems do), it will perform a clean shutdown. No behavioral difference for the stop operation.
   * - Guest Agent installed but not responding
     - No impact on shutdown. The ACPI power button signal is delivered at the hypervisor level, independent of the guest agent communication channel.
   * - Guest OS ignoring ACPI (rare)
     - The graceful ACPI signal has no effect. After the 10-second timeout, the VM is forcefully terminated. This can occur with some legacy or misconfigured operating systems that do not handle ACPI power button events.

.. NOTE:: The 10-second grace period means that VMs with long-running shutdown scripts (e.g., database flush, service drain) may be forcefully terminated before completing. For workloads requiring longer graceful shutdown times, consider stopping the application services manually before issuing the Stop Server command.

**When the QEMU Guest Agent matters for power-related operations:**

While the guest agent does not affect the Stop Server operation itself, it is used for:

- **Filesystem freeze/thaw** — Before snapshots, the guest agent freezes guest filesystems for consistency
- **Graceful reboot** — The agent can execute a clean reboot command inside the guest
- **Guest OS information** — Reporting IP addresses, OS version, and hostname back to |morpheus|

.. list-table::
   :widths: 25 35 35
   :header-rows: 1

   * - Feature
     - Linux
     - Windows
   * - Guest customization method
     - Cloud-init (ISO)
     - Sysprep via QEMU Guest Agent
   * - VirtIO drivers
     - Built into kernel
     - Must install from VirtIO ISO
   * - Hostname limit
     - No practical limit
     - 15 characters (NetBIOS)
   * - Agent communication
     - SSH or QEMU Guest Agent
     - WinRM or QEMU Guest Agent
   * - Cloud-init support
     - Yes (default)
     - No
   * - TPM/Secure Boot
     - Optional
     - Required for Windows 11
   * - Recommended chipset
     - Modern (Q35)
     - Modern (Q35) for Win 8+; Legacy (i440fx) for XP/2003
   * - ISO mount bus
     - SCSI (when available) or SATA
     - Always SATA
