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

Users can be created from `Administration -> Users` or `Administration -> Tenants -> Select a Tenant -> Users tab`.

.. NOTE:: Authorized Identity Source Users will be automatically created upon first sign in.

To create a User:

#. Navigate to either `Administration -> Users` or `Administration -> Tenants -> Select a Tenant.
#. Select :guilabel:`+ CREATE USER`.
#. From the New User Wizard input:

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
   Enabled
    If unchecked, the user will no longer be able to sign into |morpheus|, but their user data will remain.
   Password Expired
    If enabled, the User will be forced to create a new password upon next login. The expired password cannot be used again.
   Linux Settings
    Creates a User with the supplied Username, Password and/or Key-pair on Linux Instances when "Create my User" is selected during provisioning, or a User Group is added to an Instance of which this |morpheus| user is a member of.
   Windows Settings
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

#. Select :guilabel:`SAVE CHANGES`.

Edit User
^^^^^^^^^

User settings can be edited from `Administration -> Users`, `Administration -> Tenants -> Select a Tenant -> Users tab`, or from `User Settings`.

.. NOTE:: Some User data from Users created via an Identity Source Integration such as Active Directory is not editable in |morpheus|, as it is synced with the Identity Source.

To edit a User from the `Administration -> Users` Section:

#. Select the Administration link in the navigation bar.
#. Select the Users link in the sub navigation bar.
#. Click **ACTIONS** on the row of the user to edit.
#. Select **EDIT** in the ACTIONS dropdown.
#. Make changes.
#. Select :guilabel:`SAVE CHANGES`.

To edit a User from the `Administration -> Tenants -> Select a Tenant -> Users tab`:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Select a Tenant
#. Click **ACTIONS** on the row of the user to edit.
#. Select **EDIT** in the ACTIONS dropdown.
#. Make changes.
#. Select :guilabel:`SAVE CHANGES`.

User Settings
^^^^^^^^^^^^^

Additional settings for a User can be found in the User Settings section, including:

* User Photo
* Default Group
* Default Cloud
* API Access

To access User Settings:

#. Select your name in the very top right of the browser window.
#. Select `User Settings`

To edit the User you are currently logged in as from `User Settings`:

#. Select your name in the very top right of the window
#. Select `User Settings`
#. Make changes.
#. Select :guilabel:`SAVE`.

API Access
^^^^^^^^^^

API and CLI Access Tokens can be regenerated from the `User Settings` section.

To regenerate a CLI or API Access Token:

#. Select your name in the very top right of the window.
#. Select `User Settings`.
#. Select `API ACCESS` under the `Windows Settings` section.
#. Select `ACTIONS` for the Client ID the token will be generated for.
#. Select `Regenerate`.
#. Copy the Generated Access Token.

   .. IMPORTANT:: The Access Token will be masked after User Setting are saved.

#. Select :guilabel:`SAVE`.

Delete User
^^^^^^^^^^^

To delete a User from the `Administration -> Users` Section::

#. Select the Administration link in the navigation bar.
#. Select the Users link in the sub navigation bar.
#. Select **ACTIONS** on the row of the user to delete.
#. Select **REMOVE** in the ACTIONS dropdown.
#. Confirm

To delete a User from the `Administration -> Tenants -> Select a Tenant -> Users tab`:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Select a Tenant
#. Click **ACTIONS** on the row of the user to delete.
#. Select **REMOVE** in the ACTIONS dropdown.
#. Confirm


.. include:: users/usergroups.rst
