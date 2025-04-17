.. _Release Notes:

************************
|morphver| Release Notes
************************

Release Dates:

- |morphver| |releasedate|

New Features
============

:API & CLI: - Added API endpoints to support compute device passthrough from hosts to HPE VM workloads
:HPE VM: - Added GPU passthrough support with pooling. Any detached GPU is considered available to the pool. A Service Plan designates whether a workload needs a GPU and removing the VM will release the GPU
          - Added passthrough support for PCI and NVME devices from hypervisor hosts to HPE VM workloads. Added devices tab at the host and VM levels to support this feature. Devices are managed through the Actions menu for each device within the host devices tab
          - Added passthrough support for USB devices. USB devices can be viewed from the devices tab on the host detail. Devices can be detached from the host and attached to VMs. Devices are then viewable from the VM devices tab
          - Added the ability to mount a ``cdrom`` ISO by reconfiguring the Instance and adding a "CD ROM" type disk. The disk image can be selected from an ISO-type Virtual Images currently managed by |morpheus|
          - HPE VM Cluster Layout version 1.2 is now out of beta and into general availability
          - HPE VM Clusters can now be deployed through Distributed Workers without |morpheus| having direct SSH access to the hypervisor hosts
          - When reverting to a snapshot, any child snapshots of the selected one are kept rather than being deleted
:Integrations: - Added an integrations section at |AdmInt| so administrators can manage plugins and distributed workers associated with |morpheus|
:Plugins: - Backup plugins can now be designed with the option to restore to a current Instance or restore to a new Instance
:Security: - Added security enhancements to resolve potential known security vulnerabilities
:UI: - The global processes dropdown in the main menu bar (next to the global search field) now always shows the five most recent processes rather than automatically dismissing any inactive processes

Fixes
=====

:API & CLI: - Cloning HPE VM cluster Instances from |morpheus| API no longer fails when the Instance has ``cdrom``
            - Fixed 500 errors thrown under certain conditions when adding a Cluster worker via |morpheus| API
:Clusters: - Fixed the storage tab of the cluster detail page to prevent orphaned disk volume records from accumulating
:Console: - Caps lock detection is now supported for VMware hypervisor console sessions
           - ``ctrl + c`` and ``ctrl + z`` keyboard shortcuts now work for latin-based keymaps
:HPE VM: - Fixed a bug that caused VMs stopped for an extended period to be removed from hypervisor hosts
:Instances: - Converting to managed multiple times in very quick succession (such as via automated means) can no longer create multiple Instances from a brownfield VM

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

..
  Known Issues
  ============

  - **Known Issue 1 Description.** Additional description and workaround (if available) here.
  - **Known Issue 2 Description.** Additional description and workaround (if available) here.
  - **Known Issue 3 Description.** Additional description and workaround (if available) here.
