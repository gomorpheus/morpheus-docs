Active Directory
----------------

Overview
^^^^^^^^

Active Directory is Microsoft's primary authentication service widely used in Enterprise organizations and even via Microsoft's cloud services. While Active Directory also supports LDAP protocol support (which |morpheus| can integrate with as well), the main Active Directory integration can also be utilized. It is even possible to map Active Directory groups to equivalent Roles within |morpheus| .

.. NOTE:: To use Active Directory, a valid / trusted SSL certificate must be in place on the Active Directory services (self signed will not work).

.. _ad-access-control:

Access Control Behavior
^^^^^^^^^^^^^^^^^^^^^^^

.. IMPORTANT:: If the REQUIRED GROUP field is left empty, **any user who can authenticate against the Active Directory server will be allowed to log in** and a local user account is automatically created. To restrict access to authorized users only, you must set the Required Group field.

When an Active Directory identity source is configured, the following access control logic applies:

- **Required Group configured:** Only AD users who are members of the specified group are allowed to log in. Users not in the required group are denied access and no user object is created in |morpheus|.
- **Required Group empty (default):** All AD users who can authenticate are permitted to log in. A local user account is automatically created upon first sign-in, even if no role mappings apply to the user.
- **Include Member Groups enabled:** Users in groups nested inside the required group are also granted access.

The Default Role and role mappings are applied only after the Required Group check passes. |morpheus| roles provide an additional layer of RBAC that controls what the user can see and do within the platform, but they do not restrict login access itself.

**Recommended configuration for enterprise environments:**

- Always set a Required Group to prevent unauthorized directory users from authenticating
- Create a dedicated AD group (e.g., "Morpheus Users") and add only users who should have access
- Set the Default Role to the most restrictive appropriate role
- Use role mappings to grant elevated permissions to specific AD groups

Adding an Active Directory Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmTen|
#. Select a Tenant
#. Select :guilabel:`IDENTITY SOURCES`
#. Select :guilabel:`+ IDENTITY SOURCE`
#. Choose "Active Directory"
#. Populate the following:

   Name
      Unique name for authentication type.
   AD Server
    Hostname or IP address of AD Server.
   Domain
    Domain name of AD Domain.
   Binding Username
    Service account username for bind user.
   Binding Password
    Password for bind service account.
   Required Group
      The AD group users must be in to have access. If left empty, all AD users who can authenticate will be allowed to log in (see the "Access Control Behavior" section above).
   Include Member Groups
      When checked, groups nested inside the required group will also be included
   Default Role
      The default role applied to all users who pass the Required Group check. This role is always assigned in addition to any roles granted through role mappings.
   Service Account Holder
    This is the admin account type in |morpheus| and an AD group can be created and populated to a user that this role should be assigned. Roles are assigned dynamically based on group membership.

#. Select :guilabel:`SAVE CHANGES`.

Now allowed AD users can login to |morpheus| via their Active Directory credentials and a User will be automatically generated to |morpheus| with matching metadata and mapped Role permissions.

.. NOTE:: Only the username is required with password, not the username@domain.
