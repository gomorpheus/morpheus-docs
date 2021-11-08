Approvals
=========

|morpheus| and Service Now Approvals

Overview
--------

Policies can be created for Groups and Clouds to require approvals for actions with the built-in |morpheus| approvals engine, or via a ServiceNow integration. Approvals can be configured for Provisioning and Lifecycle extensions.

Configuring Approvals
---------------------

Configuring |morpheus| for Approvals

To configure |morpheus| for approvals:

#. Configure Roles for Approval access
#. Optionally configure a ServiceNow Integration for ServiceNow approvals.

   * Please note ServiceNow integration is not required for Internal Approvals.

#. Create approvals policies for:

   * Internal Approvals
   * SNOW Approvals

Configure Roles
^^^^^^^^^^^^^^^

Configure User Role access settings in |AdmRol| > (Role) > Operations: Approvals.

* All Users with a Role applied containing Operations: Approvals set to Full will have approval authority, and be able to Approve, Deny or Cancel approval requests.
* All Users with a Role applied that has Operations: Approvals set to Read will be able to view Approval requests and history, but will not be able to Approve, Deny or Cancel approval requests.
* All Users with a Role applied that has Operations: Approvals set to None will not have access to the Operations: Approvals section, and such will not be able to see or act on approval requests.
* Regardless of Role settings, any instance or app provisioned by any user to a group or cloud with an active Approval policy applied will require approval before the instance or app will provision.


ServiceNow Approvals
^^^^^^^^^^^^^^^^^^^^

Configure ServiceNow integration for SNOW Approvals

#. Navigate to Admin > Integrations
#. Select **+ NEW INTEGRATION**
#. Select **ServiceNow** from the Type dropdown in the Integration modal and enter:

   - Name
      Name of the integration in |morpheus|
   - Enabled
      Leave checked to enable the integration.
   - Host
      URL of the ServiceNow host (ex: https://ven0000.service-now.com)
   - User
      A User in ServiceNow that is able to access the REST interface and create/update/delete incidents, requests, requested items, item options, catalog items, workflows, etc.
   - Password
      Password for User above

#. Save Changes

|morpheus| then configures the integration with ServiceNow, syncs ServiceNow workflows which are available when creating approvals policies. (This process can take up to 5 minutes depending on the size of the workflow table in ServiceNow.)

Create Approval Policies
^^^^^^^^^^^^^^^^^^^^^^^^

* Policies applied to a Group are created in Infrastructure > Groups > (group) > Policies tab.
* Policies applied to a Cloud are created in Infrastructure > Clouds > (cloud) > Policies tab.

**To create an Approval policy:**

#. Navigate to the Policies tab in the Group or Cloud to which the policy will apply.
#. Select + ADD POLICY to open the New Policy wizard
#. Select Provision Approval from the Type dropdown
#. Add an optional description
#. Leave Enabled selected for this Policy to be active once saved.
    * Enabled can be deselected to disable to policy.
#. In the config section, select either Internal Approvals or ServiceNow Approvals:

   * Internal Approvals
      Approval requests will be managed within |morpheus| via the Operations: Approvals section.
   * ServiceNow Approvals
      Approval requests will be managed with ServiceNow (SNOW). Please note a ServiceNow integration (Admin: Integrations) must be configured prior to SNOW Approval policy generation.

      * For ServiceNow Approvals, select the appropriate ServiceNow workflow for this policy. Please note the workflows presented are created in ServiceNow and synced with |morpheus| .

#. Add the |morpheus| Accounts to which this policy will apply, or leave the Accounts field blank to apply to all accounts.
#. Save

Upon saving, a new policy is created in the Group or Cloud Policies tab.

.. NOTE:: SNOW Approvals will take a few moments to save as the policy is generated.

Managing Approval Requests
--------------------------

Once Instance approval policies are added to a Group or Cloud, any Instance or App provisioned into that Group or Cloud will create an approval request entry in the `Operations > Approvals` section.

.. NOTE:: User Role permission `Operations: Approvals > FULL` is required to manage Approvals.

* To Approve, Deny, or Cancel an internal approval request, select the request and use the Actions dropdown.
* To Cancel a ServiceNow Approval request, select the request and use the Actions dropdown. ServiceNow approvals are managed in ServiceNow.

.. NOTE:: Instances requiring provisioning approval will have a PENDING status until approved.

Each Approval Request will have:

* Name: A name for the approval in |morpheus|
* Monthly Price (Est.): The estimated monthly price of the Instance to be provisioned
* Request Type: What is being requested, such as Instance approval
* External Name: For ServiceNow integrations, the name of the approval in the ServiceNow console
* Type: Internal or ServiceNow
* Status
* Date Created
* Requested By: The |morpheus| user making the request
* Actions dropdown (for internal approval requests)
    * Approve
    * Deny
    * Cancel
* Actions dropdown (for ServiceNow requests)
    * Cancel

.. NOTE:: The Approvals list view can be sorted by NAME, REQUEST TYPE, EXTERNAL NAME, DATE CREATED, and REQUESTED BY

Internal approval requests
^^^^^^^^^^^^^^^^^^^^^^^^^^

To Approve, Deny or Cancel an Internal approval request:

#. Navigate to `Operations > Approvals`
#. Select the Name of the Approval request
#. Select Actions on the far right of the request
#. Select Approve, Deny, or Cancel from the Actions dropdown
#. Select OK on the confirmation modal

* When an Internal request is approved, the related instance will begin to provision immediately and the request will show approved.
* When an Internal request is denied, the related instances status will change to Denied and the request will show Rejected in the Approvals section.
* When an Internal request is canceled, the related related instances status will change to Cancelled and the request will be canceled.

ServiceNow Approval requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ServiceNow approval request are managed in ServiceNow. The process of approving or rejecting requests is determined by the ServiceNow Workflow selected when configuring the SNOW Approval policy. These Workflows are configured in ServiceNow.

.. IMPORTANT:: |morpheus| syncs with ServiceNow every 5 minutes. Once an Approval Request is Approved or Rejected in Service Now, it will take up to 5 minutes for the instance to respond accordingly, and the status for the approval request in the Approvals section in |morpheus| to update.
