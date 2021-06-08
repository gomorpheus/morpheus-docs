.. _Release Notes:

************************
|morphver| Release Notes
************************

.. No highlights this time, small update
  .. include:: highlights.rst

New Features
============

- Keys & Certs: Added support for NSX-T SSL certificate creation (Infrastructure > Keys & Certs > SSL Certificates tab) when an NSX-T integration is present
- VMware vCenter: CPU and memory hot-add settings are now evaluated independently when reconfiguring CPU and memory for vCenter Instances. Previously, these settings were evaluated as a group rather than independently which could cause VMs to be restarted even when they were configured to support hot-add of memory and/or CPU

|morpheus| API Improvements
===========================

- Jobs: Updated Jobs to run against multiple targets in parallel rather than sequentially. Job execution records are added for each target rather than just for the latest target as was the case previously
- Keys & Certs: Added support for NSX-T SSL certificate creation through |morpheus| API when an NSX-T integration is present

Fixes
=====

- Amazon/AWS: Fixed Route53 DNS integration SDK not routing through global proxy
- API: Added support a new query parameter ``details=true`` to return more details about an instance, ie. containerDetails. This parameter applies to both list and get by id, and defaults to false because it increases the payload size and response time.
- API: Fix the ``/api/instances`` response value of ``volumes`` so it is consistent between the list and get by id actions.
- Blueprints: Fixed some Custom Options not saving in blueprint due to NULL code value on Option Type record
- Cisco ACI: Fixed issue creating and deleting ACI Contexts
- Cisco ACI: Fixed issue deleting ACI Tenants 
- Convert to Managed: Fixed bulk convert to managed issue caused by required option types not rendering when using custom instance types
- Convert to Managed: Fixed custom option types not reloading when changing layout selection during convert to managed
- Convert to Managed: Plan option will now appear if the selected VMs are all of the same type (cloud)
- Custom Table Views: Names for Views are now limited to alphanumeric characters
- Deployments: Fixed new DEPLOY FOLDER values on Node Type not saving
- Failover Service: Fixed VMs shut down outside of |morpheus| getting auto-started by |morpheus| when another VM containing the same agent config/api key is started (from DR process or external cloning)
- Hosts: "Open Console" action removed from Hosts list action menus
- Hosts: Fixed ``Cores`` value on VM Detail pages
- Infoblox: Updated Infoblox sync process to no longer remove records from |morpheus| when there are no record found during a successful sync to account for Infblox outtage/reinstall & restore scenerio
- Jobs: Workflows: Fixed database session issue for long-running tasks executed via Operational Workflow Jobs
- NSX-T: Improvements to NSX-T Load Balancer profile creation functionality
- NSX-V: Fixed disabling distributed firewall rules created from Morpheus UI
- NSX-V: Fixed Load Balancer profiles not selectable from the Blueprint Apps
- NSX-V: Fixed monitor assignment for load balancer server pools in subtenants
- Oracle Cloud: Fixed issue with provisioning Windows images in OCI not finalizing
- Policies: Tag Policies: Fixed Strict Enforce Tag policies preventing new tag creation from |morpheus| API
- Policies: Workflow Policies: Fixed Platform filter on tasks associated with Workflows in a Workflow policy not being respected
- PowerDNS: Fixed TTL not matching TTL set in Morpheus
- Roles: ``Blueprint Access: Global Access`` setting now defaults to ``None``
- Roles: Fixed Global Access "Read" having higher precedence than "Custom"
- User Groups: User Group names are now required to be unique only inside same tenant, not unique across all tenants
- VMware: vCenter: Removed name match sync function that could possibly cause wrong vm to be deleted when a provision fails to a unique name constraint in |morpheus|. external-id and uuid are now only used for sync matching
- Whitelabing: Support Menu: Fixed re-enabling Support Menus in subtenants after they have been disabled
NSX-V: Fixed |morpheus| generated self-signed certificates not selectable at the time of Load balancer HTTPS based application profile creation

Appliance Updates
=================
  
- Morpheus Windows Agent: New windows agent version 1.7.0 addresses agent issue caused by new unformatted volumes being added, resulting in ```"ERROR:Error in SendAgentInit: The volume does not contain a recognized file system. Please make sure that all required file system drivers are loaded and that the volume is not corrupted."``` agent error.
