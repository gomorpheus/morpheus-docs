.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading |morpheus|

New Features
------------

- Amazon AWS Cloud Integration: Hong Kong region (ap-east-1) support added

- .. toggle-header:: :header: **Azure Clouds Integration Enhancements**

    - Azure Marketplace images now synced by region rather than by Cloud
    - Azure pricing now synced by region and currency rather than Cloud
    - Azure VM sizes (Service Plans) now synced by region rather than Cloud

- .. toggle-header:: :header: **NSX-T Integration Improvements**

    - Scope NSX-T routers to Groups and assign visibility permissions for Tenants
    - Set Tenant visibility permissions for Transport Zones
    - Added Edge Cluster inventorying from NSX-T integrations
    - Set Tenant visibility permissions for Edge Clusters
    - Tenants can view NAT rules for T-0 and T-1 routers they have been given access
    - Create and manage NAT rules for T-0 and T-1 routers
    - T-1 Interfaces tab renamed to Services Interfaces for clarity
    - Added role-based access permissions for all tabs on T-0 and T-1 routers

- Networks: Set Tenant visibility permissions for IP pools

- .. toggle-header:: :header: **Role Permission Changes**

    - Added access permissions for NSX-T T-0 and T-1 router tabs

- Openstack: Service Endpoints section added to Cloud config for manually overriding OpenStack API endpoints

- Security Scanning: Windows support added for SCAP security scans

- .. toggle-header:: :header: **UI and Usability Improvements**

    - Tokens in forgot/reset password email now expire after seven days

Fixes
-----

- Amazon: ALB’s: Fix for adding ALBs in a subtenant :superscript:`+`
- Amazon: Fixed S3 Bucket create and delete not utilizing AWS Cloud API Proxy config :superscript:`+`
- Analytics: Fixed Utilization vs. cost not reflecting Tenant Currency setting
- Ansible Tower: Fixed Inventory sync issue preventing jobs from triggering. Note: Ansible Tower tasks may need to be re-lined to tower jobs post 4.2.5 update.
- Ansible: Ansible integrations now utilize Global Proxy config for repo connections :superscript:`+`
- Automation: Fixed output of post-provision powershell tasks not displaying in process history.
- Blueprints: Fixed creating Blueprint configs using Azure/ARM Spec templates
- Certificates: Fixed legacy Add Certificate modal displayed when no trust provider integration has been added
- Clusters: Fixed system VMware HA Kubernetes layouts
- Commvault: Fixed issue with subtenant Commvault Backup Job completion when Backup and Backup Job names use custom values :superscript:`+`
- Github: Github integrations now utilize Global Proxy config for Github connections :superscript:`+`
- Identity Sources: SAML: Fixed issue with checkbox rendering in Firefox browsers :superscript:`+`
- Infoblox: Added PTR Record creation to Infoblox
- NSX-T: Fixed issue loading provisioned Tier0 & Tier1 gateways in a subtenant
- NSX-V: Fixed DLR's displaying up in the create network page outside of group scope
- NSX-V: Fixed members not automatically being added to NSX-V pools during Instance & App provisioning.
- NSX-V: Fixed new Firewall rules creation for DLR's created with group scoping
- OTC: Fixed min disk issue when uploading raw images to OTC from |morpheus|
- Policies: Extended 255 character limits for Instance ``unformatted_name`` and ``unformatted_name`` fields to allow for longer naming policies.
- Policies: Fixed Approval policy conflict when an active Workflow, Tag Compliance, or Storage policy is applied.
- Policies: Fixed issue with expiration policies not removing resources which are in a failed state :superscript:`+`
- Policies: Fixed scenario where warning emails for expiring Instances not triggered
- Policies: Power Schedule Policies will no longer power on a VM that has been shutdown and is in "Pending Removal" state from a Delayed Removal Policy.
- Tags: Fixed deleting Tags created from Option Type from Instances
- Tenants: Fixed Tenant deletion issue related to existing network_security_server records :superscript:`+`

API & CLI Enhancements
----------------------

- Hosts: Added ability to tag servers (hosts). These are automatically updated when Instance tags are updated but useful for tagging discovered servers (currently API only)
- Instances: Passing ``masked=true`` flag for tags masks the value of the tag
- Metadata: Metadata tags now referred to as ``tags`` and labels now referred to as ``labels``, previously metadata tags were referred to as ``metadata`` and labels were referred to as ``tags``
- Snapshots: Create and view snapshots
- Monitoring: Fixed /monitoring/push endpoint returning 401 unauthorized 
- Approvals: Fixed /api/approvals/<app_approval_id> returning 403 error. 
- Hosts: Fixed issue with listing hosts with as a subtenant user.

- .. toggle-header:: :header: **Virtual Images**

    - Associated ``volumes`` are returned with ``maxStorage`` viewable for each
    - Added ability to tag Virtual Images (currently API only)
    
    
.. note::

	:superscript:`+` Indicates updates included in v5.2.0.
