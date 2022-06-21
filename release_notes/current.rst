.. _Release Notes:

*************************
|morphver| Release Notes
*************************

Release Date: |releasedate|

Compatible Plugin API version: |pluginVer|

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - Refresh Clouds (Daily, Short, and Costing refresh) manually through |morpheus| API and CLI as you can currently in |morpheus| UI. :superscript:`5.5.1`
:Kubernetes: - Pod detail pages added with stats, statuses and tags plus tabs with metadata, spec, status, config, raw, events and logs. :superscript:`5.5.1`

Fixes
=====

:API & CLI: - Calls to the Instances API no longer fail to filter properly when filtering by just one label. :superscript:`5.5.1`
             - Fixed an issue causing errors when attempting to create Option Lists via |morpheus| API. :superscript:`5.5.1`
             - Fixed an issue that would clear pools if NSX-T networks were updated over |morpheus| API without a pool config in the payload. :superscript:`5.5.1`
             - The securityMode property for clouds is now an input and output parameter for surfacing the Local Firewall setting through |morpheus| API. :superscript:`5.5.1`
             - When creating users in a Tenant via |morpheus| API and passing an invalid Role ID, a warning is presented to the user rather than creating a user with the first Role in the list :superscript:`5.5.1`
             - When you pass in an offset property for a GET call to return all networks, the offset is returned as an integer in the meta block rather than a string. :superscript:`5.5.1`
:Amazon: - Fixed an issue that could prevent AWS Clouds using Assume Role from working with Security Groups under certain configurations. :superscript:`5.5.1`
:Ansible Tower: - Fixed an issue that could cause Ansible Tower integrations not to sync in all available templates. :superscript:`5.5.1`
:Ansible: - Accessing an Instance Layout version from an Ansible Task now returns the correct version value rather than "unknown". :superscript:`5.5.1`
:Apps: - Fixed an issue that could cause costs to be revealed in the provisioning wizard even when "Show Pricing" was switched off (Administration > Settings > Provisioning) :superscript:`5.5.1`
:Azure: - Added improvements to Azure Instance cost computations. :superscript:`5.5.1`
         - Fixed an issue that caused the "Assign Public IP DNS" checkbox present in Azure and Azure Stack provisioning not to work properly. :superscript:`5.5.1`
         - Improved Azure costing calculations including a fix for an issue that could duplicate line items and create incorrectly high cost figures, a fix for an issue related to computing price from cost, and a workaround for issues stemming from costs syncs that take longer than an hour and the token expires :superscript:`5.5.1`
:BIND DNS: - BIND DNS integrations can now be deleted properly when no longer needed. :superscript:`5.5.1`
            - BIND integrations can now be removed from |morpheus|. :superscript:`5.5.1`
:Backups: - Fixed an issue that caused Veeam backups to fail when backups or VMs with identical names existed in multiple Tenants. :superscript:`5.5.1`
           - Fixed the backup success widget (checks and Xs) on the backup list page (Backups > Backups) to show the results left-to-right starting with the most recent. :superscript:`5.5.1`
           - GCP backups no longer fail when uppercase characters are included in the backup name. :superscript:`5.5.1`
:Blueprints: - Fixed an issue that could cause resource pool configurations from coming unset on App Blueprints. :superscript:`5.5.1`
:CMDB: - Fixed an issue that could cause significant error traffic in the logs when Clouds with an associated CMDB went through their normal sync process. :superscript:`5.5.1`
:Catalog: - Improved validation on catalog items backed by ARM Blueprints which could allow users to provision to Groups they didn't have access to under some conditions. :superscript:`5.5.1`
           - When changing the name of an Instance provisioned from the Service Catalog Persona in the standard Persona, the new name is now reflected in the Service Catalog Persona. :superscript:`5.5.1`
:Clusters: - Inputs added to Cluster Layouts now display as expected when creating new Clusters. :superscript:`5.5.1`
:Commvault: - Commvault backups now support duplicate backup names and backups for duplicate VM names across multiple Tenants. :superscript:`5.5.1`
:Credentials: - For Option Lists that use bearer tokens, you can now remove the manually-entered token to use a |morpheus| credential set and save the Option List properly. :superscript:`5.5.1`
:Execute Schedules: - Improved validation on cron expressions when saving execute schedules to prevent saving invalid schedules. :superscript:`5.5.1`
:Identity Sources: - Advanced validation options for SAML SSO identity sources can now be edited and the changes are saved correctly. :superscript:`5.5.1`
                  - Fixed an issue that could cause authentication to fail for users going through external SSO under specific conditions. :superscript:`5.5.1`
:Infoblox: - Improved validation when adding or editing Infoblox integrations to check throttle rate, network filter, zone filter, and extra attributes. :superscript:`5.5.1`
:Inputs: - Validation is now working properly when the visibility and required status of an Input is dependent on a specific response in another Input. :superscript:`5.5.1`
:Invoices: - Fixed Invoice line items showing values in USD when other costing for the Instance is given in another currency. :superscript:`5.5.1`
:Library: - Fixed an issue that caused default catalog items for MySQL and NGINX to fail provisioning under certain configurations. :superscript:`5.5.1`
:Logs: - Fixed an issue that generated NSX-V errors in logs in each sync. :superscript:`5.5.1`
        - Fixed an issue that would cause repeated errors being raised by |morpheus| LogService. :superscript:`5.5.1`
:Monitoring: - Logs for Subtenant users are now correctly scoped not to show Monitoring-related logs from the Primary Tenant. Previously, Subtenant users could see these logs with "User" or "Full" level permissions. :superscript:`5.5.1`
              - When Monitoring Role permission is set to "User", users can now create contacts and alert rules as intended. :superscript:`5.5.1`
:Network IP Pools: - Fixed an issue that caused allocated IP addresses not to be shown correctly on the IP Pools list page. :superscript:`5.5.1`
:Nutanix: - Fixed an issue that could cause Windows Nutanix Instances to provision with the wrong time zone. :superscript:`5.5.1`
:OpenStack: - Fixed an issue that changed the device name of OpenStack Instance disks after reconfiguring the Instance to resize them. :superscript:`5.5.1`
             - Fixed an issue that could throw errors when reconfiguring OpenStack Instances to add network interfaces. :superscript:`5.5.1`
             - When an Octavia load balancer integration has been removed, |morpheus| now cleans that up rather than continuing to try syncing with the service. :superscript:`5.5.1`
             - When reconfiguring to add disks to OpenStack Instances, the new disk is now attached to the VM properly. Previously it would not be in some situations despite appearing to have worked in |morpheus| UI. :superscript:`5.5.1`
:Plans & Pricing: - Fixed issues related to provisioning dynamic service plans (custom cores, memory, etc.) under specific input scenarios. :superscript:`5.5.1`
:Policies: - Fixed an issue that caused issues extending the expiry date for workloads which were held in a delayed removal state by policy. :superscript:`5.5.1`
            - Fixed an issue that could cause Windows-based Workflows not to execute properly as part of a Workflows Policy. :superscript:`5.5.1`
:Provisioning: - Fixed an issue that caused the provisioning wizard to hang when deploying Instances based on ARM templates to Azure Clouds scoped to "All" resource groups. :superscript:`5.5.1`
:Reports: - Date ranges for cost reports can now be specified with a month selector rather than allowing freely entered date ranges as the available data only supported individual month blocks anyway. :superscript:`5.5.1`
:Roles: - The Tools menu is no longer hidden from view when the user's Role grants only access to the VDI Pools section. :superscript:`5.5.1`
:SCVMM: - Fixed an issue that could cause an incorrect host group to be selected if an SCVMM Cloud was saved while the host group select list was still being loaded in. :superscript:`5.5.1`
         - Fixed an issue that prevented SCVMM Clouds from deleting. :superscript:`5.5.1`
:Security: - Passwords entered by users as custom options when provisioning ARM blueprints as service catalog items are no longer visible in logs or Instance review summaries (they were already masked in the UI). :superscript:`5.5.1`
            - Upgraded google-oauth-client to 1.33.3 (CVE-2021-22573). :superscript:`5.5.1`
            - Upgrade Tomcat to 9.0.63 (CVE-2022-2988). :superscript:`5.5.1`
:Spec Templates: - Improved cleanup on delete of provisioned ARM spec templates which are not fully provisioned successfully. :superscript:`5.5.1`
:Tags: - Category and tag name changes are synced when they are changed in vCenter (as the tag "name" and "value", respectively, in |morpheus|) and usage records are restarted when such a change is made. :superscript:`5.5.1`
:Tasks: - Fixed an issue that caused Subtenant Tasks reading Cypher values from the Primary Tenant to fail when run from the VM context when they worked from the Instance context. :superscript:`5.5.1`
:Tenants: - Fixed an issue that prevented Tenants from being deleted if they had VMware vCenter Clouds associated with them. :superscript:`5.5.1`
:Terraform: - Fixed an issue that prevented Terraform commands which pass options to function correctly. :superscript:`5.5.1`
             - Improved teardown of deployed Terraform Spec Templates to ensure all created objects are cleaned up. :superscript:`5.5.1`
             - Terraform refresh has been adjusted to nightly rather than every 30 minutes as it could cause performance issues in some cases. :superscript:`5.5.1`
:Trust: - Fixed an issue that could cause the Add Trust Integration modal not to appear in specific scenarios involving newly-created Subtenants. :superscript:`5.5.1`
:UI: - Improved truncation of very long values (Instance name, Group name, etc) in the Info section of Instance detail pages. :superscript:`5.5.1`
:Usage: - Fixed an issue that caused additional locations to be added for Virtual Images when Instances were provisioned from them. :superscript:`5.5.1`
         - Usage records are now visible from the Subtenant when a workload has been created in the Primary Tenant and shared with the Subtenant. :superscript:`5.5.1`
:VMware: - Fixed an issue that could cause the PROPAGATE PERMISSIONS TO CHILD OBJECTS? option for VMware folders not to work correctly. :superscript:`5.5.1`
:Workflows: - Primary Tenant users can no longer retrieve configuration for Workflows belonging to Subtenants through |morpheus| API. :superscript:`5.5.1`
:vCloud Director: - The OS is now detected properly for Windows Server 2022 images synced from vCD. :superscript:`5.5.1`


Appliance & Agent Updates
=========================

:Appliance: - Fixed 5.4.3- to 5.4.4+ upgrade issue caused by grails access token migration failing when a tenant is disabled.. :superscript:`5.5.1`
            - Fixed an issue that triggered a SeedService warning in the logs on startup of freshly-installed appliances.
            - Tomcat upgraded to v9.0.63
:Security:  - Removed addressable-2.7.0.gem from Morpheus Node packages (CVE-2021-32740). :superscript:`5.5.1`
            - Removed bundler-1.16.6.gem from Morpheus Node packages (CVE-2016-7954, CVE-2021-43809). :superscript:`5.5.1`
            - Removed json-2.2.0.gem from Morpheus Node packages (CVE-2020-10663). :superscript:`5.5.1`
            - Removed rack-2.0.7.gem from Morpheus Node packages (CVE-2020-8184). :superscript:`5.5.1`


.. ..
