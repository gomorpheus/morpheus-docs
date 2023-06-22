.. _users:

Users & User Groups
===================

Users
-----

Overview
^^^^^^^^

The Users page displays a list of all Users. The following fields are surfaced for each User:

- Tenant
- Display Name
- Username
- Email
- Role

Users which are grayed out in the list are currently inactive and cannot log in. From the Actions menu in each User row, the option is given to Impersonate the User, Edit, or Remove the User.

In |morpheus| 4.2.1 and higher, click on the hyperlinked Display Name of the User to see a page detailing their effective Role permissions. This is especially useful for Users in multiple Roles where it might otherwise be difficult to determine their exact rights. This page looks identical to a User Role create/edit page except none of the fields are editable. Edit the User Role permissions for the User if changes need to be made.

.. NOTE:: Some User data created through an Identity Source integration (such as Active Directory) is not editable in |morpheus|, as it is synced from the Identity Source.

Create User
^^^^^^^^^^^

Users can be created from |AdmUse| or |AdmTen| > (selected Tenant) > Users tab`.

.. NOTE:: Authorized Identity Source Users will be automatically created upon first sign in.

To create a User:

#. Navigate to either |AdmUse| or |AdmTen| > Select a Tenant``.
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

.. NOTE:: Instance Resource Limits for a user are now configured through :ref:`Policies`

#. Select :guilabel:`SAVE CHANGES`.

Edit User
^^^^^^^^^

User settings can be edited from |AdmUse|, |AdmTen| > Select a Tenant > Users tab`, or from `User Settings`.

.. NOTE:: Some User data from Users created via an Identity Source Integration such as Active Directory is not editable in |morpheus|, as it is synced with the Identity Source.

To edit a User from the |AdmUse| Section:

#. Select the Administration link in the navigation bar.
#. Select the Users link in the sub navigation bar.
#. Click **ACTIONS** on the row of the user to edit.
#. Select **EDIT** in the ACTIONS dropdown.
#. Make changes.
#. Select :guilabel:`SAVE CHANGES`.

To edit a User from the |AdmTen| > Select a Tenant > Users tab`:

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

#. Select your name in the header
#. Select `User Settings`

To edit the User you are currently logged in as from `User Settings`:

#. Select your name in the header
#. Select `User Settings`
#. Make changes.
#. Select :guilabel:`SAVE`.

API Access
^^^^^^^^^^

API and CLI Access Tokens can be regenerated from the `User Settings` section.

To regenerate a CLI or API Access Token:

#. Select your name in the header
#. Select `User Settings`.
#. Select `API ACCESS` under the `Windows Settings` section.
#. Select `ACTIONS` for the Client ID the token will be generated for.
#. Select `Regenerate`.
#. Copy the Generated Access Token.

   .. IMPORTANT:: The Access Token will be masked after User Setting are saved.

#. Select :guilabel:`SAVE`.

Delete User
^^^^^^^^^^^

To delete a User from the |AdmUse| Section:

#. Select the Administration link in the navigation bar.
#. Select the Users link in the sub navigation bar.
#. Select **ACTIONS** on the row of the user to delete.
#. Select **REMOVE** in the ACTIONS dropdown.
#. Confirm

To delete a User from the |AdmTen| > Select a Tenant > Users tab`:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Select a Tenant
#. Click **ACTIONS** on the row of the user to delete.
#. Select **REMOVE** in the ACTIONS dropdown.
#. Confirm


.. include:: usergroups.rst
