Active Directory
----------------

Overview
^^^^^^^^

Active Directory is Microsoft’s primary authentication service widely used in Enterprise organizations and even via Microsoft’s cloud services. While Active Directory also supports LDAP protocol support (which |morpheus| can integrate with as well), the main Active Directory integration can also be utilized. It is even possible to map Active Directory groups to equivalent Roles within |morpheus| .

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
   Include Member Groups
    When checked, groups nested inside the required group will also be included
   Default Role
    The default role a user is assigned if no group is listed under AD user that maps under Role Mappings section.
   Service Account Holder
    This is the admin account type in |morpheus| and an AD group can be created and populated to a user that this role should be assigned. Roles are assigned dynamically based on group membership.

#. Select :guilabel:`SAVE CHANGES`.

Now allowed AD users can login to |morpheus| via their Active Directory credentials and a User will be automatically generated to |morpheus| with matching metadata and mapped Role permissions.

.. NOTE:: Only the username is required with password, not the username@domain.

.. NOTE:: Sub-tenant |morpheus| API authentication for Active Directory generated users is not currently supported.
