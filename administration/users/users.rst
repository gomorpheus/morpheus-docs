Users
=====

Users
-----

Overview
^^^^^^^^

The Users page displays a list of all users. From the users page:
Create, Edit, and Delete users. The list of users displayed on this page
displays Account, Name, Username, Email, and Role.

.. NOTE:: Some User data from Users created via an Identity Source Integration such as Active Directory is not editable in |morpheus|, as it is synced with the Identity Source.

Create User
^^^^^^^^^^^

To create a User:

#. Select the Administration link in the navigation bar.

#. Select the Users link in the sub navigation bar.

#. Click the :guilabel:`+ CREATE USER` button.

#. From the New User Wizard input

   Username & Email
    -  First Name
    -  Last Name
    -  Username
    -  Email address

   Receive Notifications
    Enable to receive Provisioning and Policy email notifications.

   Roles
    Role(s) to be inherited by the user. If multiple roles are selected, the higher permission levels of one role will override the other role(s).

   Password
    Password must contain at least one uppercase letter, one lowercase letter, a number, and a symbol.

   LINUX SETTINGS
    Creates a User with the supplied Username, Password and/or Key-pair on Linux Instances when "Create my User" is selected during provisioning, or a User Group is added to an Instance of which this |morpheus| user is a member of.

   WINDOWS SETTINGS
    Creates a User with the supplied Username, Password and/or Key-pair on Windows Instances when "Create my User" is selected during provisioning, or a User Group is added to an Instance of which this |morpheus| user is a member of.

    .. IMPORTANT:: Please ensure password entered is allowable by Windows.

   Limits
    Combined Instance Resource Limits for the User. When a limit is reached, the User will not be able to provision more Instances
    -  STORAGE
        - Total amount of Storage the user can Provision, set in GiB. 0.0 is unlimited.
    -  MEMORY
        - Total amount of RAM the user can Provision, set in MiB. 0.0 is unlimited.
    - CPU COUNT
       - Total combined Cores the user can Provision. 0 is unlimited.

#. Click :guilabel:`SAVE CHANGES`.

Edit User
^^^^^^^^^

To edit a User:

#. Select the Administration link in the navigation bar.
#. Select the Users link in the sub navigation bar.
#. Click **ACTIONS** on the row of the user to edit.
#. Select **EDIT** in the ACTIONS dropdown.
#. Make changes.
#. Click :guilabel:`SAVE CHANGES`.

Delete User
^^^^^^^^^^^

To delete a User:

#. Select the Administration link in the navigation bar.
#. Select the Users link in the sub navigation bar.
#. Click **ACTIONS** on the row of the user to edit.
#. Select **REMOVE** in the ACTIONS dropdown.
#. Confirm

.. include:: users/usergroups.rst
