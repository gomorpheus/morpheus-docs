.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. IMPORTANT:: |morphver| contains embedded MySQL v8 upgrade when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances)
.. IMPORTANT:: Minimum v6.x required to upgrade to |morphver| for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6, or 6.1.0 - 6.2.1 prior to upgrading to |morphver|
.. WARNING:: Rolling upgrades for HA environments using embedded RabbitMQ and/or embedded Elasticsearch services are not supported when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:Dashboard: - The Dashboard plugin has been updated to support German, French, and Italian localizations :superscript:`6.3.4`
:Inputs: - On the Instance detail page under the Runtime tab, the "Option Types" subtab has been relabeled "Inputs" :superscript:`6.3.4 `
:Nutanix Prism Central: - Added Terraform support to Nutanix Prism Central plugin :superscript:`6.3.4`
:Security: - Embedded Tomcat upgraded to 9.0.83 to mitigate CVE-2023-46589 :superscript:`6.3.4`
:Veeam: - Added official support for Veeam 12 :superscript:`6.3.4`


Fixes
=====

:API & CLI: - Access token refresh is now working properly. If the call is made while the token is valid, the ``expires_in`` property indicates how many more seconds until it expires. If the access token has expired, it refreshes the token and resets the expire date :superscript:`6.3.4`
             - Adding or updating Identity Sources via |morpheus| API, will no longer fail when adding a mapping for a built-in role (such as System Admin) :superscript:`6.3.4`
             - Creating |morpheus|-type Clouds through |morpheus| API without passing the config block is now supported :superscript:`6.3.4`
             - Fixed resized servers taking on a default plan configuration after being resized via |morpheus| API/CLI :superscript:`6.3.4 `
             - Initial setup of a |morpheus| appliance via |morpheus| CLI is now working correctly :superscript:`6.3.4`
             - Multitenant Roles created in the |mastertenant| can now be set at the default Role for an Identity Source created via |morpheus| API/CLI within a Subtenant :superscript:`6.3.4`
             - The ``instanceTypeLayouts`` block is now being returned in API calls of the form ``https://<applianceUrl>/api/instance-types?phrase=dev%25centos&details=true`` from a Subtenant :superscript:`6.3.4`
:Agent: - Agent upgrades on SLES OS now use ``zypper`` rather than ``yum`` :superscript:`6.3.4`
:Amazon: - Deactivated AWS Service Plans are no longer reactivated after the next nightly Cloud sync :superscript:`6.3.4 `
:Ansible: - The History tab on the Ansible Group detail page and the Ansible Integration detail page has been removed as it was not intended to appear there :superscript:`6.3.4`
           - The info dialog for a running Ansible Task now receives live status updates while the modal is open. Previously the modal had to be closed and reopened to refresh :superscript:`6.3.4`
:Apps: - Fixed App Instances appearing in a "Provisioning" state when they were actually still in a "Pending" state :superscript:`6.3.4`
:Azure: - Added validation to clarify that comma-separated lists of port ranges cannot be submitted as "Destination Port Range" in an Azure Security Group :superscript:`6.3.4`
         - Fixed Nordic characters in tags causing provisioning failures :superscript:`6.3.4`
         - Fixed Service Plans not syncing when Azure Clouds were scoped to all regions :superscript:`6.3.4`
:Bluecat: - Bluecat domains associated with networks are now being setup properly as resource records in Bluecat when provisioning to Amazon through |morpheus| :superscript:`6.3.4`
:Blueprints: - The lock/unlock/hidden toggle button for Terraform variables no longer disappears when clicked during Terraform App Blueprint creation :superscript:`6.3.4`
:Catalog: - When "Show Pricing" is toggled off in the Provisioning section of global settings, the cart totals are now hidden when ordering Catalog items :superscript:`6.3.4`
           - When an Input is set on both the Instance Type or Layout and the Catalog order form, the Input will no longer appear twice on the Runtime tab of the Instance detail page after provisioning :superscript:`6.3.4`
:Clusters: - The ACTIONS button on the containers tab of the cluster detail page is now active and allows for restart or delete actions on one or more containers within the cluster :superscript:`6.3.4`
:DigitalOcean: - When adding a DO Cloud and selecting "new credentials" to also save the credentials in the |morpheus| credential store, the list of Datacenters now loads through successfully :superscript:`6.3.4`
:IPAM: - Validation is no longer performed when saving disabled IPAM integrations as this could potentially make it impossible to disable an unreachable IPAM integration :superscript:`6.3.4`
:Inputs: - Inputs whose visibility was dependent on other Inputs and which are configured to "Show On Edit" are now visible when editing the Instance :superscript:`6.3.4`
:Instances: - Added additional protections against added environment variables with NULL names as this caused downstream problems within the UI :superscript:`6.3.4`
             - Instances being removed by an expiration policy now appear in a "Removing" state during this teardown as a manually-deleted Instance would be :superscript:`6.3.4`
:Kubernetes: - Fixed an issue that prevented provisioning new containers to Kubernetes clusters deployed via custom Cluster Layouts to Amazon Clouds :superscript:`6.3.4`
              - Fixed |morpheus| Agent installation failures for Rocky 9 Kubernetes cluster provisioning :superscript:`6.3.4`
              - Fixed |morpheus| Agent installation issues when provisioning custom Kubernetes clusters to Amazon Linux 2 nodes :superscript:`6.3.4`
              - Kubernetes worker nodes are now drained prior to deleting as gracefully taking worker nodes out of service prior to deleting is a recommended best practice :superscript:`6.3.4`
              - The given cluster name in |morpheus| is now injected into the cluster manifest rather than the default name "kubernetes" being used :superscript:`6.3.4`
              - When a Kubernetes worker node is made inactive (by ``sudo systemctl stop kubelet``), the status of the cluster is given as "warning" rather than as "failed" :superscript:`6.3.4`
:Load Balancers: - The load balancer virtual servers list page is now paginated to improve performance in situations where there are many :superscript:`6.3.4`
:NSX-T: - Fixed errors on integration sync when BGP is configured on a NSX-t 4.1 Tier-0 Gateway :superscript:`6.3.4`
:Node Types: - Editing a Node Type no longer resets any configurations that were inside the "Layout Specific Settings" section of the config modal :superscript:`6.3.4`
              - Removed some outdated help text that was no longer valid in the Add/Edit Node Type modal :superscript:`6.3.4`
:Nutanix: - Provisioning to Nutanix Clouds using custom images stored in CIFS shares now works properly :superscript:`6.3.4`
:Option Lists: - Fixed successfully saved Inputs referencing REST-based Option Lists leaving errors in logs :superscript:`6.3.4 `
:Oracle Cloud: - After reconfiguring Oracle Instances, the updated cores count is now reflected on the Instance detail page :superscript:`6.3.4`
:Plans and Pricing: - When creating a Price Set and setting the Type to "Software/Service," the help text now changes to offer configuration help for that specific type :superscript:`6.3.4`
:Roles: - Updated the permission description for the Monitoring: Logs feature permission to correct an error :superscript:`6.3.4`
         - When the name of a multi-Tenant and locked Role is updated in the |mastertenant|, the name is now propagated down to Subtenant. Additionally, Subtenant administrators may rename these Roles without affecting the name in other Tenants :superscript:`6.3.4`
:SCVMM: - The "Allow migration to a virtual machine host with a different processor version" checkbox on the Hardware Configuration > Process properties on the template is being honored when provisioning an instance to SCVMM Clouds :superscript:`6.3.4 `
:Tasks: - We are now using preemptive basic authentication when using username and password against an HTTPS endpoint for HTTP-type Tasks :superscript:`6.3.4`
:Tenants: - Fixed Tenant deletion failures if the Tenant owned any Option Lists :superscript:`6.3.4`
:Terraform: - Added capability to use '0' as a getter with the |morpheus| HCL parser. For example, ``disks.0.size`` is now acceptable syntax. The previous example would only be parsed successfully as ``disks[0].size`` :superscript:`6.3.4`
             - Provisioning Terraform Apps via Catalog now honors the ``autoValidate: false`` flag which skips the ``terraform plan`` run and speeds the ordering process :superscript:`6.3.4`
             - Reconfigure and Approval Policies are now properly applied when ``apply state`` is issued to Terraform Apps :superscript:`6.3.4`
             - Updated the HCL parser to correctly parse the ``!=`` operator in a variable validation
:User Settings: - Date formats now dynamically update to match the date setting configured by the user's web browser :superscript:`6.3.4`
:VDI Pools: - Fixed VDI Pool Instances with Teardown-phase Tasks getting stuck during removal :superscript:`6.3.4`
:VMware: - If an operating system is set on the OVF or VMDK and a server is provisioned from that image, |morpheus| now takes that value as the OS shown in the info section on the server detail page :superscript:`6.3.4`
          - Improved handling of situations involving movement of VMs across vCenter clusters and resource pools :superscript:`6.3.4`
          - Snapshots taken during a Cloud sync no longer disappear from |morpheus| UI until the next Cloud sync :superscript:`6.3.4`
          - When a vCenter VM is deleted, on the next Cloud sync, |morpheus| now consistently updates the status of the Instance and server to "unknown" :superscript:`6.3.4`
          - When reconfiguring to add a network interface, then selecting a network and opting for a static IP address, |morpheus| will no longer select an address from the network IP pool instead :superscript:`6.3.4`
:Veeam: - Fixed Tenant Permissions not working for Veeam backup repositories :superscript:`6.3.4`

Embedded Plugins
================

:Dashboard: - The Dashboard plugin has been updated v1.0.6 to support German, French, and Italian localizations :superscript:`6.3.4`

Appliance & Agent Updates
=========================

:Appliance: - Upgraded embedded ``tomcat`` to version 9.0.83 :superscript:`6.3.4`
:Agent: - |morpheus| Linux Agent updated to v2.5.3 :superscript:`6.3.4`
:Node Packages: - |morpheus| node and vm-node packages updated to v 3.2.21 with |morpheus| Linux Agent v2.5.3 :superscript:`6.3.4`