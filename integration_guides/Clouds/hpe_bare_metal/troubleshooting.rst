Troubleshooting and Diagnostics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section provides a structured approach to diagnose and resolve common issues encountered during compute, OS imaging, networking, and storage operations.

 Use the following details to obtain the accurate troubleshooting details: 
- Identify the symptom: locate the closest match in the table or subsection. 
- Confirm the likely cause: check the listed items using the provided tools and logs. 
- Apply the suggested fix: perform the recommended actions. 
- Collect diagnostic information: if the issue persists, gather logs and screenshots for support escalation.   When reporting an issue, you require the following diagnostics details: 
- System Details  
  - Hostname / Device ID 
  - OS version and build 
  - BIOS/Firmware version  
- Event Details  
  - Date and time of failure 
  - Step at which failure occurred 
  - Any error messages or codes  
- Logs  
  - Relevant log files for the failed component 
  - Screenshots of errors (if applicable)

Compute
-------

Compute
  The topic describes troubleshooting procedures for compute.

OS Imaging
^^^^^^^^^^

OS Imaging


.. list-table::
   :header-rows: 1
   :widths: auto

   * - S. No.
     - Symptom
     - Additional Details
     - Common Checks
     - Log Files
     - Remarks
   * - 1
     - Windows Setup fails before completion
     - Donotdismiss error dialogs immediately, as this may remove diagnostic information.UseiLO Remote Consoleto access the system.PressShift + F10to open a command prompt in the Windows PE environment.
     - Disk layout– Confirm the primary disk is attached to the local RAID controller.AutoUnattend.xml– Verify the file exists and defines required partitions:EFI System Partition (500 MB)Microsoft Reserved Partition (128 MB)Primary OS partition
     - Relevant setup logs may be found in:X:\\Windows\\PantherC:\\$WINDOWS.~BT\\Sources\\PantherKey files:setupact.logsetuperr.log
     - Use logs to identify the specific failure stage and error code.
   * - 2
     - RHEL / Oracle Linux(Autoinstall via Kickstart)
     - If the installation fails or hangs, the installer provides interactive shells and log files for debugging.
     - TTY Shortcuts:Alt + F1: Installer UIAlt + F2: Interactive shellAlt + F3: Installation logs
     - Key Logs:/var/log/anaconda/anaconda.log/var/log/anaconda/syslog/root/anaconda-ks.cfg/root/original-ks.cfg/root/post-ks.log/var/log/cloud-init.log/var/log/cloud-init-output.log
     - Use interactive shell (Alt + F2) to validate disk and network configuration before retrying installation.
   * - 3
     - Ubuntu Linux(Autoinstall via Curtin and Subiquity)
     - If the installation fails or hangs, the installer provides interactive shells and log files for debugging.
     - TTY Shortcuts:Alt + F2 or Ctrl + Alt + F2: Interactive shellInstaller runs on TTY1
     - Key Logs/var/log/installer/curtin-install.log/var/log/installer/early-commands.log/var/log/installer/subiquity-client*/var/log/installer/subiquity-server*/var/log/cloud-init.log/var/log/cloud-init-output.log
     - Use interactive shell (Alt + F2) to check network and storage configuration, then review logs for errors.

Firmware Lifecycle
^^^^^^^^^^^^^^^^^^

Firmware and Driver Lifecycle Management


.. list-table::
   :header-rows: 1
   :widths: auto

   * - S.No
     - Topic / Symptom
     - Additional Details
     - Common Checks
     - Log Files
     - Comments
   * - 1
     - Morpheus / iLO fails to initialize the server after the SPP update
     - Server provisioning fails with errors similar to:Base.1.18.ResourceMissingAtURIDrives/64515 not foundHTTP nullStorage object lists drive URIs that cannot be resolved
     - Verify storage drive URIs:curl -k -u <user>:<pass>https://<ilo>/redfish/v1/Systems/1/Storage/<controller>
     - jqValidate drive URI exists:curl -k -u <user>:<pass>https://<ilo>/redfish/v1/Chassis/<chassis>/Drives/<id>
     - jqConfirm SPP was applied recently
     - Morpheus / iLO logs
     - Typically caused by stale Redfish drive references after SPP.
   * - 2
     - After SPP, Redfish drive tree mismatch
     - Storage object shows drive count and IDs, but drive URIs return ResourceMissingAtURI
     - Perform aFull Cold Power Cycle(not reboot):Power OFF the server (OS or iLO)Remove both power cablesWait 60 secondsReconnect power cablesPower ON the server
     - iLO event log, Smart Array logs
     - Required for Gen11/Gen12 after firmware updates.

Networking
----------

.. list-table::
   :header-rows: 1
   :widths: auto

   * - S.No.
     - Topic / Symptom
     - Additional Details
     - Common Checks
     - Log Files
     - Comments
   * - 1
     - Cloud Network Mode Configuration
     - Cloud can operate inUnmanagedorManaged (ArubaCX-Int)network modes. This choice is made during cloud creation underAdvanced Options.
     - Verify the correct network mode selected during cloud creation.
     - Morpheus UI log
     - Use Unmanaged for external network control; use Managed for Morpheus-managed ArubaCX switches.
   * - 2
     - Unmanaged Network - Default Setup
     - In Unmanaged mode, Morpheus creates a minimal configuration: a default Resource Pool and a default unmanaged network. The default network isuntaggedand usesDHCP.
     - Ensure the DHCP server exists and the network is configured for an untagged VLAN.
     - Morpheus UI log
     - This allows instances to boot with connectivity without extra network configuration.
   * - 3
     - Unmanaged Network - Additional VLANs
     - Users can create additional VLANs/networks as required.
     - Check VLAN configuration and availability in provisioning options.
     - Morpheus UI log
     - Additional networks can be consumed by bare-metal instances.
   * - 4
     - Managed Network - ArubaCX Integration
     - Managed mode uses ArubaCX switches and requires the ArubaCX plugin.
     - Confirm the ArubaCX plugin is loaded in Morpheus.
     - Morpheus UI log
     - Managed networks allow Morpheus to configure VLANs on switches automatically.
   * - 5
     - AddingHPE ArubaCX Plugin
     - The plugin must be loaded to enable managed network features. Follow the procedure AddingHPE BMaaS Integration to load the plugin JAR.
     - Verify plugin status in Morpheus.
     - Morpheus UI log
     - Required before creating network integrations.
   * - 6
     - Creating ArubaCX Network Integration
     - Integration defines switch credentials and switch pairs (typically 2 per rack).
     - Verify switch IPs, username, and password are correct.
     - Morpheus UI log
     - One integration is needed per rack (switch pair).
   * - 7
     - Creating Managed Networks
     - Networks represent VLANs and include attributes like subnet, gateway, DNS, and IP allocation method.
     - Ensure VLAN ID, trunks, and subnet are correct.
     - Morpheus UI log
     - Primary VLAN is untagged, VLAN trunks are tagged.
   * - 8
     - Private Network Option
     - Private networks do not configure a primary VLAN on the uplink, making them inaccessible outside the cloud.
     - Confirm if the network should be private or public.
     - Morpheus UI log
     - Used for internal workload networks only.
   * - 9
     - Network Consumption During Provisioning
     - Networks are attached to physical or bonded interfaces. Primary VLAN is untagged, trunk VLANs are tagged.
     - Check interface type (physical or bond) and correct VLAN assignment.
     - Morpheus UI log
     - Supports Static Bond, LACP Bond, and Switch Independent Bond.
   * - 10
     - Bond Interface Configuration
     - Bond interfaces require two physical ports to form an aggregated link.
     - Ensure both physical ports are available and correctly mapped.
     - Morpheus UI log
     - Bonding provides bandwidth aggregation and redundancy.
   * - 11
     - Virtual Network Interfaces
     - Virtual networks allow tagged VLANs to be configured as IP interfaces on the server OS.
     - Verify if tagged networks require an IP interface.
     - Morpheus UI log
     - If not needed, do not configure the virtual interface.

Storage
-------

Storage
  The topic describes troubleshooting procedures for storage.

Local Boot Volume
^^^^^^^^^^^^^^^^^

Local Storage - Boot Volume Selection During Instance Creation


.. list-table::
   :header-rows: 1
   :widths: auto

   * - S.No.
     - Topic / Symptom
     - Additional Details
     - Common Checks
     - Log Files
     - Comments
   * - 1
     - Boot volume not found
     - Device UID mismatch or not yet discovered
     - Confirm device discovery is completeVerify the UID in the storage controller
     - -
     - Wait for discovery to complete and retry.
   * - 2
     - ResourceMissingAtURIerrors
     - Redfish device discovery is not complete
     - Verify Redfish discovery statusConfirm the device is visible in Redfish inventory
     - -
     - Retry after a short wait.
   * - 3
     - Script cannot find the device
     - UID format mismatch or missing disk link
     - - Verify/dev/disk/by-id/entries- Confirm correct disk UID format
     - -
     - Ensure disk links are correctly mapped and retry.

Remote Storage
^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: auto

   * - S.No
     - Topic / Symptom
     - Additional Details
     - Common Checks
     - Log Files
     - Comments
   * - 1
     - Failure to IntegrateHPE Alletra MP Plugin
     - Issues during plugin loading or integration of the HPE Alletra MP plugin in the
     - morpheus
     - Enterprise environment.
     - Confirm that the plugin.jarfile is properly loaded as per section 5.2 “AddingHPE BMaaS Integration”.Check if the correct credentials and URL for the storage array are used.
     - Plugin Logs: Look for errors during plugin loading.System Logs: Check for authentication or configuration failures.
     - Ensure compatibility between the plugin version and
     - morpheus
     - Enterprise.Network/firewall issues may prevent communication with the storage array.
   * - 2
     - Storage Server Creation Failure
     - Failure when adding a new storage server (URL, credentials, or type mismatch).
     - Verify the URL and credentials for accessing the storage array.Ensure the correct type (“HPE Alletra Block Storage HVM”) is selected.
     - Storage Server Logs: Check for error messages related to server creation (authentication issues, network problems).
     - An incorrect URL or credentials can prevent server creation.Make sure the storage server is accessible and reachable from the Morpheus interface.
   * - 3
     - Datastore Creation Failure
     - Issues while creating a datastore, such as selecting an incorrect storage server, or specifying incompatible resource pools or protocols.
     - Verify that the storage server was created successfully.Ensure correct datastore type and resource pool selection.Ensure \"FC\" is selected for protocol.
     - Datastore Logs: Check for errors when trying to create the datastore (incorrect type, wrong resource pool).
     - Mismatched storage configuration or resource pool selection can lead to datastore creation failures.Confirm network configurations for FC protocol.
   * - 4
     - Volume Creation Issues
     - Errors when creating volumes, including failure to assign the correct size, volume type (replicated/unreplicated), or datastore.
     - Ensure the storage server is selected correctly.Verify the volume size and type are correct.Confirm the datastore is properly associated.
     - Volume Logs: Errors related to volume creation (incorrect parameters, missing datastore).
     - Volume size can only be increased - check the requirements.Ensure correct replication type (CPP/APP) based on the storage array setup.
   * - 5
     - Volume Deletion Failure
     - Unable to delete volumes due to them being attached to servers or due to incorrect permission settings.
     - Confirm the volume is detached from all servers.Ensure you have the necessary permissions to delete the volume.
     - Volume Deletion Logs: Look for errors related to detachment or permission issues during deletion.
     - Volumes can only be deleted once detached.Ensure no active processes are using the volume.
   * - 6
     - Volume Resize Failure
     - Unable to resize a volume, typically due to a lack of rescan on the server OS or exceeding size limits.
     - Confirm the server OS has rescanned the volume.Ensure the new size does not exceed any system or storage limits.
     - Volume Resize Logs: Look for errors when attempting to resize (e.g., \"resize failed\" messages).
     - Resize operations are only allowed for volume increases, not reductions.Ensure the OS is aware of the new size after the resize.
   * - 7
     - Volume Consumption Issues During Provisioning
     - Difficulty attaching volumes during instance provisioning (shared/unshared, existing/new, replicated/unreplicated).
     - Ensure the correct volume type (shared/unshared) is specified.Verify replication settings (CPP/APP) are correct.Check if the volume exists and is accessible.
     - Provisioning Logs: Check for errors related to volume attachment (invalid volume, replication mismatch).
     - Volumes must be properly configured before provisioning.Shared volumes should be attached to all servers within the instance.
   * - 8
     - FC Protocol Issues
     - Issues with FC protocol during volume creation or consumption (e.g., failed attachments or slow response).
     - Check if the storage server and datastore are properly configured for FC.Confirm FC switches and network paths are properly set up.
     - Fibre Channel Logs: Look for errors indicating FC connectivity or protocol issues.
     - FC issues may be related to network misconfigurations or cable/connectivity problems.

