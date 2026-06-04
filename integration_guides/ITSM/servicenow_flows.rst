ServiceNow Flows for Approvals
================================

.. tier-note:: Enterprise
   :exclude: Essentials, Advanced

   ITSM integrations are an Enterprise-only feature.

Overview
--------

|morpheus| supports two types of ServiceNow automation for approval workflows: **Workflows** (legacy) and **Flows** (modern). ServiceNow Flows are the newer automation engine in ServiceNow (Flow Designer) that provides a more modern, visual interface compared to traditional ServiceNow Workflows.

When configuring approval policies in |morpheus|, you can select either a synced Workflow or a synced Flow as the approval automation to trigger in ServiceNow.

Workflows vs. Flows
-------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Aspect
     - Workflows (Legacy)
     - Flows (Modern)
   * - ServiceNow Engine
     - Workflow Editor
     - Flow Designer
   * - Recommended For
     - Existing implementations
     - New implementations
   * - |morpheus| Config Key
     - ``workflowId``
     - ``flowId`` (with ``workflowType: 'flow'``)
   * - ServiceNow Direction
     - Being deprecated by ServiceNow
     - Actively developed by ServiceNow

.. NOTE:: ServiceNow is progressively moving customers from Workflows to Flow Designer. New approval integrations should use Flows where possible.

Prerequisites
-------------

- A ServiceNow integration must be configured in |morpheus| (|AdmInt| > ServiceNow)
- Flows must be published and active in ServiceNow's Flow Designer
- The ServiceNow service account used by |morpheus| must have access to read Flow definitions
- Flows must be designed to handle approval catalog item requests

Configuring Flow-Based Approvals
---------------------------------

Step 1: Configure ServiceNow Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If not already configured:

#. Navigate to |AdmInt|
#. Click :guilabel:`+ NEW INTEGRATION`
#. Select **ServiceNow** from the Type dropdown
#. Enter the Host URL, User, and Password
#. Click :guilabel:`SAVE CHANGES`

|morpheus| syncs both Workflows and Flows from ServiceNow. This process may take up to 5 minutes depending on the size of your ServiceNow instance.

Step 2: Create an Approval Policy with Flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the Policies tab for the target Group or Cloud
#. Click :guilabel:`+ ADD POLICY`
#. Select an approval policy type (e.g., **Provision Approval**)
#. Select **ServiceNow** as the approval type
#. Select the ServiceNow integration
#. In the workflow/flow selection dropdown, choose the desired **Flow**

   .. NOTE:: Flows synced from ServiceNow appear alongside Workflows in the selection dropdown. They are distinguished by their naming convention from Flow Designer.

#. Click :guilabel:`SAVE`

How Flow Approvals Work
-----------------------

When a user triggers an action covered by a ServiceNow Flow approval policy:

#. |morpheus| creates an approval request in ServiceNow, triggering the configured Flow
#. The Flow executes in ServiceNow's Flow Designer engine, which may include:

   - Approval steps with designated approvers
   - Conditional logic based on request attributes
   - Notifications and escalations
   - Integration with other ServiceNow modules

#. The provisioning request in |morpheus| enters a **Pending** state
#. |morpheus| polls ServiceNow for approval status updates (every 5 minutes)
#. When the Flow reaches an approved/rejected outcome, |morpheus| updates the request accordingly

Designing Flows for |morpheus| Approvals
------------------------------------------

When designing Flows in ServiceNow's Flow Designer for use with |morpheus| approval policies:

- The Flow should accept a catalog item request as its trigger
- Include at least one **Approval** action in the Flow
- Ensure the Flow sets a clear approved/rejected final state
- Consider including notification actions for approvers
- Test the Flow in ServiceNow before connecting it to |morpheus|

Migrating from Workflows to Flows
----------------------------------

To migrate existing approval policies from Workflows to Flows:

#. Create the equivalent Flow in ServiceNow's Flow Designer
#. Test the Flow independently in ServiceNow
#. Edit the existing approval policy in |morpheus|
#. Change the selected automation from the legacy Workflow to the new Flow
#. Save the policy

.. IMPORTANT:: Pending approvals created under the old Workflow will continue to be managed by that Workflow. Only new requests after the policy change will use the Flow.

Troubleshooting
---------------

**Flows not appearing in the selection dropdown**

- Wait up to 5 minutes after saving the ServiceNow integration for sync to complete
- Verify the Flow is published and active in ServiceNow
- Confirm the service account has read access to Flow definitions

**Flow approvals not syncing back to |morpheus|**

- Check that the Flow sets a definitive approved/rejected status
- Verify |morpheus| ServiceNow integration credentials are valid
- Check the 5-minute polling interval—recent changes may not yet be reflected
