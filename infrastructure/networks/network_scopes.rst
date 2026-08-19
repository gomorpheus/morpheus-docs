.. _network_scopes:

Scopes
------

``Infrastructure > Network > Integrations > (select Network Server) > Scopes``

Overview
^^^^^^^^

Scopes define network service boundaries within a network server integration. Scopes can be used to segment and organize network resources, providing logical isolation for different environments, tenants, or applications. |morpheus| supports creating, editing, and managing scopes on network integrations that expose this capability.

Scopes are distinct from Network Labels. To filter Network records that contain every requested Label through the Networks API, see :ref:`networks_all_labels`.

.. NOTE:: The Scopes tab is available on network server integrations that support this feature (``hasScopes`` flag). The tab title may vary based on the integration type.

Viewing Scopes
^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **Scopes** tab
#. The list view displays scope names, descriptions, and related details

Adding a Scope
^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **Scopes** tab
#. Click :guilabel:`+ ADD`
#. Complete the required fields:

   :Name: (required) A name for the scope
   :Description: (optional) A description of the scope purpose

   .. NOTE:: Additional fields may appear based on the network integration type and its configured option types.

#. Click :guilabel:`SAVE`

Editing a Scope
^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **Scopes** tab
#. Click the pencil (edit) icon for the target scope
#. Modify the desired fields
#. Click :guilabel:`SAVE`

Deleting a Scope
^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **Scopes** tab
#. Click the trash (delete) icon for the target scope
#. Confirm the deletion when prompted

Permissions
^^^^^^^^^^^

Scope visibility and access can be managed through the permissions control:

#. Click the lock icon or **Permissions** action for a scope
#. Configure Group Access and Tenant Permissions as needed
#. Click :guilabel:`SAVE`

Group Access
````````````

Controls which Groups have access to the scope. Select "All" for all Groups, or select specific Groups for restricted access.

Tenant Permissions
``````````````````

Set to Public for all Tenants to access the scope, or Private to restrict to specific Tenants.

Required Role Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^

Access to scope management requires the network server scope permission (``infrastructure-network-integration``) with ``read`` or ``full`` access.
