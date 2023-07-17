.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. WARNING:: |morpheus| |morphver| only supports rolling upgrades for HA environments when upgrading from v6.0.2+.

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - Added CLI and API coverage for removing backup results. API calls and CLI commands are listed in API and CLI documentation :superscript:`6.2.0`
             - When running Workflows against Instances on demand using the API or CLI, users may select which phase should be run in the case of Provisioning Workflows. This feature is also added to |morpheus| UI with this release
:Kubernetes: - Added Kubernetes 1.25, 1.26 and 1.27 layouts for vCloud Director :superscript:`6.2.0`
              - Added default Kubernetes 1.25, 1.26, and 1.27 layouts for Google Cloud Platform :superscript:`6.2.0`
:Plugins: - IBM PowerVC Cloud plugin is now available at share.morpheusdata.com. Adding this plugin to a |morpheus| appliance will open the capability to add new PowerVC Clouds. This is an ongoing project and will be improved with future releases
:VDI Pools: - Favorited XaaS Instances will no longer appear in the VDI list page
:Workflows: - When running a Workflow on demand against an Instance, users can now select a phase of Tasks to run when a Provisioning Workflow is selected :superscript:`6.2.0`


Fixes
=====

:API & CLI: - Fixed an issue that caused some GET requests for specific networks to fail with a 500 reponse even though the networks were visible in the UI :superscript:`6.2.0`
             - GET calls to ``/api/instances`` no longer fail with permissions warnings when there is an Instance pending an internal provisioning approval :superscript:`6.2.0`
             - GET calls to ``/api/library/instance-types`` with the ``max=-1`` parameter are now returning all instance type results for instance types and library instance types :superscript:`6.2.0`
             - GET requests to ``/api/health`` now return storage metrics to match the storage information viewable on the appliance health page in UI :superscript:`6.2.0`
             - When approve provision-type Policies are active, 403 errors are no longer surfaced but rather the appropriate messages are given letting the user know that the provision is pending approval :superscript:`6.2.0`
:Automation Scale Thresholds: - When editing a Scale Threshold shared from the Primary Tenant, an error message is now received rather than a failure with a 500 error. Scale Thresholds owned by the Subtenant can still be edited :superscript:`6.2.0`
:Catalog: - Fixed an issue that could cause provisioning failures when Catalog Items requiring ServiceNow Approvals were provisioned :superscript:`6.2.0`
:Costing: - Fixed invoices continuing to show projected cost values for prior months :superscript:`6.2.0`
:DNS: - Improved DNS validation methods to improve performance of the saving action for new or edited DNS integrations
:Groups: - When creating a new Group as part of adding a Cloud, the Code field value entered for the Group is now saved properly :superscript:`6.2.0`
:Instances: - Server tags are now accessible through the Instance variable :superscript:`6.2.0`
:Kubernetes: - Fixed issue with potential records locks causing slow sync times or timeouts for managed external kubernetes clusters :superscript:`6.2.0`
:Layouts: - When clicking on the OPTIONS button for environment variables when editing Layouts or Node Types, the background tab no longer shifts back to Instance Types (from either Layouts or Node Types) :superscript:`6.2.0`
:OpenStack: - Fixed an issue that caused Resource Pools for OpenStack Clouds to disappear from |morpheus| after creation (the Projects remain in OpenStack) :superscript:`6.2.0`
             - Fixed an issue that caused an incorrect IP address to be assigned when a new NIC with static IP was added via reconfigure to OpenStack workloads :superscript:`6.2.0`
:Plans & Pricing: - Fixed a typo in Disk Only-type Prices when setting the Volume Type to "Thin disk provisioning" which was spelled incorrectly :superscript:`6.2.0`
:Policies: - When creating Cloud-scoped Policies from a Subtenant, only the Clouds available to the Subtenant are shown in the select list :superscript:`6.2.0`
:Scaling: - Fixed an issue that could cause Instances to be hung in a pending state when scaled very large (approximately 40 or more nodes) :superscript:`6.2.0`
:Usage: - Optimized usage queries to improve performance in environments with large account usage tables :superscript:`6.2.0`
:VMware: - Fixed an issue that caused shared Datastores not to be visible for some clusters that it was shared with :superscript:`6.2.0`
:Workflows: - Fixed an issue that caused Teardown-phase Tasks not to run at Instance delete :superscript:`6.2.0`
             - If Teardown-phase Tasks in Provisioning Workflows fail, the delete action is no longer taken on the Instance. Review the failure in Instance history and delete the Instance again to complete the operation :superscript:`6.2.0`
             - Workflow access permissions are now honored for Workflows which are attached to Instances :superscript:`6.2.0`
:XaaS: - Workflow Task execution is now listed in the History tab for XaaS Instances as it is for other Instance types
:vCloud Director: - Controls to start and stop VMs now work correctly from the Primary Tenant when workloads have been shared to a Subtenant :superscript:`6.2.0`


Appliance & Agent Updates
=========================

:Agents: - morpheus-vm-node packages (v3.2.15) will now do a post-inst reconfigure to fix issue with agent path after package is updated with yum/apt and reconfigure is not performed :superscript:`6.2.0`
:Appliance: - Added ``firewall['chain_input_policy']`` configuration to morpheus.rb. When set to 'DROP', the chain input policy in the appliance iptable will be set to DROP following reconfigure :superscript:`6.2.0`
            - mysql: ``mysql['innodb_buffer_pool_size']``. ``mysql['join_buffer_size']``, ``mysql['read_buffer_size']``, ``mysql['read_rnd_buffer_size']``, ``mysql['sort_buffer_size']``, and ``mysql['innodb_buffer_pool_instances']`` added as morpheus.rb config options for emb :superscript:`6.2.0`