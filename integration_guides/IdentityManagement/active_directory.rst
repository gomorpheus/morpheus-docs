Active Directory
----------------

Overview
^^^^^^^^

Active Directory is Microsoft’s primary authentication service widely used in Enterprise organizations and even via Microsoft’s cloud services. While Active Directory also supports LDAP protocol support (which |morpheus| can integrate with as well), the main Active Directory integration can also be utilized. It is even possible to map Active Directory groups to equivalent Roles within |morpheus|. |morpheus| will connect over port 389 for non-secure LDAP and port 636 for secure LDAP.

.. NOTE:: To use Active Directory, a valid / trusted SSL certificate must be in place on the Active Directory services (self signed will not work).

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
    The AD group users must be in to have access (optional)
   Default Role
    The default role a user is assigned if no group is listed under AD user that maps under Role Mappings section.
   Service Account Holder
    This is the admin account type in |morpheus| and an AD group can be created and populated to a user that this role should be assigned. Roles are assigned dynamically based on group membership.
   ENABLE ROLE MAPPING PERMISSION
    When selected, Tenant users with appropriate rights to view and edit Roles will have the ability to set role mapping for the Identity Source integration. This allows the Tenant user to edit only the role mappings without viewing or potentially editing the Identity Source configuration.
   MANUAL ROLE ASSIGNMENT
    When selected, administrators can manually edit Roles for users created through this identity source integration from the user detail page (|AdmUse| > Selected user).

  .. NOTE:: For more on Identity Source role mapping permissions, see the `associated guide <https://support.morpheusdata.com/s/article/How-to-enable-Subtenant-admins-to-edit-Identity-Source-role-mapping?language=en_US>`_ in our KnowledgeBase.

#. Select :guilabel:`SAVE CHANGES`.

Now allowed AD users can login to |morpheus| via their Active Directory credentials and a User will be automatically generated to |morpheus| with matching metadata and mapped Role permissions.

.. NOTE:: Only the username is required with password, not the username@domain.

.. NOTE:: Sub-tenant |morpheus| API authentication for Active Directory generated users is not currently supported.
