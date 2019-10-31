v4.1.1 Release Notes
====================

.. important:: v3.6.0 or later required to upgrade to 4.1.1. Upgrading from v3.6.x to v4.x contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x a database backup is recommended due to MySQL version upgrade.

New Features
------------

SCVMM : Filter datastore selections based on resource pool and host
Email branding does not follow white labelling of tenancy
Template Instance - Cloud Formation
User Settings Password Strength
API/CLI: Incidents create
Static Address not working in AWS
API/CLI: Monitoring - Alert Rules
Instances List- remove ability to execute actions on Instances in read-only groups
Amazon Plans - seed plans for T3A and R5A
Community License display changes
Free - License Type
Free - Registration
Morpheus Hub Registration - UI Tweaks
Free - License Restrictions
Subnets: API/CLI: networks and network-groups
Free - Auto Skip if can't access hub
Free - Amazon Marketplace
Free - Azure Marketplace
Free - Hub Analytics
Amazon RDS - MS SQL Server

Fixes
-----

Tenant deletion fails with "Table 'morpheusdb.storage_group_storage_volume' doesn't exist" in 3.6.4
Vmware Container Hosts Unmount Disk
Task Results from a Library Script Task = null
AWS misleading error if pub image used where disk size is lower than expected
Deleting instances with Preserve backups unchecked does not delete the snapshots in AHV
Network Filter limited to 20 list.
Network config error
Teardown workflows do not run when the user deletes the instance from the VM details page/infrastructure/servers/virtual-machines
Licenses tenant permission issues
CF Template Spec - issue using Repository
CF Template Provision - Error parsing string
CF Template Provision - Review cleanup
If container plan_id and compute_server plan_id are different then each cloud refresh will create a new usage record
Ensure that VCD cacheVirtualMachines updates instance & container plan and resource information if it differs from compute_server or when a plan/resource change is detected
CF Template - Layouts Only
SCVMM datastores being recreated
Cant delete Tenant with assigned Policy
Security group:  Morpheus rule types are not being created within Openstack
Edit Network Interface: not displaying assigned Network
CF Template: Provision - issue with variables
Service Plan Errors Out When Required Fields Aren't Selected
Add VM Type dialogue input checks incorrect, incorrectly documented or missing (trivial)
Cloud vCD| When user sets a hostname during a instance provision, The hostname is being applied to the vm and vapp instead of the instance name.
Issue with Budget policies and Azure Blob storage
Deploying App from Blueprint default cloud is not required, which is causing network not to load correctly
AMI region validation for VirtualImageLocation unsuccessful on Amazon Instance type provisioning
AWS AMI's in Dev Morpheus are not sychronizing (Previous Case: 45600)
Amazon Cost Explorer not working for China Region cn-north-1
DNS Integration stopped working - MicrosoftDNS won't pull in records or domains.t
Correct managed virtual machines that have not got associated container & instance records
VMware instance reconfigure option & plan code variable issue
Cloud details: Networks - issue with pagination
500 Error when trying to delete node type that in use
CF Template - surface provision failures
API: Refresh Access Token issues
API Access - Refresh Token
CF Template - failing to provision amazon services
CF Template: Provision - errors when switching layouts
Fresh Setup - 500 errors
CF Template: Provision - Install Agent and AWS Instance Stats
CF Template: Resource Type - Instance
CF Template: Instance Details - connection info
ESXi: image data store selection on cloud not saving on cloud when updated.l
CF Template - layout form issue on validation error

CLI
---

Enhancements
^^^^^^^^^^^^

Fixes
^^^^^

Security
--------

Morpheus Hub
------------
Morpheus Hub Login - bad creds
Morpheus Hub Registration - insufficient password
