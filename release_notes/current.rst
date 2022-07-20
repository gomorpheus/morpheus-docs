.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. important:: Morpheus |morphver| requires Morpheus Worker |workerVer|. Please upgrade any existing Morpheus Workers to the |workerVer| Worker package to ensure compatibility with Morpheus |morphver|.

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

.. .. include:: highlights.rst

Release Dates
  - 5.5.1-1 |releasedate|
  - 5.5.1-2 Jul 20 2022

.. toggle-header:: 
    :header: 5.5.1-2 Updates **Click to Expand/Hide**

      5.5.1-2 contains the following updates not included in 5.5.1-1:

     :Security: - CVE-2022-35912 - Grails updated to v5.1.9. Morpheus 5.4.3+ versions are not vulnerable to CVE-2022-35912. The vulnerability applies systems using java 9 and morpheus-ui 5.4.3+ uses java 11. Out of an abundance of caution we upgraded grails to v5.1.9. Customers on morpheus v5.4.2 or earlier are advised to upgrade to morpheus v5.4.3+. :superscript:`5.4.8-2`
     :Azure: - Costing: Fixed Azure costing failing when 429 too many attempts api error is encountered :superscript:`5.4.8-2`
             - Costing: Fixed Azure costing issues related to currency conversion :superscript:`5.4.8-2`
     :Inputs: - Options Types: Fixed export as tag and display value on details not working for catalog items :superscript:`5.4.8`
              - Options Types: Improved handling of api option list loading. "No options found" no longer displayed prior to api response, "Failed to load options" now displayed on empty response. :superscript:`5.4.8-2`
     :Openstack: - Reverted 5.4.8-1 update that tied Openstack IP Pool visibility to network visibility :superscript:`5.4.8-2`
     :Plugins: - Update the plugin core to handle the "show on detail" flag in seed. morpheus-plugin-api:0.12.6 :superscript:`5.4.8-2`
     :Security Groups: - Fixed maxSize constraint on security group rule destination causing sync error when destination block contains > 1000 chars :superscript:`5.4.8-2`

|

New Features
============

:API & CLI: - Create and manage Scale Thresholds (Library > Automation > Scale Thresholds) from |morpheus| API and CLI.
             - Improved prompting in |morpheus| CLI to ensure users are able to set all available options. |morpheus| API load balancer documentation improved to include examples for adding these options.
             - Kubernetes clusters can be easily upgraded through |morpheus| API and CLI as they can be in |morpheus| UI.
             - Multiple permissions can now be updated with a single call or command to |morpheus| API and CLI. Previously only one permission could be updated each time.
             - Refresh Clouds (Daily, Short, and Costing refresh) manually through |morpheus| API and CLI as you can currently in |morpheus| UI. :superscript:`5.4.7`
             - Stored credential sets can be used to authenticate integrations with third party technologies created with |morpheus| API or CLI.
             - Validation patterns (regex) for text-based (text-type and text area-type) Inputs can now be set through |morpheus| API and CLI. This can also be done through |morpheus| UI.
:AppDynamics: - Appdynamics agent removed from |morpheus| node package for security reasons.
:Blueprints: - Fixed an issue that prevented provisioning some App Blueprints from CloudFormation templates with certain AMI ID parameter formats. :superscript:`5.4.8`
:Clouds: - Updated Cloud logos which were out of date. :superscript:`5.4.8`
:Credentials: - Credentials have been expanded to integrations. Create new integrations with third party technologies and authenticate them with stored credential sets.
:Hashicorp Vault: - Hashicorp Vault plugin updated to include support for the Vault KV1 engine.
.. :Identity Sources: - .. (waiting on validation) SAML Identity Source Integrations now support "Relay State" parameters. :superscript:`5.4.7`
:Inputs: - Entries in text-based Inputs (Text-type and Text Area-type) can now be validated against a regex pattern. A UI warning is presented to the user if their input does not fit the given pattern.
:Installer: - Added support for installing |morpheus| distributed worker on Ubuntu 22.04. :superscript:`5.4.8`
:Kubernetes: - MKS Kubernetes clusters can now be easily upgraded to higher versions (ex. Kubernetes 1.20 to 1.23). The upgrade flow includes a UI warning encouraging the user to read the Kubernetes release notes and be aware of potential breaking changes.
              - Pod detail pages added with stats, statuses and tags plus tabs with metadata, spec, status, config, raw, events and logs.. :superscript:`5.4.7`
:Plans and Pricing: - Updated Plans list page (Administration > Plans & Pricing > Plans) to include custom view builds (gear icon) to add and remove data fields or sort by custom fields. :superscript:`5.4.8`
:Plugins: - The plugins API version compatible with the current version of |morpheus| is now shown on the Plugins page (Administration > Integrations > Plugins).
:Policies: - Approval Policies (Approve Provisioning and Approve Delete) now apply to Clusters whether provisioning, deleting, or adding Hosts to the Cluster.
:Roles: - Roles and Users views have been updated to include more information such as whether the Role is multitenant, its default Persona, and edit and delete buttons. The users list can also now be filtered by Roles.
:Security: - Remove gem docs from Morpheus Node package (CVE-2015-9251). :superscript:`5.4.7`
            - Upgrade google-oauth-client to 1.33.3 or above (CVE-2021-22573). :superscript:`5.4.7`
            - Upgraded addressable-2.7.0.gem to 2.8.0 or later (CVE-2021-32740). :superscript:`5.4.7`
            - Upgraded bundler-1.16.6.gem (CVE-2016-7954, CVE-2021-43809). :superscript:`5.4.7`
            - Upgraded json-2.2.0.gem to 2.3.0 or late (CVE-2020-10663). :superscript:`5.4.7`
            - Upgraded rack-2.0.7.gem to 2.1.4 either 2.2.3 (CVE-2020-8184). :superscript:`5.4.7`
:Terraform: - Added Google Compute Engine for Terraform logo which is now displayed on relevant views.
             - When executing a Terraform template for GCP, any VMs created are now mapped to |morpheus| Instances as we already do for AWS and Azure.
:VMware: - A friendly name (Display Name) can now be set on VMware resource pools, this name is displayed in the Resource Pool list for the Cloud.


Fixes
=====

:API & CLI: - Calls to the Instances API no longer fail to filter properly when filtering by just one label. :superscript:`5.4.7`
             - Fixed an issue causing errors when attempting to create Option Lists via |morpheus| API. :superscript:`5.4.7`
             - Fixed an issue that could cause port parameters not to be set when specified for Docker-based Node Types in |morpheus| API and CLI. :superscript:`5.4.8`
             - Fixed an issue that would clear pools if NSX-T networks were updated over |morpheus| API without a pool config in the payload. :superscript:`5.4.7`
             - The securityMode property for clouds is now an input and output parameter for surfacing the Local Firewall setting through |morpheus| API. :superscript:`5.4.7`
             - When creating users in a Tenant via |morpheus| API and passing an invalid Role ID, a warning is presented to the user rather than creating a user with the first Role in the list. :superscript:`5.4.7`
             - When you pass in an offset property for a GET call to return all networks, the offset is returned as an integer in the meta block rather than a string. :superscript:`5.4.7`
:Amazon: - Fixed an issue that could prevent AWS Clouds using Assume Role from working with Security Groups under certain configurations. :superscript:`5.4.7`
:Ansible Tower: - Fixed an issue that could cause Ansible Tower integrations not to sync in all available templates. :superscript:`5.4.7`
:Ansible: - Accessing an Instance Layout version from an Ansible Task now returns the correct version value rather than "unknown". :superscript:`5.4.7`
           - Ansible Playbook execution will authenticate with Git via a token, if present. Previously if a username and password were also present, they would take precedence even when a token was also given. :superscript:`5.4.8`
           - Improved handling of validation when Ansible Tasks or Jobs are run against Instances that can no longer be found. :superscript:`5.4.8`
:Apps: - Fixed an issue that could cause costs to be revealed in the provisioning wizard even when "Show Pricing" was switched off (Administration > Settings > Provisioning). :superscript:`5.4.7`
:Archives: - Fixed an issue that could arise when uploading a second file to an Azure backed Archive with the same name as an existing file. :superscript:`5.4.8`
:Automation Execute Schedules: - Improved validation on cron expressions when saving execute schedules to prevent saving invalid schedules. :superscript:`5.4.7`
:Azure: - Added improvements to Azure Instance cost computations. :superscript:`5.4.7`
         - Fixed an issue that caused the "Assign Public IP DNS" checkbox present in Azure and Azure Stack provisioning not to work properly. :superscript:`5.4.7`
         - Fixed an issue that could prevent Azure provisioning under specific scenarios if a stored credential set was used to authenticate the Cloud integration. :superscript:`5.4.8`
         - Improvements made to Azure CSP costing to ensure more accurate figures. Improved Azure costing calculations including a fix for an issue that could duplicate line items and create incorrectly high cost figures, a fix for an issue related to computing price from cost, and a workaround for issues stemming from costs syncs that take longer than an hour and the token expires :superscript:`5.4.7`
:BIND DNS: - BIND DNS integrations can now be deleted properly when no longer needed. :superscript:`5.4.7`
            - BIND integrations can now be removed from |morpheus|. :superscript:`5.4.7`
:Backups: - Fixed an issue that caused Veeam backups to fail when backups or VMs with identical names existed in multiple Tenants. :superscript:`5.4.7`
           - Fixed the backup success widget (checks and Xs) on the backup list page (Backups > Backups) to show the results left-to-right starting with the most recent. :superscript:`5.4.7`
           - GCP backups no longer fail when uppercase characters are included in the backup name. :superscript:`5.4.7`
:Blueprints: - Fixed an issue that could cause resource pool configurations from coming unset on App Blueprints. :superscript:`5.4.7`
:Buckets: - There is no longer a pipe character ("|") superimposed over the bucket name on a bucket detail page. :superscript:`5.4.8`
:CMDB: - Fixed an issue that could cause significant error traffic in the logs when Clouds with an associated CMDB went through their normal sync process. :superscript:`5.4.7`
:Catalog: - Improved validation on catalog items backed by ARM Blueprints which could allow users to provision to Groups they didn't have access to under some conditions. :superscript:`5.4.7`
           - In the Inventory section of the Dashboard tab on the Service Catalog Persona, the Pagination options have been removed from the view options (gear) menu. This option did not function and the Dashboard Inventory view was never meant to allow pagination. :superscript:`5.4.7`
           - In the Inventory section of the Dashboard tab on the Service Catalog Persona, the search bar has been removed. This search bar did not function and the Dashboard Inventory view was never meant to be searchable. :superscript:`5.4.7`
           - When changing the name of an Instance provisioned from the Service Catalog Persona in the standard Persona, the new name is now reflected in the Service Catalog Persona. :superscript:`5.4.7`
:Clusters: - Inputs added to Cluster Layouts now display as expected when creating new Clusters. :superscript:`5.4.7`
:Commvault: - Commvault backups now support duplicate backup names and backups for duplicate VM names across multiple Tenants. :superscript:`5.4.7`
:Costing: - Additional work has been done on Azure costing to add further reduction in duplicated invoice line items. :superscript:`5.4.8`
           - Improvements made to costing estimates given in the Create Cluster wizard to ensure correct pricing in a greater number of scenarios. :superscript:`5.4.7`
:Credentials: - For Option Lists that use bearer tokens, you can now remove the manually-entered token to use a |morpheus| credential set and save the Option List properly. :superscript:`5.4.7`
:Google Cloud (GCP): - Improved plan matching for GCP workloads, previously |morpheus| would not set the plan properly depending on how it was named. :superscript:`5.4.8`
:Identity Sources: - Advanced validation options for SAML SSO identity sources can now be edited and the changes are saved correctly. :superscript:`5.4.7`
                  - Fixed an issue that could cause authentication to fail for users going through external SSO under specific conditions. :superscript:`5.4.7`
:Infoblox: - Improved validation when adding or editing Infoblox integrations to check throttle rate, network filter, zone filter, and extra attributes. :superscript:`5.4.7`
:Inputs: - Dependent Inputs are now populated correctly when displayed in App Blueprint deployments. :superscript:`5.4.8`
          - Inputs dependent on other Inputs are now populated correctly when displayed on an Edit Instance dialog. :superscript:`5.4.8`
          - Validation is now working properly when the visibility and required status of an Input is dependent on a specific response in another Input. :superscript:`5.4.7`
:Instances: - Fixed an issue that could cause Windows Server 2022 Instances to hang on reconfigure. :superscript:`5.4.8`
:Invoices: - Fixed Invoice line items showing values in USD when other costing for the Instance is given in another currency. :superscript:`5.4.7`
:Jobs: - Execution history for Jobs has been improved, previously some executions weren't shown under specific conditions. :superscript:`5.4.8`
        - Fixed an issue that caused duplicate jobs to be created when using the New Job wizard. :superscript:`5.4.7`
:Kubernetes: - Fixed an issue that would cause workers to be added to Kubernetes clusters with the wrong version if the cluster had been upgraded at some point previously.
:Library: - "Enable Scaling (horizontal)" setting is now honored for specific Layouts even if it is disabled on the Instance Type. :superscript:`5.4.8`
           - Fixed an issue that caused default catalog items for MySQL and NGINX to fail provisioning under certain configurations. :superscript:`5.4.7`
:Logs: - Fixed an issue that generated NSX-V errors in logs in each sync. :superscript:`5.4.7`
        - Fixed an issue that would cause repeated errors being raised by |morpheus| LogService. :superscript:`5.4.7`
:Monitoring: - Logs for Subtenant users are now correctly scoped not to show Monitoring-related logs from the Primary Tenant. Previously, Subtenant users could see these logs with "User" or "Full" level permissions. :superscript:`5.4.7`
              - When Monitoring Role permission is set to "User", users can now create contacts and alert rules as intended. :superscript:`5.4.7`
:Network IP Pools: - Fixed an issue that caused allocated IP addresses not to be shown correctly on the IP Pools list page. :superscript:`5.4.7`
:Nutanix: - Fixed an issue that could cause Windows Nutanix Instances to provision with the wrong time zone. :superscript:`5.4.7`
:OpenStack: - Fixed an issue that changed the device name of OpenStack Instance disks after reconfiguring the Instance to resize them. :superscript:`5.4.7`
             - Fixed an issue that could cause additional networks to be exposed to the user via the provisioning wizard when their Role restricted Infrastructure: Networks permission to "None". :superscript:`5.4.8`
             - Fixed an issue that could throw errors when reconfiguring OpenStack Instances to add network interfaces. :superscript:`5.4.7`
             - When an Octavia load balancer integration has been removed, |morpheus| now cleans that up rather than continuing to try syncing with the service. :superscript:`5.4.8`
             - When reconfiguring to add disks to OpenStack Instances, the new disk is now attached to the VM properly. Previously it would not be in some situations despite appearing to have worked in |morpheus| UI. :superscript:`5.4.7`
:Option Lists: - |morpheus| API-type Option Lists for Network Security Groups now return the internal database ID for the Security Group as expected. :superscript:`5.4.8`
:Plans & Pricing: - Fixed issues related to provisioning dynamic service plans (custom cores, memory, etc.) under specific input scenarios. :superscript:`5.4.7`
:Policies: - Fixed an issue that caused issues extending the expiry date for workloads which were held in a delayed removal state by policy. :superscript:`5.4.7`
            - Fixed an issue that could cause Windows-based Workflows not to execute properly as part of a Workflows Policy. :superscript:`5.4.7`
:Power Scheduling: - Fixed an issue that caused problems provisioning Instances with Power Schedules during a time when the Instance was scheduled to be off. :superscript:`5.4.8`
:Provisioning: - Fixed an issue that caused the provisioning wizard to hang when deploying Instances based on ARM templates to Azure Clouds scoped to "All" resource groups. :superscript:`5.4.7`
:Reports: - Date ranges for cost reports can now be specified with a month selector rather than allowing freely entered date ranges as the available data only supported individual month blocks anyway. :superscript:`5.4.7`
           - Fixed issue with nginx timeouts during massive report exports. :superscript:`5.4.7`
:Roles: - The Tools menu is no longer hidden from view when the user's Role grants only access to the VDI Pools section. :superscript:`5.4.7`
:SCVMM: - Fixed an issue that could cause an incorrect host group to be selected if an SCVMM Cloud was saved while the host group select list was still being loaded in. :superscript:`5.4.7`
         - Fixed an issue that prevented SCVMM Clouds from deleting. :superscript:`5.4.7`
:Security: - Passwords entered by users as custom options when provisioning ARM blueprints as service catalog items are no longer visible in logs or Instance review summaries (they were already masked in the UI). :superscript:`5.4.7`
:Spec Templates: - Improved cleanup on delete of provisioned ARM spec templates which are not fully provisioned successfully. :superscript:`5.4.7`
:Tags: - Category and tag name changes are synced when they are changed in vCenter (as the tag "name" and "value", respectively, in |morpheus|) and usage records are restarted when such a change is made. :superscript:`5.4.7`
:Tasks: - Fixed an issue that caused Subtenant Tasks reading Cypher values from the Primary Tenant to fail when run from the VM context when they worked from the Instance context. :superscript:`5.4.7`
         - Fixed an issue that prevented creating or managing Tasks if "Infrastructure: Credentials" permissions were not set to "Full".
         - Improved clean-up of stuck or very long-running processes (such as Tasks) to ensure appliance performance. :superscript:`5.4.7`
:Tenants: - Fixed an issue that prevented Tenants from being deleted if they had VMware vCenter Clouds associated with them. :superscript:`5.4.7`
           - The existence of stored credentials (Infrastructure > Credentials > Trust) no longer prevents Tenants from being deleted. :superscript:`5.4.7`
:Terraform: - Fixed an issue that prevented Terraform commands which pass options to function correctly. :superscript:`5.4.7`
             - Improved teardown of deployed Terraform Spec Templates to ensure all created objects are cleaned up. :superscript:`5.4.7`
             - Terraform Outputs are now updated correctly after applying state changes which update them. :superscript:`5.4.8`
             - Terraform refresh has been adjusted to nightly rather than every 30 minutes as it could cause performance issues in some cases. :superscript:`5.4.7`
             - When running Terraform commands from the State tab, |morpheus| no longer automatically appends the "-var" option to certain commands where it wasn't needed. :superscript:`5.4.8`
:Trust: - Fixed an issue that could cause the Add Trust Integration modal not to appear in specific scenarios involving newly-created Subtenants. :superscript:`5.4.7`
:UI: - Improved truncation of very long values (Instance name, Group name, etc) in the Info section of Instance detail pages. :superscript:`5.4.7`
      - In the History section of the Instance detail page, text will not truncate properly in certain areas where it could previously become overset.
:Usage: - Fixed an issue that caused additional locations to be added for Virtual Images when Instances were provisioned from them. :superscript:`5.4.7`
         - Usage records are now visible from the Subtenant when a workload has been created in the Primary Tenant and shared with the Subtenant. :superscript:`5.4.7`
:VMware: - Applying tags and VMware Content Library sync are now working properly when VMware vCenter is accessed behind the |morpheus| Distributed Worker. :superscript:`5.4.8`
          - Fixed an issue that could cause the PROPAGATE PERMISSIONS TO CHILD OBJECTS? option for VMware folders not to work correctly. :superscript:`5.4.7`
:Workflows: - Primary Tenant users can no longer retrieve configuration for Workflows belonging to Subtenants through |morpheus| API. :superscript:`5.4.7`
:XaaS: - Filtering the Instances list page by Cloud will now also show XaaS Instances which are provisioned to the selected Cloud. :superscript:`5.4.8`
        - The Cloud hyperlink on Instance detail pages for XaaS Instances now links properly to the Cloud the Instance has been provisioned to. :superscript:`5.4.8`
        - The Cloud name now appears on Instance detail pages for XaaS Instances when the user has Infrastructure: Clouds permission set to "None". The name is not hyperlinked in this case due to the user's Role permission. :superscript:`5.4.8`
        - When pricing is correctly configured, price estimates are now shown on detail pages for XaaS Instances. Previously, a "no pricing configured" message was given even if pricing was correctly established. :superscript:`5.4.8`
:vCloud Director: - Fixed an issue that prevented deploying MKS 1.22 clusters on Ubuntu 20.04 to vCD Clouds. :superscript:`5.4.8`
                  - The OS is now detected properly for Windows Server 2022 images synced from vCD. :superscript:`5.4.7`


Appliance & Agent Updates
=========================

:Appliance: - Elasticsearch upgraded to 7.17.5. :superscript:`5.4.8`
             - Embedded Elasticsearch TLS & Basic Authentication support added. :superscript:`5.4.8`
             - Fixed 5.4.3- to 5.4.4+ upgrade issue caused by grails access token migration failing when a tenant is disabled.. :superscript:`5.4.7`
             - Improved Elasticsearch cleanup job to handle non-system or morpheus created indices.. :superscript:`5.4.8`
             - OpenSSL upgraded to 1.1.1p. :superscript:`5.4.8`
             - RabbitMQ and Erlang upgraded to 3.9.20 and 23.3.4.2, respectively. :superscript:`5.4.8`
             - Tomcat upgraded to 9.0.64. :superscript:`5.4.8`

