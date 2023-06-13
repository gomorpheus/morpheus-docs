.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. WARNING:: |morpheus| |morphver| only supports rolling upgrades for HA environments when upgrading from v6.0.2+.

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|

.. IMPORTANT:: In |morpheus| |morphver|, many third party integrations have been moved out of the core installer package and converted to |morpheus| plugins. As a result, during the upgrade process your appliance will need to be able to access share.morpheusdata.com, the online repository for all |morpheus| plugins. Where this is not possible, users may instead apply the supplemental installer package which is also available at |morpheus| Hub alongside the main installer package.

.. IMPORTANT:: NSX-V support is deprecated though still supported as of |morpheus| 6.0.0. It will be removed and unsupported in 6.1.1 and higher.

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - Both Instance name and Instance display name can be updated via |morpheus| API and CLI :superscript:`6.1.2`
             - Removed ``/api/doc`` endpoint from |morpheus| API and ``doc`` command from |morpheus| CLI :superscript:`6.1.2`
             - The load-balancer-pools get, update, and remove CLI commands are now working properly for NSX-t pools, load balancers, integrations, and clouds private to a sub-tenant :superscript:`6.1.2`
:Clouds: - When deleting Clouds and removing associated infrastructure, updated the warning text to more clearly convey exactly what will be deleted :superscript:`6.1.2`
:Currency: - Added support for Mongolian Tugriks (MNT) currency :superscript:`6.1.2`
:Installer: - Added morpheus.rb entries which allow users to add additional configuration to the morpheus and morpheus-ssl nginx server blocks
:MicrosoftDNS: - Updated MicrosoftDNS plugin to improve validation and standardize Powershell script blocks and error handling. Upgrade can be downloaded from share.morpheusdata.com :superscript:`6.1.2`
:Personas: - Added the Support menu to the upper menu area for all Personas rather than just having it on the Standard Persona :superscript:`6.1.2`
:Plugins: - Additional improvements made to the Nutanix Prism Central plugin. Access the latest version at share.morpheusdata.com
           - The DigitalOcean Cloud type has been ported to a plugin. Appliances which have DO Clouds integrated will automatically have the plugin installed on upgrade. Others may access the plugin from share.morpheusdata.com if they wish to use this Cloud type
:Security: - JDK/JRE upgraded to version 11.0.19+7 (resolves CVE-2023-21930) :superscript:`6.1.1`
            - Upgraded Apache Mina SSHD to 2.9.2 to mitigate CVE-2022-45047 :superscript:`6.1.2`
            - Upgraded Jettison to 1.5.4 to mitigate CVE-2022-45693 :superscript:`6.1.2`
            - Upgraded Tomcat to 9.0.74 to mitigate CVE-2023-24998 and CVE-2023-28709 :superscript:`6.1.2`
            - Upgraded Tomcat-embed-core to version 9.0.62 to mitigate CVE-2021-43980 :superscript:`6.1.2`
            - Upgraded Xstream/woodstox to 6.4.0 to mitigate CVE-2022-40152 :superscript:`6.1.2`
            - Upgraded cxf-core to version 3.4.10 to mitigate CVE-2022-46364 :superscript:`6.1.2`
            - Upgraded h3database to 2.1.214 to mitigate CVE-2022-45868 :superscript:`6.1.2`
            - Upgraded jackson-databind to 2.14.0 to mitigate CVE-2022-42003 and CVE-2022-42004 :superscript:`6.1.2`
            - Upgraded netty-common to version 4.1.77.Final to mitigate CVE-2022-24823 :superscript:`6.1.2`
            - Upgraded snakeyaml to 1.32 to mitigate CVE-2022-25857 :superscript:`6.1.2`
:Workflows: - Added Scale Down phase for Provisioning Workflows. Tasks in this phase are run on nodes being deleted when Instances are scaled down (horizontally). This phase is invoked during both manual and automatic scale down events


Fixes
=====

:API & CLI: - It is now possible to use the instances add, blueprints add, and apps add CLI commands in a sub-tenant and use a custom instance type and layout shared from the master tenant :superscript:`6.1.2`
             - Small fixes and improvements made to bulk Role permissions changes made via |morpheus| API (equivalent to updating all permissions for a specific object type in the UI, for example, setting all Instance Types to FULL access) :superscript:`6.1.2`
:Amazon: - Updated logic for creating Cost and Usage Reports (CUR) in |morpheus| to account for changing requirements from the AWS side :superscript:`6.1.2`
          - When provisioning RDS, Security Groups and DB Subnet Groups are now filtered based on the selected VPC :superscript:`6.1.2`
:Apps: - App status is now upgraded to healthy when manually re-running (successfully) any failed provisioning Tasks which initially caused one or more of the App Instances to "fail" provisioning :superscript:`6.1.2`
:Backups: - Fixed an issue that could caused automated backup jobs to fail when Instances had a very large number of disks :superscript:`6.1.2`
:Clouds: - When Clouds are deleted and the user has opted to delete infrastructure as well, Workloads which have been associated to new Clouds (via Change Cloud action) are no longer deleted
          - When deleting Clouds with "Remove Associated Resources" left unchecked, Teardown-phase Tasks are no longer run on workloads in the Cloud :superscript:`6.1.2`
:DNS: - Fixed an issue where DNS integrations could retain association with Groups in the background after the association was removed in the UI :superscript:`6.1.2`
:Hosts: - The Info section of a Host detail page now shows the ESXi version correctly :superscript:`6.1.2`
:Instances: - Day of Week-type Schedule Thresholds set on Instances now include a timezone selector rather than defaulting to UTC :superscript:`6.1.2`
             - Fixed an error that could be thrown when editing Instances and triggering any Reconfigure-phase Tasks on the Provisioning Workflow associated with the Instance Layout :superscript:`6.1.2`
             - IP addresses for additional (non-primary) network interfaces are now surfaced into |morpheus| immediately where previously they were not surfaced until the next cloud sync :superscript:`6.1.2`
             - Instance and server detail pages now show tags in alphabetical order (by the name of the name/value pair) :superscript:`6.1.2`
             - Tasks can now be run against Instance when its owner attribute is removed or when the owning user's account is deleted leaving no owner :superscript:`6.1.2`
             - When adding a node to an Instance, the Cloud selection is now honored :superscript:`6.1.2`
:Kubernetes: - Fixed an issue that could cause MKS clusters on VMware to fail provisioning :superscript:`6.1.2`
:Layouts: - Fixed an issue that could cause errors when Layouts were edited with existing Instances already provisioned from them :superscript:`6.1.2`
           - When clicking on the OPTIONS button for environment variables when editing Layouts or Node Types, the background tab no longer shifts back to Instance Types (from either Layouts or Node Types) :superscript:`6.1.2`
:NSX-T: - Gateway Firewall Services can now be added to NSX-T routers created in Subtenants on NSX-T integrations shared from the Primary Tenant :superscript:`6.1.2`
         - The Virtual Machines tenant scoping when adding a Member Type to a NSX-t server group is now working properly :superscript:`6.1.2`
:NetScaler: - Fixed load balancer creation failing due to SSL certificate import failure
:OpenStack: - Creating an OpenStack Private Network with the DHCP Server flag unchecked in |morpheus| now properly sets the "Enable DHCP" flag on the OpenStack side :superscript:`6.1.2`
             - Fixed an issue that stopped new or edited OpenStack Clouds from saving when a primary Project was not set for the user in OpenStack :superscript:`6.1.2`
             - OpenStack Clouds scoped to all regions now sync routers correctly :superscript:`6.1.2`
             - tbc :superscript:`6.1.2`
:Policies: - Fixed how expiration Policies adjust the delete date when an extension is applied to ensure Instances cannot be deleted before the expiration date :superscript:`6.1.2`
:Roles: - Fixed an issue that caused the |ProCod| section of the UI to be inaccessible when Infrastructure: Groups permission was set to NONE :superscript:`6.1.2`
         - Fixed an issue where having FULL or READ access to Operations: Usage with no rights to Invoices or Budgets would allow the Costing menu selection to appear but the page to never load :superscript:`6.1.2`
         - When Lifecycle: Environment Variables permission is set to a level which does not allow them to be deleted, the delete button is now hidden in the UI :superscript:`6.1.2`
:SCVMM: - For SCVMM Clouds, VMs are now inventoried by Cloud, Host Group, and then Cluster to ensure a correct amount of VMs is inventoried into |morpheus| :superscript:`6.1.2`
         - Improved cleanup within SCVMM when deleting Instances and servers from |morpheus| :superscript:`6.1.1`
:ServiceNow: - Fixed an issue with the ServiceNow plugin which caused Catalog Items to be duplicated when manually deleting them from SN tables and doing no other cleanup :superscript:`6.1.2`
              - When exposing Catalog Items to ServiceNow, fixed an issue that could cause items to be duplicated in ServiceNow :superscript:`6.1.2`
:Storage: - Improved reserved storage calculation logic for CentOS VMs using LVM :superscript:`6.1.1`
:Tasks: - Fixed an issue that caused Repository-sourced Shell Script-type Tasks to fail when set to a "Local" execute target :superscript:`6.1.2`
         - Fixed an issue that caused errors running Tasks or Operational Workflows after the target Instance was removed and a new target Instance was set :superscript:`6.1.2`
:Tenants: - Tenants no longer fail to delete when they have associated Monitoring Checks or Groups :superscript:`6.1.2`
:VMware: - Cluster hosts in VMware Clouds are now synced correctly when the Cloud is scoped to a specific Resource Pool :superscript:`6.1.2`
          - It is now possible to select the SCSI x:15 mount point for a disk in the Instance wizard or Instance/host reconfigure on VMware :superscript:`6.1.2`
:Whitelabel: - Fixed intermittent issues that could cause Subtenant whitelabeling to be overridden by whitelabeling in the Primary Tenant :superscript:`6.1.2`
:Wiki: - Instance Wiki pages will now use the Instance display name first, if set, and use Instance name as a fallback when not set :superscript:`6.1.2`
:phpIPAM: - Fixed an issue that caused IPs in phpIPAM pools not to be reserved for NICs added after a reconfigure :superscript:`6.1.2`


Appliance & Agent Updates
=========================

:Appliance: - Added ``morpheus.rb`` setting to specify a ``guacd`` host :superscript:`6.1.1`
            - Added ``morpheus.rb`` settings for UI and ES xms/xmx configuration for customers experiencing high memory issues :superscript:`6.1.1`
            - Added ``morpheus.rb`` settings for (``nginx['ssl_server_include']`` and ``nginx['server_include']``). Note: These are advanced configurations. |morpheus| support will not troubleshoot configuration issues related to these advanced options.
            - JRE updated to version 11.0.19+7 :superscript:`6.1.1`
            - Tomcat updated to 9.0.74 :superscript:`6.1.2`
:Node & VM Node Packages: - Morpheus Node & VM Node Packages updated to v3.2.14 :superscript:`6.1.2`
                          - JDK/JRE updated to version 11.0.19+7 :superscript:`6.1.1`
:Agents: - Morpheus Linux Agent updated to v2.4.1 with fix for lvm stats :superscript:`6.1.1`