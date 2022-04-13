.. _Release Notes:

*************************
|morphver| Release Notes
*************************

Release Date: |releasedate|

.. important:: Database indexes added for account_usage and metadata_tag tables. Customers with very large account_usage and/or metadata_tag tables (10 million+) **may experience slower initial morpheus-ui loading times and additional database load after upgrading to 5.4.5** while the indexes are being added. 
.. warning:: **AVI Load Balancer** renamed to **NSX Advanced Load Balancer**
.. warning:: Cloud Types disabled by default: **Dell**, **HPE** (NOT HPE Oneview), **Supermicro** and **Cloud Foundry**. Users would still be able to re-enable this clouds in the appliance settings. Does not affect existing Clouds.
.. warning:: **A10 Load Balancer** type has been disabled, and will no longer be an option when adding new Load Balancers. Contact |morpheus| if you need to re-enable A10 Load Balancer option. This does not affect existing Load Balancers.
.. warning:: |morpheus| Cluster type **Combo Cluster** renamed to **KVM/Docker Cluster**

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:A10: - Ability to add A10 Load Balancers has been disabed
:API & CLI: - Instances endpoint now has Terraform Apply and Terraform Refresh as the Apps endpoint already did
             - Software license functionality (Administration > Settings > Software Licenses) is viewable from |morpheus| API and CLI
:AppDynamics: - The AppDynamics integration, which was previously deprecated, has been removed from the product
:Clouds: - Improvements made to Cloud details pages seen for users given read-only access to a particular Cloud
          - Some seldom-used Cloud integration types have been disabled by default, these include Dell, HPE, Supermicro, and CloudFoundry. Users can still enable them in Administration > Settings if needed
:Clusters: - Add tags when provisioning a cluster or adding a host :superscript:`5.5.0`
            - Combo Clusters have been renamed KVM/Docker clusters
:Credentials: - Stored Credential sets (Infrastructure > Trust) can now be used with some Option List configurations, just as authenticating against a REST API for REST-sourced lists
               - Stored credentials can now be used with HTTP-type Tasks and for access to remote execution for other Task types
               - Users can now integrate all Cloud types using stored credentials (Infrastructure > Trust) and |morpheus| will filter the list of selectable credentials to only types supported by the target cloud
:Currency: - |morpheus| now supports Argentine Peso (ARS) currency
:Cypher: - Added Cypher Access Policy type to enable granular control over access to List, Read, Write and Delete on arbitrary Cypher paths for Global, Role, and User scopes
:EfficientIP: - EfficientIP SOLIDserver IPAM plugin is now available on request. Can be added to |morpheus| (Administration > Integrations > Plugins) to add the new IPAM integration type (Infrastructure > Network > Integrations) to the appliance
:F5: - Added F5 Policy and Policy Rule creation & management, including http forwarding policies
      - Added Partition sync & selection
:Github: - Updates made to ensure full functionality of Github integrations after Github deprecated SHA-1
:Instances: - Greenfield workloads can no longer be removed from |morpheus| without also removing the underlying infrastructure
             - Removed the edit action (pencil icon) from the Network tab of the Instance detail page
             - The Instances list page can now be filtered to show only the Instances owned by the current user. Click the gear icon at the top of the list to edit output fields and filter criteria
:KVM: - The host-local image pool (morpheus-images) now has automatic purging behavior to ensure the allocation doesn't get too full. At 80% full, images will be purged beginning with the oldest accessed cached volumes until 50% capacity is reached
       - When provisioning to KVM hosts and selecting plans with custom CPU and memory parameters, configured maximum CPU and memory values (if any) on the plan are now honored :superscript:`5.5.0`
:Kubernetes: - CPU, Memory, Storage and Network metrics shown for pods running on a connected Kubernetes cluster
              - Pricing for AKS, EKS, and GKE controllers and workers is now displayed on the review tab of the provisioning wizard
:Load Balancers: - AVI Load Balancer has been renamed NSX Advance Load Balancer to reflect the renaming of the technology itself
:NSX: - Distributed firewalls for NSX-T are now accessible to Subtenants when an NSX-T integration and distributed firewall has been shared from the primary Tenant :superscript:`5.4.4`
:OpenStack: - The version picker for OpenStack Clouds has been removed as it did not need to be set in most cases and created confusion
:Policies: - Added Policy type to limit number of virtual servers on a network
            - Added Policy type to limit the number of members in each load balancer pool within the policy scope
            - Additional scopes added for max load balancer pool policies. Global, Cloud, and User-scoped Policies can now be created
:Python: - Added local workspace path for Python task execution to resolve slow venv execution when /var/opt/morpheus/morpheus-ui is on nfs
:Security: - CVE-2021-30129 Upgrade sshd-core to version 2.7.0
            - Embedded Elasticsearch jackson-databind upgraded to 2.13.2.1. (CVE-2020-36518)
:ServiceNow: - After exposing a |morpheus| Catalog Item to ServiceNow, the default workflow can be set and edited without resetting to the default after the nightly sync
              - In most cases, default Input values and help blocks are synced over for exposed Catalog Items as they would be if the Catalog Item were provisioned from |morpheus|
              - The "title" value for the |morpheus| category of the |morpheus| plugin section of ServiceNow can now be updated without reverting back on the next daily sync
:Trust Integrations: - The Venafi integration, which was previously deprecated, has been removed from the product
:UI: - Database optimizations added for usage and tag tables to improve application performance
      - On Instance delete, the "Preserve Backups" option is only shown when backups are enabled for the Instance
:Usage: - "Usage Retainment" setting added to |AdmSet|. Determines how long to keep usage records in database. Retainment period is not set by default. Usage records will remain indefinitely like prior releases if Usage Retainment is not set.
:VMware: - Added "Enable Storage Type Selection" to VMware vCenter Cloud integrations. If selected, storage type (thin, thick-lazy zero, thick-eager) can be selected at provision time
:XaaS: - Pricing data is now displayed correctly for `XaaS provisioning <https://docs.morpheusdata.com/en/latest/getting_started/guides/xaas_instance.html>`_


Fixes
=====

:API & CLI: - "api/apps/:id/prepare-apply" endpoint has been restored to |morpheus| API. It was removed in a previous release
             - A generic warning is now returned when attempting to POST to "/provisioning/apps" using a Blueprint ID the user cannot access
             - Fixed an issue that caused VMs to go into an unknown state when activating or deactivating clusters via |morpheus| API
             - Fixed an issue that caused errors to be thrown when applying |morpheus| IP Pools to GCP networks via API
             - Fixed issue with "incomplete configuration" error when updating catalog items via API
             - Fixed |morpheus| API-type created via API and shared with a subtenant containing Primary Tenant objects in some cases
             - When simultaneously adding/updating tags and customOptions values on an Instance, existing tags are no longer wiped out. The new tag is simply appended to the existing tags as expected
             - |morpheus| API and CLI can now be used to create Cloud-scoped Policies targeted to Clouds which are private to the Subtenant
:Amazon: - Cached and expired STS keys are now cleared properly which prevents authentication issues
:Ansible Galaxy: - Improved cleanup of Ansible Galaxy collection caches to prevent unnecessary storage use
:Ansible Tower: - Fixed an issue that caused the option to disable Ansible Tower at provision time not to work properly
                 - Fixed an issue that prevented changes made on the Ansible Tower side not to be synced back to |morpheus|
:Ansible: - Fixed an issue that could cause Ansible Tasks in the Provisioning Phase of a Workflow to fail
:Apps: - Resolved issue with ${instance.name} variable not evaluating for VIP Hostname
:Bluecat: - Fixed an issue that prevented removal of Bluecat integrations
:Blueprints: - Editing App Blueprints and provisioning Apps to target Clouds named with their FQDN now works properly
:Budgets: - Fixed an issue that prevented Subtenant users from creating Cloud budgets
           - Fixed incorrect time period labels on multi-year budgets set on quarterly scale with a configured custom fiscal year
:Catalog: - Added executions section to Catalog inventory pages so users can better confirm success of workflows run against multiple Instances and servers
           - Fixed an issue causing a permissions error to be displayed after ordering a Catalog Item if the user did not also have access to see the Inventory which is where the user was redirected after completing a Catalog order
           - Removed "copies" parameter from the JSON config body for Catalog Items as this concept is intended only for provisioning executed via the full provisioning wizard
:Clouds: - Users can no longer advance to the configuration step of the Add Clouds modal without first selecting a Cloud type
:Dashboard: - Fixed issues with log counts and graphs on the Dashboard page (Operations > Dashboards) which caused counts to stay at zero
:Distributed Worker: - Fixed an issue that prevented deletion of distributed workers via |morpheus| UI
:F5: - Fixed an issue that caused Instances to become inaccessible when provisioned with F5 load balancer and floating IP address
:Google Cloud (GCP): - Fixed an issue that caused the console to become inaccessible for GCP Instances using private IP addresses
:Identity Sources: - Fix db lock issue causing user creation failure when using Custom External SSO Identity source
:Infoblox: - Infoblox host records are no longer created with the zone name in the "name" field
:Inputs: - "No Options Found" message on empty Select List Inputs is no longer selectable to prevent confusion and satisfying required Inputs
          - Fixed a display issue when editing Instances that caused updated Input values to revert and the Edit Instance modal not to close after saving changes despite the changes being saved in the background
          - Improved handling of dependent Inputs which are shown on the Edit Instance modal when making changes on the Instance detail page
:Instances: - Fixed an issue that caused the "Cloud" link (to the target Cloud detail page) to appear on Instance detail pages for users with "None" access to "Infrastructure: Clouds" under certain conditions
:KVM: - Fixed an issue that could cause failures when reconfiguring KVM Instances to add or remove secondary network interfaces
:Kubernetes: - Fixed an issue that could cause failures when adding container nodes to a Kubernetes cluster
              - Fixed an issue that could cause failures when provisioning MKS clusters using Plans with a custom storage range
              - Health checks for container services provisioned to Kubernetes Clusters now work as intended
:Layouts: - "Enable Scaling (Horizontal)" option now works on individual Layouts even when the Instance Type is configured to disable it
:Monitoring: - The breadcrumb link from a Monitoring Group detail page back to the Monitoring Groups list page now works correctly
:NSX-T: - Fixed an issue causing member groups on NSX-T load balancer pools not to be saved and persisted properly
         - Fixed an issue that could prevent editing and resaving NSX-T segments with errors
         - Fixed an issue that prevented selection of NSX-T load balancer SSL profiles in App Blueprint and App wizards
         - Subtenant users with sufficient Role permissions can now drill into NSX-T routers shared from the Primary Tenant
:Network: - Corrected an issue that could result in Instances having multiple primary NICs
           - Fixed an issue that prevented removal of IP Pools from a subnet
:Node Types: - System-default scripts are no longer selectable on user-defined Node Types since they lack the inputs needed to work properly and weren't intended for use outside of the default Node Types
:OpenStack: - Fixed an issue causing errors when resizing network for OpenStack Instances via reconfigure
             - Fixed an issue related to OpenStack floating IP Pools not respecting associated network permissions
:Option Lists: - Fixed an issue that caused the Option List size value (on the list page for Option Lists) not to be reported corrected in some cases
:Plans & Pricing: - "Show Pricing" setting (Administration > Settings > Provisioning) is now honored in Subtenants as well
                  - Snapshot price sets can now include 'datastore' price types in addition to the required storage price type ('Disk Only')
                  - Software prices are now included in computed prices
:Provisioning: - Fixed an issue that caused the provisioning wizard not to work properly when only one Instance Type and Layout was exposed to a Subtenant user
:Roles: - The Tools menu will now be shown for users whose Role only gives access to VDI Pools and nothing else under Tools
         - Users with no permissions to "Library: Virtual Images" can now see and add additional disks on cloned Instances
:Security: - Fixed permission issue with /library/services api endpoint
            - Fixed permission issue with /settings/software-licenses api endpoint
            - Layout descriptions are now limited to 1,000 characters for security and performance reasons
            - Password reset email links are now active for 30 minutes for security reasons. Previously they were active for seven days
            - Security enhancements added to close potential XSS and CSRF attack vectors
:ServiceNow: - Fixed an issue with custom ServiceNow CMDB class mapping
              - Removed the "enabled" flag displayed for exposed Catalog Items on the ServiceNow integration detail page as there is currently no concept of enabling or disabling exposed Catalog Items
:Storage: - Fixed an issue provisioning uploaded images with many disks
:Terraform: - Added capability to add tfvar secret to Terraform Layouts using |morpheus| API and CLI
:UI: - Fixed a display issue that caused App Blueprint configuration windows to be compressed when the App Blueprint was given a very long name
:Usage: - Fixed usage issues associated with Snapshot, Virtual Image and Load Balancer price types. Datastore ID property added to disk price types API queries
:VDI Pools: - Fixed broken custom logos for VDI apps
:VMware: - Fixed Resource Pool folders not syncing in order which caused unexpected behaviors
          - Fixed an issue that could lead to duplicate SCSI controller and volume external IDs which created additional problems
          - Fixed issue that could cause disk layout to be mismatched in |morpheus| compared with the vCenter console
:Wiki: - Improved sync of Wiki information between the main Wiki section (Operations > Wiki) and the Wiki tab of Instance detail pages
:Workflows: - Added ``apiAccessToken`` for "configuration" workflow phase
:vCloud Director: - Fixed an issue that could cause provisioning failures to vCD networks created in |morpheus|
                  - VDCs associated with a private vCD Cloud are no longer visible in Subtenants


Appliance & Agent Updates
=========================

:Appliance: - ```ui['jobs_enabled'] = true``` config setting added to morpheus. This option disables the appliance jobs service on the appliance node when set to false. This should be disabled only when configuring jobs to run on specific app nodes in HA environments.
