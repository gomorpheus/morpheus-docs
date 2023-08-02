.. _tenants:

Tenants
=======

Overview
--------

A Tenant in |morpheus| is an isolated environment with unique users and workloads. The Master Tenant is the default Tenant in |morpheus|, created upon installation. All other Tenants outside of the Master Tenants are Subtenants.

.. begin_tenants_bulleted_list

- The Master Tenant is the default Tenant created during the installation of |morpheus|
- All Tenants created after installation are Subtenants. Only one Master Tenant can exist
- The Master Tenant creates and controls all Subtenants.
- Tenants are isolated environments with unique users, workloads, and Groups
- The Master Tenant can share or assign its resources to Subtenants
- Subtenants cannot share their resources with other Tenants
- Subtenants cannot see resources from other Subtenants
- Subtenants can only access Master Tenant resources that have been set to Public visibility or specifically assigned to the Subtenant

.. end_tenants_bulleted_list

Roles
-----

There are two Role types in |morpheus|, Tenant Roles and User Roles. Understanding these Role types is key to effectively administering Role permissions in |morpheus|. These two Role types are discussed in greater detail in this section.

Tenant Roles
^^^^^^^^^^^^

Tenant Roles set the maximum permission levels for Users in the Tenant. User Role permissions will not exceed the permissions of the Tenant Role.

- Tenant Roles set the maximum permissions for a Tenant
- User Roles in a Tenant cannot exceed the permissions of the Tenant Role
- A Tenant Role can be assigned to one or multiple Tenants
- Tenant Roles determine Cloud access for the Subtenant such that all Clouds in the Master Tenant which have visibility set to Public will show as options in the Tenant Role Cloud Access tab
- Only Master Tenant Clouds given access in the Tenant Role will be accessible in the Subtenant

.. IMPORTANT:: Tenant Roles cap permissions on all Subtenant User Roles. User Roles can be created in the Subtenant with lesser permissions than the Tenant Role allows. Tenant Roles are designed for a Master Tenant Admin to set max permissions for the Subtenant, and a Subtenant Admin to configure User Roles inside the Subtenant.

User Roles
^^^^^^^^^^

User Roles determine feature, Group, and Instance Type access for all Users. In a multi-Tenant environment, there are two types of User Roles: Single-Tenant User Roles and Multi-Tenant User Roles.

- **Single-Tenant User Roles:** These exist solely in the Tenant they are created in. All Roles created in a Subtenant will be Single-Tenant User Roles
- **Multi-Tenant User Roles:** The Master Tenant can create Multi-Tenant User Roles. These Roles are automatically seeded into Subtenants and can be assigned to Subtenant Users. Changes to Multi-Tenant User Roles made in the Master Tenant are propagated to all Subtenants. However, once a Multi-Tenant User Role is edited inside a Subtenant, it is no longer linked to the Multi-Tenant User Role and becomes its own unique Role. It will no longer receive propagated changes.

.. NOTE:: Multi-Tenant User Roles are intended to make Subtenant User Role creation easier, so Master Tenant Users do not have to re-create the same base Subtenant Users Roles for every Subtenant. Multi-Tenant User Roles are not a single Role across Tenants, but more like a template that creates new Subtenant User Roles that can then be managed in the Sub Tenant.

Tenants
--------

The Tenants page displays a list of all Tenants. This page enables users to Create, Edit, and Delete Tenants. The list of Tenants displays the Tenant Name, Role, Total Instances, Total Users, and the Created Date.

Click the Tenant Name to drill into the Tenant View where you can again Edit or Delete the Tenant, as well as Create Users, Edit Users, and Delete Users users belonging to the Tenant.

Create Tenants
^^^^^^^^^^^^^^

To Create Tenants:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the Create Tenant button.
#. From the New Tenant wizard input:

   - Name
   - Description (optional)
   - Subdomain
   - Base Role
   - Currency

#. Within the Advanced Options section, track customer data related to the Tenant if needed:

   - Account Number
   - Account Name
   - Customer Number

#. Click the :guilabel:`Save Changes`

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

The Tenant View displays a list of users belonging to the Tenant and their Name, Username, Email, and Role.

From this page: Create, Edit, and Delete users within the Tenant.

.. IMPORTANT:: In versions 3.1.1 and 2.12.5 and later, a Multi-Tenant User Role must be created prior to adding Subtenant Users or the User will not save. In previous versions a default Multi-Tenant Role was seeded. Due to customer requests, the seeded role was removed and a Multi-Tenant Role must be created by the Master Tenant for Subtenant Users.

Create Tenant User
^^^^^^^^^^^^^^^^^^
To create a Tenant User:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the Tenant Name on the row of the Tenant where the user will be added.
#. Click :guilabel:`+ ADD USER`
#. From the New User wizard, input the fields below:

   - First Name
   - Last Name
   - Username
   - Email address
   - Role (to be inherited by the user)
   - Password
   - Any default Windows or Linux credentials

Click :guilabel:`SAVE CHANGES`

.. IMPORTANT:: In versions 3.1.1 and 2.12.5 and later, a Multi-Tenant User Role must be created prior to adding Subtenant Users or the User will not save. In previous versions a default Multi-Tenant Role was seeded. Due to customer requests, the seeded role was removed and a Multi-Tenant Role must be created by the Master Tenant for Subtenant Users.

Edit a Tenant User
^^^^^^^^^^^^^^^^^^

To edit a User:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the specific Tenant name from the row of available Tenants.
#. Click the Edit pencil icon for your selected Tenant.
#. Edit User information

   .. NOTE:: Name, Username, Passwords and e-mail addresses cannot be edited on Users created from Identity Source Integrations.

Click :guilabel:`SAVE CHANGES`

Delete Tenant User
^^^^^^^^^^^^^^^^^^

To delete a Tenant User:

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the Tenant Name from the row for the Tenant containing the user.
#. Click the Delete trashcan icon of the row of the user to delete.
#. Confirm

Subtenant User Login
^^^^^^^^^^^^^^^^^^^^^

Subtenant Users can have the same Username as the User on the Master Tenant or any other Tenant. Subtenant Users will now have to login using the subdomain prefix.

.. important:: Subtenant users will no longer be able to login from the main login page without specifying their subdomain.


Example:
  I have a username ``subuser`` that belongs to a tenant with the subdomain ``subaccount``.
  When logging in from the main login url, I would now need to enter in: ``subaccount\subuser``

.. include:: configuring_multi_tenancy.rst
