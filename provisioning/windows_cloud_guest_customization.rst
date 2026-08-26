Windows Guest Customization (Image Preparation)
=================================================

This guide covers preparing Windows virtual images for provisioning with |morpheus| guest customization — including hostname assignment, network configuration, and Active Directory domain join. The approach varies by cloud type.

Customization Approaches by Cloud Type
----------------------------------------

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Cloud Type
     - Primary Method
     - How It Works
   * - HVM (KVM)
     - Pre-sysprep'd image
     - Image is sysprep'd before capture. On first boot, Windows completes OOBE, |morpheus| Agent installs and handles hostname/domain join.
   * - VMware / VME
     - Force Guest Customization
     - VM is provisioned from a template with VMware Tools installed. |morpheus| triggers a guest customization pass — transferring the unattend.xml to the running VM, then rebooting to apply hostname, network, and domain settings.
   * - SCVMM / Hyper-V
     - Pre-sysprep'd image + unattend.xml
     - Image must be sysprep'd before capture into the SCVMM library. When provisioning from a template, |morpheus| injects an unattend.xml to configure hostname, network, and domain join. For clone operations, unattend.xml injection is not supported — |morpheus| installs the Agent post-provisioning to handle configuration.
   * - AWS / Azure / GCP
     - Cloud-native (userdata)
     - Cloud provider handles customization via instance metadata and userdata. Image prep follows cloud-specific requirements.

Force Guest Customization (VMware / VME)
-----------------------------------------

On VMware and VME clouds, **Force Guest Customization** works differently than on other platforms:

#. The VM is provisioned from a template that has **VMware Tools installed** (not necessarily sysprep'd)
#. |morpheus| boots the VM
#. VMware guest customization transfers an unattend.xml into the running guest via VMware Tools
#. The VM reboots to apply the customization (hostname, network, SID regeneration, domain join)

This means the source template does **not** need to be in a sysprep'd state — VMware Tools handles the customization injection and triggers the re-specialize pass.

.. note::

   Force Guest Customization on VMware requires VMware Tools to be installed and running in the template. Without Tools, the customization payload cannot be delivered to the guest.

Pre-Sysprep'd Images (HVM / General Use)
------------------------------------------

For HVM clusters (and any cloud where Force Guest Customization is not available), the image must be **sysprep'd before capture**:

Step 1: Prepare the Template VM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install Windows (Server 2016, 2019, 2022, 2025 or Windows 10/11)
#. Install all Windows Updates
#. Install VirtIO drivers (for HVM — use the **Attach VirtIO Drivers** advanced option during initial ISO provisioning)
#. Install any required software or roles
#. Configure Windows Firewall to allow WinRM (port 5985/5986)

Step 2: Sysprep
^^^^^^^^^^^^^^^^

.. code-block:: powershell

   & "$env:SystemRoot\System32\Sysprep\sysprep.exe" /generalize /oobe /shutdown

The VM shuts down after generalizing. **Do not boot it again** — capture it as a virtual image at this point.

Step 3: Upload as Virtual Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to :menuselection:`Library --> Virtual Images`, click :guilabel:`+ Add`, and configure:

.. list-table::
   :widths: 25 20 55
   :header-rows: 1

   * - Setting
     - Value
     - Purpose
   * - Is Sysprep
     - **Enabled**
     - Indicates the image is in a generalized state and will go through OOBE on first boot
   * - Install Agent
     - Enabled
     - Installs the |morpheus| Agent for management and domain join
   * - Username
     - ``Administrator``
     - Local admin account for initial agent connection
   * - Password
     - (set password)
     - Local admin password for agent authentication

Virtual Image Options Reference
--------------------------------

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Option
     - Applicable Clouds
     - Description
   * - Is Force Customization
     - VMware, VME
     - Triggers guest customization via VMware Tools — transfers unattend.xml and reboots the VM to apply settings. Does NOT require the image to be pre-sysprep'd.
   * - Is Sysprep
     - All
     - Indicates the image is in a sysprep'd (generalized) state. Used by |morpheus| to know the VM will go through OOBE on first boot.
   * - Is Cloud Init
     - HVM, OpenStack
     - Generates a cloud-init ISO with metadata/userdata and attaches it to the VM. Used for Linux guests primarily.
   * - Is Auto Join Domain
     - All
     - Automatically triggers domain join when a Network Domain is configured, without requiring explicit domain selection during provisioning.
   * - Install Agent
     - All
     - Installs the |morpheus| Agent on the guest for management, monitoring, and remote execution.
   * - Skip Network Wait
     - All
     - Skips waiting for network availability before proceeding with provisioning. Useful for isolated networks.
   * - VirtIO Supported
     - HVM
     - Indicates the image has VirtIO drivers installed. When disabled, |morpheus| uses IDE/SATA disk bus instead of VirtIO.

Domain Join Configuration
--------------------------

Domain join is triggered by the **Network Domain** configuration, not by image settings. The Network Domain can be associated via:

- **Network selection at provisioning** — The network chosen during instance creation has an associated Network Domain with Domain Controller enabled
- **Cloud default** — A default Network Domain set on the Cloud configuration applies to all VMs in that Cloud unless overridden

See :doc:`/integration_guides/windows_domain_join` for full domain join setup instructions.

What Gets Customized
---------------------

.. list-table::
   :widths: 25 35 40
   :header-rows: 1

   * - Customization
     - VMware/VME (Force Customization)
     - HVM (Pre-Sysprep'd)
   * - Hostname
     - Applied via unattend.xml during reboot
     - Set by |morpheus| Agent after OOBE completes
   * - Network (static IP)
     - Applied via guest customization spec
     - Configured by |morpheus| Agent
   * - Domain join
     - Can be included in unattend OR handled by |morpheus| Agent post-boot
     - Handled by |morpheus| Agent post-boot
   * - SID regeneration
     - Yes (forced re-specialize)
     - Yes (sysprep generalize)
   * - Admin password
     - Set via customization spec
     - Set from Virtual Image credentials

Troubleshooting
----------------

Force Customization Not Working (VMware)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Verify VMware Tools is installed and running in the template
- Check that the template is powered off (not suspended)
- Verify **Is Force Customization** is enabled on the Virtual Image in |morpheus|

VM Boots to OOBE Setup Screen (HVM)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Verify **Is Sysprep** is enabled on the Virtual Image
- Check that the image was properly sysprep'd before capture (not booted after sysprep)
- Ensure the |morpheus| Agent can reach the appliance to receive configuration

Hostname Not Applied
^^^^^^^^^^^^^^^^^^^^^

- Verify the |morpheus| Agent is running (check Services for "Morpheus Windows Agent")
- Check that the Instance name does not exceed 15 characters (NetBIOS limit)
- For VMware, verify guest customization completed (check vCenter recent tasks)
