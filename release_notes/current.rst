.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: Items appended with :superscript:`5.2.x` are also included in that version

.. might not do highlights this time
  .. include:: highlights.rst

New Features
============

- Azure: Morpheus now syncs available (non-preview) AKS Kubernetes versions daily. Existing synced versions that are no longer supported by Azure are automatically disabled. The table below includes available AKS versions at time of |morphver| release.
- Clouds: Added scale factor setting for Instance scaling at provision time to all cloud integrations that didn't currently support it
- Clouds: Xen, Nutanix, Google and Upcloud cloud types now support option to skip |morpheus| Agent installation at provision time.
- Google Cloud: Added disk type selection support. When provisioning (Instances, Apps, Clusters), cloning and reconfiguring, choose standard, balanced or ssd disk types. Pricing is synced based on the selected disk type and disk type information is onboarded or updated on Cloud sync
- Costing: Added a standard costing service with invoice support (Operations > Costing > Invoices) for on-prem clouds to mirror the public cloud real-time costing experience. This functionality must be enabled by setting the COSTING field to "Sync Costing" in the Advanced Options section of the add/edit Cloud modal (Infrastructure > Clouds > Selected Cloud > EDIT button)
- Huawei Cloud: Image upload functionality now supports images greater than 2GB in size. When adding/editing the Cloud, set an OBS bucket in the IMAGE STORE field as a permanent store location for |morpheus| virtual images
- Hyper-V: Added discovery and inventory for Hyper-V Clouds. Mark checkbox to "INVENTORY EXISTING INSTANCES" on the add/edit Cloud modal to enable or disable this option. As with other Cloud types, discovered VMs can be converted to managed Instances and deleted with or without removing the underlying infrastructure
- Job Executions: A job execution record is now created for every target the job is run against, previously a record was only created for the last target the job was run against
- Job Executions: UI updated with a detail page for each job execution providing easier access to process outputs and error messages for each Task and target associated with the job
- NSX-T: Create and manage NSX-T load balancer profiles (Infrastructure > Load Balancers > Selected Load Balancer > Profiles Tab), previously this tab was read-only :superscript:`5.2.6`
- Open Telekom Cloud: Image upload functionality now supports images greater than 2GB in size. When adding/editing the Cloud, set an OBS bucket in the IMAGE STORE field as a permanent store location for |morpheus| virtual images
- Option Types: "Radio List" Option Types can now be added which present options to the provisioning user as radio buttons
- Roles: Report Types tab added to user and tenant role permission sets. Assign access permissions for specific report types for users with access to the Reports section under the Operations menu
- Software: Patch version numbers are now surfaced on the Software tab of server detail pages (mouse hover over software name) and in Software reports :superscript:`5.2.6`
- Storage: Added support for Google Cloud Storage bucket creation and management (Infrastructure > Storage > Buckets tab)
- vCloud Director: Added support for API version 34.0 on vCD 10.2+ :superscript:`5.2.6`
- VMware vCenter: Added the option to select a folder when cloning an Instance to image (Actions menu of the Instance detail page). Previously, images were copied to the root folder
- VMware vCenter: CPU and memory hot-add settings are now evaluated independently when reconfiguring CPU and memory for vCenter Instances. Previously, these settings were evaluated as a group rather than independently which could cause VMs to be restarted even when they were configured to support hot-add of memory and/or CPU :superscript:`5.2.7`

Fixes
=====

- Amazon: EKS: Fixed display and convert to managed issue with discovered EKS Clusters
- Amazon/AWS: CloudFormation: Fixed ``name`` tag value being set to logical id instead of tag value when ``name`` tag is specified in CF :superscript:`5.2.6`
- Amazon/AWS: Fixed Route53 DNS integration SDK not routing through global proxy :superscript:`5.2.7`
- Amazon/AWS: Fixed an issue that prevented AWS Gov Cloud accounts from syncing costing data through a linked AWS commercial account
- Ansible Tower: Updated ``job_executions`` : ``config_settings`` field data type to LONGTEXT
- API: Fix the ``/api/instances`` response value of ``volumes`` so it is consistent between the list and get by id actions. :superscript:`5.2.7`
- Azure: Fixed non-ASCII UTF8 characters adminPassword encoding problem
- Azure: Fixed provisioning issue when using and existing availability set :superscript:`5.2.6`
- Azure: Fixed tags created in |morpheus| not being pushed to Azure for SQL Server instance types :superscript:`5.2.6`
- Blueprints: Fixed display issue with Typeahead option types in blueprints/apps :superscript:`5.2.6`
- Blueprints: Fixed some Custom Options not saving in blueprint due to NULL code value on Option Type record :superscript:`5.2.7`
- Cisco ACI: Fixed issue creating and deleting ACI Contexts :superscript:`5.2.7`
- Cisco ACI: Fixed issue deleting ACI Tenants :superscript:`5.2.7`
- Console: Fixed paste function still showing when using Hypervisor Console mode
- Convert to Managed: Fixed bulk convert to managed issue caused by required option types not rendering when using custom instance types :superscript:`5.2.7`
- Convert to Managed: Fixed custom option types not reloading when changing layout selection during convert to managed :superscript:`5.2.7`
- Convert to Managed: Plan option will now appear if the selected VMs are all of the same type (cloud) :superscript:`5.2.7`
- Dashboard: Fixed permission scoping for widget visibility in the dashboard
- Deployments: Fixed new DEPLOY FOLDER values on Node Type not saving :superscript:`5.2.7`
- Failover Service: Fixed VMs shut down outside of |morpheus| getting auto-started by |morpheus| when another VM containing the same agent config/api key is started (from DR process or external cloning) :superscript:`5.2.7`
- Hosts: "Open Console" action removed from Hosts list action menus :superscript:`5.2.7`
- Hosts: Fixed ``Cores`` value on VM Detail pages :superscript:`5.2.7`
- Infoblox: Updated Infoblox sync process to no longer remove records from |morpheus| when there are no record found during a successful sync to account for Infblox outtage/reinstall & restore scenerio :superscript:`5.2.7`
- Jobs: Workflows: Fixed database session issue for long-running tasks executed via Operational Workflow Jobs :superscript:`5.2.7`
- KVM: Fixed VM sync for brownfield KVM Host after initial sync
- Login: Specifying an invalid/non-existent subdomain in account login url ``/login/account/<subdomain>`` now redirects to ``/login`` instead of causing error. :superscript:`5.2.6`
- Maas: Fixed Maas provisioning issue caused by null tag being passed :superscript:`5.2.6`
- NSX-T: Fixed issue removing Passive Monitors from server pools
- NSX-T: Fixed issue with health check monitors created in sub-tenants not being removed from server pools when the NSX-T integration is owned by the master tenant :superscript:`5.2.6`
- NSX-T: Improvements to NSX-T Load Balancer profile creation functionality :superscript:`5.2.7`
- NSX-V: Fixed disabling distributed firewall rules created from Morpheus UI :superscript:`5.2.7`
- NSX-V: Fixed ESG/DLR uplink interfaces deletion
- NSX-V: Fixed Load Balancer profiles not selectable from the Blueprint Apps :superscript:`5.2.7`
- NSX-V: Fixed monitor assignment for load balancer server pools in subtenants :superscript:`5.2.7`
- Option Types: Fixed issue with hidden option type value saving when toggling between layouts in provisioning wizard
- Option Types: Fixed required option type validation issue on workflow execution that could prevent workflow from executing
- Oracle Cloud: Fixed issue with provisioning Windows images in OCI not finalizing :superscript:`5.2.7`
- Policies: Approvals: Fixed cloning an Instance in a subtenant with an active approval policy not producing approval record, leaving Instance in pending approval state :superscript:`5.2.6`
- Policies: Workflow Policies: Fixed Platform filter on tasks associated with Workflows in a Workflow policy not being respected :superscript:`5.2.7`
- PowerDNS: Fixed TTL not matching TTL set in Morpheus :superscript:`5.2.7`
- Proxies: Fixed issue with Proxy settings not being applied to Windows Instances during provisioning
- Roles: Fixed Global Access "Read" having higher precedence than "Custom" :superscript:`5.2.7`
- Security: XSS Vulnerability remediated :superscript:`5.2.7`
- Service Catalog: Fixed validation error for ARM and CF Blueprint catalog item ordering :superscript:`5.2.6`
- Sync: Fixed some cloud types sycning FQDN as container/compute_server hostname, resulting in a computed FQDN of hostname>.<domain>.<domain>
- UI: Some UI pages have been updated to display data differently when the number of relevant objects is high enough to potentially impact application performance :superscript:`5.2.6`
- User Groups: User Group names are now required to be unique only inside same tenant, not unique across all tenants :superscript:`5.2.7`
- vCloud Director/vCD: Fixed issue where datastore sync would only return first 25 records :superscript:`5.2.6`
- VMware Cloud AWS/VMC: Fixed scenario causing editing modal of existing Cloud to hang :superscript:`5.2.6`
- VMware: Fixed duplicate VM names in different folders causing external Id conflict :superscript:`5.2.7`
- VMWare: Fixed Managed VM ``hostname`` changes syncing and updating server record but not associated container record :superscript:`5.2.6`
- VMware: Fixed issue with discovered Windows 2019 VM's ``os_type`` being set to ``other.64``; ``windows2019srv_64Guest`` mapping added :superscript:`5.2.8`
- VMware: vCenter: Removed name match sync function that could possibly cause wrong vm to be deleted when a provision fails to a unique name constraint in |morpheus|. external-id and uuid are now only used for sync matching :superscript:`5.2.7`
- Whitelabing: Support Menu: Fixed re-enabling Support Menus in subtenants after they have been disabled :superscript:`5.2.7`

Appliance & Agent Updates
=========================

- Appliance: - The local code repository path has been moved from ``/var/opt/morpheus/morpheus-ui/repo`` to ``/var/opt/morpheus/morpheus-local/repo`` to reduce potential shared storage issues and performance restrictions. The reconfigure process creates the folders and sets the paths in application.yml, no manual intervention is needed unless symlinks exist on ``/var/opt/morpheus/morpheus-ui/repo/git`` which will need to be removed prior to reconfiguring 5.3.2. The old ``/var/opt/morpheus/morpheus-ui/repo`` path will be automatically deleted in a future release but can be manually recursively deleted at any time for storage recursively.
- Morpheus Windows Agent: New windows agent version 1.7.0 addresses agent issue caused by new unformatted volumes being added, resulting in ```"ERROR:Error in SendAgentInit: The volume does not contain a recognized file system. Please make sure that all required file system drivers are loaded and that the volume is not corrupted."``` agent error. :superscript:`5.2.7`

Refer to :ref:`compatibility` for additional details.

|morpheus| API & CLI Improvements
=================================

- Instances: The ``details`` parameter is set to ``true`` by default for API calls to GET a specific Instance. For calls to GET all Instances, the ``details`` parameter is still ``false`` by default
- Instances: The ``instances`` endpoint now returns ``volumes`` and ``containers`` lists under ``containerDetails`` to match data which was already returned for VMs
- NSX-T: Subtenant users can access shared NSX-T integrations and load balancers through Morpheus API and CLI as they already can through Morpheus UI :superscript:`5.2.6`
- NSX-V: Router management support added in Morpheus API and CLI to match functionality currently available in Morpheus UI :superscript:`5.2.6`
- Option Lists: API calls to get all Option Lists (``api/option-type-lists/``) or get a specific Option List (``api/option-type-lists/:id``) no longer return ``listItems`` as this could potentially return millions of values in some scenarios. Users can now issue a GET request to ``/api/option-type-lists/:id/items`` to return all items in a specific Option List
- Servers: The ``servers`` API endpoint returns the ``volumes`` and ``controllers`` lists when passing the ``details=true`` parameter to match behavior already included with the ``instances`` endpoint
- ServiceNow Integration: Expose or unexpose |morpheus| Clouds, Library items, Blueprints, and Catalog Items to ServiceNow through |morpheus| API and CLI. Users can also view items which are currently exposed
