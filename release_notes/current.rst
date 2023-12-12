.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. IMPORTANT:: Minimum v6.x required to upgrade to v6.0.7+ for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6 prior to upgrading to v6.0.7+
.. IMPORTANT:: v6.0.7+ contains embedded MySQL v8 upgrade. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances) and upgrading from v6.0.0 - v6.0.6.
.. WARNING:: Rolling upgrades for HA environments using embedded RabbitMQ and/or embedded Elasticsearch services are not supported when upgrading from v6.0.0 - v6.0.6.

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - Added the ability to configure ServiceNow integrations to use table-based CMDB mode rather than the newer IRE via |morpheus| API and CLI. This configuration was added previously to |morpheus| UI :superscript:` 6.2.5 6.3.2`
:Currency: - Added support for Botswanan Pula (BWP) currency :superscript:` 6.2.5 6.3.1`
:Dashboard: - Added localization to the upgraded dashboard (now a plugin) which was added to the product in 6.0.0 :superscript:` 6.2.5 6.3.2`
:Hyper-V: - Added support for Hyper-V Gen 2 virtual machines :superscript:` 6.2.5 6.3.2`
:Kubernetes: - The ``default-docker-secret`` value as stored in ``etcd`` for MKS Kubernetes 1.28+ clusters is now encrypted :superscript:` 6.2.5 6.3.2`
:Network: - Using the search function on the Domains list page now searches on the Domain Name and Description fields in addition to the Domain field that was searched previously :superscript:` 6.2.5 6.3.2`
:OpenStack: - When provisioning an Instance, App, or Cluster to an all-Projects OpenStack Cloud, the Security Group dropdown options are being filtered properly to the selected Resource Pool :superscript:` 6.2.5 6.3.2`
:Security: - Embedded ``curl`` upgraded to 8.4.0 to mitigate CVEs associated with the prior installed version :superscript:`6.2.5 6.3.2 `
            - Upgraded ``netty-all`` to 4.1.77.Final to mitigate CVE-2022-24823 :superscript:` 6.2.5 6.3.2`


Fixes
=====

:API & CLI: - Fixed returned IPv6 address value changing with each subsequent call to GET an Instance which has a single network interface which has a single IPv4 and IPv6 address :superscript:` 6.2.5 6.3.2`
             - GET calls for a specific Service Plan which include the parameter to get the Zones array (?includeZones=true) will now include the Zones array in the response :superscript:` 6.2.5 6.3.2`
             - When adding a new volume to an Instance via |morpheus| API, an inaccurate message about a network adapter being removed from the instance is no longer added to History :superscript:` 6.2.5 6.3.2`
:Apps: - Fixed a bug which could cause the App provisioning wizard to hang indefinitely on an infinite loop associated with Instance Naming Policy conflicts :superscript:` 6.2.5 6.3.2`
:Azure: - Improved Azure price and plan sync logic to improve sync times and make more efficient use of memory :superscript:` 6.2.5 6.3.2`
:F5: - Fixed the "Persistence" configuration not being selectable from the Instance provisioning wizard for F5 load balancers shared down to Subtenants :superscript:` 6.2.5 6.3.2`
:Google Cloud (GCP): - |morpheus| is now detecting and displaying the OS type (Linux or Windows) for discovered GCP workloads :superscript:` 6.2.5 6.3.2`
:IPAM: - IPv6 pools can now be deleted even if they're referenced by existing workloads :superscript:` 6.2.5 6.3.2`
        - When creating a record in a |morpheus|-type IPv6 pool and manually specifying the IP address, |morpheus| will now honor the entered address rather than using the next available address in the pool instead :superscript:` 6.2.5 6.3.2`
:Instances: - Domain selections on the Instance provisioning wizard now properly override domains set on the Cloud or Network configuration :superscript:` 6.2.5 6.3.2`
             - Fixed disabled Instance action buttons (start, stop, restart service) from working on the Instance list page :superscript:` 6.2.5 6.3.2`
             - In Instance History after rebooting an Instance, the name of the user who initiated the reboot is shown in the history entry rather than the name of the Instance owner :superscript:` 6.2.5 6.3.2`
             - The History tab of Instance and Server detail pages will now list the User which has performed various actions rather than listing the owner of the workload :superscript:` 6.2.5 6.3.2`
:Integrations: - Fixed the logic that controlled the sync interval for integrations which could sometimes compute an incorrect time for next sync :superscript:` 6.2.5 6.3.2`
:Kubernetes: - Addresses IPv6 pools can now be used with Kubernetes Cluster deployments. Previously IPv6 flags were ignored and an IPv4 address was used in its place :superscript:` 6.2.5 6.3.2`
              - Cleaned up a few UI-related bugs associated with the Create Kubernetes Cluster wizard :superscript:`6.2.5 6.3.2 `
:Layouts: - Fixed issues related to filtering and displaying Workflows in the dropdown menu when adding or editing Layouts :superscript:` 6.2.5 6.3.2`
:Library: - When adding or editing Instance Types, Layouts, or Node Types and including more than one Environment Variable, the flyout OPTIONS menu for setting "Masked" or "Exportable" attributes on EVars now works correctly on EVars beyond the first one :superscript:` 6.2.5 6.3.2`
:Morpheus IP Pools: - Fixed an issue with IP Pools which could cause the number of IP addresses in the pool to be computed incorrectly :superscript:` 6.2.5 6.3.2`
:Network: - Gateway and DNS server information are now set properly when linked to an external pool type for IPv6 networks :superscript:` 6.2.5 6.3.2`
           - The VCD Edge network routers are now scoping the firewall rule groups on the router detail page Firewall Groups tab to the selected Edge routers rather than showing all :superscript:` 6.2.5 6.3.2`
           - When creating a new Network and setting the Network Service from the dropdown, |morpheus| will no longer revert the selection back to the first one if you attempt to change the value prior to saving the new Network :superscript:` 6.2.5 6.3.2`
:OpenStack: - Creating Security Groups within project-scoped and all project-scoped OpenStack Clouds is now working properly :superscript:` 6.2.5 6.3.2`
:Policies: - Instances which are deleted but subject to a Delete Approval Policy and which also have an Always-On Power Schedule will no longer revert immediately from a Pending Delete state to a Running state once again :superscript:` 6.2.5 6.3.2`
:SCVMM: - Fixed an issue that caused the Plan for provisioned SCVMM Instances to revert after the next Cloud sync :superscript:` 6.2.5 6.3.1`
:Security: - Access tokens are now encrypted in the |morpheus| database for security purposes :superscript:` 6.2.5 6.3.1`
            - Attempting to access Integrations which are owned by other Tenants by modifying a URL to include an updated Integration ID will now trigger a 404 error rather than a 500 error :superscript:` 6.2.5 6.3.2`
            - For security reasons, 2FA authentication tokens can now only be used once rather than potentially being used multiple times within their expiration window :superscript:` 6.2.5 6.3.2`
             - The first and last names columns on the Users database table are no longer encrypted. This is reverting a recent change that encrypted these values due to some unforeseen downstream issues this caused :superscript:` 6.2.5 6.3.2`
            - TRACE HTTP method set to false in embedded Tomcat config :superscript:`6.2.5 6.3.2 `
:Tags: - Additional sql optimizations for nightly duplicate and orphaned metadata tag cleanup job :superscript:`6.2.5 6.3.2 `
:Tenants: - Having created and run a Task in a Tenant will no longer prevent it from being deleted :superscript:` 6.2.5 6.3.2`
           - Tenants which contain Azure networks which have subnets are no longer prevented from being deleted for that reason :superscript:` 6.2.5 6.3.2`
           - Tenants which have associated storage volumes are no longer prevented from being deleted for that reason :superscript:` 6.2.5 6.3.2`
           - Tenants which have integrated GCP Clouds and synced in Virtual Images from them are no longer prevented from being deleted for this reason :superscript:` 6.2.5 6.3.2`
:VMware: - Added additional protection against orphaned storage controllers and other constructs from failed VM discoveries filling up the database over time :superscript:` 6.2.5 6.3.2`
          - Adding more than 14 disks to VMware nodes as well as adding additional SCSI controllers and applying them to the additional volumes is now working properly :superscript:` 6.2.5 6.3.2`
          - For discovered VMs, |morpheus| now displays the IP address for the primary NIC when multiple are present where previously it was inconsistent :superscript:` 6.2.5 6.3.2`
          - When a VMware Instance fails provisioning in |morpheus| and is subsequently deleted, |morpheus| now also will removed the failed workloads from VMware :superscript:` 6.2.5 6.3.2`
:Workflows: - Having a Restart Task in a Provisioning Workflow will no longer cause the Instance status to become green (successful provision, completed state) before all Provisioning Workflow Tasks are completed :superscript:` 6.2.5 6.3.2`
:phpIPAM: - Editing names and IP addresses in phpIPAM now syncs properly in |morpheus| :superscript:` 6.2.5 6.3.2`
           - Improved logic for computing used and available addresses in phpIPAM IP Pools which could sometimes be computed slightly incorrectly :superscript:` 6.2.5 6.3.2`
           - |morpheus| now gracefully handles the deletion of phpIPAM subnets from the phpIPAM side when Instances have already been provisioned from |morpheus| using addresses from that pool. Previously integration sync errors would surface :superscript:` 6.2.5 6.3.2`


Appliance & Agent Updates
=========================

:Appliance: - Embedded ElasticSearch upgraded to 8.11.2 :superscript:`6.2.5 6.3.2 `
             - Embedded MySQL upgraded to 8.0.35 :superscript:`6.2.5 6.3.2 `
             - Embedded RabbitMQ upgraded to 3.12.9 :superscript:`6.2.5 6.3.2 `
             - Fixed |morpheus| appliance reconfigures failing on Ubuntu-based appliances when ``iptables-persistent`` package is installed and configured in certain ways :superscript:` 6.2.5 6.3.2`

Embedded Plugins
================

:BigIP: BigIP plugin updated to v1.1.1
:Dashboard: Morpheus Home Dashboard plugin updated to v1.0.5
:phpIPAM: phpIPAM plugin updated to v1.1.2
