.. _users:

Users
===================

Users
-----

Overview
^^^^^^^^

The Users page displays a list of all Users. The following fields are surfaced for each User:

- Display Name
- Username
- Email
- Role

Users which are grayed out in the list are currently inactive and cannot log in. The pencil and trash icons at the end of each row allow for editing or deleting Users. Click MORE to see the "impersonate" button. This allows administrators to impersonate any User, which may help confirm their Role permissions meet and do not exceed the desired result.

Click on the hyperlinked Display Name of the User to see a page detailing their effective Role permissions. This is especially useful for Users in multiple Roles where it might otherwise be difficult to determine their exact rights. This page looks identical to a User Role detail page except none of the fields are editable. Edit the User Role permissions for the User if changes need to be made.

.. NOTE:: Some User data created through an Identity Source integration (such as Active Directory) is not editable in |morpheus|, as it is synced from the Identity Source.

Create User
^^^^^^^^^^^

Users are created in |AdmUse|.

.. NOTE:: Authorized Identity Source Users will be automatically created upon first sign in.

To create a User:

#. Navigate to |AdmUse|
#. Select :guilabel:`+ CREATE USER`.
#. From the New User Wizard input:

   Username & Email
    -  First Name
    -  Last Name
    -  Username
    -  Email address

   Receive Notifications
    Enable to receive provisioning email notifications.

   Roles
    Role(s) to be inherited by the user. If multiple roles are selected, the higher permission levels of one role will override the other role(s). See the Roles section of this documentation for more information on stacking Roles and specific Role permissions.

   Password
    Password must contain at least one uppercase letter, one lowercase letter, a number, and a symbol.
   Enabled
    If unchecked, the user will no longer be able to sign into |morpheus|, but their user data will remain.
   Account Locked
    This box is checked when a User has tried unsuccessfully to log in too many times. An administrator will need to uncheck this box in order for the User to be able to make another login attempt.
   Password Expired
    If enabled, the User will be forced to create a new password upon next login. The expired password cannot be used again.
   Linux Settings
    Creates a User with the supplied Username, Password and/or Key-pair on Linux Instances when "Create my User" is selected during provisioning, or a User Group is added to an Instance of which this |morpheus| user is a member of.
   Windows Settings
    Creates a User with the supplied Username, Password and/or Key-pair on Windows Instances when "Create my User" is selected during provisioning, or a User Group is added to an Instance of which this |morpheus| user is a member of.

    .. IMPORTANT:: Please ensure password entered is allowable by Windows.

#. Select :guilabel:`SAVE CHANGES`.

Edit User
^^^^^^^^^

User settings can be edited from |AdmUse|.

.. NOTE:: Some User data from Users created via an Identity Source Integration such as Active Directory is not editable in |morpheus|, as it is synced with the Identity Source.

To edit a User from the |AdmUse| Section:

#. Select the Administration link in the navigation bar.
#. Select the Users link in the sub navigation bar.
#. Click the edit (pencil) icon from within the row of the selected User
#. Make changes and select :guilabel:`SAVE CHANGES`.

.. rst-class:: hidden
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

Additional settings for a User can be found in the User Settings section, including a user photo, API access, two-factor authentication settings, default Groups and Clouds, and more. User Settings is accessed by clicking on the name of the User in the upper-right corner of the application window and selecting "User Settings." See the dedicated section on User Settings elsewhere in this documentation for a more in-depth description of User Settings.

.. rst-class:: hidden
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
