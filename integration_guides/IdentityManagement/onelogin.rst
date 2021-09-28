OneLogin
--------

Adding OneLogin Identity Source Integration

#. Navigate to Administration -> Tenants
#. Select the Tenant to add the Identity Source Integration
#. Select :guilabel:`IDENTITY SOURCES`
#. Select :guilabel:`+ IDENTITY SOURCE`
#. Enter the following:

  TYPE
    OneLogin
  NAME
    Name of the Identity Source Integration in Morpheus
  DESCRIPTION
    Optional Description of the Identity Source
  ONELOGIN SUBDOMAIN
    example: morpheus-dev
      .. WARNING:: Please verify the subdomain carefully. An invalid subdomain will cause authentication attempts by OneLogin users to fail.
  ONELOGIN REGION
    Specify US or EU region
  API CLIENT SECRET
    OneLogin API Client Secret from the Settings - API section in OneLogin portal
  API CLIENT ID
    OneLogin API Client ID from the Settings - API section in OneLogin portal
  REQUIRED ROLE
    Enter a role if OneLogin users logging into morpheus must have at least this OneLogin role to gain access to Morpheus.
  DEFAULT ROLE
    The default Morpheus Role applied to users created from OneLogin Integration if no other role mapping is specified below
  ROLE MAPPINGS
    Existing Morpheus Roles will be listed with fields to enter OneLogin Roles to map to. Users with OneLogin roles matching the role mappings will be assigned the appropriate Role(s) in Morpheus when signing in.
  ENABLE ROLE MAPPING PERMISSION
    When selected, Tenant users with appropriate rights to view and edit Roles will have the ability to set role mapping for the Identity Source integration. This allows the Tenant user to edit only the role mappings without viewing or potentially editing the Identity Source configuration.
  MANUAL ROLE ASSIGNMENT
    When selected, administrators can manually edit Roles for users created through this identity source integration from the user detail page (Administration > Users > Selected user).

    .. NOTE:: For more on Identity Source role mapping permissions, see the `associated guide <https://support.morpheusdata.com/s/article/How-to-enable-Subtenant-admins-to-edit-Identity-Source-role-mapping?language=en_US>`_ in our KnowledgeBase.

#. Select :guilabel:`SAVE CHANGES` and the OneLogin Integration will be added.

Users can now login to Morpheus with OneLogin credentials. The first Login will create a user in Morpheus matching the Username, email and Password from OneLogin. If a REQUIRED ROLE is specified in the Identity Source settings, only users with that Role in OneLogin will be able to login to Morpheus.

.. IMPORTANT:: OneLogin users will not authenticate in Morpheus if there is an existing Morpheus User with matching username or email address.
