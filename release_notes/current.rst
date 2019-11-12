v4.1.1 Release Notes
====================

.. important:: v3.6.0 or later required to upgrade to 4.1.1. Upgrading from v3.6.x to v4.x contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x a database backup is recommended due to MySQL version upgrade.

New Features
------------

- AWS: Plans: Seeded plans for R5A and T3A AWS Instance Types added
- AWS: RDS: MSSQL Server support added
- AWS: Support added for Static IP Assignment
- Cloud Formation: CF templates can now be provisioned as Instances using Cloud Formation layout types and Spec Templates
- Instances: List View: Actions selection removed when multiple Instances are selected and at least one is in a Read Only Group
- IPAM: ``THROTTLE RATE`` setting added to Infoblox and Bluecat to control API/sync rate.
- Library: Node Types: New Cloud Formation Layout technology Type. Allows CF Spec Templates as Instances
- Library: Spec Templates: New Cloud Formation Spec Template type
- SCVMM : Datastore selection options now filter based on selected resource pool and host
- Usage: createdByUser, createdByUserId, siteId, siteName, siteUUID, siteCode, and metadata [] now returned for /api/billing records. serverUniqueId added for Containers, serverUniqueId added for Servers, zoneCode added for Zones/Clouds. NOTE: These values will only be populated for newly created usage records. Not all record will have values for all fields, such as createdByUser and createdByUserId for discovered servers, site information for non-instance records)
- User Settings: Complex Passwords now required for Linux and Windows users in User Settings. Password must contain at least one uppercase letter, one lowercase letter, a number, and a symbol.
- White Labelling: Sub-tenant notifications branding added

Fixes
-----

- Apps: Fix for Blueprint configurations not loading when no Cloud is selected during New App -> Setup step
- AWS: Fix for "image is larger than select plan" error displaying on Plan when volume size is less than minimum requirement for Image
- AWS: Fix for AMI Image Location issue when two AMI's have them same name in different regions, affecting provisioning of Images to Regions added after first Region.
- AWS: Fix for Proxy Settings not applying to Amazon Cost Service data
- Azure: Fix for provisioning issue using Azure Blob storage in conjunction with an active Budget Policy
- Docker: Fix for cloud-init iso not being ejected after VMware Docker host creation
- Instances: Hourly Job added to update `Managed` VM records to `Unmanaged` when no Instance association exists
- IPAM Integrations: Fix for Network Filter and Zone Filter field character limit <255
- Library: Fix for 500 Error when trying to delete Node Type that in use or was previously used
- Library: Node Types: Fix for Count and Image selection validation
- Licenses: Fix for Windows Licenses still being applied to scoped Images in Tenants without permissions to Licenses
- Microsoft DNS: Fix for ``Last Updated`` date display
- Nutanix: Fix for deleting instances with ``Preserve Backups`` unchecked not deleting associated snapshots in AHV
- Reconfigure: Validation added for Plan selection before Reconfigure can be triggered
- Security Groups:  Fix for non-applicable Security Group Rule Types listed when scoped Cloud does not have associated Instance
- Service Plans: Fix for Required Field validation
- Tasks: Fix for Task Results for Library Script Task task types returning ``null``
- Tenants: Fix for inability to delete a tenant with an assigned Master Tenant Policy
- Tenants: Fix for Tenant deletion failing due to "'morpheusdb.storage_group_storage_volume' doesn't exist"
- Usage: Fix for Instance Plan not updating when source VM plan is change but associated Instance is not in a running state
- vCloud Director: Fix for CD-ROM addressed potentially conflicting with additional network interface addresses
- vCloud Director: Fix for DSN Hostname field override
- VMware: Child Network: Fix for ``network config error`` when using IP Pools with VMware Child Networks
- Workflows: Fix for teardown workflows do not run when the user deletes a VM and its associated Instance from the VM details page (infrastructure/servers/virtual-machines) instead of from Instances section

.. API: Refresh Access Token issues
.. API Access - Refresh Token
.. Fresh Setup - 500 errors
.. - ESXi: Fix for image data store selection on cloud not saving when updated.

CLI
---

v4.1.5
^^^^^^
Enhancements
````````````
- New format for -S, --sort ORDER Sort Order. DIRECTION may be included as "ORDER [asc|desc]". Example: instances list -S "dateCreated desc"
- New command monitor-alerts. Requires appliance version 4.1.1
- Improved commands monitor-contacts add, monitor-checks, monitor-groups and monitor-apps by adding prompting.

Fixes
````````````
- Fixed roles update to support the --payload option.
- Fixed issue with instances logs, containers logs, etc displaying records in the reverse order. Changed to match the UI.
- Fixed instances view and apps view only allowing one [instance] argument.

v4.1.4
^^^^^^
Fixes
````````````
- Fix issue with blueprints add-instance that would not allow multiple instances of the same type for a tier.
- Fix issue with blueprints add-instance-config not prompting for Group, and instance can now be specified by name or index instead of just type.

v4.1.3
^^^^^^
Fixes
````````````
- Fix issue with instances clone that would result in a 'Cloud not found' error when trying to use a shared/public cloud.
- Fixed an error that could be seen with select options having an Integer default value.

v4.1.2
^^^^^^
Enhancements
````````````
- Improved APIClient so that is easier to use. See APIClient.

v4.1.1
^^^^^^
Fixes
````````````
- Fix issue with resource-pools add resulting in no Group and Plan access. Now it passes resourcePermissions.all=true by default.

Security
--------
- Appliances: Java updated to OpenJDK JRE 8u232
- Node Packages: Java updated to OpenJDK JRE 8u232

System
------

- Added improved handling of messages when database is unreachable to prevent out of memory errors and improve application recovery

Morpheus Hub
------------

- Morpheus Hub Registration and Login added to initial Appliance Setup for licenses. Note the registration and login options will only appear if the Appliance can reach https://morpheushub.com
