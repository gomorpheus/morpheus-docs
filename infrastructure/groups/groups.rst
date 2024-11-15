Groups
======

Overview
--------

Groups in |morpheus| define the available resources for each user. Group access is defined by Roles. Clouds are added to Groups, and a User can only access the Clouds associated with Groups in their Role. Resources such as networks, datastores, resource pools, and folders have additional Group access settings.

The Groups list page displays all current groups, which can be filtered by applied Labels or by simple search. Existing Groups can be edited here and new Groups can be created.

To View Groups:

#. Hover over the Infrastructure link in the menu bar
#. Click the Groups link

.. Viewing Groups

UI
---
  #. Select the Infrastructure link in the navigation bar
  #. Click the Groups link

CLI
---

  To view all groups: ``groups list``.

  To use the group: ``groups use <id>`` or ``groups use "group name"``

  To get a JSON output of a specific group: ``groups get <id> -j`` or ``groups get "group name" -j``

API
---
  To view all groups: ``curl https://api.gomorpheus.com/api/groups -H "Authorization: BEARER access_token"``

  To view a specific group: ``curl https://api.gomorpheus.com/api/groups/:id -H "Authorization: BEARER access_token"``

Adding Groups
-------------

.. UI

To add a group:

#. Select the Infrastructure link in the navigation bar
#. Click the Groups link
#. Click the Create Group button
#. Input out the Name and Location (optional) fields
#. Click the Save Changes button to save

.. CLI

.. All in one command: ``groups add CLITest -O code=cli -O location=`` I have added code and value for location is empty. The value for code and location are optional.
.. Minimal values: ``groups add CLITest`` There would be prompt to provide optional values for code and location.

.. API

.. HTTP Request
  ``POST https://api.gomorpheus.com/api/groups``

.. shell

.. .. code-block:: bash
    curl -XPOST "https://api.gomorpheus.com/api/groups" \
      -H "Authorization: BEARER access_token" \
      -H "Content-Type: application/json" \
      -d '{"group":{
        "name": "My Group",
        "description": "My description",
        "location": "US EAST"
      }}'

Managing Groups
---------------

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
Wiki
  Provides a text area for entering wiki content related to the Group in Markdown format. Additional information on Wiki is available in the |OpeWik| documentation section

Edit Group
----------

To edit a Group:

#. Select the Infrastructure link in the navigation bar.
#. Click the Groups link.
#. Click the name of the group you wish to edit.
#. Click the Edit button.
#. From the Edit Group Wizard modify information as needed.
#. Click the Save Changes button to save.

Delete Group
------------

To delete a Group:

#. Select the Infrastructure link in the navigation bar.
#. Click the Groups link.
#. Click the name of the group you wish to delete.
#. Click the Delete button.
#. Confirm

User Access
-----------

.. IMPORTANT:: User access to Groups is determined by their Role(s). Group access for Roles can be configured in the Group Access section of a Role's Settings.
