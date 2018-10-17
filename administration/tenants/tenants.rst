Tenants & Tenant Users
=======================

Overview
--------

The Tenants page displays a list of all Tenants. This page enables users to Create, Edit, and Delete Tenants. The list of Tenants displays the Tenant Name, Role, Total Instances, Total Users, and the Created Date.

Click the Tenant Name to drill into the Tenant View where you can again Edit, Delete, as well as Create Users, Edit Users, and Delete Users users belonging to the Tenant.

Tenants
--------

Create Tenants
^^^^^^^^^^^^^^^^

To create Tenants

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the Create Tenant button.
#. From the New Tenant wizard input:

   - Name
   - Description (optional)
   - Base Role
     Primary role of the Tenant. All User roles within the Tenant cannot exceed the permission of this Role.
   - Limits
     Restricts the amount of Storage and Memory allocated to the Tenant

#. Click the Save Changes button.

Edit Tenant
^^^^^^^^^^^^

To edit a Tenant:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the Edit pencil icon on the row of the Tenant to edit.
#. Edit the Edit Tenant settings.

Disabling Tenant
^^^^^^^^^^^^^^^^

When disabling a tenant, they are not able to login and cannot be impersonated by another tenant. However all of their information will still remain in |morpheus| and they may still receive notifications and alerts.

To disable a Tenant:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the Edit pencil icon on the row of the Tenant to edit.
#. Uncheck the ``Enabled`` box.

Delete Tenant
^^^^^^^^^^^^^^

To delete a Tenant:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the Delete trashcan icon on the row of the Tenant to delete.
#. Confirm

Tenant Users
------------

The Tenant View displays a list of users belonging to the Tenant and their
Name, Username, Email, and Role.

From this page: Create, Edit, and Delete users within the Tenant.

.. IMPORTANT:: In versions 3.1.1 and 2.12.5 and later, a multi-tenant user role must be create prior to adding sub-tenant users or the user will not save. In previous versions a default multi-tenant role was seeded, but due to customer requests the seeded role was removed and a multi-tenant role must be created by the master tenant for sub-tenant users.

Create Tenant User
^^^^^^^^^^^^^^^^^^
To create a Tenant User:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the Tenant Name on the row of the Tenant where the user will be added.
#. Click the Create User button.
#. From the New User wizard input the fields below

   - First Name of the user being created
   - Last Name of the user being created
   - Username used to login
   - Email address of the new user
   - Role to be inherited by the user
   - Password
   - Limits

     - Restricts the amount of Storage and Memory the user can provision.

   - Save Changes.

.. IMPORTANT:: In versions 3.1.1 and 2.12.5 and later, a multi-tenant user role must be create prior to adding sub-tenant users or the user will not save. In previous versions a default multi-tenant role was seeded, but due to customer requests the seeded role was removed and a multi-tenant role must be created by the master tenant for sub-tenant users.

Edit a Tenant User
^^^^^^^^^^^^^^^^^^

To edit a User:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the Tenant Name on the row of the Tenant containing the user to be edited.
#. Click the Edit pencil icon of the row of the to edit.
#. Edit User information

   .. NOTE:: Name, Username, Passwords and e-mail addresses cannot be edited on Users created from Identity Source Integrations.

#. Save Changes.

Delete Tenant User
^^^^^^^^^^^^^^^^^^

To delete a Tenant User

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the Tenant Name on the row of the Tenant containing the user.
#. Click the Delete trashcan icon of the row of the user to delete.
#. Confirm

Subtenant User Login
^^^^^^^^^^^^^^^^^^^^^

Subusers can have the same username as the user on the master tenant or any other tenant. Subusers will now have to login using the subdomain prefix.

.. important::

  Subtenant users will no longer be able to login from the main login page without specifying their subdomain.


Example:
  I have a username ``subuser`` that belongs to a tenant with the subdomain ``subaccount``.
  When logging in from the main login url, I would now need to enter in: ``subaccount\subuser``

.. include:: configuring_multi_tenancy.rst
