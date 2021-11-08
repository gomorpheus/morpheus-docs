Creating Roles
--------------

User Roles
^^^^^^^^^^

User Roles can be single or multitenant. A Multitenant User Role is automatically copied into all existing subtenants as well as placed into a subtenant when created. Useful for providing a set of predefined roles a Customer can use. The Multitenant Locked option prevent subtenant from modifying FEATURE ACCESS settings in the Role. Note Group, Instance Type and Blueprint Access settings will still be editable as Groups are unique per Tenant, and Instance and Blueprints can be a mix of unique and shared items.

.. important:: Multitenant Roles still need to be configured/managed be each subtenant, as Groups are unique per Tenant, and Instance and Blueprints can be a mix of unique and shared items.

.. note:: User Roles cannot exceed Tenant Role permissions. If a Multitenant User Role has higher permissions than the Tenant Role assigned to a subtenant, the Multitenant User Role permissions in that Tenant will automatically be reduced to match the Tenant Role permissions.


Create a Single Tenant User Role
````````````````````````````````

#. In the Master Account, navigate to |AdmRol|
#. Select :guilabel:`+ CREATE ROLE`
#. Enter a name for the Role and optional Description
#. For TYPE, select "User Role"
#. Leave the "Multi-tenant Role" checkbox blank.
#. Optionally select an existing Role to copy in the COPY FROM ROLE dropdown.
   * This will configure the new Role with the same configuration as the selected role to copy. A new role that is not copied from another role will be generated with all permissions set to NONE.
#. Select :guilabel:`SAVE CHANGES`

After saving the Role will be created, and you will be redirected to the Roles Permissions settings.

Create a MultiTenant User Role
``````````````````````````````

A Multitenant User Role is automatically copied into all existing subtenants as well as placed into a subtenant when created. Useful for providing a set of predefined roles a Customer can use. The Multitenant Locked option prevent subtenant from modifying FEATURE ACCESS settings in the Role. Note Group, Instance Type and Blueprint Access settings will still be editable as Groups are unique per Tenant, and Instance and Blueprints can be a mix of unique and shared items.

#. In the Master Account, navigate to |AdmRol|
#. Select :guilabel:`+ CREATE ROLE`
#. Enter a name for the Role and optional Description
#. For TYPE, select "User Role"
#. Optionally select an existing Role to copy in the COPY FROM ROLE dropdown.
   * This will configure the new Role with the same configuration as the selected role to copy. A new role that is not copied from another role will be generated with all permissions set to NONE.
#. Select the MULTITENANT ROLE checkbox
#. Optionally select the MULTITENANT LOCKED checkbox
   * When enabled, the FEATURE ACCESS settings in the Role will not be editable by subtenants. Group, Instance Type and Blueprint Access settings will still be editable as Groups are unique per Tenant, and Instance and Blueprints can be a mix of unique and shared items.
#. Select :guilabel:`SAVE CHANGES`

After saving the Role will be created, and you will be redirected to the Roles Permissions settings.

.. important:: Multitenant Roles still need to be configured/managed be each subtenant, as Groups are unique per Tenant, and Instance and Blueprints can be a mix of unique and shared items.

.. note:: User Roles cannot exceed Tenant Role permissions. If a Multitenant User Role has higher permissions than the Tenant Role assigned to a subtenant, the Multitenant User Role permissions in that Tenant will automatically be reduced to match the Tenant Role permissions.

Tenant Roles
^^^^^^^^^^^^

A Tenant Role sets the highest possible permissions for a Tenant. User Roles within that Tenant cannot exceed those of the Tenants assigned Tenant Role. Tenant Roles can be assigned to single or multiple Tenants, and do not apply to the Master Account.

To create a Tenant Role:
````````````````````````

#. In the Master Account, navigate to |AdmRol|
#. Select :guilabel:`+ CREATE ROLE`
#. Enter a name for the Role and optional Description
#. For TYPE, select "Tenant Role"
#. Optionally select an existing Role to copy in the COPY FROM ROLE dropdown.
   * This will configure the new Role with the same configuration as the selected role to copy. A new role that is not copied from another role will be generated with all permissions set to NONE.
#. Select :guilabel:`SAVE CHANGES`

After saving, the Role will be created and you will be redirected to the Roles Permissions settings.
