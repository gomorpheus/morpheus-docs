.. _Release Notes:

************************
|morphver| Release Notes
************************

.. No highlights this time, small update
  .. include:: highlights.rst

New Features
============

- Ansible: ``DEFAULT BRANCH`` git setting added for Ansible integrations
- Logging: Added support for custom NGINX log formats by updating ``morpheus.rb`` with a new ``log_format_name`` and ``log_format`` value
- NSX-T: Create and manage NSX-T load balancer profiles (Infrastructure > Load Balancers > Selected Load Balancer > Profiles Tab), previously this tab was read-only
- Software: Patch version numbers are now surfaced on the Software tab of server detail pages (mouse hover over software name) and in Software reports
- vCloud Director: Added support for API version 34.0 on vCD 10.2+

|morpheus| API Improvements
===========================

- 2FA: Enable, disable and manage two-factor authentication settings with |morpheus| API and CLI
- Integrations: Create and manage integrations between |morpheus| and third-party technologies (including Ansible, ServiceNow, Git, Github, and several more) via |morpheus| API and ClI
- Networking: Add a NIC to existing VMs through |morpheus| API
- NSX-T: Existing Server Pool Member IP addresses can now be edited 
- NSX-T: Subtenant users can access shared NSX-T integrations and load balancers through |morpheus| API and CLI as they already can through |morpheus| UI
- NSX-V: Router management support added in |morpheus| API and CLI to match functionality currently available in |morpheus| UI

Fixes
=====

- Administration: Health: Fixed scenario where ``/admin/health`` ui page would throw 403 error
- Amazon/AWS: CloudFormation: CF Blueprints & Spec Templates: Fixed issue where ``default`` user was not included in user metadata causing specified ``keyName`` key to not be added to the ami's default users ``authorized_keys`` file unless ``default`` was set as a created users name
- Amazon/AWS: Fixed discovered server volume discovery for non io1/gp2 volumes.
- Amazon/AWS: LBs: Fixed AWS Load Balancer target groups configured for for HTTPS on 443 being set as HTTP on 443
- Ansible: Resolved issue creating Ansible integrations where the default git branch is ``main`` with the new ``DEFAULT BRANCH`` integration setting.
- IPAM: Fixed issue where editing an IPAM integration from Administration -> Integrations section would set invalid integration ref.
- Login: Specifying an invalid/non-existent subdomain in account login url ``/login/account/<subdomain>`` now redirects to ``/login`` instead of causing error. 
- Maas: Fixed Maas provisioning issues caused by null tag being passed
- NSX-T: Fixed issue with health check monitors created in sub-tenants not being removed from server pools when the NSX-T integration is owned by the master tenant 
- Oracle Cloud: Fixed an issue that prevented Oracle Linux Layouts from being provisioned onto Oracle Clouds in certain scenarios
- Pricing: Removed price estimates in reconfigure modal when 'Show Pricing' admin setting is disabled. 
- UI: Some UI pages have been updated to display data differently when the number of relevant objects is high enough to potentially impact application performance
- vCloud Director/vCD: Fixed issue where datastore sync would only return first 25 records
- VMware Cloud AWS/VMC: Fixed scenario causing editing modal of existing Cloud to hang
- VMware: Fixed duplicate VM names in different folders causing external Id conflict
- Workflows: Clusters provisioned used cluster layouts that have a workflow selected are now properly running the workflow at provisioning time. 
- Amazon/AWS: CloudFormation: Fixed ``name`` tag value being set to logical id instead of tag value when ``name`` tag is specified in CF 
- Service Catalog: Fixed validation error for ARM and CF Blueprint catalog item ordering
- Azure: Fixed tags created in |morpheus| not being pushed to Azure for SQL Server instance types
- Azure: Fixed provisioning issue when using and existing availability set
- Blueprints: Fixed display issue with Typeahead option types in blueprints/apps
- VMWare: Fixed Managed VM ``hostname`` changes syncing and updating server record but not associated container record
- Policies: Approvals: Fixed cloning an Instance in a subtenant with an active approval policy not producing approval record, leaving Instance in pending approval state

Appliance Updates
=================

- Appliance: mysql: Added ``mysql['max_connections']`` setting option to morpheus.rb for configuring system mysql max_connections parameter. Note the ``mysql['max_connections']`` setting only applies to the system managed mysql appliance service, not applicable for external appliance database configurations. 
- Appliance & Agent java version updated to ``8u292-b10``

  .. important:: jdk8u292 disables TLS 1.0 and 1.1 by default.

Refer to :ref:`compatibility` for additional details.

..
 - Azure: Pricing fields removed for Service Plans where no pricing is available from Azure


 

 
 VMWare: Managed VM Hostname updates not synced into container record
 
