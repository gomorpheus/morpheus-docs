v3.6.5
======

Release date: 10/29/2019

New Features
------------
- Apps: Asynchronous App Provisioning added
- AWS: Plans: Seeded plans for M5A, M5AD, R5A, T3A Instance Types added
- AWS: Support added for Static IP Assignment
- Instances: Hourly Job added to update `Managed` VM records to `Unmanaged` when no Instance association exists
- Openstack/Huawei/OTC: Available EIPs/FIPs now updated immediately after provisioning
- Provisioning: "Reuse Naming Sequence Numbers" setting added to ``Administration > Provisioning``. If enabled, ``${sequence}`` numbers used in naming patterns will be re-used once they are available again. When disabled, ``${sequence}`` numbers will always increase by one, ensuring the same number in a pattern is never re-used (default and previous behavior).
- SCVMM: Associated Host or Cluster name prepended to datastores names for identification
- vCloud Director: Static IP address assignment on vCD clouds via guest customizations added
- UpCloud: Ubuntu 18.04 System Image added
- Usage: ``createdByUser``, ``createdByUserId``, ``siteId``, ``siteName``, ``siteUUID``, ``siteCode``, and ``metadata []`` now returned for ``/api/billing`` records. ``serverUniqueId`` added for Containers, ``serverUniqueId`` added for Servers, ``zoneCode`` added for Zones/Clouds. NOTE: These values will only be populated for newly created usage records. Not all record will have values for all fields, such as ``createdByUser`` and ``createdByUserId`` for discovered servers, site information for non-instance records)
- Usage: Usage records for deleted Clouds are no longer filtered from Usage
- User Settings: Complex Passwords now required for Linux and Windows users in User Settings. Password must contain at least one uppercase letter, one lowercase letter, a number, and a symbol.
- Veeam: SCVMM Support added
- Veeam: Support for Veeam 9.5u4 added
- White Labelling: Sub-tenant notifications branding added

Fixes
-----
- Ansible: Fix for Inventory File VM naming in multi-node deployments using old style of <instancename>, <instancename>-2, <instancename>-3
- Apps: Fix for ${app.name} variable not being evaluated in scale-factor during provisioning
- Apps: Fix for Blueprint configurations not loading when no Cloud is selected during New App -> Setup step
- Apps: Fix for Blueprint fields locks
- Apps: Fix for not reloading properties from config when clicking Previous from Review panel
- AWS: Fix for "image is larger than select plan" error displaying on Plan when volume size is less than minimum requirement for Image
- AWS: Fix for inconsistent synced AMI region validation for Ireland region
- AWS: Fix for Proxy Settings not applying to Amazon Cost Service data
- Azure: Fix for provisioning issue using Azure Blob storage in conjunction with an active Budget Policy
- CLI: Fix for ``NameError: undefined local variable or method `layout_id``` when removing node types via CLI
- Convert-To-Managed: Fix for Group Selection when converting more than one VM to managed at a time
- Docker: Fix for cloud-init iso not being ejected after VMware Docker host creation
- Instances: Cloud Hyperlink removed when user does not have access to Cloud Detail page (500 Error)
- IPAM Integrations: Fix for Network Filter and Zone Filter field character limit <255
- Library > Instance Types: Fix for Filters not applying to pagination
- Library: Node Types: Fix for Count and Image selection validation
- Licenses: Fix for Windows Licenses still being applied to scoped Images in Tenants without permissions to Licenses
- Morpheus UI Bug -filter doesn't apply to pagination
- Nutanix: Fix for deleting instances with ``Preserve Backups`` unchecked not deleting associated snapshots in AHV
- Openstack/Huawei/OTC: Fix for previously used floating IPs not displaying in IP selection list
- Prices: Storage and Datastore prices: Updated the output in applicablePrices to change the pricePerUnit and costPerUnit to be consistent with the other price types.
- Reconfigure: Validation added for Plan selection before Reconfigure can be triggered
- Security Groups: Accepted port ranges updated from ``0-65535`` to ``1-65535``
- Security Groups:  Fix for non-applicable Security Group Rule Types listed when scoped Cloud does not have associated Instance
- Service Plans: Fix for Price Sets & Prices not loading on fresh installs when no tenants other than Master Tenant defined
- Service Plans: Fix for Required Field validation
- Tasks: Fix for Task Results for Library Script Task task types returning ``null``
- Tenants: Fix for inability to delete a tenant with an assigned Master Tenant Policy
- Tenants: Fix for Tenant deletion failing due to 'morpheusdb.storage_group_storage_volume' doesn't exist" in 3.6.4
- Usage: Fix for Duplicate account usage records created when `startDate` is in the last half of a sec
- Usage: Fix for Instance Plan not updating when source VM plan is change but associated Instance is not in a running state
- Usage: Fix for Usage records restarting when $0 price added or when Plan Name or Details are edited.
- vCloud Director: Fix for CD-ROM addressed potentially conflicting with additional network interface addresses
- vCloud Director: Fix for DSN Hostname field override
- vCloud Director: Fix for large VM counts causing multiple Usage record restarts
- vCloud Director: Fix for potential for Discovered VM records to be removed when network outage occurs during cloud sync
- VMware: Child Network: Fix for ``network config error`` when using IP Pools with VMware Child Networks
- VMware: Fix for scsi order when using Templates with multiple Disks.
- Workflows: Fix for teardown workflows do not run when the user deletes a VM and its associated Instance from the VM details page (infrastructure/servers/virtual-machines) instead of from Instances section

CLI Updates
-----------

Enhancements
^^^^^^^^^^^^
- New format for -S, --sort ORDER Sort Order. DIRECTION may be included as "ORDER [asc|desc]". Example: ``instances list -S "dateCreated desc"``
- Improved commands monitor-contacts add, monitor-checks, monitor-groups and monitor-apps by adding prompting.

Fixes
^^^^^
- Fixed roles update to support the --payload option.
- Fixed issue with instances logs, containers logs, etc displaying records in the reverse order. Changed to match the UI.
- Fixed instances view and apps view only allowing one [instance] argument.

API Updates
-----------
The ``/billing`` API endpoint has changed now to include some new behavior and new query parameters.
 - For the ``/billing/zones``, ``/billing/instances``, ``/billing/servers``, and ``/billing/discoveredServers`` endpoints, the following changes have been made:

   - Existing behavior is preserved. Only the current Account data is returned.
   - An optional ``includeTenants=true`` query parameter may be passed. If the account is a master account, the tenant billing/usage records will also be included
   - An optional ``accountId=2`` query parameter may be passed when calling from a master tenant user. It will then scope the return values to only that account. (When specified with the 'includeTenants=true' this parameter is ignored)
   - Users of the Pricing API should be migrating to using the UUIDs rather than IDs. Therefore, a UUID may now be passed to these calls in addition to the previously supported ID.

..  issue where plan change that coincided with rabbit problem caused usage records to be stopped and not restarted. processPriceChanges discovered the plan change, stopped the appropriate usage records and then the task to start the new usage records was sent through rabbit - which never executed. From a discussion on slack this case was created as a suggestion on preventing this rare occurrence in the future.

System Updates
--------------
- Appliances: Java updated to OpenJDK JRE 8u232
- Node Packages: Java updated to OpenJDK JRE 8u232
