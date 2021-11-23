.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

.. warning:: SERVICE NOW DEPRECATION NOTICE: In v5.4.1, Instance and Blueprint specific exposures will be removed from ServiceNow plugin support. More advanced configurations of Instances and Blueprints, in addition to Workflows, can be exposed utilizing Catalog Items

.. warning:: VCLOUD DIRECTOR DEPRECATION NOTICE: Beginning in v5.4.1, VCD 9.x will no longer be supported by Morpheus

New Features
============

:API & CLI: - Get NSX-T Edge Cluster details from |morpheus| API and CLI :superscript:`5.2.13`
             - Individual Report Type access levels can now be set on Roles from |morpheus| API and CLI
             - Refresh and Apply state functions for Apps, such as Terraform Apps, can now be executed from |morpheus| API and CLI
:Amazon: - Added support for additional regions: ``eu-south-1`` Europe (Milan), ``eu-west-3`` Europe (Paris), and ``me-south-1`` Middle East (Bahrain) :superscript:`5.2.13`
:Costing: - Usage records (Operations > Costing > Usage) can now be expanded in the UI to show more granular usage and cost breakdowns
:Currency: - Added support for new currencies: Jordan Dinar (JD), Saudi Arabia Riyal (SAR), and United Arab Emirates Dirham (AED) :superscript:`5.2.13`
:Kubernetes: - Amazon EKS: Added ability to scale EKS clusters
              - Azure AKS: NODE PLAN field updated to Option List
:Option Lists: - Added new Option List type: Instance Networks. When tied to an Input, the list will contain networks filtered by the selected resource pool and region
:Oracle Cloud: - Added support for Oracle Public Cloud Dubai region :superscript:`5.2.13`
:Policies: - Tag Policies can now automatically apply tags in addition to enforcement. Select lists added for value selection for Tag Policies utilizing option lists.
:Reports: - The CSV-formatted export for the Time Series Cost report is now updated for complete parity with the data revealed in the UI report
:Tasks: - Powershell: Local Execution target option added for PowerShell tasks. NOTE: ``pwsh`` must be installed on the appliance for this to work.
:UI: - An export button has been added to the |morpheus| Logs tab in the Health section (Administration > Health > |morpheus| Logs tab). This will export the last 10,000 entries as a log file. |Morpheus| CLI and API adds this health log export feature as well
:VDI: - Added a new VDI pool type to support RDS servers where multiple RDP sessions can run on a single server
:Workflows: - Executions tab added for Workflows to list the executions for that specific Workflow. This feature was added for Tasks in a prior release


Fixes
=====

:API & CLI: - Calls to the ``provision-types`` API are now paginated and support ``max``, ``offset``, ``sort``, and ``direction`` parameters
:Amazon: - Fixed an issue with Amazon provisioning where, if you stepped through the wizard and selected a Security Group, then went back and chose another AWS Cloud, the Security Group from the first Cloud was still present and could cause provisioning failure :superscript:`5.2.13`
          - Snapshot usage records are now stopped when deleting an Amazon Instance without preserving its backups
:Ansible: - Fixed an issue causing Ansible Tasks to fail due to Ansible Galaxy install issues :superscript:`5.2.13`
:Billing: - Fixed an issue where billing data would not be updated to reflect changes to VMs (when adding disks, etc.) until the machine was next power cycled
:Catalog: - Fixed an issue where the Catalog could become inaccessible for a user after adding an item to the cart which contained an Option List with invalid data :superscript:`5.2.13`
:Clusters: - Added minor improvements to cluster health and power state reporting in the UI
            - Added validation for required API URL and API Token fields when onboarding external Kubernetes clusters through the Create Cluster wizard
            - Docker Cluster provisioning now respects custom ranges on Plans when CUSTOMIZE EXTRA VOLUMES and ADD VOLUMES is enabled on the plan :superscript:`5.2.13`
            - Teardown and Reconfigure-phase Workflow Tasks now are applied to Kubernetes Cluster nodes
:Executions: - Fix execution request issue that could prevent communication through load balancers
:F5: - Fixed an issue that could cause F5 load balancers for Apache HTTPS backends to fail on creation
:Google Cloud Platform: - Fixed an issue that could result in timeouts and failed provisions when provisioning a GCP Library item that required uploading the RAW image
:Guidance: - Users with ``Guidance -> Full`` but ``Read`` Group permissions are no longer able to perform full actions in Guidance against resources in that Group :superscript:`5.2.13`
:Identity Sources: - Fixed issue with customSSO API 500 response for multiple customsso user token requests :superscript:`5.2.13`
:Instances: - Fixed an issue that could cause the convert-to-managed process to not work correctly when converting multiple Windows boxes with duplicate tags
             - Startup and shutdown entries no longer show in the History tab of the Instance Detail page if there are no Tasks associated with those phases of the Instance Provisioning Workflow :superscript:`5.2.13`
:Kubernetes: - Fixed an issue causing workers, kubeconfig, and API tokens to be synced in for discovered clusters. These should only be visible after converting the cluster to managed
              - Fixed an issue that caused Control Tab functions on the Cluster Detail Page not to work when adding an existing EKS cluster as an "External Kubernetes Cluster"
              - Fixed an issue that could cause inventoried AKS hosts to remain even after they were deleted from the cloud and |morpheus| had completed subsequent cloud syncs
              - Fixed an issue that could prevent user selection of a Node Plan value when creating AKS clusters
              - Fixed an issue which caused AKS clusters not to receive kubeconfig or API token after converting to managed
:Library: - DOCKER COMMAND EXTRA field added to Docker Node Types to add arbitrary docker command line args :superscript:`5.2.13`
:Load Balancers: - Improved UI error messages when load balancer virtual server creation fails :superscript:`5.2.13`
:Logs: - Added optimizations for Agent logs to improve performance and scalability :superscript:`5.2.13`
:NSX-T: - Cleaned up Gateway Interface sync errors which would appear in logs on NSX-T integration sync :superscript:`5.2.13`
         - Fixed an issue that caused IP Management Settings on an NSX-T router not to be set properly on the |morpheus| side compared to what was in NSX-T :superscript:`5.2.13`
         - NSX-T load balancer virtual server creation no longer gives the option for generating a self-signed server. This change was made to prevent confusion as NSX-T LB virtual servers cannot use self-signed certificates :superscript:`5.2.13`
         - Subtenant users can now select an NSX-T integration shared from the Primary Tenant for purposes of creating SSL certificates :superscript:`5.2.13`
:NSX-V: - Fixed an issue that caused errors to be thrown when attempting to edit locked NSX-V distributed firewall rules :superscript:`5.2.13`
:Policies: - Fixed a number of issues related to the Create Cluster wizard respecting policy limits for Max Storage and Max Hosts
:Provisioning: - Added validation of Windows usernames before injecting them into Unattend.xml during Windows provisioning to prevent failure due to invalid usernames
                - When provisioning into a network with a |morpheus| IP Pool and selecting a static IP, the IP is no longer automatically assigned to the first range in the pool, which could cause errors when the address was outside that range :superscript:`5.2.13`
:SCVMM: - Fixed an issue where Instances provisioned to SCVMM Clouds from Subtenants would not correctly receive static IP addresses as selected during provisioning :superscript:`5.2.13`
:Security Scans: - Windows SCAP scans can now utilize XML files in addition to ZIP files :superscript:`5.2.13`
:Security: - When creating new Apps, certain detailed MySQL exceptions are no longer surfaced into the UI. Instead, a more generic error message is surfaced directing the user to check logs for the complete exception :superscript:`5.2.13`
:Tasks: - Task config content can now be copied to the paste buffer when viewed on the Task detail page (Library > Automation > Tasks > Specific Task)
:Terraform: - Fixed an error caused in Terraform Blueprints when Terraform code contained a ``Date`` value of ``timestamp()``
             - Fixed an issue that would cause Terraform validation not to run in specific scenarios when provisioning Instances from Terraform Spec Templates
             - Fixed issue with terraform ``bool`` variable validation
:UI: - Fixed an issue with pagination on the Catalog Inventory page (Provisioning > Catalog > Inventory)
      - Fixed presentation issues with some automated email, including inactive user warning email, old password warning email, disabling inactive user email, and login attempts with locked email warnings :superscript:`5.2.13`
      - Inputs can now be edited on Instance Types. Previously after saving, associated Inputs could not be changed or removed
:Users: - Fixed an issue that could cause 500 errors and failure when editing a User synced from an identity source integration to have a Linux password of insufficient complexity :superscript:`5.2.13`
:VMware: - Updated VMware Content Library integration to account for situations where users may have multiple content library hosting the same files in the same vCenter
:Whitelabel: - The opacity slider in the whitelabel color picker (Administration > Settings > Whitelabel) now works correctly :superscript:`5.2.13`


Appliance & Agent Updates
=========================

:Appliance: - Cleaned up some minor ``seedService`` warnings that could present on startup
            - Fixed issue with rolling upgrades for 3-Node HA clusters utilizing Morpheus embedded RabbitMQ where the first time an Applaince is upgraded the RabbitMQ cluster data was not retained and the cluster had to be manually re-established.
            - MacOS Node package jre version updated to 8u312-b07


.. ..