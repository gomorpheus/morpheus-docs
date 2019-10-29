v3.6.5
======

Release date:

New Features
------------

Amazon Plans - seed plans for T3A and R5A Add Amazon M5A and M5AD Instance Types
Static Address not working in AWS
don't filter usage records for deleted zones
SCVMM : Prepend host name or cluster name to datastores
API/CLI: Incidents create
User Settings Password Strength
Async App Provision
UpCloud Ubuntu 18
Veeam: SCVMM Support
Static IP address assign on vCD cloud via guest customisations
Openstack Clouds: should update available EIPs/FIPs immediately after provision
Provision Setting: Reuse Sequence Numbers
Support Veeam 9.5
Additional metadata for /api/billing records.
- White Labelling: Sub-tenant notifications branding added

Fixes
-----

- Ansible: Fix for Inventory File VM naming in multi-node deployments using old style of <instancename>, <instancename>-2, <instancename>-3
- Usage: Fix for Duplicate account usage records created when `startDate` is in the last half of a sec
- Apps: Fix for Blueprint fields locks
- Openstack/Huawei/OTC: Fix for previously used floating IPs not displaying in IP selection list
- Apps: Fix for not reloading properties from config when clicking Previous from Review panel
- Prices: Storage and Datastore prices: Updated the output in applicablePrices to change the pricePerUnit and costPerUnit to be consistent with the other price types.
- vCloud Director: Fix for CD-ROM addressed potentially conflicting with additional network interface addresses
- Apps: Fix for ${app.name} variable not being evaluated in scale-factor during provisioning
- Service Plans: Fix for Price Sets & Prices not loading on fresh installs when no tenants other than Master Tenant defined
- Convert-To-Managed: Fix for Group Selection when converting more than one VM to managed at a time
- Morpheus UI Bug -filter doesn't apply to pagination
- Library > Instance Types: Fix for Filters not applying to pagination
- CLI: Fix for ``NameError: undefined local variable or method `layout_id``` when removing node types via CLI
- VMware: Fix for scsi order when using Templates with multiple Disks.
- Instances: Cloud Hyperlink removed when user does not have access to Cloud Detail page (500 Error)
- Usage: Fix for Usage records restarting when $0 price added or when Plan Name or Details are edited.
- Security Group: Accepted port ranges updated from ``0-65535`` to ``1-65535``
- vCloud Director: Fix for large VM counts causing multiple Usage record restarts
VMs can be removed from Morpheus if a network problem interrupts the API call to vapps (VcdComputeUtility.callApi("${vappUrl.protocol}://${vappUrl.host}".toString()) 
Instance provisioning does not complete
Tenant deletion fails with "Table 'morpheusdb.storage_group_storage_volume' doesn't exist" in 3.6.4
Vmware Container Hosts Unmount Disk
Task Results from a Library Script Task = null
AWS misleading error if pub image used where disk size is lower than expected
Deleting instances with Preserve backups unchecked does not delete the snapshots in AHV
Network Filter limited to 20 list.
Network config error
Teardown workflows do not run when the user deletes the instance from the VM details page/infrastructure/servers/virtual-machines
Licenses tenant permission issues
If container plan_id and compute_server plan_id are different then each cloud refresh will create a new usage record
Ensure that VCD cacheVirtualMachines updates instance & container plan and resource information if it differs from compute_server or when a plan/resource change is detected
Cant delete Tenant with assigned Policy
Security group:  Morpheus rule types are not being created within Openstack
Service Plan Errors Out When Required Fields Aren't Selected
Add VM Type dialogue input checks incorrect, incorrectly documented or missing (trivial)
vCD: When user sets a hostname during a instance provision, The hostname is being applied to the vm and vapp instead of the instance name.
Issue with Budget policies and Azure Blob storage
Deploying App from Blueprint default cloud is not required, which is causing network not to load correctly
AMI region validation for VirtualImageLocation unsuccessful on Amazon Instance type provisioning
AWS AMI's in Dev Morpheus are not sychronizing (Previous Case: 45600)
Amazon Cost Explorer not working for China Region cn-north-1
DNS Integration stopped working - MicrosoftDNS won't pull in records or domains.t
Correct managed virtual machines that have not got associated container & instance records
VMware instance reconfigure option & plan code variable issue



The api has changed now to include some new behavior and new query parameters. (Existing functionality should also be retested.. along with tenant vs master account behavior)

For the /zones, /instances, /servers, and /discoveredServers endpoints, the following changes have been made:

Existing behavior is preserved.. only the current account data is returned.
An optional 'includeTenants=true' query parameter may be passed. If the account is a master account, the tenant billing/usage records will also be included
An optional 'accountId=2' query parameter may be passed when calling from a master tenant user. It will then scope the return values to only that account. (When specified with the 'includeTenants=true' this parameter is ignored)
Users of the api should be migrating to using the UUIDs rather than IDs. Therefore, a UUID may now be passed to these calls in addition to the previously supported ID.

..  issue where plan change that coincided with rabbit problem caused usage records to be stopped and not restarted. processPriceChanges discovered the plan change, stopped the appropriate usage records and then the task to start the new usage records was sent through rabbit - which never executed. From a discussion on slack this case was created as a suggestion on preventing this rare occurrence in the future.

System Updates
--------------

- Appliances: Java updated to OpenJDK JRE 8u232
- Node Packages: Java updated to OpenJDK JRE 8u232
