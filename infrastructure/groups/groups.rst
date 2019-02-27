Groups
======

Overview
--------


Groups in |morphes| define what resources a user has access to. Group access is defined by User Roles. Clouds are added to groups, and a User can only access the Clouds that are in the Groups their Role(s) gives them access to. Resources such as Networks, Datastores, Resources Pools, and Folders have additional Group access settings.

Policies applied to a Group will be enforced on all Instances provisioned or moved into that Group.



.. NOTE:: Groups are not multi-tenant. A group only exists in the tenant is it is created in.

.. //* User Roles determine Group Access
.. //* Clouds are added to groups, user can only access the Clouds in their Group(s).
.. //* Config Management
.. //* DNS
.. //* Service Registry
.. //* Network Permissions
.. //* Policies
.. //** Limits
.. //** Lifecycle
.. //** Approvals
.. //** Naming

The Groups view displays all current groups, includes search feature, and also enables the addition of new groups.

.. To View Groups:

.. #. Select the Infrastructure link in the navigation bar
.. #. Click the Groups link

Viewing
^^^^^^^

Groups in UI
------------

Groups in Cli
-------------

Groups via API
--------------

Adding Groups
-------------

.. image:: /images/infrastructure/add_group.png

.. [caption="Figure 1: ", title="Add Group", alt="Add Group"]

To add a group:

#. Select the Infrastructure link in the navigation bar
#. Click the Groups link
#. Click the Create Group button
#. Input out the Name and Location (optional) fields
#. Click the Save Changes button to save

Managing Groups
---------------

.. image:: /images/infrastructure/group_view.png

To view a Group:

#. Select the Infrastructure link in the navigation bar
#. Click the Groups link
#. Click the Group name to view/modify

Available tabs in group view

Hosts
  Lists available hosts in the group and displays power, os, name, type, cloud, ip address, nodes, disc space, memory, and status. You can add a host from this tab panel by clicking Add Host.
Virtual Machines
  List all Virtual Machines in the Group.
Bare Metal
  List all Bare Metal Hosts added to the Group
Clouds
  Lists Clouds added to the Group. Existing Clouds or new Clouds can be added from the Group by clicking Add Cloud.
Policies
  Lists and allows creation or management of Policies applied to the Group.

Edit Group
----------

To edit a group:

#. Select the Infrastructure link in the navigation bar.
#. Click the Groups link.
#. Click the name of the group you wish to edit.
#. Click the Edit button.
#. From the Edit Group Wizard modify information as needed.
#. Click the Save Changes button to save.

Delete Group
------------

To delete a group:

#. Select the Infrastructure link in the navigation bar.
#. Click the Groups link.
#. Click the name of the group you wish to delete.
#. Click the Delete button.
#. Confirm

User Access
-----------

.. IMPORTANT:: User access to Groups is determined by their user Role(s). Group access for Roles can be configured in the Group Access section of a Roles Settings.
