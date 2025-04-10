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

:API & CLI: - Added API endpoints to support compute device passthrough from hosts to HPE VM workloads
:Azure: - When restoring Azure backups, added storage account selection to select the staging location (datastore) in the same way as the Azure portal itself allows
:HPE VM: - Added GPU passthrough support with pooling. Any detached GPU is considered available to the pool. A Service Plan designates whether a workload needs a GPU and removing the VM will release the GPU
          - Added passthrough support for PCI and NVME devices from hypervisor hosts to HPE VM workloads. Added devices tab at the host and VM levels to support this feature. Devices are managed through the Actions menu for each device within the host devices tab
          - Added passthrough support for USB devices. USB devices can be viewed from the devices tab on the host detail. Devices can be detached from the host and attached to VMs. Devices are then viewable from the VM devices tab
          - Added the ability to mount a ``cdrom`` ISO by reconfiguring the Instance and adding a "CD ROM" type disk. The disk image can be selected from an ISO-type Virtual Images currently managed by |morpheus|
          - HPE VM Cluster Layout version 1.2 is now out of beta and into general availability
          - HPE VM Clusters can now be deployed through Distributed Workers without |morpheus| having direct SSH access to the hypervisor hosts
          - When reverting to a snapshot, any child snapshots of the selected one are kept rather than being deleted
:Integrations: - Added an integrations section at |AdmInt| so administrators can manage plugins and distributed workers associated with |morpheus|
:Kubernetes: - Added the capability to put MKS worker nodes into maintenance mode. Maintenance mode makes the node unschedulable and all running pods that can be moved elsewhere will be moved. Once out of maintenance mode, the node becomes schedulable again
              - Requests to put MKS Clusters into maintenance mode (feature added with this release) can be handled through |morpheus| API
              - When upgrading a Kubernetes Cluster, the packages associated with the new Cluster Layout are being installed and the upgrade history has been made clearer in the UI
:Plugins: - Backup plugins can now be designed with the option to restore to a current Instance or restore to a new Instance
:Security: - Added security enhancements to resolve potential known security vulnerabilities
:Settings: - The selection of Dashboards to display in the global settings section is now a typeahead field with a browse button rather than just a typeahead field
:Terraform: - The |morpheus| Terraform provider now offers MKS support for Cluster provisioning, Cluster resizing, and for adding/removing workers
:UI: - The global processes dropdown in the main menu bar (next to the global search field) now always shows the five most recent processes rather than automatically dismissing any inactive processes


Fixes
=====

:API & CLI: - Cloning HPE VM cluster Instances from |morpheus| API no longer fails when the Instance has ``cdrom``
             - Enabled workflow selection when provisioning Clusters via |morpheus| API
             - Fixed 500 errors thrown under certain conditions when adding a Cluster worker via |morpheus| API
:Azure: - Fixed Availability Zone detection for discovered Azure VMs which was preventing snapshot and restore functionality if the VM was converted to managed
         - Fixed Cloud sync errors related to Security Group syncing
         - When Instance tags are updated in the Azure portal, they are now picked up on the next Cloud sync without having to perform some other action to cause them to be picked up
:Clusters: - Fixed the storage tab of the cluster detail page to prevent orphaned disk volume records from accumulating
:Console: - Caps lock detection is now supported for VMware hypervisor console sessions
           - ``ctrl + c`` and ``ctrl + z`` keyboard shortcuts now work for latin-based keymaps
:HPE VM: - Fixed a bug that caused VMs stopped for an extended period to be removed from hypervisor hosts
:Instances: - Converting to managed multiple times in very quick succession (such as via automated means) can no longer create multiple Instances from a brownfield VM
:Kubernetes: - Persistent volumes are now deleted from clusters as expected in both the cluster and in the |morpheus| UI even when an associated PVC does not exist
:Nutanix Prism Central: - Fixed ISO mounts not being ejected after finalizing deployments under certain conditions
:OpenStack: - Improved cleanup of temporary snapshot volumes
:Rubrik: - Added proxy support for the Rubrik plugin
:Terraform: - Fixed Terraform App provisioning failures which could surface under specific configuration conditions


Appliance & Agent Updates
=========================

:Appliance: - Elasticsearch upgraded to v8.15.5
            - Guacamole reverted to v1.2.0 due to high cpu thread issue with v1.6.0
            - Java updated to v17.0.14+7
            - RabbitMQ upgraded to v3.13.7
            - Tomcat upgraded to v9.0.102
            - Ubuntu 24.04 now supported for Appliance OS


:Agent & Node Packages: - :morpheus: Linux Agent updated to v2.9.5
                        - : Node and VM node packages update to v3.2.35 with v2.9.5 Linux Agent

:Embedded Plugins: - Rubrik plugin updated to v2.0.1
                   - Digital Ocean plugin updated to v1.4.3
                   - xpc-ng (xenserver) plugin updated to v1.1.5
                   - Nutanix Prism Element updated to v1.0.2