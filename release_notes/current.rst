.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: Features appended with :superscript:`5.2.4` or :superscript:`5.2.5` debuted previously in the 5.2.x LTS version

.. include:: highlights.rst

New Features
============
- Ansible Tower: Added Tenant default execution of Ansible Tower Jobs. Tower Jobs created in the Master Tenant can be set to Tenant default execution mode which, when shared and run in a Subtenant, ensures the Job is automatically run against inventories associated with the Tenant of execution
- Ansible Tower: Added Inventories tab to Ansible Tower integration detail pages (Administration > Integrations > Selected existing Ansible Tower integration) to surface inventories by name and allow for configuration related to Tenant defaults
- Ansible Tower: Select "Static" or "Tenant Default" inventory modes when building Ansible Tower Job Tasks or running an Ansible Tower Job at provision time. Selecting Static allows the user to choose any inventory available within the integration while Tenant Default hides the inventory select list and automatically selects default inventories for the Tenant
- Ansible Tower: Associate default inventories with |morpheus| Tenants from the inventory permissions menu (Administration > Integrations > Selected Ansible Tower integration > Inventory tab > MORE menu > Permissions). When executing a Tower Job and selecting the Tenant Default inventory mode, the inventories associated with the Tenant are automatically selected
- Boot Menus: Track type values (bios, uefi, ipxe, grub) on Boot Menus (Infrastructure > Boot > Boot Menus)
- CloudFormation: Instances based on CloudFormation spec now have a State tab on the Instance detail page. Check for state drift, edit the resource spec, and apply state directly from the Instance detail page
- Costing: Invoices associated with Clouds owned by master tenant but assigned to or shared with subtenants are now visible in the master Tenant UI (previously only listed for Master Tenant users via API/CLI)
- Costing: Improvements to Tenant, Group, and Cloud Invoice Summary calculations
- Costing: Aggregation of both metered and actual costing data now supported by summary invoices
- Costing: Improvements to Invoice cost currency conversion
- Costing: Fix for scenario where container costs were counted twice on summary invoices
- Costing: Fixed actuals not reflected in MTD Costs in summary invoices
- Costing: Amazon: Invoice Line Item costs associated with aws ``global`` region are now associated with us-east-1 region invoices
- Budgets: Fixed subtenant costs from clouds owned by master tenant not displaying in the master tenant budget graphs for Tenant scoped budgets
- GCP: Added the ability to create GCP Projects from within |morpheus|. Projects are added as Resource Pools from the Cloud detail page (Infrastructure > Clouds > Selected GCP Cloud > Resources tab)
- GCP: Added the ability to scope GCP Cloud inegrations to all Projects and/or all regions
- GCP: Create and manage Google networks from the networks list page (Infrastructure > Networks)
- GCP: Create and manage subnets for Google networks (Infrastructure > Networks > Selected Google network > Subnets tab)
- GCP: Sync, create and manage Google Cloud routers (Infrastructure > Networks > Routers tab)
- GCP: Sync, create and manage Google NAT Gateways (Infrastructure > Networks > Routers tab)
- GCP: Update sync process to onboard Google networks and subnets distinctly. Previously, subnets were onboarded as |morpheus| networks
- GCP: Create and manage Security Groups scoped to GCP Clouds
- GCP: Firewall tab added to Google network detail page for creating and managing firewall rules
- GCP: Improved pricing sync and computation
- GCP: Google Cloud Instance IDs are now synced into |morpheus| as the internalId server variable value
- Library: Canonical MaaS and Lumen Edge are now selectable as technology types for Library items such as Layouts and Node Types :superscript:`5.2.4`
- Library: Kubernetes 1.20 cluster layouts (MKS, AKS, and EKS) added to the default library for many Cloud types including Amazon, VMware, Azure, Google, Nutanix, OpenStack, and more
- Load Balancers: When configuring an Amazon ALB for an Instance, added stickiness mode setting, balance mode setting, and session duration setting
- Logging: Added support for custom NGINX log formats by updating ``morpheus.rb`` with a new ``log_format_name`` and ``log_format value``
- NSX-T: Visibility permissions added to NSX-T integrations allowing master tenant administrators to share integrations with subtenants :superscript:`5.2.5`
- NSX-T: Distributed firewalls for NSX-T integrations shared with a subtenant can now be created and managed by subtenant users :superscript:`5.2.5`
- NSX-T: Load balancers and LB virtual servers for NSX-T integrations shared with a subtenant can now be created and managed by subtenant users :superscript:`5.2.5`
- NSX-T: Load balancer rule creation capability added as part of load balancer virtual server creation in Morpheus UI :superscript:`5.2.5`
- NSX-V: Visibility permissions added to NSX-T integrations allowing master tenant administrators to share integrations with subtenants :superscript:`5.2.5`
- NSX-V: Configure DHCP and DHCP log levels on Edge Gateways :superscript:`5.2.4`
- NSX-V: Create and manage DHCP Pools for Edge Gateways :superscript:`5.2.4`
- NSX-V: Create and manage DHCP Relay for Edge Gateways and Logical Routers :superscript:`5.2.4`
- NSX-V: Create and manage DHCP Bindings for Edge Gateways :superscript:`5.2.4`
- Reports: Improvements to Tenant and Group costing reports
- Security: Two-factor authentication added for |morpheus| local users as well as users from Active Directory and LDAP identity sources :superscript:`5.2.5`
- Settings: Add IP addresses or hostnames to approved or denied lists which limits users to only approved sources when creating HTTP Tasks or populating Option Lists through REST calls. Previously, specific hosts could be denied but now administrators can opt to deny all hosts except those which are specifically approved :superscript:`5.2.5`
- UI: Automation executions list (Provisioning > Automation > Executions tab) updated for a cleaner look and easier access to execution outputs
- UI: Added support for French UI translation
- VDI: |morpheus| VDI is no longer a beta feature
- VDI: Added VDI jump host feature
- VDI: Added VDI console gateway
- VDI: Added local printer support

Fixes
=====

Appliance Updates
=================


|morpheus| API & CLI Improvements
=================================
- Billing: The ``billing`` API endpoint now returns ``resourcePoolId`` and ``resourcePoolName`` :superscript:`5.2.4`
- Clouds: ``scalePriority`` is now handled properly for get, add and update requests to the ``clouds`` API :superscript:`5.2.4`

Enhancements
------------


Fixes
-----

- Oracle Cloud: Fixed an issue that prevented Oracle Linux Layouts from being provisioned onto Oracle Clouds in certain scenarios

Agent/Node Package Updates
==========================
