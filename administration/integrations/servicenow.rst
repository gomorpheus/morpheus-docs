ServiceNow
----------

Add ServiceNow Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Administration -> Integrations``
#. Select ``+ NEW INTEGRATION``
#. Select ``ServiceNow`` from the TYPE dropdown.
#. Add the following:

   NAME
    Name of the Integration in Morpheus.
   ENABLED
    Leave checked to enable the Integration.
   HOST
    Url of the ServiceNow Instance ex: https://your.instance.service-now.com
   USER
    A user in ServiceNow that is able to access the REST interface and create/update/delete incidents, requests, requested items, item options, catalog items, workflows, etc.
   PASSWORD
    Above ServiceNow user's password

#. Save Changes


Add ServiceNow Provision Approval Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add Cloud Policy
''''''''''''''''

#. Navigate to ``Infrastructure -> Clouds``
#. Select a Cloud by clicking on the Cloud Name link
#. Select the POLICIES tab
#. Select + ADD POLICY
#. Select ``Provision Approval``
#. Optionally enter a description for the Policy
#. Configure the following:

   APPROVAL INTEGRATION
    Select the ServiceNow Integration already configured in ``Administration -> Integrations`` to use for the Approval Policy.

   WORKFLOW
    Select the ServiceNow workflow for the Approval workflow in ServiceNow. Note these workflows are configured and synced in from the ServiceNow Integration.

   TENANTS (if applicable)
     Only required for multi-tenant permission scoping. For the policy to apply to a sub-tenant, type the name of the tenant(s) and select the Tenant(s) from the list.

#. Save Changes

Add Group Policy
''''''''''''''''

#. Navigate to ``Infrastructure -> Groups``
#. Select a Group by clicking on the Group Name link
#. Select the POLICIES tab
#. Select + ADD POLICY
#. Select ``Provision Approval``
#. Optionally enter a description for the Policy
#. Configure the following:

   APPROVAL INTEGRATION
    Select the ServiceNow Integration already configured in ``Administration -> Integrations`` to use for the Approval Policy.

   WORKFLOW
    Select the ServiceNow workflow for the Approval workflow in ServiceNow. Note these workflows are configured and synced in from the ServiceNow Integration.

   TENANTS (if applicable)
     Only required for multi-tenant permission scoping. For the policy to apply to a sub-tenant, type the name of the tenant(s) and select the Tenant(s) from the list.

#. Save Changes

Using Approval Policies
^^^^^^^^^^^^^^^^^^^^^^^

Any Instance provisioned into a Cloud or Group with an Approval Policy enabled will be in a PENDING state until the request in Approved.

Instances pending a ServiceNow approval will show "Waiting for Approval" with the Requested Item number and Request number, ex: ``Waiting for Approval [RITM0010002 - REQ0010002]``.

ServiceNow Approval requests are displayed in ``Operations -> Approvals``.
Instances pending a ServiceNow approval must be Approved in ServiceNow for provisioning to initiate. Approval requests from a ServiceNow Approval Policy cannot be approved in Morpheus, only Internal Approvals.

ServiceNow Approval requests are displayed in Morpheus under ``Operations -> Approvals``. Pending ServiceNow Approval requests can be cancelled in Morpheus by selecting the request and then selecting ``ACTIONS -> Cancel``.

Once a pending ServiceNow Approval request is Approved in ServiceNow, the Instance(s) will begin to provision in Morpheus within 5 minutes of being approved in ServiceNow.
