.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. WARNING:: Rolling upgrades to |morphver| from |morpheus| version 6.0.2 or lower are not supported for HA environments.

.. WARNING:: 6.1.1 & 6.0.3 contain database datatype modifications on account_invoice and account_invoice_item that may cause long initial ui start up times while the modifications are ran in mysql for environments with over 100k invoice records.

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - Added CLI and API coverage for removing backup results. API calls and CLI commands are listed in API and CLI documentation :superscript:`6.0.5`
:Code: - Configure code repositories (|ProCod|) as import or export repositories. Export |morpheus| items as code and import them into new environments. See `documentation <https://docs.morpheusdata.com/en/latest/provisioning/code/code.html#import-and-export>`_
:Forms: - Form Inputs now have "Export As Tag" and "Display Value on Details" options as standard Inputs have
         - Input default are now honored when Inputs are applied to Forms
         - Quality of life improvements made to Forms. This includes display, spacing and localization improvements related to the presentation of Forms
:Kubernetes: - Added Kubernetes 1.25, 1.26 and 1.27 layouts for vCloud Director :superscript:`6.0.5`
              - Added default Kubernetes 1.25, 1.26, and 1.27 layouts for Google Cloud Platform :superscript:`6.0.5`
:MySQL Database: - ``mysql['innodb_buffer_pool_size']``. ``mysql['join_buffer_size']``, ``mysql['read_buffer_size']``, ``mysql['read_rnd_buffer_size']``, ``mysql['sort_buffer_size']``, and ``mysql['innodb_buffer_pool_instances']`` added as morpheus.rb config options for emb :superscript:`6.0.5`
:Workflows: - When running a Workflow on demand against an Instance, users can now select a phase of Tasks to run when a Provisioning Workflow is selected :superscript:`6.0.5`


Fixes
=====

:API & CLI: - Fixed an issue that caused some GET requests for specific networks to fail with a 500 reponse even though the networks were visible in the UI :superscript:`6.0.5`
             - GET calls to ``/api/instances`` no longer fail with permissions warnings when there is an Instance pending an internal provisioning approval :superscript:`6.0.5`
             - GET calls to ``/api/library/instance-types`` with the ``max=-1`` parameter are now returning all instance type results for instance types and library instance types :superscript:`6.0.5`
             - GET requests to ``/api/health`` now return storage metrics to match the storage information viewable on the appliance health page in UI :superscript:`6.0.5`
             - When approve provision-type Policies are active, 403 errors are no longer surfaced but rather the appropriate messages are given letting the user know that the provision is pending approval :superscript:`6.0.5`
:Agent: - morpheus-vm-node packages (v3.2.15) will now do a post-inst reconfigure to fix issue with agent path after package is updated with yum/apt and reconfigure is not performed :superscript:`6.0.5`
:Automation Scale Thresholds: - When editing a Scale Threshold shared from the Primary Tenant, an error message is now received rather than a failure with a 500 error. Scale Thresholds owned by the Subtenant can still be edited :superscript:`6.0.5`
:Catalog: - Fixed an issue that could cause provisioning failures when Catalog Items requiring ServiceNow Approvals were provisioned :superscript:`6.0.5`
:Costing: - Fixed invoices continuing to show projected cost values for prior months :superscript:`6.0.5`
:DNS: - DNS integrations set to Groups or Clouds are no longer used. Since domain records already refer to their DNS integration, this is now used over what is set on the Group or Cloud
:Forms: - "Display Value on Details" option for existing Inputs is now honored when Input is used in Forms. This displays the Input value on the provisioned Instance's detail page
         - Fixed Networks not populating after changing configured Group on Catalog Items built from Forms which had been shared down to Subtenants
         - Fixed required disks and networks not sharing down to Subtenants when Catalog Items built from Forms were shared
         - The disk type and network type selection checkboxes on the Cloud are now being properly factored into the catalog item types using Forms
         - Updated Clouds Inputs for Forms to account for specific situations in multiple Clouds
:Groups: - When creating a new Group as part of adding a Cloud, the Code field value entered for the Group is now saved properly :superscript:`6.0.5`
:Health: - The search functionality within the Logs tab of the Health page (|AdmHea|) now works properly. Elasticsearch query syntax is supported in this search field :superscript:`6.0.6`
:Instances: - Server tags are now accessible through the Instance variable :superscript:`6.0.5`
:Layouts: - Fixed an issue that caused a duplicate Ubuntu 20.04 Layout to be seeded in as part of the default catalog for each Cloud type
           - When clicking on the OPTIONS button for environment variables when editing Layouts or Node Types, the background tab no longer shifts back to Instance Types (from either Layouts or Node Types) :superscript:`6.0.5`
:OpenStack: - Fixed an issue that caused Resource Pools for OpenStack Clouds to disappear from |morpheus| after creation (the Projects remain in OpenStack) :superscript:`6.0.5`
             - Fixed an issue that caused an incorrect IP address to be assigned when a new NIC with static IP was added via reconfigure to OpenStack workloads :superscript:`6.0.5`
:Oracle Cloud: - When OCI Clouds are scoped to specific Compartments, VMs are now only discovered from the scoped Compartment :superscript:`6.0.6`
:Plans & Pricing: - Fixed a typo in Disk Only-type Prices when setting the Volume Type to "Thin disk provisioning" which was spelled incorrectly :superscript:`6.0.5`
:Policies: - When creating Cloud-scoped Policies from a Subtenant, only the Clouds available to the Subtenant are shown in the select list :superscript:`6.0.5`
:Scaling: - Fixed an issue that could cause Instances to be hung in a pending state when scaled very large (approximately 40 or more nodes) :superscript:`6.0.5`
:User Settings: - The Dark Mode theme now works properly from within Subtenants
:VMware: - Fixed an issue that caused shared Datastores not to be visible for some clusters that it was shared with :superscript:`6.0.5`
:Workflows: - Fixed an issue that caused Post Provision-phase Tasks not to run in Provisioning Workflows which were attached to Terraform-type Layouts :superscript:`6.0.5`
             - Fixed an issue that caused Teardown-phase Tasks not to run at Instance delete :superscript:`6.0.5`
             - If Teardown-phase Tasks in Provisioning Workflows fail, the delete action is no longer taken on the Instance. Review the failure in Instance history and delete the Instance again to complete the operation :superscript:`6.0.5`
             - Workflow access permissions are now honored for Workflows which are attached to Instances :superscript:`6.0.5`
:vCloud Director: - Controls to start and stop VMs now work correctly from the Primary Tenant when workloads have been shared to a Subtenant :superscript:`6.0.5`


Appliance & Agent Updates
=========================

:Appliance: - Added ``firewall['chain_input_policy']`` configuration to morpheus.rb. When set to 'DROP', the chain input policy in the appliance iptable will be set to DROP following reconfigure :superscript:`6.0.5`