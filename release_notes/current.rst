.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. WARNING:: Rolling upgrades to |morphver| from |morpheus| version 6.0.2 or lower are not supported for HA environments.

.. WARNING:: 6.1.1 & 6.0.3 contain database datatype modifications on account_invoice and account_invoice_item that may cause long initial ui start up times while the modifications are ran in mysql for environments with over 100k invoice records.

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - Both Instance name and Instance display name can be updated via |morpheus| API and CLI :superscript:`6.0.4`
             - Removed ``/api/doc`` endpoint from |morpheus| API and ``doc`` command from |morpheus| CLI :superscript:`6.0.4`
             - The load-balancer-pools get, update, and remove CLI commands are now working properly for NSX-t pools, load balancers, integrations, and clouds private to a sub-tenant :superscript:`6.0.4`
:Clouds: - When deleting Clouds and removing associated infrastructure, updated the warning text to more clearly convey exactly what will be deleted :superscript:`6.0.4`
:Currency: - Added support for Mongolian Tugriks (MNT) currency :superscript:`6.0.4`
:Forms: - Added Text Array input type for Forms which allows the user to enter a list of values separated by a delimiter. Once entered, the values are parsed out and may be individually deleted prior to submitting the form
         - Added new ability to filter available Cloud types on Forms. Select a Cloud type from the LIMIT TO CLOUD TYPE dropdown or select FILTER FROM RESOURCE. The option to filter from resource reads the Cloud type from the Catalog Item Instance config
:Kubernetes: - Added default Kubernetes 1.27 layouts for many Clouds, including Amazon and VMware
:MicrosoftDNS: - Updated MicrosoftDNS plugin to improve validation and standardize Powershell script blocks and error handling. Upgrade can be downloaded from share.morpheusdata.com :superscript:`6.0.4`
:Personas: - Added the Support menu to the upper menu area for all Personas rather than just having it on the Standard Persona :superscript:`6.0.4`
:Security: - Upgraded Apache Mina SSHD to 2.9.2 to mitigate CVE-2022-45047 :superscript:`6.0.4`
            - Upgraded Jettison to 1.5.4 to mitigate CVE-2022-45693 :superscript:`6.0.4`
            - Upgraded Tomcat to 9.0.74 to mitigate CVE-2023-24998 and CVE-2023-28709 :superscript:`6.0.4`
            - Upgraded Tomcat to 9.0.74 to mitigate CVE-2023-24998 and CVE-2023-28709 :superscript:`6.0.4`
            - Upgraded Tomcat-embed-core to version 9.0.62 to mitigate CVE-2021-43980 :superscript:`6.0.4`
            - Upgraded Xstream/woodstox to 6.4.0 to mitigate CVE-2022-40152 :superscript:`6.0.4`
            - Upgraded cxf-core to version 3.4.10 to mitigate CVE-2022-46364 :superscript:`6.0.4`
            - Upgraded h3database to 2.1.214 to mitigate CVE-2022-45868 :superscript:`6.0.4`
            - Upgraded jackson-databind to 2.14.0 to mitigate CVE-2022-42003 and CVE-2022-42004 :superscript:`6.0.4`
            - Upgraded netty-common to version 4.1.77.Final to mitigate CVE-2022-24823 :superscript:`6.0.4`
            - Upgraded snakeyaml to 1.32 to mitigate CVE-2022-25857 :superscript:`6.0.4`


Fixes
=====

:API & CLI: - It is now possible to use the instances add, blueprints add, and apps add CLI commands in a sub-tenant and use a custom instance type and layout shared from the master tenant :superscript:`6.0.4`
             - Small fixes and improvements made to bulk Role permissions changes made via |morpheus| API (equivalent to updating all permissions for a specific object type in the UI, for example, setting all Instance Types to FULL access) :superscript:`6.0.4`
:Amazon: - Updated logic for creating Cost and Usage Reports (CUR) in |morpheus| to account for changing requirements from the AWS side :superscript:`6.0.4`
          - When provisioning RDS, Security Groups and DB Subnet Groups are now filtered based on the selected VPC :superscript:`6.0.4`
:Apps: - App status is now upgraded to healthy when manually re-running (successfully) any failed provisioning Tasks which initially caused one or more of the App Instances to "fail" provisioning :superscript:`6.0.4`
:Backups: - Fixed an issue that could caused automated backup jobs to fail when Instances had a very large number of disks :superscript:`6.0.4`
:Catalog: - Input visibility which is based on a Checkbox-type Input now works correctly on Catalog Items
:Clouds: - When deleting Clouds with "Remove Associated Resources" left unchecked, Teardown-phase Tasks are no longer run on workloads in the Cloud :superscript:`6.0.4`
:DNS: - Fixed an issue where DNS integrations could retain association with Groups in the background after the association was removed in the UI :superscript:`6.0.4`
:Hosts: - The Info section of a Host detail page now shows the ESXi version correctly :superscript:`6.0.4`
:Inputs: - Fixed an issue that prevented Inputs from being deleted if they'd been added to a Form even after the Form was deleted
:Instances: - Day of Week-type Schedule Thresholds set on Instances now include a timezone selector rather than defaulting to UTC :superscript:`6.0.4`
             - Fixed an error that could be thrown when editing Instances and triggering any Reconfigure-phase Tasks on the Provisioning Workflow associated with the Instance Layout :superscript:`6.0.4`
             - IP addresses for additional (non-primary) network interfaces are now surfaced into |morpheus| immediately where previously they were not surfaced until the next cloud sync :superscript:`6.0.4`
             - Instance and server detail pages now show tags in alphabetical order (by the name of the name/value pair) :superscript:`6.0.4`
             - Tasks can now be run against Instance when its owner attribute is removed or when the owning user's account is deleted leaving no owner :superscript:`6.0.4`
             - When adding a node to an Instance, the Cloud selection is now honored :superscript:`6.0.4`
:Kubernetes: - Fixed an issue that could cause MKS clusters on VMware to fail provisioning :superscript:`6.0.4`
:Layouts: - Fixed an issue that could cause errors when Layouts were edited with existing Instances already provisioned from them :superscript:`6.0.4`
:NSX-T: - Gateway Firewall Services can now be added to NSX-T routers created in Subtenants on NSX-T integrations shared from the Primary Tenant :superscript:`6.0.4`
         - The Virtual Machines tenant scoping when adding a Member Type to a NSX-t server group is now working properly :superscript:`6.0.4`
:OpenStack: - Creating an OpenStack Private Network with the DHCP Server flag unchecked in |morpheus| now properly sets the "Enable DHCP" flag on the OpenStack side :superscript:`6.0.4`
             - Fixed an issue that stopped new or edited OpenStack Clouds from saving when a primary Project was not set for the user in OpenStack :superscript:`6.0.4`
             - OpenStack Clouds scoped to all regions now sync routers correctly :superscript:`6.0.4`
:Policies: - Fixed how expiration Policies adjust the delete date when an extension is applied to ensure Instances cannot be deleted before the expiration date :superscript:`6.0.4`
:Provisioning: - Morpheus no longer attempts to create local users when provisioning virtual images with all configuration options (cloud-init/sysprep/vmtools etc) disabled, resolving "An Error Occurred while attempting to create linux users - null" error :superscript:`6.0.4`
:Roles: - Fixed an issue that caused the |ProCod| section of the UI to be inaccessible when Infrastructure: Groups permission was set to NONE :superscript:`6.0.4`
         - Fixed an issue where having FULL or READ access to Operations: Usage with no rights to Invoices or Budgets would allow the Costing menu selection to appear but the page to never load :superscript:`6.0.4`
         - When Lifecycle: Environment Variables permission is set to a level which does not allow them to be deleted, the delete button is now hidden in the UI :superscript:`6.0.4`
:SCVMM: - For SCVMM Clouds, VMs are now inventoried by Cloud, Host Group, and then Cluster to ensure a correct amount of VMs is inventoried into |morpheus| :superscript:`6.0.4`
:ServiceNow: - Fixed an issue with the ServiceNow plugin which caused Catalog Items to be duplicated when manually deleting them from SN tables and doing no other cleanup :superscript:`6.0.4`
              - When exposing Catalog Items to ServiceNow, fixed an issue that could cause items to be duplicated in ServiceNow :superscript:`6.0.4`
:Tasks: - Fixed an issue that caused Repository-sourced Shell Script-type Tasks to fail when set to a "Local" execute target :superscript:`6.0.4`
         - Fixed an issue that caused errors running Tasks or Operational Workflows after the target Instance was removed and a new target Instance was set :superscript:`6.0.4`
:Tenants: - Tenants no longer fail to delete when they have associated Monitoring Checks or Groups :superscript:`6.0.4`
:VMware: - Cluster hosts in VMware Clouds are now synced correctly when the Cloud is scoped to a specific Resource Pool :superscript:`6.0.4`
          - It is now possible to select the SCSI x:15 mount point for a disk in the Instance wizard or Instance/host reconfigure on VMware :superscript:`6.0.4`
:Whitelabel: - Fixed intermittent issues that could cause Subtenant whitelabeling to be overridden by whitelabeling in the Primary Tenant :superscript:`6.0.4`
:Wiki: - Instance Wiki pages will now use the Instance display name first, if set, and use Instance name as a fallback when not set :superscript:`6.0.4`
:phpIPAM: - Fixed an issue that caused IPs in phpIPAM pools not to be reserved for NICs added after a reconfigure :superscript:`6.0.4`

