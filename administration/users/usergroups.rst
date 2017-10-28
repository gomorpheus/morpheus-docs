User Groups
-----------

Overview
^^^^^^^^

User Groups can be selected during provisioning to add each group members credentials to the Instance. User Groups can be configured for sudo access and in Linux will assign Group members to a groupId in linux.

Creating User Groups
^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Administration -> Users`
#. Select the USER GROUPS tab.
#. Select + CREATE USER GROUP
#. Enter the following:

   NAME
    Name of the User Group
   DESCRIPTION
    Optional User Group Description
   SERVER GROUP
    Name of the groupId to assign Group members to in linux.
   SUDO ACCESS
    Enable to give Group members sudo access
   USERS
    Search for and select existing Users to add to the User Group.

#. Save Changes

Editing User Groups
^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Administration -> Users`
#. Select the USER GROUPS tab.
#. Select ACTIONS dropdown next to the target User Group.
#. Select EDIT
#. Make changes, add or remove users from the group.
#. Save Changes

Adding a User Group when Provisioning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. When provisioning, in the CONFIG section expand the USER section.
#. Select an existing Group from the USER GROUP dropdown.
#. Users will be created for members in the selected User Group on the provisioned Instance(s).
