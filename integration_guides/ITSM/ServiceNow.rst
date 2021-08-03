.. _snow:

ServiceNow
----------

Overview
^^^^^^^^

IT Service Management (ITSM) is an important area of focus for many organizations. Organizations invested in ServiceNow as an ITSM provider will find that |morpheus| integrates tightly with some of the most-used features. After integrating ServiceNow with |morpheus|, both environments can be used interchangeably and the results are synced to both places. This guide walks administrators through the process of integrating ServiceNow with |morpheus| and how |morpheus| can be used to effectively leverage the best of ServiceNow.

.. TIP:: The ServiceNow integration guide is also available as a `PDF download <https://morpheusdata.com/wp-content/uploads/content/ServiceNow-Cloud-Management-Morpheus-CMP-1.pdf>`_, which includes additional example use cases and screenshots.

Add ServiceNow Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Administration > Integrations``
#. Select :guilabel:`+ NEW INTEGRATION`
#. Select "ServiceNow" from the dropdown list
#. Add the following:

   NAME
    A friendly name to describe the ServiceNow integration in |morpheus|.
   ENABLED
    Check "Enabled" to allow consumption of this ServiceNow integration in |morpheus|.
   HOST
    URL of the ServiceNow instance (ex: https://your.instance.service-now.com), keep in mind you can create multiple ServiceNow integrations in |morpheus| if needed.
   USER/PASSWORD
    A user in ServiceNow that is able to access the REST interface and create/update/delete incidents, requests, requested items, item options, catalog items, workflows, etc. The list of necessary roles includes ``x_moda_morpheus_ca.integration`` (available if the |morpheus| ServiceNow plugin is installed from the ServiceNow Store), ``catalog_admin``, ``itil``, ``rest_service``, and ``import_transformer``.
   CMDB CUSTOM MAPPING
    If needed, administrators can opt to populate a specific field in the ServiceNow table and such mapping is identified here with a JSON code snippet. Below is an example that populates the ``object_id`` field in the CM database with the |morpheus| instance name:

    .. code-block:: bash

      {
      "object_id":"<%=instance.name%>",
      "SN_field_id2":"<%=morph.varname2%>",
      "SN_field_id3":"<%=morph.varname3%>"
      }

   CMDB BUSINESS OBJECT
    Allows the user to define the table CMDB records are written to if they prefer this over |morpheus| default. By default, |morpheus| writes to the ``cmdb_ci_vm_instance`` table.

#. Save Changes

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
    Select the ServiceNow Integration already configured in ``Administration > Integrations`` to use for the approval policy.

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
    Select the ServiceNow Integration already configured in ``Administration > Integrations`` to use for the approval policy.

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

.. NOTE:: A ServiceNow integration must be already configured in ``Administration > Integrations`` to enable ServiceNow monitoring.

The ServiceNow monitoring integration is enabled and configured in `Administration > Settings > Monitoring`. As long as the "Enabled" switch is activated, |morpheus| will report monitoring data to ServiceNow. Configuration selections are described below:

Enabled
  Enables the ServiceNow monitoring integration
Integration
  Select from an existing ServiceNow integration in `Administration > Integrations`
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

In addition to integrating with key ServiceNow features, |morpheus| offers a free plugin directly from the ServiceNow Store. At the time of this writing, the plugin supports ServiceNow releases New York, Orlando, and Paris. Once the plugin is installed, |morpheus| Instance Types, Blueprints, and Self-Service Catalog Items can be presented as provisioning options in the ServiceNow catalog for ordering. The following is a guide to installing the Morpheus ServiceNow application.

.. IMPORTANT:: A valid SSL Certificate is required on the |morpheus| Appliance for the ServiceNow plugin to be able to communicate with the appliance.

ServiceNow Configuration
````````````````````````

#. Install the |morpheus| plugin from the ServiceNow store.

     - Refer to the `MORPHEUS DATA APPLICATION PLUG-IN FOR SERVICENOW <https://store.servicenow.com/appStoreAttachments.do?sys_id=73029271dbbd6450087656a8dc961995>`_ Installation Instructions for plugin installation.

#. Navigate to |morpheus| Catalog > Properties
#. Set the following properties:

   |morpheus| Appliance Endpoint
    The full URL to your |morpheus| appliance
   Username
    Username of the user in |morpheus| that the plugin will connect to the |morpheus| API with.

   Password
    Password of the user in |morpheus| that the plugin will connect to the |morpheus| API with.
   MID Server
    If desired, specify the name of a configured MID server to use

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

Adding to ServiceNow Catalog
````````````````````````````

Once the ServiceNow plugin is installed and configured, items can be added to the ServiceNow catalog from back in |morpheus|. Follow the guide below to expose |morpheus| Clouds, Library Items, and Blueprints to users in the ServiceNow catalog.

#. Navigate to `Administration > Integrations`
#. Select the relevant ServiceNow integration
#. From the Instances tab we can :guilabel:`+ ADD CLOUD` or :guilabel:`+ ADD LIBRARY ITEM`
#. From the Blueprints tab we can :guilabel:`+ ADD BLUEPRINT`
#. From the Catalog Items tab, we can :guilabel:`+ ADD CATALOG ITEM`
#. Back in ServiceNow, access the |morpheus| plugin from the Service Catalog
#. Exposed |morpheus| Library Items, Catalog Items, and Blueprints are visible here for ServiceNow users with sufficient role permissions

.. image:: /images/integration_guides/itsm/servicenow/5addCatalogItem.png
