.. _snow:

ServiceNow
----------

Overview
^^^^^^^^

IT Service Management (ITSM) is an important area of focus for many organizations. Organizations invested in ServiceNow as an ITSM provider will find that |morpheus| integrates tightly with some of the most-used features. After integrating ServiceNow with |morpheus|, both environments can be used interchangeably and the results are synced to both places. This guide walks administrators through the process of integrating ServiceNow with |morpheus| and how |morpheus| can be used to effectively leverage the best of ServiceNow.

.. TIP:: The ServiceNow integration guide is also available as a `PDF download <https://morpheusdata.com/wp-content/uploads/content/ServiceNow-Cloud-Management-Morpheus-CMP-1.pdf>`_, which includes additional example use cases and screenshots.

Add ServiceNow Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmInt|
#. Select :guilabel:`+ NEW INTEGRATION`
#. Select "ServiceNow" from the dropdown list
#. Add the following:

   NAME
    A friendly name to describe the ServiceNow integration in |morpheus|.
   ENABLED
    Check "Enabled" to allow consumption of this ServiceNow integration in |morpheus|.
   SERVICENOW HOST
    URL of the ServiceNow instance (ex: https://your.instance.service-now.com), keep in mind you can create multiple ServiceNow integrations in |morpheus| if needed.
   USER/PASSWORD
    A user in ServiceNow that is able to access the REST interface and create/update/delete incidents, requests, requested items, item options, catalog items, workflows, etc. The list of necessary roles includes ``x_moda_morpheus_ca.integration`` (available if the |morpheus| ServiceNow plugin is installed from the ServiceNow Store), ``catalog_admin``, ``itil``, ``rest_service``, ``web_service_admin`` and ``import_transformer``.
   CMDB CUSTOM MAPPING
    If needed, administrators can opt to populate a specific field in the ServiceNow table and such mapping is identified here with a JSON code snippet. Below is an example that populates the ``object_id`` field in the CM database with the |morpheus| instance name and two other field examples:

    .. code-block:: bash

      {
      "object_id":"<%=instance.name%>",
      "SN_field_id2":"<%=morph.varname2%>",
      "SN_field_id3":"<%=morph.varname3%>"
      }

   CMDB CLASS MAPPING
    Define the mapping between |morpheus| server types and ServiceNow CI classes. Select a |morpheus| server type from the dropdown menu and a new field will appear in the list. Enter a ServiceNow CI class into the text field to create the association
   CMDB BUSINESS OBJECT
    Allows the user to define the table CMDB records are written to if they prefer this over |morpheus| default. By default, |morpheus| writes to the ``cmdb_ci_vm_instance`` table.

#. Save Changes

.. important:: |morpheus| supports integration with single-domain and multi-domain ServiceNow appliances. In multi-domain installations, a selected ServiceNow company can be mapped to a selected |morpheus| Tenant for purposes of exposing |morpheus| Library items only to users within a certain company. In this configuration, ServiceNow integrations should be added in each relevant |morpheus| Tenant. Further setup steps for exposing |morpheus| library items to ServiceNow are included in a later section below.

ServiceNow Configuration Management Database (CMDB)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ServiceNow CMDB is central to maintaining a complete record of IT infrastructure at many organizations. The |morpheus| ServiceNow integration can create and update configuration item (CIs) records as new services are provisioned or existing services are reconfigured. Once a ServiceNow integration is set as the CMDB for a Cloud or Group, CI records are created and managed by |morpheus|.

Setting a CMDB on a Group
`````````````````````````

When adding or editing a |morpheus| Group, any active ServiceNow integration can be set as the CMDB.

#. Navigate to Infrastructure > Groups
#. Select an existing Group name from the list
#. Click :guilabel:`EDIT`
#. Under "Advanced Options", select an active ServiceNow integration from the CMDB dropdown menu
#. If desired, select "CMDB DISCOVERY" to create CMDB CI records for discovered (unmanaged) servers that |morpheus| automatically onboards to this Group

This setting is also available when creating a Group. Rather than selecting an existing Group in step two above, click :guilabel:`+ CREATE` to make a new Group.

Setting a CMDB on a Cloud
`````````````````````````

When adding or editing a |morpheus| Cloud, any active ServiceNow integration can be set as the CMDB.

#. Navigate to Infrastructure > Clouds
#. Select an existing Cloud name from the list
#. Click :guilabel:`EDIT`
#. Under "Advanced Options", select an active ServiceNow integration from the CMDB dropdown menu
#. If desired, select "CMDB DISCOVERY" to create CMDB CI records for discovered (unmanaged) servers that |morpheus| automatically onboards to this Cloud

This setting is also available when creating a Cloud. Rather than selecting an existing Cloud in step two above, click :guilabel:`+ ADD` to make a new Cloud.

Provisioning and CI Records
```````````````````````````

With a ServiceNow instance integrated with |morpheus| and the instance set as the CMDB for a |morpheus| Group or Cloud, we will see CI records created as new resources are provisioned to the Cloud or Group in |morpheus|. After the provisioning process has completed, a CI record should exist with a name value equal to the Instance name in |morpheus|.

Provisioned and active Instances in |morpheus| will have CI records with an "On" state in ServiceNow. After they are deleted in |morpheus|, the state value will be rolled to "Terminated" in ServiceNow as expected.

|morpheus| will also populate a number of additional fields in ServiceNow including IP address, FQDN and more. Custom views can be created in ServiceNow to expose these fields.

ServiceNow Approval Policies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|morpheus| offers its own approval engine out of the box, but some organizations prefer ServiceNow to be their final approval authority. With a ServiceNow instance integrated with |morpheus|, administrators can create provision approval policies and tie them to an active ServiceNow integration. With the policy in place, any new provisioning within the policy scope (Global, Group, Cloud, User, or Role) is sent to ServiceNow for approval before provisioning will go ahead in |morpheus|. Approvals are synced between the two applications every minute.

Add ServiceNow Provision Approval Policy to a Cloud
```````````````````````````````````````````````````

.. NOTE:: Any Instance provisioned into a Cloud with an approval policy enabled will not proceed without the required approval.

To add a ServiceNow Approval policy to a Cloud:

#. Navigate to ``Infrastructure > Clouds``
#. Select a Cloud by clicking on the desired Cloud name link
#. Select the POLICIES tab
#. Click :guilabel:`+ ADD POLICY`
#. Select ``Provision Approval`` from the type dropdown
#. Optionally enter a description for the Policy
#. Configure the following:

   APPROVAL INTEGRATION
    Select the ServiceNow Integration already configured in |AdmInt| to use for the approval policy.

   WORKFLOW
    Select the ServiceNow workflow for the approval in ServiceNow (if desired). These workflows are configured and synced in from the ServiceNow Integration.

   TENANTS (if applicable)
     Only required for multi-tenant permission scoping. For the policy to apply to a Subtenant, type the name of the tenant(s) and select the Tenant(s) from the typeahead list.

#. Save Changes

Add ServiceNow Provision Approval Policy to a Group
```````````````````````````````````````````````````

.. NOTE:: Any Instance provisioned into a Group with an approval policy enabled will not proceed without the required approval.

To add a ServiceNow Approval policy to a Group:

#. Navigate to ``Infrastructure > Groups``
#. Select a Group by clicking on the Group name
#. Select the POLICIES tab
#. Click :guilabel:`+ ADD POLICY`
#. Select ``Provision Approval``
#. Optionally enter a description for the Policy
#. Configure the following:

   APPROVAL INTEGRATION
    Select the ServiceNow Integration already configured in |AdmInt| to use for the approval policy.

   WORKFLOW
    Select the ServiceNow workflow for the approval in ServiceNow (if desired). These workflows are configured and synced in from the ServiceNow Integration.

   TENANTS (if applicable)
    Only required for multi-tenant permission scoping. For the policy to apply to a Subtenant, type the name of the tenant(s) and select the Tenant(s) from the typeahead list.

#. Save Changes

Using ServiceNow Approval Policies
``````````````````````````````````

Any Instance provisioned into a Cloud or Group with an approval policy enabled will be in a PENDING state until the request is approved.

Instances pending a ServiceNow approval will show "Waiting for Approval" with the Requested Item number and Request number, ex: ``Waiting for Approval [RITM0010002 - REQ0010002]``.

ServiceNow approval requests are displayed in ``Operations > Approvals``. Instances pending a ServiceNow approval must be approved in ServiceNow for provisioning to initiate. Approval requests from a ServiceNow approval policy cannot be approved in |morpheus|, only approvals originating from |morpheus|.

ServiceNow approval requests are displayed in |morpheus| under ``Operations > Approvals``. Pending ServiceNow approval requests can be cancelled in |morpheus| by selecting the request and then selecting ``ACTIONS > Cancel``.

Once a pending ServiceNow approval request is approved in ServiceNow, the Instance(s) will begin to provision in |morpheus| within one minute of being approved in ServiceNow.

ServiceNow Monitoring Integration Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: A ServiceNow integration must be already configured in |AdmInt| to enable ServiceNow monitoring.

The ServiceNow monitoring integration is enabled and configured in |AdmSetMon|. As long as the "Enabled" switch is activated, |morpheus| will report monitoring data to ServiceNow. Configuration selections are described below:

Enabled
  Enables the ServiceNow monitoring integration
Integration
  Select from an existing ServiceNow integration in `|AdmInt|`
New Incident Action
  The ServiceNow action to take when a |morpheus| incident is created
Close Incident Action
  The Service Now action to take when a |morpheus| incident is closed

Incident Severity Mapping

.. [width="40%",frame="topbot",options="header"]

=================== =================
|morpheus| Severity ServiceNow Impact
------------------- -----------------
Info                Low/Medium/High
Warning             Low/Medium/High
Critical	          Low/Medium/High
=================== =================

Once finished working with configuration, click :guilabel:`APPLY`

.. image:: /images/integration_guides/itsm/servicenow/3monitoringConfig.png
  :width: 50%

ServiceNow Service Catalog Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to integrating with key ServiceNow features, |morpheus| offers a free plugin directly from the ServiceNow Store. Once the plugin is installed, |morpheus| Self-Service Catalog Items can be presented as provisioning options in the ServiceNow catalog for ordering.

The |morpheus| plugin supports integration with ServiceNow whether it’s configured for a single tenant or for multiple domains. When both |morpheus| and ServiceNow are configured for multiple Tenants, we can create ServiceNow integrations in any relevant |morpheus| Tenant and map those to specific companies in ServiceNow. Any exposed library items would only be shared with users in the relevant ServiceNow company. The |morpheus| plugin will automatically detect whether the *ServiceNow Domain Support–Domain Extensions Installer plugin* has been installed and respond accordingly. Additionally, the *User Criteria Scoped API plugin* must also be enabled on the ServiceNow instance for multi-tenant use.

Depending on the scenario, setup steps for the |morpheus| plugin will be slightly different. Setup steps for both single and domain-separated ServiceNow environments are included below.

.. IMPORTANT:: A valid SSL Certificate is required on the |morpheus| Appliance for the ServiceNow plugin to be able to communicate with the appliance.

Single-Domain ServiceNow Configuration
``````````````````````````````````````

#. Install the |morpheus| plugin from the ServiceNow store, refer to the `Morpheus Data plugin for ServiceNow <https://store.servicenow.com/appStoreAttachments.do?sys_id=73029271dbbd6450087656a8dc961995>`_ installation instructions for additional help with the installation steps
#. Navigate to |morpheus| Catalog > Properties
#. Set the following properties:

   MID Server
    If desired, specify the name of an existing MID server
   |morpheus| Appliance Endpoint
    The full URL to your |morpheus| appliance
   Username
    |morpheus| user that the plugin will connect as to the |morpheus| API
   Password
    Password to the above |morpheus| account
   |morpheus| Manage Workflows?
    Indicate whether |morpheus| should manage workflows. If this option is checked, |morpheus| will overwrite the workflow and set it to "Morpheus (Internal) Catalog Item Provision Instance" on sync

  .. important:: The |morpheus| service account integrated with the plugin interacts with the |morpheus| appliance through |morpheus| API and must have the appropriate Role permissions to complete all provisioning requests from the ServiceNow plugin. Often it's easiest to make a service account with full administrator rights to avoid failed provisioning. If you'd prefer to create a minimal service account for security reasons, ensure the Role for the service account User has the following permissions:

    - Personas: Standard: Full
    - Personas: Service Catalog: Full
    - Features: Provisioning: Instances: Full
    - Features: Provisioning: Apps: Full
    - Groups: Full rights to all Groups containing Clouds you will expose to ServiceNow
    - Instance Types: Full rights to all Instance Types you will expose to ServiceNow
    - Blueprints: Full rights to all Blueprints you will expose to ServiceNow
    - Catalog Item Types: Full rights to all Catalog Item Types you will expose to ServiceNow

    Users created from SAML Identity Sources cannot authenticate with the |morpheus| API and cannot be used for the ServiceNow plugin.

.. image:: /images/integration_guides/itsm/servicenow/4servicenowProperties.png
  :width: 50%

Multi-Domain ServiceNow Configuration
`````````````````````````````````````

#. Install the |morpheus| plugin from the ServiceNow store, refer to the `Morpheus Data plugin for ServiceNow <https://store.servicenow.com/appStoreAttachments.do?sys_id=73029271dbbd6450087656a8dc961995>`_ installation instructions for additional help with the installation steps
#. Navigate to |morpheus| Catalog > Multi-Tenant Credentials
#. Set the following properties:

   |morpheus| Appliance Endpoint
    The full URL to your |morpheus| appliance
   |morpheus| Tenant ID
    The integer database ID for the selected Tenant
   Username
    |morpheus| user that the plugin will connect as to the |morpheus| API. This user must exist within the |morpheus| Tenant being linked to the chosen ServiceNow company
   Password
    The password for the above user
   ServiceNow Company
    Select a company from the list to link with the Tenant whose ID was entered above
   MID Server
    If desired, specify the name of an existing MID server. Note that configuring a multi-domain MID server requires the ``glide.ecc.enable_multidomain_mid`` property in ``sys_properties.list`` be set to ``true`` prior to creating the MID server in the global domain. This allows the MID server to explore any domain for which it has the credentials. The ServiceNow user (which the MID server authenticates with) must be in the global domain as well. For more, see `this section of ServiceNow documentation <https://docs.servicenow.com/bundle/rome-servicenow-platform/page/product/mid-server/concept/c_MIDServerDomainSeparation.html>`_.
   |morpheus| Manage Workflows?
    Indicate whether |morpheus| should manage workflows. If this option is checked, |morpheus| will overwrite the workflow and set it to "Morpheus (Internal) Catalog Item Provision Instance" on sync

  .. important:: The |morpheus| service account integrated with the plugin interacts with the |morpheus| appliance through |morpheus| API and must have the appropriate Role permissions to complete all provisioning requests from the ServiceNow plugin. Often it's easiest to make a service account with full administrator rights to avoid failed provisioning. If you'd prefer to create a minimal service account for security reasons, ensure the Role for the service account User has the following permissions:

    - Personas: Standard: Full
    - Personas: Service Catalog: Full
    - Features: Provisioning: Instances: Full
    - Features: Provisioning: Apps: Full
    - Groups: Full rights to all Groups containing Clouds you will expose to ServiceNow
    - Instance Types: Full rights to all Instance Types you will expose to ServiceNow
    - Blueprints: Full rights to all Blueprints you will expose to ServiceNow
    - Catalog Item Types: Full rights to all Catalog Item Types you will expose to ServiceNow

    Users created from SAML Identity Sources cannot authenticate with the |morpheus| API and cannot be used for the ServiceNow plugin.

Adding to ServiceNow Catalog
````````````````````````````

Once the ServiceNow plugin is installed and configured, Service Catalog items can be exposed to the ServiceNow catalog from |morpheus|. Follow the guide below to expose |morpheus| Clouds, Library Items, and Blueprints to users in the ServiceNow catalog.

#. Navigate to |AdmInt|
#. Select the relevant ServiceNow integration
#. Within the "EXPOSED CATALOG ITEMS" section is a list of currently-exposed Service Catalog items
#. To expose a new item, click :guilabel:`+ ADD CATALOG ITEM`
#. Select an available item from the dropdown menu and click :guilabel:`SAVE CHANGES`
#. Back in ServiceNow, access the |morpheus| plugin from the Service Catalog
#. Exposed |morpheus| Service Catalog items are visible here for ServiceNow users with sufficient role permissions

.. image:: /images/integration_guides/itsm/servicenow/addCatalogItemNew.png
