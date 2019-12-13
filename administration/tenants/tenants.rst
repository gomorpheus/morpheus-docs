Tenants
=======

Overview
--------

A Tenant in |morpheus| is an isolated environment with unique users and workloads. The Master Tenant is the default Tenant in |morpheus|, created upon installation. All other Tenants besides the Master Tenants are Sub Tenants.

- The Master Tenant is the default Tenant created during the installation of |morpheus|.
- All Tenants created after installation are Sub Tenants. Only one Master Tenant can exist.
- The Master Tenant creates and controls all Sub Tenants.
- Tenants are isolated environments.
    - Tenants have unique users
    - Tenants have unique workloads
    - Tenants have unique Groups
- The Master Tenant can share or assign Master Tenants resources with/to Sub Tenants
- Sub Tenants cannot share their resources with other tenants
- Sub Tenants cannot see resources from other Sub Tenants
- Sub Tenants can only access Master Tenant resources that have been set to Public visibility or assigned to the Sub Tenant.

Roles
^^^^^

It is important to understand Role types and permission when creating and managing Tenants.

Tenant Roles
    Tenant Roles are for capping Sub Tenant permissions by setting the maximum permissions for a Tenant. User Roles in a Tenant cannot exceed the permissions of the Tenant Role assigned to the Tenant.
       - Tenant Roles set the maximum permissions for a Tenant
       - User Roles in a Tenant cannot exceed the permissions of the Tenant Role assigned to the Tenant.
       - Tenants Roles can be set on one or multiple tenants
       - Tenant Roles determine Public Cloud access for the tenant.
          - All Clouds in the Master Tenants the have Visibility set to `Public` will show as options in the Tenant Role Cloud Access.
          - Only Master Tenant Clouds given access in a Tenants assigned Tenants role will be accessible in the Sub Tenant.

          .. IMPORTANT:: Tenant Roles cap permissions on all Sub Tenant user roles. Sub Tenant user roles can be created in the sub Tenant will lesser permissions than the Tenant Role allows. Tenant Roles are designed for a Master Tenant Admin to set max permissions for a Tenant, and a Sub Tenant Admin to configure User Roles inside the Sub Tenant.

User Roles
   User Roles determine Feature, Group and Instance Type access for all Users. For multi-tenancy, there are two types of User Roles, Single Tenant User Roles and Multi Tenant User Roles.
    Single Tenant User Roles
      Single Tenant User Roles only exist in the Tenant they exist in. All Roles created in a Sub Tenant are Single Tenant User Roles.
    Multi Tenant User Roles
      The Master Tenant and only the Master Tenant can create Multi Tenant User Roles. These Roles are for automatically creating base user Roles in Sub Tenants.
        - Multi Tenant User Roles will automatically create matching User Roles in all Tenants

        .. NOTE:: Multi Tenant User Roles are intended to make Sub Tenant User Role creation easier, so Master Tenant users do not have to re-create the same base Subtenant Users Roles for every Subtenant. Multi-Tenant User Roles are not a single role across Tenants, but more of a template that creates new Sub Tenant User Roles that can then be managed in the Sub Tenant.

        - Multi Tenant User Role changes will propagate to all Sub Tenants unless edited by a Sub Tenant
        - Once a Multi Tenant User Role is edited inside a Sub Tenant, it is no longer connected to the Multi Tenant User Role and is it own unique Role.
        - At least one Multi-Tenant User Role is required before Users can be created within a Subtenant.

        .. IMPORTANT:: Deleting a Multi Tenant User Role from the Master tenant will not remove that Role from Sub Tenants.

        .. IMPORTANT:: Renaming a Multi Tenant User Role from the Master tenant will not rename Roles created from the multi Tenant User Role in Sub Tenants.


Tenants
--------

The Tenants page displays a list of all Tenants. This page enables users to Create, Edit, and Delete Tenants. The list of Tenants displays the Tenant Name, Role, Total Instances, Total Users, and the Created Date.

Click the Tenant Name to drill into the Tenant View where you can again Edit, Delete, as well as Create Users, Edit Users, and Delete Users users belonging to the Tenant.

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

Subtenant users can have the same username as the user on the master tenant or any other tenant. Subusers will now have to login using the subdomain prefix.

.. important:: Subtenant users will no longer be able to login from the main login page without specifying their subdomain.


Example:
  I have a username ``subuser`` that belongs to a tenant with the subdomain ``subaccount``.
  When logging in from the main login url, I would now need to enter in: ``subaccount\subuser``

.. include:: configuring_multi_tenancy.rst
