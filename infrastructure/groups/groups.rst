Groups
======

.. update

Overview
--------

Groups are used to organize clouds, roles, and hosts.

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

To View Groups:

#. Select the Infrastructure link in the navigation bar
#. Click the Groups link

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
  Lists and allows creation ro managment of Policies applied to the Group.

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
#. Note: You will be prompted for confirmation on this action.

.. image:: infrastructure/delete_group.png

.. [caption="Figure 3: ", title="Delete Group", alt="Delete Group"]

User Access
-----------

User access to Groups is determing by their user Role(s). Group access for Roles can be configured in the Group Access section of a Roles Settings.
