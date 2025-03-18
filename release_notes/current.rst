.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade versions: Non-rolling: |minUpgradeVer| (Rolling upgrades not supported for 8.0.4)

.. .. NOTE:: Items appended with :superscript:`7.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

.. _Release Notes:

*************************
|morphver| Release Notes
*************************

New Features
============

:API & CLI: - Clusters have a new property ``provisionComplete`` which returns ``true`` after provisioning is completed
             - Integrations (``/api/integrations``) and integration types (``/api/integration-types``) can now be queried through |morpheus| API
             - The ``/api/setup`` endpoint now returns an ``applianceId`` value
             - The ``terminal-access`` permission accepts ``none`` and ``full`` permission values when updated via |morpheus| API to bring it in line with standard terminology for other permissions
             - The result of creating Clusters without providing a Resource Name value is now consistent across |morpheus| UI, API and CLI (default cluster name and node names are provided)
:Clouds: - "Cost this Month" label on the Cloud detail page has been changed to "Estimated Cost" to increase clarity of the shown figure
:Dashboard: - Multiple Dashboard plugins can now be added to the same appliance. Within the Appliance section of Global settings, administrators can set the order they should appear
:HPE VM: - Added initial admin password confirm to the HPE VM Manager setup process to prevent the need for reinstallation if the initial password is mistyped
          - HPE VM Cluster Layout version 1.2 added in BETA. Clusters running layout version 1.2 should be used for testing purposes and should not be used for running production workloads
          - The HPE VM installer now prompts for interface names (ex. compute or management interface) using a dropdown menu to prevent failures due to simple typos
          - When installing the HPE VM Manager, an error is now logged if the installer is unsuccessful in downloading the Manager QCOW image from the URL provided
:Installer: - Added additional checks that the appliance URL DNS name is resolvable to warn the user prior to beginning the Manager installation process
:Library: - Added updated default images for many Linux flavors (and versions within each flavor) for each major provisioning technology
:License: - |morpheus| appliances now allow stacking licenses. When stacked, the cumulative total of license privileges are allowed
:Nutanix Prism Central: - Added support for Nutanix Prism Central VMM GA v4.0 API. See the VMM API VERSION dropdown list when adding or editing Nutanix Prism Central Clouds
:Nutanix Prism Element: - Embedded Nutanix Prism Element Cloud type has been removed, Nutanix Prism Element plugin added to embedded plugins.
:OneLogin: - OneLogin integrations now support global proxies if they are configured
:Oracle Cloud: - Added sort logic to the Regions dropdown list when adding or editing Oracle Clouds
                - Added support for EU sovereign regions for Oracle Cloud
:Plugins: - Improved appliance cleanup when plugins are removed
:Roles: - Added feature Role permission "Infrastructure: Server Software" which controls access to the Software tab on the server detail page. This tab shows installed software on the server
:UI: - Added a live history and process widget to the UI. Click the list icon in the top menu bar (to the left of the bell icon and the right of the global search bar). The live progress of certain processes (ex. Instance provisioning) is shown
             - The links in the support menu dropdown are now customizable via ``morpheus.rb`` file configuration. See docs section on ``morpheus.rb`` configuration for details


Fixes
=====

:API & CLI: - API calls to resize no longer require "Reconfigure: Disk Change Type" permission when the resize doesn't affect storage
             - Adding a network via |morpheus| API now always results in a prompt to select a Network Domain
             - Fixed Inventory Options flags not being returned in GET calls for Clouds of certain Cloud types
             - When a Cloud is added in the |mastertenant| and Resource Pools or folders are privately assigned to different Tenants, a Subtenant API can no longer be used to view all Resource Pools and/or folders
             - When updating NSX network firewall rules via |morpheus| API, the response is now improved to clarify when the user has been successful and when an improper update payload was sent
:Amazon: - Fixed AWS pricing calculations using "i01" disk pricing regardless of the selected storage type
:Azure: - Added Azure backup logic changes to improve stability and consistency of scheduled backups and error recovery
         - Fixed an issue that caused storage costs to be calculated based on ``Azure - Premium Managed Disk/P1 (Units) (Locally Redundant) (US East)`` disk type regardless of the type selected
         - Fixed non-ASCII UTF8 characters in tags causing provision failures
:Backups: - When deleting an Instance and opting to preserve the backups, |morpheus| no longer attempts to take new backups (which fail) on the scheduled backup job interval
:Clone: - Cloud-init configuration files removed prior to taking a snapshot to clone are now restored on the source VM after the clone is complete
:Clouds: - The "No Proxy" and "Bypass proxy for appliance URL" configurations on the Cloud now affect |morpheus| Agent installations on running VMs
:Costing: - Synced up logic for cost projections on Cloud detail pages and cost projections on invoices to bring them into closer alignment
           - Updated data types for certain database fields related to costing to prevent "out of range" scenarios
:Data Stores: - The "Default" and "Image Target" configurations are now available for Data Stores in environments which have only one Tenant
:Docker: - Added an "ENTRYPOINT" and "COMMAND EXTRAS" configuration to the built-in Docker Instance Type provisioning wizard
:HPE VM: - Fixed an issue with restarting VMs if snapshots were deleted prior to attempting restart
          - Improved Snapshot handling when VMs were not running
          - Improved handling of configured proxy information in the HPE VM installer
          - When resizing HPE VM Instances which change disk size or remove a disk, the user is warned that existing snapshots will be purged and, if accepted, all existing snapshots are purged
:Huawei Cloud: - Huawei network integrations are no longer seen by Tenant users if the Cloud has not been shared with the Tenant
:Instances: - Fixed a situation where disk labels could be duplicated under certain conditions when disks were removed and added via reconfigures
             - Fixed an issue that could cause the Policy-based Instance name or hostname to be used rather than the user's manual override of the Policy name under certain scenarios
             - On Instance resize, the user who triggers the resize is credited in Instance history with all processes associated, even those resulting from Provisioning Workflow Tasks set by a different user
:Kubernetes: - Fixed an issue caused when a worker was added to an MKS cluster and storage was modified simultaneously
              - Fixed an issue that prevented deleting failed EKS clusters when they had a space (" ") in the name
              - Upgrading the Kubernetes version on MKS clusters no longer results in running Instances being restarted
:License: - Fixed an issue that caused workloads using provisioning technologies other than HPE VM Clusters not to count correctly against license limits
:NSX: - Updating NSX segment-type networks from a Cloud page no longer throws an exception
:Network: - Fixed an issue that caused orphaned network records in |morpheus| if the network was deleted from vCenter during a |morpheus| Cloud sync
           - When changing the network selection at provision time, the DHCP/pool/static selection now resets
:Nutanix Prism Central: - Fixed Instance name sanitation that was more aggressive than necessary
:Nutanix Prism Element: - Fixed hypervisor console connections for workloads running on Nutanix Prism Element Clouds
:OpenStack: - When the OpenStack Cloud integration service account is changed, added validation and logic to confirm only Projects accessible to the new user are selectable and any old tokens are purged
:Policies: - Added cleanup logic so Instances denied provisioning approval will eventually be deleted to free up the license space they are consuming
            - Fixed automatic power on configuration overriding delayed delete policies preventing the policy from ever deleting workloads
:Reports: - Fixed a potential mismatch between the number of report types listed on the Reports page and the actual number of report types available
:Roles: - Fixed a scenario where a newly created Role with default access levels for some constructs set to NONE could have them elevated to FULL following a restart
         - Fixed incorrect access to the Tools menu when certain specific and limited access was given to Tools components
:Storage: - Moved Azure Buckets under the File Shares tab to reflect how the same storage construct is represented in the Azure web UI
:Tasks: - Powershell Tasks run against VMware Instances without |morpheus| Agent installed will now default to using ``guestTools`` for execution
         - Users without permissions to decrypt Cypher values can no longer run Tasks utilizing the ``<%=cypher.read%>`` function
:Terraform: - Added multiple fixes related to VM deployment with Terraform
:Users: - Fixed 500 errors being thrown when enabling a User which is also part of a User Group
:VMware: - Added improved keymap handling for VMware hypervisor console for German, UK (PC), and Italian layouts for both Windows and Linux servers
:Whitelabel: - PNG files with the file extension in all capital letters (ex. ``file.PNG``) can now be uploaded successfully
:vCloud Director: - Enabled VNC keyboard mappings for console connections to workloads running on vCD Clouds


Appliance & Agent Updates
=========================

:Embedded Plugins: - Added support for AurbaCX network plugin. See `integration guide <https://docs.morpheusdata.com/en/8.0.4/integration_guides/Networking/hpe_arubacx.html>`_ for setup details and use cases
          - Added support for HPE Alletra MP storage plugin. See `integration guide <https://docs.morpheusdata.com/en/8.0.4/integration_guides/storage/hpe-alletra-mp.html>`_ for setup details and use cases
          - Nutanix Prism Element plugin v1.0.1 added to embedded plugins.
