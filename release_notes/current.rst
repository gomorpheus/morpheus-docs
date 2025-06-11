.. _Release Notes:

************************
|morphver| Release Notes
************************

Release Dates:

- |morphver| |releasedate|

New Features
============

:HVM: - Added attach and detach actions for cluster volumes to the Volumes subtab within the Storage tab on cluster detail pages. Click the gear (|gear|) icon to access these actions
      - When provisioning VMs to |clusters|, added the ability to specify the disk type and mountpoint (VirtIO, SATA). Edit the Cloud and mark ENABLE DISK TYPE SELECTION under Advanced Options to enable in the provisioning wizard
:User Settings: - Added "HPE dark" as a theme selection in User Settings 
:NSX: - Added iPv6 DHCP configuration for NSX segments
:Roles: - Added "List" level rights to the "Tools: Cypher" Role permission. "List" access allows the user to list out available Cypher entries in |morpheus| UI or API but not to consume them in scripts or decrypt them in any way

Fixes
=====

:Identity Sources: - When a user is created using a Custom External SSO identity source, the token expiration period is now correct to the interval set in global client settings rather than defaulting to one year
:Rubrik: - Fixed backup durations being lost after an integration sync
          - Removed the retention count configuration for Rubrik backups as they did not apply to that backup type
:VMware: - Fixed an issue that could cause the max memory metric displayed on the Instance detail page to occasionally be greater than the memory available to the Instance
          - Fixed an issue with French language hypervisor console keymaps
:Veeam: - Fixed backup jobs failing to sync when large numbers of VMs were attached

Appliance & Agent Updates
=========================

:Appliance: - The ``external_id`` column size in the ``morpheus.network`` table has been increased to varchar(500) due to being too small for some customers
            - Embedded Tomcat updated to v9.0.104
            - |morpheus| Linux Agent updated to v2.9.7
            - |morpheus| Node and VM Node packages updated to v3.2.37 with updated |morpheus| Linux Agent v2.9.7
:Embedded Plugins: - alletramp-plugin v1.1.1 added to embedded plugins
                   - arubacx-plugin v1.1.0 added to embedded plugins
                   - morpheus-home-dashboard-plugin updated to v1.1.3
                   - rubrik-plugin updated to v2.0.2

Known Issues
============

:Alletra MP Storage Plugin: - VM creation with specific ISO virtual images could fail volume creation. Recommendation is to use Qcow2 based images in case the error is seen. Fix will be available in 8.0.7 release.
                            - No support for iface for Software iSCSI
                            - VM Migration to other hosts may fail under heavy write-iops load on the VM. Recommendation is to reduce write-iops prior to migration
                            - Virtual images created without a specified disk capacity will fail to provision if the associated disk size is smaller than the minimum required
                            - VM in shutdown state will not migrate to the new node until it's powered on
                            - If the default image store is created after the virtual image is uploaded, it may cause issues with VM provisioning. Workaround is to ensure the store is created prior to virtual image creation
                            - Reconfigure Instance with HPE Alletra MP datastore fails if there is an attached CD ROM. Workaround is to delete the CD Drive before performing any subsequent actions for reconfigure
                            - Mixed datastore type is not supported for snapshot related features. Workaround is to specify the Alletra datastore by changing the disk type to Standard, selecting the datastore, and changing back to CD ROM
                            - Ubuntu VM created using ISO fails to start after snapshot revert due to cdrom device becoming unmapped from the host during revert
                            - When a VM undergoes multiple root disk reconfigurations across different datastores, subsequent attempts to add a new disk from the Alletra datastore result in a false success report in the UI
                            - VM creation fails intermittently with ``StorageException while creating volume: Resource Already Exists`` error using plugin version 1.1.1
                            - Cdrom not removed from VM created on Alletra plugin datastore after successful reconfiguration
                            - Additional cdrom and morpheus-image cdrom not removed after successful reconfiguration
:Installer: - |morpheus| installer 1.0.7 fails to deploy |manager| version 8.0.6 when using TUI. Use version 1.0.8.
