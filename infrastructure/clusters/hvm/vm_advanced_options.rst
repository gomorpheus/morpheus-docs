VM Advanced Options
===================

When provisioning or reconfiguring HVM virtual machines, the **Advanced Options** section provides controls for firmware, boot behavior, security, graphics, and virtualization settings. These options are found on the CONFIGURE tab during provisioning or through the :guilabel:`Actions` > :guilabel:`Reconfigure` menu on an existing VM.

.. NOTE:: Some options are only available at initial provisioning, and some are only available during reconfigure. See the availability notes for each option below. Changing firmware or boot options on an existing VM typically requires the VM to be powered off and its configuration regenerated.

Hardware / Chipset
------------------

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Option
     - Default
     - Description
   * - Hardware Compatibility
     - Modern
     - Selects the emulated machine chipset type. **Modern** uses the q35 chipset, which supports PCIe and is recommended for most workloads. **Legacy** uses the i440fx chipset for guest operating systems that do not support VirtIO drivers (e.g., Windows XP, older Linux distributions). *Provision only.*

Firmware & Boot
---------------

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Option
     - Default
     - Description
   * - UEFI
     - Off
     - Enables UEFI firmware instead of legacy BIOS. Required for Secure Boot and recommended for modern operating systems.
   * - Secure Boot
     - Off
     - Enables UEFI Secure Boot, which verifies the integrity of the boot chain. Requires UEFI to be enabled.
   * - BIOS Host Mode
     - Off
     - Passes the physical host's SMBIOS/DMI data directly into the guest VM instead of using emulated values. When disabled (default), the guest sees the virtualized identity (manufacturer "Morpheus", product "MVM", and a generated serial number). When enabled, the guest sees the actual physical server's SMBIOS data (manufacturer, product name, serial number, BIOS version, etc.) as if it were running directly on the hardware. This is required for software that validates hardware identity through SMBIOS, such as certain enterprise licenses tied to physical serial numbers or hardware-aware monitoring agents.
   * - Network Boot
     - Off
     - Enables PXE/network boot for the VM. When enabled, the VM can boot from a network interface, which is useful for customers with established PXE-based deployment automation workflows.
   * - Boot to BIOS/UEFI
     - Off
     - When enabled, the VM boots directly into the BIOS/UEFI firmware setup menu on every restart until this option is disabled. Useful for troubleshooting boot issues or changing firmware settings. *Reconfigure only.*
   * - Boot Menu Timeout (seconds)
     - 3
     - The number of seconds the boot menu waits before auto-selecting the default boot entry. Valid range is 1-30 seconds. Only visible when Boot to BIOS/UEFI is enabled. *Reconfigure only.*

Security
--------

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Option
     - Default
     - Description
   * - TPM
     - Off
     - Enables an emulated Trusted Platform Module (TPM) device for the VM using software TPM (swtpm). Required for Windows 11 and other operating systems that mandate TPM 2.0. TPM state is stored on shared storage and is automatically recovered during VM failover.

QEMU & Virtualization
---------------------

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Option
     - Default
     - Description
   * - QEMU Arguments
     - (empty)
     - Custom QEMU command-line arguments passed directly to the hypervisor process. Use this for advanced tuning or enabling features not exposed through the standard options.
   * - Enable Nested Virtualization
     - Off
     - Exposes VMX/SVM CPU flags to the guest, allowing it to run its own hypervisor inside the VM. Required for use cases such as running Docker with hardware virtualization, nested KVM, or Hyper-V inside a VM. *Provision only.*

.. WARNING:: Use QEMU Arguments with caution. Invalid arguments can prevent the VM from starting. Consult KVM/QEMU documentation for valid options.

Drivers & Graphics
------------------

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Option
     - Default
     - Description
   * - Attach VirtIO Drivers
     - Off
     - Attaches a VirtIO drivers ISO to the VM as a secondary CD-ROM device. Enable this when provisioning Windows guests from an ISO to install VirtIO storage and network drivers during OS setup. See the HVM Clusters (Legacy) guide for a detailed Windows image preparation walkthrough. *Provision only.*
   * - Disable Emulated Graphics
     - Off
     - Disables the emulated video/graphics adapter. Use this for headless VMs that do not require console access, such as dedicated appliances or GPU-passthrough workloads where the physical GPU provides the display.

Memory
------

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Option
     - Default
     - Description
   * - Huge Pages
     - Off
     - Enables huge pages (2 MB) memory backing for the VM. Huge pages reduce TLB (Translation Lookaside Buffer) misses and improve memory access performance for memory-intensive workloads such as databases and HPC applications. The host must have sufficient free huge pages allocated. *Provision only.*
   * - vNUMA Mode
     - Off
     - Controls virtual NUMA topology for the VM. See :doc:`vm_compute` for detailed documentation on vNUMA modes (Off, Auto, Manual).

Identity
--------

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Option
     - Default
     - Description
   * - Asset Tag
     - (VM name)
     - Sets the SMBIOS asset tag visible to the guest operating system. If left blank, the VM name is used. This value can be read inside the guest using tools such as ``dmidecode`` and is useful for inventory tracking and automation scripts that need to identify the VM.

Option Availability Summary
---------------------------

.. list-table::
   :widths: 40 15 15
   :header-rows: 1

   * - Option
     - Provision
     - Reconfigure
   * - Hardware Compatibility
     - Yes
     - No
   * - UEFI
     - Yes
     - Yes
   * - Secure Boot
     - Yes
     - Yes
   * - BIOS Host Mode
     - Yes
     - Yes
   * - Network Boot
     - Yes
     - Yes
   * - Boot to BIOS/UEFI
     - No
     - Yes
   * - Boot Menu Timeout
     - No
     - Yes
   * - TPM
     - Yes
     - Yes
   * - QEMU Arguments
     - Yes
     - Yes
   * - Nested Virtualization
     - Yes
     - No
   * - Attach VirtIO Drivers
     - Yes
     - No
   * - Disable Emulated Graphics
     - Yes
     - Yes
   * - Huge Pages
     - Yes
     - No
   * - vNUMA Mode
     - Yes
     - Yes
   * - Asset Tag
     - Yes
     - Yes
