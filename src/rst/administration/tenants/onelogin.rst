OneLogin
--------
Administration -> Tenants -> Select Tenant -> Identity Sources

Adding OneLogin Identity Source Integraiton

#. Navigate to Administration -> Tenants
#. Select the Tenant to add the Identity Source Integraiton
#. Select the IDENTITY SOURCES button
#. Seelct + ADD IDENTITY SOURCE
#. Enter the following:

   TYPE
      OneLogin
   NAME
      Name of the Identity Source Integraiton in Morpheus
    DESCRIPTION
      Optional Description of the Identiry Source
    ONELOGIN SUBDOMAIN
      example: morpheus-dev
        .. WARNING:: Please verify the subdomain carefully. An invalid subdomain will cause authentication attempts by OneLogin users to fail.
    ONELOGIN REGION
      Speciify US or EU region
    API CLIENT SECRET
      OneLogin API Client Secret from the Settings - API section in OneLogin portal
    API CLIENT ID
      OneLogin API Client ID from the Settings - API section in OneLogin portal
    REQUIRED ROLE
      Enter a role if OneLogin users logging into morpheus must have at least this OneLogin role to gain access to Morpheus.
    DEFAULT ROLE
      The default Morpheus Role applied to users created from OneLogin Integraiton if no other role mapping is specified below
    ROLE MAPPINGS
      Existing Morpheus Roles will be listed with fileds to enter OneLogin Roles to map to. Users with OneLogin roles matching the role mappings will be assigned the approprie Role(s) in Morpheus when sigining in.

#. Select SAVE CHANGES and the OneLogin Integraitnn will be added.

Users can now login to Morpheus with OneLogin credentials. The first Login will create a user in Morpheus matching the Username, email and Password from OneLogin. If a REQUIRED ROLE is specified in the Identiry Source settings, only users with that Role in OneLogin will be able to login to Morpheus.

.. IMPORTANT:: OneLogin users will not authenticate in Morpheus if there is an existing Morpheus User with matching username or email address.
