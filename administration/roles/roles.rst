.. _roles:

Roles
=====

Overview
---------

Within |morpheus| is a wide array of role based access control capabilities. These roles can be managed within the Admin > Roles section of the |morpheus| UI as well as through the API or CLI. They are designed to be robust enough to fit within a wide array of enterprise and managed service provider scenarios so they can be a bit hard to grasp at first, but should make sense once a few simple concepts are explained. There are two types of roles within |morpheus| called Tenant and User based roles. Both sets of roles allow restrictions to be imposed on a user at the feature access level. Entire sections within the appliance UI can be hidden based on the specified access levels for features within |morpheus|. Features have different access scopes that can be selected from and can range depending on the specific feature. The most common scope set involves none, read, and full. Instance Type access is also common among both role types which allow the administrator to restrict which service catalog items they are allowed to provision within |morpheus| .

There are several handy tricks for creating new roles within |morpheus| and users can be assigned more than one role. When a user is assigned more than one role, permissions are granted by the role with the highest level of scope access. This allows roles to be built with small subsets of features and combined to grant different individuals relevant permission control.

.. NOTE:: Feature access control not only applies to the |morpheus| UI but also applies to the public developer API. It is sometimes necessary to logout and back in for changes to a users feature access level to be respected.

Role Types
----------

Tenant Roles
^^^^^^^^^^^^

A Tenant based role (formerly called an Account based role) is used to ensure access control enforcement across an entire tenant with many sub-users. This allows the subtenant to manage their own set of internal user based roles without worrying master tenant involvement in setting them up. The master tenant is the only tenant able to create and manage these types of roles. When editing a Tenant, a singular tenant role can be assigned to the account. Users within the tenant can be assigned roles but those user based roles will never be able to supersede the level of access granted by the tenant role. This allows a super administrator the ability to restrict access at the department or organization level without having to worry about per user access control within said tenant.

Tenant roles also have an additional section not in User based roles related to Cloud Access. Cloud Access allows the master tenant the ability to assign cloud integration resources to specific subtenants or groups of subtenants. An example would be granting access to a specific VMware cluster only to a subset of tenants using the tenant based role control.

User Roles
^^^^^^^^^^

User roles can be created by any tenant given permission at the tenant role level. These allow tenants to manage their own sets of users and their levels of access. They also allow tenants to control which users have access to specific “Groups” for provisioning into within |morpheus|. Groups are not cross tenant and therefore need to be controlled within the individual tenant in |morpheus|.

Master tenants are able to create a special type of user role called a multi-tenant user role. A multi-tenant user role is copied / duplicated
down to all subtenants within |morpheus|. These can be viewed as pre-canned role templates available to new tenants when their account is first created. Any changes made to the main role are propagated down to the subtenants version of the shared role so long as the subtenant has not previously adjusted/changed that role. The moment a subtenant makes adjustments to the shared role within their account, it is unlinked from the parent role and treated entirely independently.

Another note about user roles is that when a user role is copied down to a subtenant, the permission scopes cannot supersede the tenants assigned
tenant role. If they do they are automatically downgraded when propagated to the specific tenant. Any changes made to the tenant role will automatically ensure roles within the tenant are downgraded appropriately.

Multi-Tenant User Role Lock
^^^^^^^^^^^^^^^^^^^^^^^^^^^

As discussed above, multi-tenanted user roles are made available within all subtenants as ‘canned’ user role sets. Master tenant administrators can prevent changes to these ‘canned’ user roles by marking the box labeled ‘MULTITENANT LOCKED’ when creating or editing the role. In addition to preventing subtenant administrators from modifying permissions of these roles within their subtenancy, this option also ensures master tenant administrators can propagate new changes to that role. Modification of the role by the subtenant (if allowed) breaks the link back to the master tenant and the copy of the role within the subtenant will become its own unlinked role.

.. NOTE:: Multi-tenant role lock applies only to permission sets on the ‘FEATURE ACCESS’ tab. Permissions in the ‘GROUP ACCESS’, ‘INSTANCE TYPE ACCESS’, and ‘BLUEPRINT ACCESS’ tabs are not locked. Similarly, changes made to the role on these tabs in the master tenant are not synced down.

Roles and Identity Sources
--------------------------

It is very common for large Enterprises to have an existing identity source that they would like to plug in to |morpheus| for authentication. This includes services like LDAP, Active Directory, OKTA, Jump Cloud, One Login, and SAML. When using these services it becomes important to configure a role mapping between the |morpheus| role assignments to the equivalent identity source groups/roles the user belongs to. This is configurable within the identity source management UI. Sections are
provided allowing things like LDAP groups to be directly mapped to specific roles within |morpheus|. If a user matches more than one LDAP/role group then both sets of roles are applied to the user automatically. Configuring Identity Sources is done in Tenant management or user management in |AdmTen| or |AdmUse|, and has to be configured on a per-tenant basis. Additionally, administrators may opt to lock users to their mapped role in |morpheus| or keep the roles unlocked to manually administer roles in one-off scenarios.

.. include:: role_permissions.rst
.. include:: roles_adding.rst
