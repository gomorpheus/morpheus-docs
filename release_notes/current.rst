v3.6.4
======

Release date: 8/26/2019

New Features
------------

API/CLI: Advanced extra config options on node type added
Openstack: Parallel provisioning added
Tenants don't inherit the correct iteration of the instance naming policy and instead start from the beginning
Ansible based catalog instances - use Ubuntu 16 base
Azure: ARM deployments: ARM Deployment operations now synced into Morpheus as history
Azure: ARM deployments: Deployment records from Azure
Azure: ARM deployments: 'Create new Resource Group' option added
vCloud Director: Network reconfigure added
Provisioning: Instances: Manual Agent Install Action added. Generates and downloads manual Agent Install script
Nutanix: Snapshot creation and rollback support added (separate from Backups).
AWS: GovCloud US East Region added
API: Environments added
Reports: Filtering by tag and metadata added
Amazon: Security Group list and management on instance detail page added
Azure: ARM deployments: API Version updated to latest
Azure: Network and Volume sync added for discovered VMs
VMware: Snapshot creation and rollback support added (separate from Backups).
vCloud Director: Shared/public catalog management added
.. Instance: Edit Security Groups - improvements
Appliance: All-in-one RabbitMQ: Broadcast message Consumer Queue names now use hostname instead of uuid
Azure: Security Group list and management on instance detail page added
ServiceNow: CMDB: CMDB Target table now customizable
ServiceNow: CMDB: Custom Mapping for CMDB records added
Clouds: Toggle for automatically powering on managed VMs added to Cloud settings (defaults to off)
Plans & Pricing: Default Datastore Pricing. ``APPLY PRICE ACROSS CLOUDS`` option will apply Datastore price for selected Datastore across all Clouds with same Datastore. Note: Additional Prices defined for the same datastore but scoped to a specific Tenant take priority.
Plans & Pricing: RESOURCE POOL scoping option added to Price Set configurations.
Veeam: Tenant permissions for Veeam backup jobs and repositories added
Openstack: Availability Zones added
SCVMM: LIBRARY SHARE selection added to Cloud settings.
Ansible: Ansible Integration updated to use ``morpheus-local`` for improved security

Fixes
-----

CLI: Instances: Delenv: triggers 500 error
Router options getting removed
White label custom support links return a 404
Instance Detail: not surfacing VM provisioning error
Very slow database query updating current authenticated user settings through Administration -> Users causing timeouts
Null protection missing for Azure Security Groups on Provision.
nutanix console missing SE ( swedish keyboard layout) on advanced host options
Sub-tenant: VMware Instance backups are not exporting to NFS share managed by sub-tenant
VCD Interface type defaults to 'E1000E' for windows instance types when template is set to VMXNET3
AWS Docker provisioning on M5.xlarge fails
api/library/container-types missing null protector for config
500 error when creating new Task in Automation
Cloud vCD: Problem when adding an additional ethernet adapter to a instance the MAC address of the original ethernet adapter is being reset
Cloudformation Parameter type 'String' With AllowedValues Constraint in Not shown as list item while deploying app
Azure ARM app provisioning in subtenant does not populate cloud and resource group information
New usage records on every cloud sync for made managed Nutanix VM's without agent installed
OVM: provisioning fails because it is trying to resize CD-ROM drive when customizing volume
API: Billing: zoneId not being returned for zones/clouds that were deleted
CLI: Instances/Apps: should remove firewall parameters
Pagination on /infrastructure/networks/domains/ Zone Records list throws 403
CLI: Instances: issues
Host level firewall generates Ambiguous method overloading for method when Security Server has been specified on a cloud.
Security Groups not showing up for a tenant
Openstack - Morpheus should pick up a Floating IP from an External Network
OpenStack Docker Host problem with custom images & creation of image location
API: cannot get property error on compute server create
Openstack: Security Group sync issues
CLI Virtual Image Upload results in type vmware instead of vmdk
Sometimes multidisk chooses the IDE mount point type
Add Amazon Domain Record broken
- Huawei: Fix for Huawei Hypervisor Console
- Plans & Pricing: Fix for incorrect price association when multiple prices of same priceType are attached to price-set(s) within a plan
- vCloud Director: Fix for missing Datastores not getting re-attached to compute_server volumes
- Azure: Fix for incompatible plans listed in Reconfigure wizard when using availability sets
- OptionLists: Fix for public option list values not displaying in subtenants.
- OptionTypes: Fix for required option types not being enforced when user select a value and then selects ``select`` for value.
- Migrations: Storage Bucket field now set as Required in Migrations Wizard
- Apps: Fix for when exported Environment Variables values are not properly set on target
- SCVMM: Fix for synced SCVMM Pool Network association
- vCloud Director: Error message added for failed disk resize/add
- vCloud Director: Fix for updating vm resource data on sync when vm is resized in vcd
- VMware: Fix for cores per socket configuration when when plan has ``cores per socket = 0`` (setting cores per socket = 0 in a plan will now automatically be updated to ``cores per socket = 1``)
- Azure: ARM: Fix for Instance and Hostname evaluation when using ``"vmName": "[parameters('adminUsername')]",``
- AWS: Fix for AMIs with same name in different regions not syncing correctly
- Appliance: Database: Retention policy added for operation_event table
- Openstack: SFS: Fix or access rule creation
- Openstack: SFS: Fix for share path on share detail not diplaying
- VMware: Fix for IP address is not syncing for certain OVAs
- Billing & Usage: Fix for null datastore price added to usage records when associated datastore has been removed
- SCVMM: Fix for unattend file path when multiple library shares are present
- Apps: Fix for ${app.name} variable not being evaluated on addition nodes when  using scale-factor

.. Docker host provision fails on VIO when provisioning with additional volume
.. Price estimation UI on instance creation does not take into account PriceSet for that region
.. Floating IPs not visible in Morpheus
.. Correct Azure VM name not updated in morpheus for compute_server records
.. Avamar integration not displaying tenants or hypervisors



Usage does not get restarted when a price is added to a price set

Update for not-yet-commons-ssl
Change Java from Oracle to OpenJDK on node packages
Update Java for LTS appliance to OpenJDK JRE 8u222
