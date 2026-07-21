.. _terraform_tools:

Terraform
=========

Overview
--------

|morpheus| provides Terraform integration as both a provisioning engine and a management tool. The Tools-level Terraform features focus on state management, drift detection, and operational commands for Terraform-managed infrastructure within |morpheus|.

Terraform state and operations are accessible from App and Instance detail pages for resources provisioned using Terraform blueprints or Terraform Instance Types.

Terraform State Management
---------------------------

|morpheus| stores and manages Terraform state for all Terraform-provisioned resources:

State Storage
^^^^^^^^^^^^^

- Terraform state is stored within |morpheus| (no external backend required)
- State is encrypted at rest in the |morpheus| database
- State versioning is maintained for rollback capability
- State can be viewed and edited from the App or Instance detail page

Viewing State
^^^^^^^^^^^^^

To view the current Terraform state:

#. Navigate to the App or Instance provisioned with Terraform
#. Select the **State** tab
#. The current state JSON is displayed with syntax highlighting

Editing State
^^^^^^^^^^^^^

.. WARNING:: Editing Terraform state directly is an advanced operation that can cause infrastructure inconsistencies. Only modify state when necessary (e.g., importing existing resources, removing orphaned entries).

To edit state:

#. Navigate to the App or Instance **State** tab
#. Click :guilabel:`EDIT STATE`
#. Modify the state JSON as needed
#. Click :guilabel:`SAVE`

Role permission **Provisioning: State** with ``Full`` access is required for state editing.

Drift Detection
---------------

|morpheus| can detect drift between the declared Terraform configuration and the actual infrastructure state:

- Drift is identified by running ``terraform plan`` against the current state
- Resources that have changed outside of Terraform management are flagged
- Drift information helps identify configuration issues and unauthorized changes

Running Terraform Commands
---------------------------

From the App or Instance detail page, Terraform commands can be executed:

#. Navigate to the App or Instance provisioned with Terraform
#. Open the **Console** or **Terraform** tab
#. Enter Terraform commands in the command field:

   - ``plan`` — Preview changes without applying
   - ``apply`` — Apply the current configuration
   - ``destroy`` — Destroy managed resources
   - ``refresh`` — Update state to match real infrastructure
   - ``output`` — Display output values
   - ``state list`` — List resources in state
   - ``state show <resource>`` — Show details of a specific resource

#. Click :guilabel:`EXECUTE`

Command output is displayed in real-time and stored in execution history.

.. NOTE:: Terraform commands are prefixed with ``terraform`` automatically. Enter only the subcommand (e.g., ``plan`` not ``terraform plan``).

Terraform Settings
------------------

Global Terraform settings are configured in :menuselection:`Administration --> Settings --> Provisioning` (Administration > Settings > Provisioning):

Terraform Runtime
^^^^^^^^^^^^^^^^^

- **TERRAFORM RUNTIME:** Select the Terraform runtime version (e.g., ``1.5.x``, ``1.6.x``)
- This sets the default Terraform version used for new deployments
- Individual Apps/Instances may specify version constraints in their configuration

State Backend
^^^^^^^^^^^^^

- By default, |morpheus| acts as the state backend
- Remote backends (S3, Azure Blob, GCS, Consul) can be configured in the Terraform configuration files

Terraform Providers
^^^^^^^^^^^^^^^^^^^

|morpheus| supports all Terraform providers available in the Terraform Registry. Provider plugins are downloaded automatically during ``terraform init`` based on the configuration's ``required_providers`` block.

Terraform Variables
-------------------

Variables for Terraform plans can be supplied from multiple sources:

- **Instance configuration:** Variables set during provisioning
- **Cypher secrets:** Sensitive values pulled from |morpheus| Cypher (``tfvars`` mount)
- **Input variables:** User-supplied values at execution time
- **Environment variables:** ``TF_VAR_*`` environment variables

To store Terraform variable files securely:

#. Navigate to |TooCyp| (Tools > Cypher)
#. Create a key with the ``tfvars`` mount point: ``tfvars/myapp/variables``
#. Store the tfvars content as the value
#. Reference in your Terraform configuration

Workspaces
----------

Terraform workspaces allow managing multiple environments with a single configuration:

- |morpheus| tracks the active workspace for each Terraform deployment
- Workspace selection can be part of the provisioning configuration
- State is maintained per-workspace

Execution History
-----------------

All Terraform command executions are tracked:

#. Navigate to the App or Instance detail page
#. Select the **History** tab
#. View past Terraform operations including:

   - Command executed
   - Execution timestamp
   - User who initiated the command
   - Exit code and output
   - Execution duration

Role Permissions
----------------

Terraform operations are controlled by the following role permissions:

- **Provisioning: State** — ``None``, ``Read``, ``Full``

  - **None:** Cannot access Terraform state
  - **Read:** Can view state and execution history
  - **Full:** Can edit state and execute Terraform commands

- **Provisioning: Apps** or **Provisioning: Instances** — Required to access the parent resource
