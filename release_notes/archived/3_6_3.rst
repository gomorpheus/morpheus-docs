v3.6.3
======

Release date: 6/10/2019

Highlights
----------

Enhanced Security Group Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cloud Security Groups can now be fully managed in Morpheus! AWS, Azure, Openstack, Huawei & Open Telekom Cloud Security Group and Rules sync and can be created, edited and deleted directly in |morpheus|.

New Storage Integrations & Policies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Huawei OBS, Huawei SFS, Open Telekom Cloud & Huawei OBS & SFS Storage Server Integrations added, including OBS Bucket and SFS File Share creation and management. These are accompanied by a new Storage Server Storage Quota Policy, which also governs existing Storage Integrations.

Windows File Deployments
^^^^^^^^^^^^^^^^^^^^^^^^

Previously only available for Linux, ``Provisioning -> Deployments`` now support Windows Operating Systems! Windows Instances can now utilize the ``DEPLOY`` feature for local or source controlled File Deployments, Upgrades and Rollbacks.

Infoblox DNS Expansion
^^^^^^^^^^^^^^^^^^^^^^

In addition to the existing IPAM integration associated DNS record creation, Infoblox Integrations now can be set as the DNS Provider on Clouds and Groups, allowing automated DNS record creation in Infoblox for clouds not utilizing IPAM.

Cherwell Additions
^^^^^^^^^^^^^^^^^^

The Cherwell Integration has been expanded to support dynamic business object creation and adds additional field configuration options for change requests

Full Python Tasks
^^^^^^^^^^^^^^^^^

``Python Script (jython)`` updated to ``Python Script``, removing the limitations of jython tasks. Please ensure Python is installed on appliance app nodes if you are using Python Tasks.

Unattend Agent Install mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The |morpheus| Windows Agent can now be installed via the unattend.xml during Guest Customizations in VMware and vCloud Director clouds. To enabled, set Agent Install Mode to ``Cloud-init / Unattend (when available)`` in target Cloud(s) Advanced Settings.

VMware Extra Options
^^^^^^^^^^^^^^^^^^^^

Extra Options key/value fields added to VMware Node Types for setting Advanced Options on VMware VM's. ``*``

Ubuntu 18.04 Support for Morpheus App Nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

v3.6.3 adds native support for Installing |morpheus| on Ubuntu 18.04, in addition to Ubuntu 16.04. Ubuntu 14.04 has also been removed from recommended versions.



New Features
------------

- Ansible:  Now handling group and host vars relative to inventory
- API & CLI: Resource Pool and Folder endpoints added
- API & CLI: Security Groups updated to support Security Group Rule management
- API & CLI: vCloud Director Datastore ID added to Billing Data
- Appliance: Expired license notification added
- Appliance: Removed requirement for multi-app node configurations to use shared storage for Morpheus Agent yum repo. ``*``
- Apps: AWS Scale Groups created from Cloud Formation and Terraform Blueprints are now automatically created in |morpheus|
- Apps: Retry added for ARM App resource updates
- Apps: Security Groups created from Cloud Formation and Terraform Blueprints are now automatically associated with the App
- Apps: Terraform: Validation errors now displayed in Configure step
- Automation: Tasks: `Python Script (jython)` updated to `Python Script`
- AWS: Security Group Rule management added. AWS Security group rules can now be created, edited and deleted in |morpheus|
- Azure: Network Security Group Rule management added. Azure Network Security group rules can now be created, edited and deleted in |morpheus|
- Backups: Enhanced error messages with STDOUT added to failed mysql backups
- Blueprints: AWS Scale Groups created in Cloud Formation and Terraform templates now automatically created in |morpheus|
- Cherwell: Added ignore ssl flag Cherwell Integration options
- Cherwell: Expansion of integration to support dynamic business object creation and additional field configurations for advisory change requests
- Clouds : Code and Tenant fields added to Cloud Wizard when creating cloud from `Infrastructure -> Clouds ->` :guilabel:`+ ADD`, matching wizard from `Infrastructure -> Groups -> Clouds ->` :guilabel:`+ ADD`
- Clouds: ``Security Server`` setting for AWS, Azure, Openstack, Open Telekom Cloud, and Huawei Clouds configurations will be automatically set to matching type on Appliance start up
- Clouds: Added support for 'local firewall' option to Security Mode selection in cloud edit for clouds which do not have native security group support (azure, openstack flavors, amazon)
- Deployments: Windows Deployment support added
- Huawei: ``af-south-1`` & ``eu-west-0`` Regions added
- Infoblox: Infoblox DNS Integration added.
- Library: Node Types retain Image link when Image is not found, retaining the info for Virtual Images that are converted to templates or for another reason not found during a sync.
- Load Balancers: LBaaS v2 support added for Open Telekom and Huawei
- Load Balancers: Tenant assignment added
- Network: Routers: Tenant Permissions added to Routers
- OpenStack: `REGION` scope option added to Openstack Cloud configurations
- Policies: Role scope option added for Policies with flag to enforced in aggregate or per user.
- Policies: Storage Server Storage Quota Policy type added
- Provisioning: Error messages now included in Failed provision email notifications
- Provisioning: Instance and App wizards now can create multiple load balancer ports
- Remedy: Added ignore ssl flag to Remedy Integration options
- Roles: ``MULTITENANT LOCKED`` option added for User Roles. When lock is enabled, the linked sub-tenant roles cannot be edited in subtenant.
- SCVMM: Additional disks can now be added to sync templates during provisioning
- Storage: Buckets: Huawei OBS Bucket, Open Telekom OBS Bucket creation and management added
- Storage: File Shares: Huawei SFS Share, Open Telekom SFS Share creation and management added
- Storage: Servers: Huawei OBS, Huawei SFS, Open Telekom OBS, Open Telekom SFS Integrations added
- vCloud Director: Hypervisor Console support added
- vCloud Director: Routed Network Support Added
- vCloud Director: Windows Agent Install via guest customizations unattend.xml added. NOTE: Requires ``Agent Install Mode`` set to ``Cloud-init / Unattend (when available)`` in vCloud Director Cloud(s) Advanced Options (Windows 2008 support added in 3.6.3-2)
- VMware: Windows Agent Install via guest customizations unattend.xml added. NOTE: Requires ``Agent Install Mode`` set to ``Cloud-init / Unattend (when available)`` in VMware Cloud(s) Advanced Options (Windows 2008 support added in 3.6.3-2)
- VMware: Windows Agent Install: Timeout and Retries added to reachability command to improve Windows Agent Install via VMware Tools Guest Exec

System Updates
--------------

- `runit` updated to to 4.3.0. Services such as nginx will now restart when config changes are detected during |morpheus| reconfigures
- Added new MySQL JDBC override string for morpheus/rb using ``mysql['mysql_url_overide']``
- Added setting for `SQLTransientConnectionException` in JDBC, the failover settings can be modified using the setting ``mysql['mysql_failover_params']``
- Database: Database Level Encryption upgraded to AES-256
- Fixed post install script that was prepping for ElasticSearch upgrade on a new install
- Fixed restart of nginx and guac when the configuration changes.
- Guacamole updated to 1.0.0
- jython removed per CVE-2016-4000. IMPORTANT: Jython replaced with Python. Users with python tasks are responsible for ensuring Python is installed on their appliance(s)
- Logs: Updates to mask additional sensitive data in logs
- MySQL: 5.7 replaces 5.6 for Azure, Bluemix, DigitalOcean, SoftLayer and UpCloud System Layouts
- NTP config is skipped on Ubuntu 18.04 and Debian 9
- Oracle Cloud: Default |morpheus| Docker Host Image updated to Ubuntu 16.04
- Redis: Added 3.0 for Azure, Bluemix and UpCloud
- Ubuntu 18.04 now supported for Morpheus Appliance Installations
- Update for commons-compress, addresses CVE-2018-11771
- Update for spring-security-oauth2, addresses CVE-2019-3778

Fixes
-----

- Amazon: Fix for security groups not being filtered by resource pool in Instance and App wizards when default security group is populated
- Ansible Tower: Fix for ``Limit to Instance`` flag
- API & CLI: Amazon: Add Network: Fix for issue creating networks due to ``vpcId`` error
- API/CLI: Fix for AWS Provisioning Issue when image disk size is greater than Plan disk size
- API & CLI: Fix for Oracle VM provisioning failures when using |morpheus| API & CLI
- API & CLI: Fixes for cloning Instances with Custom Options, VMware clones potentially triggering ovf exports ``*``
- CLI: networks: Fix for setting Domain on Networks via |morpheus| CLI Shell
- AWS:  Fix for security groups not filtering by VPC
- Azure: Fix for creating |morpheus| Docker Hosts with custom Image
- Azure: Updates to Azure Sync: Plan change detection
- Backups: Fix for running on-demand backup creating a scheduled job.
- Backups: Unscheduled Backups Jobs are no longer listed on Backups Summary page
- Commvault: Fix for Backups tab in Provisioning Wizard showing Nutanix Snapshot instead of Commvault when Commvault is set to Nutanix Cloud Backup Provider
- Console: Fix for in-page Hypervisor Console window height becoming progressively smaller on page refresh
- Dashboard: Fix for displaying old Instance name on the Dashboard after an Instance is renamed
- Database: Fix for default encoding not set to utf-8
- General: Made it more  clear on the summary page which jobs are not scheduled to running
- Guidance: Fix for shutdown discovery service errors
- Health:  Fix for sensitive info shown in Health Logs
- Health: Logs: Additional masking added for sensitive data
- Instances: Fix for issue Restoring and Cloning Instances in Groups or Clouds with an active Approval Policy
- Instances: Fix for powering on VM directly in Nutanix or Azure not triggering a status change to "running" for associated Instance within Morpheus
- Instances: Process History: Fix for negative execution times
- Integrations: Fix for Syslog integration creating Ansible integration
- KVM: Fix for unknown power status on KVM nodes
- Library: Added Error message for when attempting to delete an Option Type that is in use
- Library: Fix for custom Node Types not displaying default ``/var/log/`` logs in Instance detail Logs tab when no log path is set on Node Type. NOTE: Node Types must be edited and saved to enable fix
- Library: vCloud Director Node Types: The VM Image dropdown under the vCloud Director VM Options will now find image types ``vmware/vmdk/ovf``, where it previously only found ``vmdk/ovf``
- Load Balancer:  Fix for missing LBAAS2 logo on ``Infrastructure > Load Balancers`` and ``Load Balancers`` details page
- Migration: Fix for multiple running Usage records for Instances migrated from onapp to VMware
- Monitoring:  Fix for hyperlink hover behavior in the Apps and Checks sections
- Monitoring: Checks no longer automatically configured when Agent install is not selected on `Convert to Managed`
- |morpheus| Docker Hosts: Fix for |morpheus| Docker Host provisioning failures when using ``Infrastructure > Hosts`` and browser language is to German
- Networks: Fix for edits to Network Name or DNS settings not propagating to Openstack; CIDR field updated to read-only on edit.
- Open Telekom Cloud: Fix for backups not being deleted on instance deletion and backup archive list when preserve backups is not checked
- Open Telekom Cloud: Fix for default security groups being disassociated with VM's
- Open Telekom Cloud: Fix for Hypervisor Console not displaying
- OpenStack: Fix for incorrect memory utilization shown for Openstack Cloud on Cloud detail page and Virtual Machine Inventory Summary reports
- Openstack: Validation added to CIDR field when creating Openstack Networks
- Operations: Activity: Alarms: Fix for alarms for a cloud not being removed when cloud is deleted
- Oracle VM: CD-ROM slot assignment no longer uses Slot 4
- Policies: Updates to Max Price policy enforcement
- Policy: Fix for active Naming Policy not applying to first selected Cloud when no Default Cloud is set and multiple Clouds exist in selected Group.
- Provisioning: Fix for App and Clone wizards not displaying validation error for blank disk size
- Provisioning: Fix for evaluation of Platform variable on Provisioning Wizard Review panel
- Provisioning: Fix for review tab of the Instance and App Wizards incorrectly showing networks as set to an IP Range when using network override
- Roles: Fix for ``Provisioning : User`` role permission setting inhibiting Deployments
- SCVMM: Fix for discovered VMs not being removed when deleted in SCVMM
- SCVMM: Fix for Morpheus overriding some settings in SCVMM VM templates
- SCVMM: Fix for |morpheus| defaulting to the same target Host when Host is not specified during provisioning.
- Security Groups: Fix for duplicate AWS Security groups being displayed in |morpheus|
- Security: Fix for potential server side injection vulnerability
- Tasks: Fix for Chef Tasks -> Chef Run execution
- Tasks: Fix for some Results not working for Local Shell Script tasks
- Tasks: Fix for Local Shell Script tasks permissions issue ``*``
- Tasks: Fix for SSH task auth when using Keys
- Tenant:  Fix for reconfiguring Openstack Instance in subtenant not applying new flavor
- Tenant: Fix for deleting Tenants with existing custom Environments
- Usage: Fix for non-stopped usage records for discovered servers not closing after converting to managed and changing plan at same time.
- User Settings: Improvements added to user password salting
- vCloud Director: Fix for adding a private vCloud Director Cloud assigned to a subtenant not assigning networks and data stores to the subtenant
- vCloud Director: Fix for creating a vCloud Director Docker Host with custom image using default image instead
- vCloud Director: Fix for datastores recreated on cloud sync error
- vCloud Director: Fix for Discovered VM Plan matching not using Plans with `Custom Cores` checked and `Custom Memory` not checked on Plan config
- vCloud Director: Fix for Provisioning issue when using Isolated Networks ``*``
- vCloud Director: Fix for Windows Agent install when guest customization takes longer then 5 minutes
- vCloud Director: |morpheus| will now automatically remove ``/api`` or ``/api/`` if added to end of vCloud Director integration url
- Virtual Images: Fix for Master Tenant Private Images with no Tenant assigned being listed in Sub-Tenants Virtual Images section
- Virtual Images: Fix for Minimum Memory setting not saving when uploading a new Image
- Virtual Images: Users can no longer choose Image Source -> Target Conversion Type if the conversion type is not supported for source Image
- VMware: Fix for additional networks not defaulting type to ``vmxnet3``
- VMware: Fix for incorrect Operating System mappings on discovered Virtual Machines
- VMware: Fix for power state showing as running on Managed VM's that have been removed from vCenter
- VMware: Fix for unattend Agent Install mode on Windows 2008/R2*

Security Vulnerabilities Remediated
-----------------------------------

- CVE-2019-5427
- CVE-2019-12086
- CVE-2017-5929
- CVE-2019-0199
- CVE-2012-0881
- CVE-2013-4002
- CVE-2013-5960
- CVE-2013-5679
- CVE-2018-11771
- CVE-2019-3778

``* Included in 3.6.3-2 packages``
