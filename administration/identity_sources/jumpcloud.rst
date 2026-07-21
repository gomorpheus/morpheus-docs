JumpCloud Identity Source
=========================

Overview
--------

|morpheus| can integrate with JumpCloud as an identity source, allowing users to authenticate with their JumpCloud credentials. JumpCloud user attributes and roles can be mapped to |morpheus| roles, providing centralized identity management through the JumpCloud Directory Platform.

Adding a JumpCloud Identity Source
-----------------------------------

#. Navigate to |AdmTen|
#. Select the Tenant to add the Identity Source Integration
#. Select :guilabel:`IDENTITY SOURCES`
#. Select :guilabel:`+ IDENTITY SOURCE`
#. Select **JumpCloud** from the TYPE dropdown
#. Enter the following:

   NAME
     A name for this Identity Source integration in |morpheus|.

   DESCRIPTION
     Optional description of the Identity Source.

   ORGANIZATION ID
     The JumpCloud Organization ID. This can be found in the JumpCloud Admin Console under Settings > General > Organization ID.

   BINDING USERNAME
     A JumpCloud API user or admin account username used for API authentication. This account is used to validate user credentials and sync group/role data.

   BINDING PASSWORD
     The password or API key for the binding account.

   REQUIRED ROLE
     (Optional) Enter a JumpCloud group name or role. Only JumpCloud users with this role/group membership will be allowed to authenticate to |morpheus|. If left empty, all JumpCloud users who can authenticate will be allowed to log in and a local user account is created automatically. It is strongly recommended to set this field in enterprise environments.

   DEFAULT ROLE
     The default |morpheus| Role applied to all users who pass the Required Role check. This role is always assigned in addition to any roles granted through role mappings below.

   ROLE MAPPINGS
     Map JumpCloud groups or roles to |morpheus| roles. Each existing |morpheus| role is listed with a field to enter the corresponding JumpCloud group name. Users with matching JumpCloud group membership will be assigned the mapped |morpheus| role at login.

#. Select :guilabel:`SAVE CHANGES`

The JumpCloud Identity Source integration is now active.

User Authentication
-------------------

Once configured, users can log in to |morpheus| using their JumpCloud credentials:

- On first login, a |morpheus| user account is automatically created matching the JumpCloud username and email
- Subsequent logins validate credentials against JumpCloud and update role assignments based on current group membership
- If a REQUIRED ROLE is specified, only users with that JumpCloud group/role can authenticate

.. IMPORTANT:: JumpCloud users will not authenticate in |morpheus| if there is an existing |morpheus| user with a matching username or email address that was not created by this identity source.

Role Mapping
------------

Role mappings allow granular control over |morpheus| permissions based on JumpCloud group membership:

- Enter JumpCloud group names in the role mapping fields next to each |morpheus| role
- Users may be assigned multiple |morpheus| roles based on their JumpCloud group memberships
- Role assignments are re-evaluated on each login, reflecting any JumpCloud group changes
- If no role mapping matches and no Required Role blocks access, the Default Role is assigned

Tenant Subdomain Login
-----------------------

When an identity source is configured for a Tenant, users can access the Tenant-specific login URL:

- The subdomain login URL is shown on the Identity Sources page
- Users navigating to this URL will be prompted to authenticate via the configured identity source
- This allows direct login without selecting a Tenant first

Removing the Integration
-------------------------

To remove a JumpCloud identity source:

#. Navigate to |AdmTen| > (Tenant) > Identity Sources
#. Click on the JumpCloud identity source
#. Click :guilabel:`DELETE`
#. Confirm the deletion

.. WARNING:: Removing an identity source does not delete users that were created through it. Those users will no longer be able to authenticate via JumpCloud but their |morpheus| accounts remain.
