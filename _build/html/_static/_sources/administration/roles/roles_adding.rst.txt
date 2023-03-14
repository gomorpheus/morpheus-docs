Adding & Configuring Roles
^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating a Tenant Role
Creating a User Role (Single Tenant)
Creating a Multi Tenant Role

==== Creating a Tenant Role

A Tenant Role sets the highest possible permissions for a Tenant. User Roles within that Tenant cannot exceed those of the Tenants assigned Tenant Role. Tenant Roles can be assigned to single or multiple Tenants, and do not apply to the Mater Account.

===== To create a Tenant Role:

. In the Master Account, navigate to Administration -> Roles
. Select the + CREATE ROLE button
. Enter a name for the Role and optional Description
. For TYPE, select "Tenant Role"
. Optionally select an existing Role to copy in the COPY FROM ROLE dropdown.
** This will configure the new Role with the same configuration as the selected role to copy. A new role that is not copied from another role will be generated with all permissions set to NONE.
. Optionally set Limits for Storage, Memory or CPU Count. These limits will apply for any Tenant the Role is assigned to. 0.0 is default and is equal to no limit.

After saving the Role will be created, and you will be redirected to that Roles Permissions settings.

==== Create a User Role (Single Tenant):

. In the Master Account, navigate to Administration -> Roles
. Select the + CREATE ROLE button
. Enter a name for the Role and optional Description
. For TYPE, select "User Role"
. Leave the "Multi-tenant Role" checkbox blank.
. Optionally select an existing Role to copy in the COPY FROM ROLE dropdown.
** This will configure the new Role with the same configuration as the selected role to copy. A new role that is not copied from another role will be generated with all permissions set to NONE.
. Optionally set Limits for Storage, Memory or CPU Count. These limits will apply for any User the Role is assigned to. 0.0 is default and is equal to no limit.

After saving the Role will be created, and you will be redirected to the Roles Permissions settings.

==== Create a Multi Tenant Role:

. In the Master Account, navigate to Administration -> Roles
. Select the + CREATE ROLE button
. Enter a name for the Role and optional Description
. For TYPE, select "User Role"
. Select the "Multi-tenant Role" checkbox.
. Optionally select an existing Role to copy in the COPY FROM ROLE dropdown.
** This will configure the new Role with the same configuration as the selected role to copy. A new role that is not copied from another role will be generated with all permissions set to NONE.
. Optionally set Limits for Storage, Memory or CPU Count. These limits will apply for any User the Role is assigned to. 0.0 is default and is equal to no limit.

After saving the Role will be created, and you will be redirected to that Roles Permissions settings.

NOTE: It is important to note, while a Multi-tenant role is automatically copied into all existing subtenants as well as placed into any new Tenants, the generated roles inside each Tenant should be treated and managed as their own role. The Group Access configuration of a multi-tenant role only applies to the Tenant the role is being edited in, as Groups are unique to each tenant and not shared across Tenants. The purpose of a multi-tenant role is to facilitate an easy method of generating multiple pre-defined user roles for Tenants, NOT manage tenant user roles from the master tenant.
When editing the permissions for a sub-tenant user, be sure to edit their user role(s) from inside the sub-tenant and not from the Master account by impersonating a sub-tenant admin with full Role permissions.
