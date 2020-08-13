.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading to |morpheus| |morphver|.

|morpheus| UI Updates
*********************

Highlights
==========

New Features
============


- Amazon: Create and manage Amazon Internet Gateways 
- Amazon: Create and manage Amazon VPC Routers including syncing, creating and managing Routes
- Amazon: |morpheus| can now create or sync in a correctly-configured AWS Costing and Utilization Report (CUR) needed to consume highly-granular invoicing data in |morpheus|, previously these needed to be configured in AWS
- Amazon: Unattached AWS volumes now sync to |morpheus|
- Approvals: Added estimated pricing details to approval list and detail pages (Operations > Approvals) as well as to the price field for the request in ServiceNow for clients routing their approvals through a ServiceNow integration
- Apps: Error output exposed on App detail page in the event of a provisioning issue
- Apps: Process history details added to App detail page with tf process output 
- Apps: Provisioning process/status bar added to App detail page
- Apps: VM & Container lists added to App Detail Pages with list, stats an actions for all nodes in an App Apps: Summary tab added to App details page with App statistics 
- Azure: Added support for Azure Run Command as "RPC Mode" setting in addition to SSH/WinRM which previously existed
- Backups: Backup Jobs can be scoped to specific Tenants ("ACTIONS" > Permissions from the Backup Jobs list page)
- Blueprints: Form validation improved when creating or editing Blueprints to specifically highlight the invalid field rather than give a generic validation warning
- Clouds: Added the ability to bypass configured proxy traversal for a specific group of IP addresses or name servers
- Clusters: Scope Clusters by Group, Service Plan, or Tenant by clicking Permissions from inside the "MORE" dropdown on the Clusters list page
- Identity Sources: Identity source integrations can now be configured from the Users page (Administration > Users). This allows Tenant administrators to configure these integrations without giving access to the Tenants page (Administration > Tenants), which exposes information on other Tenants
- Networks: Added capability to activate and deactivate network security groups when creating or editing (Infrastructure > Networks > Security Groups)
- NSX-T: Added ability to created, manage, and delete NSX-T IP Pools from |morpheus|
- NSX-T: Added support for version 3
- NSX-T: Create, manage and delete NSX-T load balancers from the scale tab of the Instance detail page
- OpenTelekom Cloud: A floating IP can now have variable bandwidth, option is available in the Instance and App provisioning wizards
- Oracle VM: Images with the same name syncing from multiple Oracle VM Clouds are now grouped for easier selection when creating Node Types similar to the way they are already grouped for VMware Clouds
- Reports: Added Software Inventory report to group together servers in a chosen cloud which are running specific software
- Reports: Added the Software Inventory By Server report to list out all software running on each server within the chosen cloud
- Roles: "Group" feature permission added to "Infrastructure: Clouds". When selected, the user will only see Clouds in their assigned Groups when viewing the Cloud list page (Infrastructure > Clouds)
- Roles: Added controls around Instance actions (Provisioning > Instance > Selected Instance > Actions): "Provisioning: Clone Instance", "Provisioning: Execute Script", "Provisioning: Execute Task", Provisioning: Execute Workflow", "Provisioning: Import Image"
- Roles: User roles can be manually assigned for users coming through an identity source integration rather than being locked to the automatic mapping based on their role in the identity service
- Security: General security enhancements
- Tasks: Added the option to ignore SSL errors for HTTP Tasks to allow REST calls to systems without a trusted SSL certificate
- Terraform: All tf app created resources are now inventoried  Terraform: Added support for generated keypairs in terraform
- Terraform: Azure support added
- Terraform: Implemented template validation in App wizard prior to review step.
- Terraform: Morpheus now continuously refresh state looking for drift Terraform: Preview section added to Blueprint and App Modals
- Terraform: v0.12 support added
- UI: Advanced and customizable views added to many new UI pages including the integrations list page (Administration > Integration), the network domains tab (Infrastructure > Network > Domains), the network groups tab (Infrastructure > Network > Network Groups), the network IP pools tab (Infrastructure > Network > IP Pools), the network proxies tab (Infrastructure > Network > Proxies), the network routers tab (Infrastructure > Network > Routers), the network security groups tab (Infrastructure > Network > Security Groups), the network list page (Infrastructure > Network), the user groups list page (Administration > Users > User Groups), the users list page (Administration > Users). In addition, these capabilities and views have been standardized across supported pages
- UI: Advanced views and filtering added to networks list page (Infrastructure > Networks)
- UI: Environment Tag field relabeled as "Environment" on Group tab of the Instance provisioning wizard
- UI: The Clouds list page (Infrastructure > Clouds) is now paginated
- vCloud Director: Veeam servers can now be selected as backup destinations for vCD Clouds, restore actions are also supported
- Whitelabeling: Improved handling of whitelabel images for the login screen to prevent low image quality in specific scenarios

Fixes
=====

- Roles: Access to the Network Proxies tab (Infrastructure > Networks > Proxies) is now controlled exclusively by the "Infrastructure: Network Proxies" feature permission
- Roles: Access to monitoring settings (Administration > Monitoring) is now controlled exclusively by the "Admin: Monitoring Settings" feature permission

|morpheus| API Updates
**********************

API Enhancements
================

- Azure: Added granular invoice and line item costing as we currently have for Amazon and Oracle Clouds
- Azure: CSP pricing support
- Billing: Service Plan Name (servicePlanName) can now be returned from the Billing API
- Networks: Security Groups can now be activated and deactivated
- User Sources: The ``userSources`` API now returns ``externalLogin`` and ``allowCustomMappings`` fields
- Users: Users across all Tenants can now be returned with a single call

API Fixes
=========

|morpheus| CLI Updates
**********************

CLI Enhancements
================

- Networks: Security Groups can now be activated and deactivated
- User Sources: External Login and Allow Custom Mappings can now be displayed

CLI Fixes
=========
