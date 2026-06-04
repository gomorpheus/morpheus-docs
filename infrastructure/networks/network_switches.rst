.. _network_switches:

Switches
--------

``Infrastructure > Network > Integrations > (select Network Server) > Switches``

Overview
^^^^^^^^

The Switches tab within a network server integration provides management of network switches. Switches connect network segments and forward traffic based on MAC addresses. |morpheus| syncs switch configurations from supported network integrations and allows for creation, editing, and management of switches directly from the UI.

.. NOTE:: Switch management is available on network server integrations that support this capability (``hasSwitches`` flag). The tab title may vary depending on the integration type.

Viewing Switches
^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **Switches** tab
#. The list view displays switch name, description, and related configuration details

Adding a Switch
^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **Switches** tab
#. Click :guilabel:`+ ADD`
#. Complete the required fields:

   :Name: A name for the switch
   :Description: (optional) A description of the switch purpose or location

   .. NOTE:: Additional fields may appear based on the network integration type and its configured option types.

#. Click :guilabel:`CREATE`

Editing a Switch
^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **Switches** tab
#. Click the pencil (edit) icon or select the switch from the list
#. Modify the desired fields
#. Click :guilabel:`SAVE`

Deleting a Switch
^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **Switches** tab
#. Click the trash (delete) icon for the target switch
#. Confirm the deletion when prompted

.. WARNING:: Deleting a switch will remove it from both |morpheus| and the upstream network integration. Ensure no active workloads depend on the switch before deletion.

Required Role Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^

Access to switch management requires the appropriate network server permissions (``infrastructure-network-integration``) with ``read`` or ``full`` access.
