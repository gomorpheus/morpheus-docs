.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|

.. IMPORTANT:: In |morpheus| |morphver|, many third party integrations have been moved out of the core installer package and converted to |morpheus| plugins. As a result, during the upgrade process your appliance will need to be able to access share.morpheusdata.com, the online repository for all |morpheus| plugins. Where this is not possible, users may instead apply the supplemental installer package which is also available at |morpheus| Hub alongside the main installer package.

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - NSX-T integrations can now be refreshed manually through |morpheus| API/CLI calls :superscript:`6.1.0`
:Currency: - Vietnamese Dong (VND) currency is now supported :superscript:`6.1.0`
:Logs: - When logs are disabled, the flow of logs back to the appliance is now stopped. Previously they were still sent but not retained
:Plans & Pricing: - Added the ability to set a cores per socket range on VMware-type Service Plans :superscript:`6.1.0`
:Policies: - Added Max VM Snapshot Policies to allow users to limit the number of stored snapshots per VM which allows greater control over storage :superscript:`6.1.0`
            - Max Policies (Max Cores, Storage, and Memory) now include the option to include or exclude container resources in the Policy :superscript:`6.1.0`
:ServiceNow: - Refactored API calls to ServiceNow which provide integration functionality within |morpheus|. This results in greater fault prevention and some performance improvements :superscript:`6.1.0`


Fixes
=====

:API & CLI: - Duplicate or missing members are no longer present when creating NSX-T groups with VM members via |morpheus| API :superscript:`6.1.0`
            - Provisioning an App through the CLI ``apps add`` call now works properly even when no user groups are defined :superscript:`6.1.0`
            - The Tenants block containing details on the Tenants to which a load balancer is applied are now returned in the payload for load balancer GET requests :superscript:`6.1.0`
:Ansible: - Default Branch value is now being validated again when adding or editing an Ansible integration
          - Fixed an issue that prevented setting the default branch for an Ansible integration to anything other than "master" :superscript:`6.1.0`
:Azure: - Fixed an issue that caused power status to become unknown when an Azure Cloud is scoped to region and resource group :superscript:`6.1.0`
        - Fixed refresh of the service plans available in the provisioning wizard when a new resource pool is selected
:Google Cloud (GCP): - Fixed an issue that prevented GCP costing sync when a project name contained "-1" :superscript:`6.1.0`
:Infoblox: - Fixed an issue that caused IP reservation failure when the default DNS view did not exist in the Infoblox environment
:Instances: - Fixed an issue that caused failures when adding nodes to brownfield Instances which were converted to managed :superscript:`6.1.0`
:Kubernetes: - Namespaces under the Access tab on a Kubernetes cluster detail page are now paginated correctly when more than 25 namespaces are present :superscript:`6.1.0`
:Load Balancers: - Fixed an issue with SSL Client Profile and SSL Server Profile selections for NSX-T load balancers in Instance, App, Blueprint, clone and restore wizards :superscript:`6.1.0`
:MicrosoftDNS: - Fixed an issue that caused the Microsoft DNS plugin integration to stop refreshing in some circumstances :superscript:`6.1.0`
:NSX-T: - Refreshing the NSX-T network service will no longer cause the database IDs for any recently-created firewall rules or groups to change :superscript:`6.1.0`
        - When attempting to save an NSX-T segment with errors, normal UI validation and error messages are surfaced rather than throwing a 500 error :superscript:`6.1.0`
:Policies: - Fixed an issue that could cause the number of workload cores to be evaluated incorrectly which could lead to false triggering of a Max Cores-type Policy :superscript:`6.1.0`
:Security: - grails-spring upgraded to 5.3.2 and micronaut-spring upgraded to 4.5.0 to mitigate CVE-2022-22965 :superscript:`6.1.0`
:ServiceNow: - Fixed an issue that caused the ServiceNow plugin to incorrectly read the version number from the target |morpheus| appliance
:Tasks: - Fixed creating Cyphers with Groovy Script and shell tasks
:VMware: - Fixed an issue that caused Kubernetes Masters and Workers to be assigned to incorrect Resource Pools when provisioned to Clouds with multiple Resource pools :superscript:`6.1.0`
         - When |morpheus| Agent is not installed on VMware workloads and the Cloud RPC Mode is set to VMware Tools, Shell Tasks and Powershell Tasks will be run via VMware Tools. When RPC Mode is set to SSH/WinRM, VMware Tools is not used


Appliance & Agent Updates
=========================

:Appliance: - Added RELOAD privilege to |morpheus| mysql user for 5.7.41 backup execution :superscript:`6.1.0`
            - Fixed sysctl error during |morpheus| Appliance Installations on CentOS 9 :superscript:`6.1.0`
:Node & VM Node Packages: -  |morpheus| Node & VM Node Packages updated to v3.2.12 with new |morpheus| Linux Agent v2.4.0 :superscript:`6.1.0`
:Agents: - Agents updated with ability to disable log forwarding when log aggregation is disabled on |morpheus| Appliance :superscript:`6.1.0`
- |morpheus| Linux Agent updated to v2.4.0 with log setting update :superscript:`6.1.0`
- |morpheus| Windows Agent updated to v2.4.0 with log setting update :superscript:`6.1.0`