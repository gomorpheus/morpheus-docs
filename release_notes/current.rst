v3.6.4
======

Release date: 8/26/2019

New Features
------------

- Ansible: Ansible Integration updated to use ``morpheus-local`` for improved security
- API/CLI: Advanced extra config options on node types added
- API/CLI: Environments added
- Appliance: All-in-one RabbitMQ: Broadcast message Consumer Queue names now use hostname instead of uuid
- AWS: GovCloud US East Region added
- AWS: Security Group list and management on Instance detail pages added
- Azure: ARM deployments: 'Create new Resource Group' option added
- Azure: ARM deployments: API Version updated to latest
- Azure: ARM deployments: ARM Deployment operations now synced into Morpheus as history
- Azure: ARM deployments: Deployment records from Azure
- Azure: Network and Volume sync added for discovered VMs
- Azure: Security Group list and management on instance detail page added
- Clouds: Toggle for automatically powering on managed VMs added to Cloud settings (defaults to off)
- Instances: Manual Agent Install Action added. Generates and downloads manual Agent Install script
- Instances: Network: Security Groups: :guilabel:`EDIT SECURITY GROUPS` modal improvements
- Library: System Ansible based catalog instances now use Ubuntu 16.04 base
- Nutanix: Snapshot creation and rollback support added (separate from Backups).
- Openstack: Availability Zones added
- Openstack: Parallel provisioning added
- OVM: Fix for intermittent disk mapping issue, causing provisioning failure due to resize attempt on cd-rom
- Plans & Pricing: Default Datastore Pricing. ``APPLY PRICE ACROSS CLOUDS`` option will apply Datastore price for selected Datastore across all Clouds with same Datastore. Note: Additional Prices defined for the same datastore but scoped to a specific Tenant take priority.
- Plans & Pricing: RESOURCE POOL scoping option added to Price Set configurations.
- Reports: Filtering by tag and metadata added
- SCVMM: LIBRARY SHARE selection added to Cloud settings.
- Security Groups: Tenant Permissions for Security Groups adding. Includes ``Allow Manage`` flag per assigned tenant in Security Group settings
- ServiceNow: CMDB: CMDB Target table now customizable
- ServiceNow: CMDB: Custom Mapping for CMDB records added
- Tenants don't inherit the correct iteration of the instance naming policy and instead start from the beginning
- vCloud Director: Network reconfigure now supported
- vCloud Director: Shared/public catalog management added
- vCloud Director: v9.5 now supported
- Veeam: Tenant permissions for Veeam backup jobs and repositories added
- VMware: Snapshot creation and rollback support added (separate from Backups)

Fixes
-----

- Administraiton: Whitelabel: Updated ``Support Menu Links`` help text to state fully qualified url's required for linking to external sites
- Administration: Fix for slow performance when updating current authenticated user settings through ``Administration -> Users``
- API/CLI: Fix for ``/api/library/container-types`` missing null protector for config
- Appliance: Database: Retention policy added for operation_event table
- Apps: Fix for ${app.name} variable not being evaluated on addition nodes when  using scale-factor
- Apps: Fix for exported Environment Variables values not properly set on target
- Avamar integration not displaying tenants or hypervisors
- AWS: Cloudformation: Fix for parameter type ``String`` With ``AllowedValues`` constraint not shown as list item
- AWS: Fix for AMIs with same name in different regions not syncing correctly
- AWS: Fix for AWS Docker provisioning on ``M5.xlarge`` instance types failing due to incorrect storage device naming
- Azure: ARM: Fix for Cloud selection in ARM Blueprints for sub-tenants
- Azure: ARM: Fix for Instance and Hostname evaluation when using ``"vmName": "[parameters('adminUsername')]",``
- Azure: ARM: Fix for sync of VM name changes
- Azure: Fix for incompatible plans listed in Reconfigure wizard when using availability sets
- Billing & Usage: Existing usage records now update when a new price is added to an associated price set
- Billing & Usage: Fix for null datastore price added to usage records when associated datastore has been removed
- CLI: ``virtual-images add`` now sends ``vmdk`` instead of ``vmware``, ``/api/options/virtualImageTypes`` now returns ``vmdk`` instead of ``vmware``
- Domains: Zone Records: Fix for pagination issue on ``/infrastructure/networks/domains/`` -> ``Zone Records``
- Huawei: Fix for Huawei Hypervisor Console
- Migrations: Storage Bucket field now set as Required in Migrations Wizard
- Nutanix: Fix for new usage records being generated on cloud sync for converted-to-managed Nutanix VM's without agent installed
- Nutanix: Hypervisor Console: Keyboard Layout setting for Nutanix Hosts removed (not supported by Nutanix)
- OpenStack: Fix 500 error when using custom image on Openstack docker host.
- Openstack: Fix for listing previously used Floating IP records
- Openstack: Fix for tenant Security Group creation when Host Level Firewall is enabled on a Cloud
- Openstack: Fix for VIO Docker host provisioning issue when adding additional volumes
- Openstack: SFS: Fix for share path on share detail not displaying
- Openstack: SFS: Fix or access rule creation
- OptionLists: Fix for public option list values not displaying in subtenants.
- OptionTypes: Fix for required option types not being enforced when user select a value and then selects ``select`` for value.
- Plans & Pricing: Fix for incorrect price association when multiple prices of same priceType are attached to price-set(s) within a plan
- SCVMM: Fix for synced SCVMM Pool Network association
- SCVMM: Fix for unattend file path when multiple library shares are present
- Storage: Fix for missing "Archive Snapshots" option on Storage Providers in sub-tenants
- Tasks: Fix for 500 error when creating new Task using Internet Explorer
- vCloud Director: Error message added for failed disk resize/add
- vCloud Director: Fix for adding additional ethernet adapter to a instance resetting MAC address of the original ethernet adapter
- vCloud Director: Fix for missing Datastores not getting re-attached to compute_server volumes
- vCloud Director: Fix for price estimation on instance creation not taking into account associated Price Set for that region
- vCloud Director: Fix for updating vm resource data on sync when vm is resized in vcd
- vCloud Director: Fix fro VCD Interface type defaulting to 'E1000E' for Windows images when template is set to VMXNET3
- VMware: Fix for additional volumes intermittently being set to IDE mount point type
- VMware: Fix for cores per socket configuration when when plan has ``cores per socket = 0`` (setting cores per socket = 0 in a plan will now automatically be updated to ``cores per socket = 1``)
- VMware: Fix for IP address is not syncing for certain OVAs

System Updates
--------------

- Appliances: Java updated to OpenJDK JRE 8u222
- Appliance: not-yet-commons-ssl updated to 0.3.15 (address CVE-2014-3604)
- Node Packages: Java updated to OpenJDK JRE 8u222
