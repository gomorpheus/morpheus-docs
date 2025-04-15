.. _Release Notes:

************************
|morphver| Release Notes
************************

Release Dates:

- |morphver| |releasedate|

New Features
============

:API & CLI: - Clusters have a new property ``provisionComplete`` which returns ``true`` after provisioning is completed
            - Integrations (``/api/integrations``) and integration types (``/api/integration-types``) can now be queried through |morpheus| API
            - The result of creating Clusters without providing a Resource Name value is now consistent across |morpheus| UI, API and CLI (default cluster name and node names are provided)
:HPE VM: - Added initial admin password confirm to the HPE VM Manager setup process to prevent the need for reinstallation if the initial password is mistyped
          - HPE VM Cluster Layout version 1.2 added in BETA. Clusters running layout version 1.2 should be used for testing purposes and should not be used for running production workloads
          - The HPE VM installer now prompts for interface names (ex. compute or management interface) using a dropdown menu to prevent failures due to simple typos
          - When installing the HPE VM Manager, an error is now logged if the installer is unsuccessful in downloading the Manager QCOW image from the URL provided
:Installer: - Added additional checks that the appliance URL DNS name is resolvable to warn the user prior to beginning the Manager installation process
:License: - |morpheus| appliances now allow stacking licenses. When stacked, the cumulative total of license privileges are allowed
:Plugins: - Added support for AurbaCX network plugin. See `integration guide <https://hpevm-docs.morpheusdata.com/en/8.0.4-vme/integration_guides/Networking/hpe-arubacx.html>`_ for setup details and use cases
          - Added support for HPE Alletra MP storage plugin. See `integration guide <https://hpevm-docs.morpheusdata.com/en/8.0.4-vme/integration_guides/Storage/hpe-alletra-mp.html>`_ for setup details and use cases
          - Improved appliance cleanup when plugins are removed

Fixes
=====

:API & CLI: - API calls to resize no longer require "Reconfigure: Disk Change Type" permission when the resize doesn't affect storage
             - Adding a network via |morpheus| API now always results in a prompt to select a Network Domain
             - Fixed Inventory Options flags not being returned in GET calls for Clouds of certain Cloud types
:Backups: - When deleting an Instance and opting to preserve the backups, |morpheus| no longer attempts to take new backups (which fail) on the scheduled backup job interval
:Clone: - Cloud-init configuration files removed prior to taking a snapshot to clone are now restored on the source VM after the clone is complete
:Clouds: - The "No Proxy" and "Bypass proxy for appliance URL" configurations on the Cloud now affect |morpheus| Agent installations on running VMs
:HPE VM: - Fixed an issue with restarting VMs if snapshots were deleted prior to attempting restart
          - Improved Snapshot handling when VMs were not running
          - Improved handling of configured proxy information in the HPE VM installer
          - When resizing HPE VM Instances which change disk size or remove a disk, the user is warned that existing snapshots will be purged and, if accepted, all existing snapshots are purged
:Instances: - Fixed a situation where disk labels could be duplicated under certain conditions when disks were removed and added via reconfigures
            - On Instance resize, the user who triggers the resize is credited in Instance history with all processes associated, even those resulting from Provisioning Workflow Tasks set by a different user
:License: - Fixed an issue that caused workloads using provisioning technologies other than HPE VM Clusters not to count correctly against license limits
:Network: - Fixed an issue that caused orphaned network records in |morpheus| if the network was deleted from vCenter during a |morpheus| Cloud sync
           - When changing the network selection at provision time, the DHCP/pool/static selection now resets
:Roles: - Fixed a scenario where a newly created Role with default access levels for some constructs set to NONE could have them elevated to FULL following a restart
        - Fixed incorrect access to the Tools menu when certain specific and limited access was given to Tools components
:Tasks: - Powershell Tasks run against VMware Instances without |morpheus| Agent installed will now default to using ``guestTools`` for execution
         - Users without permissions to decrypt Cypher values can no longer run Tasks utilizing the ``<%=cypher.read%>`` function
:VMware: - Added improved keymap handling for VMware hypervisor console for German, UK (PC), and Italian layouts for both Windows and Linux servers

Appliance & Agent Updates
=========================

:Linux Agent: - |morpheus| linux agent updated to v2.9.4
:guacd: - guacamole-server updated to v1.6.0
:Node Packages: - Updated to v3.2.34 with |morpheus| linux agent v2.9.4
                - Java updated to 17.0.14+7

..
  Known Issues
  ============

  - **Known Issue 1 Description.** Additional description and workaround (if available) here.
  - **Known Issue 2 Description.** Additional description and workaround (if available) here.
  - **Known Issue 3 Description.** Additional description and workaround (if available) here.
