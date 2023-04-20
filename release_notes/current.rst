.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. WARNING:: Rolling upgrades to |morphver| from |morpheus| version 6.0.1 or lower are not supported for HA environments.

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|

.. IMPORTANT:: In |morpheus| |morphver|, many third party integrations have been moved out of the core installer package and converted to |morpheus| plugins. As a result, during the upgrade process your appliance will need to be able to access share.morpheusdata.com, the online repository for all |morpheus| plugins. Where this is not possible, users may instead apply the supplemental installer package which is also available at |morpheus| Hub alongside the main installer package.

.. IMPORTANT:: NSX-V support is deprecated though still supported as of |morpheus| 6.0.0. It will be removed and unsupported in 6.1.1 and higher.

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - NSX-T integrations can now be refreshed manually through |morpheus| API/CLI calls :superscript:`6.0.2`
:Currency: - Vietnamese Dong (VND) currency is now supported :superscript:`6.0.2`
:Forms: - Added Form builder for creating Input forms for Catalog Items. See `Forms documentation <https://docs.morpheusdata.com/en/latest/library/options/options.html#forms>`_ for complete details on using Forms
:Installer: - MySQL upgraded to 5.7.42
:Logs: - When logs are disabled, the flow of logs back to the appliance is now stopped. Previously they were still sent but not retained :superscript:`6.0.2`
:Plans & Pricing: - Added the ability to set a cores per socket range on VMware-type Service Plans :superscript:`6.0.2`
:Policies: - Added Max VM Snapshot Policies to allow users to limit the number of stored snapshots per VM which allows greater control over storage :superscript:`6.0.2`
            - Max Policies (Max Cores, Storage, and Memory) now include the option to include or exclude container resources in the Policy :superscript:`6.0.2`
:ServiceNow: - Refactored API calls to ServiceNow which provide integration functionality within |morpheus|. This results in greater fault prevention and some performance improvements :superscript:`6.0.2`


Fixes
=====

:API & CLI: - Duplicate or missing members are no longer present when creating NSX-T groups with VM members via |morpheus| API :superscript:`6.0.2`
             - Provisioning an App through the CLI ``apps add`` call now works properly even when no user groups are defined :superscript:`6.0.2`
             - The Tenants block containing details on the Tenants to which a load balancer is applied are now returned in the payload for load balancer GET requests :superscript:`6.0.2`
             - The ``catalog add --payloads`` command is now properly iterating through all files of a particular syntax, or the entire folder
:Ansible: - Fixed an issue that prevented setting the default branch for an Ansible integration to anything other than "master" :superscript:`6.0.2`
:Azure: - Fixed an issue that caused power status to become unknown when an Azure Cloud is scoped to region and resource group :superscript:`6.0.2`
:Google Cloud (GCP): - Fixed an issue that prevented GCP costing sync when a project name contained "-1" :superscript:`6.0.2`
:Instances: - Fixed an issue that caused failures when adding nodes to brownfield Instances which were converted to managed :superscript:`6.0.2`
:Kubernetes: - Namespaces under the Access tab on a Kubernetes cluster detail page are now paginated correctly when more than 25 namespaces are present :superscript:`6.0.2`
:Load Balancers: - Fixed an issue with SSL Client Profile and SSL Server Profile selections for NSX-T load balancers in Instance, App, Blueprint, clone and restore wizards :superscript:`6.0.2`
:MicrosoftDNS: - Fixed an issue that caused the Microsoft DNS plugin integration to stop refreshing in some circumstances :superscript:`6.0.2`
:NSX-T: - Fixed ``AbstractNetworkService EntityNotFoundException`` errors related to NSX-T networks
         - Refreshing the NSX-T network service will no longer cause the database IDs for any recently-created firewall rules or groups to change :superscript:`6.0.2`
         - When attempting to save an NSX-T segment with errors, normal UI validation and error messages are surfaced rather than throwing a 500 error :superscript:`6.0.2`
:Policies: - Fixed an issue that could cause the number of workload cores to be evaluated incorrectly which could lead to false triggering of a Max Cores-type Policy :superscript:`6.0.2`
:Security: - grails-spring upgraded to 5.3.2 and micronaut-spring upgraded to 4.5.0 to mitigate CVE-2022-22965 :superscript:`6.0.2`
:VMware: - Fixed an issue that caused Kubernetes Masters and Workers to be assigned to incorrect Resource Pools when provisioned to Clouds with multiple Resource pools :superscript:`6.0.2`
          - When |morpheus| Agent is not installed on VMware workloads and the Cloud RPC Mode is set to VMware Tools, Shell Tasks and Powershell Tasks will be run via VMware Tools. When RPC Mode is set to SSH/WinRM, VMware Tools is not used :superscript:`6.0.2`


Appliance & Agent Updates
=========================

:Appliance: - Added RELOAD privilege to morpheus mysql user for backup execution :superscript:`6.0.2`
            - mysql version updated to 5.7.42
