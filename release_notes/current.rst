.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: Items appended with :superscript:`5.2.x` are also included in that version

.. include:: highlights.rst

New Features
============

- Ansible Tower: Added Inventories tab to Ansible Tower integration detail pages (Administration > Integrations > Selected existing Ansible Tower integration) to surface inventories by name and allow for configuration related to Tenant defaults
- Ansible Tower: Added Tenant default execution of Ansible Tower Jobs. Tower Jobs created in the Master Tenant can be set to Tenant default execution mode which, when shared and run in a Subtenant, ensures the Job is automatically run against inventories associated with the Tenant of execution
- Ansible Tower: Associate default inventories with |morpheus| Tenants from the inventory permissions menu (Administration > Integrations > Selected Ansible Tower integration > Inventory tab > MORE menu > Permissions). When executing a Tower Job and selecting the Tenant Default inventory mode, the inventories associated with the Tenant are automatically selected
- Ansible Tower: Select "Static" or "Tenant Default" inventory modes when building Ansible Tower Job Tasks or running an Ansible Tower Job at provision time. Selecting Static allows the user to choose any inventory available within the integration while Tenant Default hides the inventory select list and automatically selects default inventories for the Tenant
- Ansible: ``DEFAULT BRANCH`` git setting added for Ansible integrations :superscript:`5.2.6`
- Boot Menus: Track type values (bios, uefi, ipxe, grub) on Boot Menus (Infrastructure > Boot > Boot Menus)
- Budgets: Fixed subtenant costs from clouds owned by master tenant not displaying in the master tenant budget graphs for Tenant scoped budgets
- CloudFormation: Instances based on CloudFormation spec now have a State tab on the Instance detail page. Check for state drift, edit the resource spec, and apply state directly from the Instance detail page
- Costing: Aggregation of both metered and actual costing data now supported by summary invoices :superscript:`5.2.6`
- Costing: Amazon: Invoice Line Item costs associated with aws ``global`` region are now associated with us-east-1 region invoices
- Costing: Improvements to Tenant, Group, and Cloud Invoice Summary calculations :superscript:`5.2.6`
- Costing: Invoices associated with Clouds owned by master tenant but assigned to or shared with subtenants are now visible in the master Tenant UI (previously only listed for Master Tenant users via API/CLI) :superscript:`5.2.6`
- GCP: Added the ability to create GCP Projects from within |morpheus|. Projects are added as Resource Pools from the Cloud detail page (Infrastructure > Clouds > Selected GCP Cloud > Resources tab)
- GCP: Added the ability to scope GCP Cloud inegrations to all Projects and/or all regions
- GCP: Create and manage Google networks from the networks list page (Infrastructure > Networks)
- GCP: Create and manage Security Groups scoped to GCP Clouds
- GCP: Create and manage subnets for Google networks (Infrastructure > Networks > Selected Google network > Subnets tab)
- GCP: Firewall tab added to Google network detail page for creating and managing firewall rules
- GCP: Google Cloud Instance IDs are now synced into |morpheus| as the internalId server variable value
- GCP: Improved pricing sync and computation
- GCP: Sync, create and manage Google Cloud routers (Infrastructure > Networks > Routers tab)
- GCP: Sync, create and manage Google NAT Gateways (Infrastructure > Networks > Routers tab)
- GCP: Update sync process to onboard Google networks and subnets distinctly. Previously, subnets were onboarded as |morpheus| networks
- Library: Canonical MaaS and Lumen Edge are now selectable as technology types for Library items such as Layouts and Node Types :superscript:`5.2.4`
- Library: Kubernetes 1.20 cluster layouts (MKS, AKS, and EKS) added to the default library for many Cloud types including Amazon, VMware, Azure, Google, Nutanix, OpenStack, and more
- Load Balancers: When configuring an Amazon ALB for an Instance, added stickiness mode setting, balance mode setting, and session duration setting
- Logging: Added support for custom NGINX log formats by updating ``morpheus.rb`` with a new ``log_format_name`` and ``log_format value``
- Logging: Kubernetes container logs are now shown in the Logs tab of the Cluster detail page (Infrastructure > Clusters > Selected Kubernetes cluster > Logs tab)
- NSX-T: Distributed firewalls for NSX-T integrations shared with a subtenant can now be created and managed by subtenant users :superscript:`5.2.5`
- NSX-T: Load balancer rule creation capability added as part of load balancer virtual server creation in Morpheus UI :superscript:`5.2.5`
- NSX-T: Load balancers and LB virtual servers for NSX-T integrations shared with a subtenant can now be created and managed by subtenant users :superscript:`5.2.5`
- NSX-T: Visibility permissions added to NSX-T integrations allowing master tenant administrators to share integrations with subtenants :superscript:`5.2.5`
- NSX-V: Configure DHCP and DHCP log levels on Edge Gateways :superscript:`5.2.4`
- NSX-V: Create and manage DHCP Bindings for Edge Gateways :superscript:`5.2.4`
- NSX-V: Create and manage DHCP Pools for Edge Gateways :superscript:`5.2.4`
- NSX-V: Create and manage DHCP Relay for Edge Gateways and Logical Routers :superscript:`5.2.4`
- NSX-V: Visibility permissions added to NSX-T integrations allowing master tenant administrators to share integrations with subtenants :superscript:`5.2.5`
- Plugins: Added soft reloads for updating Plugins. An updated plugin file can now be uploaded without having to delete the previous file, preserving settings such as Role Access permissions. :superscript:`5.2.4`
- Plugins: Added support for custom report type creation
- Plugins: Added support for custom server tab creation
- Reports: Improvements to Tenant and Group costing reports
- Security: Two-factor authentication added for |morpheus| local users as well as users from Active Directory and LDAP identity sources :superscript:`5.2.5`
- Settings: "Reuse Naming Sequence Numbers" setting in Administration > Settings > Provisioning now applies to all Instance naming patterns using ``${sequence}`` values. Previously Reuse Naming Sequence Numbers = false was only applicable for Naming Policies :superscript:`5.2.4`
- Settings: Add IP addresses or hostnames to approved or denied lists which limits users to only approved sources when creating HTTP Tasks or populating Option Lists through REST calls. Previously, specific hosts could be denied but now administrators can opt to deny all hosts except those which are specifically approved :superscript:`5.2.5`
- Terraform: Build new Instance Types from Terraform spec, then deploy and conduct day-two operations such as monitoring and applying state, updating spec, and more
- UI: Added dropdown list functionality to Option Types using Typeahead lists which gives users the ability to browse the list if the name of the target item is not precisely known
- UI: Added support for French UI translation
- UI: Added view customization to Tasks and Workflow lists (Provisioning > Automation) including support for customizing output columns (Gear icon) and sorting the list by additional columns
- UI: Automation executions list (Provisioning > Automation > Executions tab) updated for a cleaner look and easier access to execution outputs
- UI: Hosts list page (Infrastructure > Hosts) is now relabeled as Compute (Infrastructure > Compute) and now lists containers and resources in addition to Hosts, VMs, and Bare Metal which were shown previously. The Containers tab shows any containers which are associated with |morpheus| Instances while the Resources tab shows IaC resources, such as those from Terraform, CloudFormation or ARM templates
- VDI: |morpheus| VDI is no longer a beta feature
- VDI: Added local printer support
- VDI: Added VDI console gateway
- VDI: Added VDI jump host feature

Fixes
=====

- Administration: Health: Fixed scenario where ``/admin/health`` ui page would throw 403 error :superscript:`5.2.6`
- Amazon/AWS: Fixed discovered server volume discovery for non io1/gp2 volumes. :superscript:`5.2.6`
- Amazon/AWS: LBs: Fixed AWS Load Balancer target groups configured for for HTTPS on 443 being set as HTTP on 443 :superscript:`5.2.6`
- Ansible: Resolved issue creating Ansible integrations where the default git branch is ``main`` with the new ``DEFAULT BRANCH`` integration setting. :superscript:`5.2.6`
- App: Fixed error messages that contained database exception response :superscript:`5.2.5`
- Azure: Fixed evaluated name not being used for Azure public ip dns hostname when using Naming Policy containing ``customOptions`` variable(s), causing "DNS name label not available" error :superscript:`5.2.4`
- Azure: Fixed network sync issue when multiple address Prefixes exist for the ip range on a network and subnet :superscript:`5.2.4`
- Azure: Fixed sync issue where a public IP would still show in |morpheus| for Azure Instances when the Public IP has been deleted/removed in Azure :superscript:`5.2.4`
- Backups: Fixed default schedule displayed on backup screen when no job schedule is configured :superscript:`5.2.5`
- Blueprints: Fixed Custom Options value overrides reverting to default value when saving Blueprints. :superscript:`5.2.4`
- CLI: Service Plans: Group Permissions: Fixed ``service-plans update <servicePlanId> --group-access-all on`` setting Group Visibility to ``null`` :superscript:`5.2.4`
- Cloud-init: Fixed multiple Default Gateway flags when creating multiple networks :superscript:`5.2.5`
- Clusters: Kubernetes: Fixed issue with VM and DNS naming discrepancies when using a Cluster Resource Name/Host Name Policy (Note the "Host Name" Policy type has been renamed to "Cluster Resource Name") :superscript:`5.2.4`
- Costing: Improvements to Invoice cost currency conversion :superscript:`5.2.6`
- Costing: Fix for scenario where container costs were counted twice on summary invoices :superscript:`5.2.6`
- Costing: Fixed actuals not reflected in MTD Costs in summary invoices :superscript:`5.2.6`
- Dell Isilon: Fixed share creation not creating the share in the correct storage group :superscript:`5.2.4`
- Hosts/Compute: Advanced Filters: Removed "Discovered" option from ``STATUS`` filter as it was being confused with Server Type "Discovered" (Discovered is a Status for Bare Metal Servers) :superscript:`5.2.4`
- IPAM: Fixed issue where editing an IPAM integration from Administration -> Integrations section would set invalid integration ref. :superscript:`5.2.6`
- Microsoft DNS: Integration validation requests now use elevated flag to lower service account permission requirements :superscript:`5.2.4`
- Networks: Reduced network activity and connections when "Scan Network" is enabled on a Network :superscript:`5.2.4`
- NSX-T: Fixed issue with health check monitors created in sub-tenants not being removed from server pools when the NSX-T integration is owned by the master tenant  :superscript:`5.2.6`
- NSX-T: Fixed network delete when network is part of a network group :superscript:`5.2.5`
- Pricing: Removed price estimates in reconfigure modal when 'Show Pricing' admin setting is disabled. :superscript:`5.2.6`
- Reports: Tenant Usage Report: Removed additional unreadable date being include when exporting Tenant Usage Reports :superscript:`5.2.4`
- Roles: Updated error handling for editing VDI Pool Access permissions on roles in subtenants
- Rubrik: Blueprints: Fixed SLA Domain option not displayed in Blueprints :superscript:`5.2.4`
- Security: Fixed occurrence of user csrf token being transmitted via query string parameter :superscript:`5.2.4`
- Security: XSS vulnerabilities closed for Reconfigure and Library :superscript:`5.2.4`
- Service Catalog: Option Types:  Fixed VISIBILITY FIELD not respecting``matchAll`` logic :superscript:`5.2.5`
- Snapshots: Fixed revert action failing on Brownfield Snapshots when compute_server moved to another tenant :superscript:`5.2.5`
- UI: Fixed unexpected logouts due to Session Expiration in another non-active tab :superscript:`5.2.4`
- VMware: Folders: Fixed Group Access -> Default Folder setting only saving for one cloud when multiple VMware Clouds are in the same target Group :superscript:`5.2.5`
- Workflows: Clusters provisioned used cluster layouts that have a workflow selected are now properly running the workflow at provisioning time.  :superscript:`5.2.6`
- Workflows: Fixed issue with available Group scoping during Task execution on Instances where the Instances' assigned Group is not accessible to the User who created the Instance. :superscript:`5.2.4`
- Workflows: Fixed Task phase assignment changing upon edit and save of a Workflow when using the same Task in multiple phases in the same Workflow :superscript:`5.2.4`

Appliance & Agent Updates
=========================

- Appliance: mysql: Added ``mysql['max_connections']`` setting option to ``/etc/morpheus/morpheus.rb`` file for configuring system mysql max_connections parameter. Note the ``mysql['max_connections']`` setting only applies to the system managed mysql appliance service, not applicable for external appliance database configurations. 
- Appliance & Agent java version updated to ``8u292-b10``

  .. important:: jdk8u292 disables TLS 1.0 and 1.1 by default.

Refer to :ref:`compatibility` for additional details.

|morpheus| API & CLI Improvements
=================================
- Azure: Added "All" region support for Azure Clouds to |morpheus| API and CLI
- Billing: The ``billing`` API endpoint now returns ``resourcePoolId`` and ``resourcePoolName`` :superscript:`5.2.4`
- Clouds: ``scalePriority`` is now handled properly for get, add and update requests to the ``clouds`` API :superscript:`5.2.4`
- VDI: Added support for creating and managing VDI Pools, Apps, and Gateways through |morpheus| API and CLI

Fixes
-----

- API: Fixed Access to virtual images not allowed in UI but successful using the API :superscript:`5.2.4`
- API: Prices: Fixed ```account`` value not respected when creating a price and assigning to a Tenant. :superscript:`5.2.4`