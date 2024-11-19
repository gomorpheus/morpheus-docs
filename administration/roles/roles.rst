.. _roles:

Roles
=====

Overview
---------

Within |morpheus| is a wide array of role-based access control capabilities. These roles can be managed within the |AdmRol| section of the |morpheus| UI as well as through the API or CLI. Entire sections within the appliance UI can be hidden based on the specified access levels for features within |morpheus|. Features have different access scopes that can be selected from and can range depending on the specific feature. The most common scope set involves none, read, and full.

There are several handy tricks for creating new roles within |morpheus| and users can be assigned more than one role. When a user is assigned more than one role, permissions are granted by the role with the highest level of scope access. This allows roles to be built with small subsets of features and combined to grant different individuals relevant permission control. With resource permissions (that is, all types of permissions other than Feature permissions), a default access can be given as opposed to a specific (Full or None) permission for any resource. A specific permission will always supersede a default permission regardless of whether it's more permissive or more restrictive. In other cases (default vs default OR specific vs specific) the more permissive access will be given.

It's also important to note that built-in Roles, such as the System Admin "Superuser" Role carry no special prominence. For resource permissions, the System Admin user has defaults set to Full in each section. Thus, pairing the System Admin Role with another Role that may include specific line item permissions for various resource categories may cause your System Admin users to take on a reduced permission set.

.. NOTE:: Feature access control not only applies to the |morpheus| UI but also applies to the public developer API. It is sometimes necessary to logout and back in for changes to a users feature access level to be respected.

.. rst-class:: hidden
  Role Types
  ----------

  Tenant Roles
  ^^^^^^^^^^^^

  A Tenant based role (formerly called an Account based role) is used to ensure access control enforcement across an entire tenant with many sub-users. This allows the subtenant to manage their own set of internal user based roles without worrying master tenant involvement in setting them up. The master tenant is the only tenant able to create and manage these types of roles. When editing a Tenant, a singular tenant role can be assigned to the account. Users within the tenant can be assigned roles but those user based roles will never be able to supersede the level of access granted by the tenant role. This allows a super administrator the ability to restrict access at the department or organization level without having to worry about per user access control within said tenant.

  Tenant roles also have an additional section not in User based roles related to Cloud Access. Cloud Access allows the master tenant the ability to assign cloud integration resources to specific subtenants or groups of subtenants. An example would be granting access to a specific VMware cluster only to a subset of tenants using the tenant based role control.

Role Creation
^^^^^^^^^^^^^

Roles are created within |AdmRol|. Creating a Role requires minimal information, just a Name for the Role in |morpheus|. You can optionally add a Description and a Landing URL as well. The landing URL determines the starting page for the User on initial login (such as the Instances list page or perhaps the detail page for a primary |cluster|). Following creation, click into the Role from the Roles list page and you will see the granular controls available to Roles. These controls include access permissions for UI feature sections, Groups, Cluster types, and configured Tasks. Changes are automatically saved for the Role, there is no need to click a button to save any updates. See the next section for a detailed breakdown of individual feature permissions.

.. rst-class:: hidden
  User roles can be created by any tenant given permission at the tenant role level. These allow tenants to manage their own sets of users and their levels of access. They also allow tenants to control which users have access to specific “Groups” for provisioning into within |morpheus|. Groups are not cross tenant and therefore need to be controlled within the individual tenant in |morpheus|.

  Master tenant users are able to create a special type of user role called a multi-tenant user role. A multi-tenant user role is copied / duplicated down to all subtenants within |morpheus|. These can be viewed as canned role templates available to new tenants when their account is first created. Any changes made to the main role are propagated down to the subtenants version of the shared role so long as the subtenant users have not previously adjusted/changed that role. The moment a subtenant makes adjustments to the shared role within their account, it is unlinked from the parent role and treated entirely independently. In order to relink the Role in the Subtenant, a Master Tenant user would have to edit the Role, uncheck MULTITENANT USER ROLE, save the Role, check MULTITENANT USER ROLE once again, then save the Role once again.

  Another note about user roles is that when a user role is copied down to a subtenant, the permission scopes cannot supersede the tenant's assigned tenant role. If they do they are automatically downgraded when propagated to the specific tenant. Any changes made to the tenant role will automatically ensure roles within the tenant are downgraded appropriately.

  .. NOTE:: Master Tenant administrators may edit permissions for Roles in other Tenants by viewing the Tenant detail page (|AdmTen| > Selected Tenant) and accessing the Roles tab. From there, select the Role to edit and make changes on the resulting Role detail page.

.. rst-class:: hidden
  Multi-Tenant User Role Lock
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^

  As discussed above, Multi-Tenant User Roles are made available within all Subtenants and can be thought of as ‘canned’ user role sets provided to the Subtenant. |mastertenant| administrators can prevent changes to these ‘canned’ user roles by marking the box labeled ‘MULTITENANT LOCKED’ when creating or editing the role. In addition to preventing Subtenant administrators from modifying permissions of the role copied down to their Subtenant, this option also ensures |mastertenant| administrators can propagate new changes to that role. Modification of the role by the subtenant (if allowed) breaks the link back to the |mastertenant| and the copy of the role within the Subtenant will become its own unlinked role.

  .. NOTE:: Multi-tenant role lock applies only to permission sets on the Features, Report Types, Personas and VDI Pools tabs. Permissions in other tabs (such as Groups, Instance Types, Blueprints or Catalog Item Types) tabs are not locked. Similarly, changes made to the role on these tabs in the master tenant are not synced down.

  Editing User Roles in other Tenants
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Administrators in the Primary Tenant have the unique ability to edit feature permissions for User Roles that exist within other Tenants (Subtenants). In order to view the Roles within the Tenant, navigate to the Tenant detail page (|AdmTen|) and select the Roles tab. Click the pencil (|pencil|) icon to the right of a Role in the list to edit basic information, such as the name and description of the Role. Click on the name of the Role to view its complete permission set and edit the permissions if desired. This will update the feature access rights of users in the selected Tenant which have the Role.

Roles and Identity Sources
--------------------------

It is very common for large Enterprises to have an existing identity source that they would like to plug in to |morpheus| for authentication. This includes services like LDAP, Active Directory, OKTA, Jump Cloud, One Login, and SAML. When using these services it becomes important to configure a role mapping between the |morpheus| role assignments to the equivalent identity source groups/roles the user belongs to. This is configurable within the identity source management UI. Sections are provided allowing things like LDAP groups to be directly mapped to specific roles within |morpheus|. If a user matches more than one LDAP/role group then both sets of roles are applied to the user automatically. Configuring Identity Sources is done in |AdmUse|. Additionally, administrators may opt to lock users to their mapped role in |morpheus| or keep the roles unlocked to manually administer roles in one-off scenarios. See the docs section dedicated to identity sources for more information on configuring the specific SSO technologies |morpheus| supports.

.. include:: role_permissions.rst
.. rst-class:: hidden
  .. include:: roles_adding.rst
