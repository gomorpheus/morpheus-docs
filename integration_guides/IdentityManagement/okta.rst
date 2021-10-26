Okta
----

Overview
^^^^^^^^

|morpheus| allows users to integrate an Okta deployment for user management and authentication. In |morpheus|, identity sources are added on a per-Tenant basis and Morpheus allows you to map Okta user groups to |morpheus| user groups. User accounts are automatically created with matching metadata and role permissions when users are authenticated.

Adding an Okta Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Administration -> Tenants``
#. Select a Tenant
#. Select :guilabel:`IDENTITY SOURCES`
#. Select :guilabel:`+ IDENTITY SOURCE`
#. Choose TYPE: "Okta"
#. Populate the following, then select :guilabel:`SAVE CHANGES`:

Name
  Unique name for authentication type
Description
  A description for your new Okta Identity Source
Okta URL
  Your Okta URL
Administrator API Token
  Your Okta Administrator API Token
Required Group
  The Okta group that users must be in to have access (optional)
Default Role
  The default role a user is assigned if no group is listed under an Okta user that maps within the Morpheus Role Mappings section
ENABLE ROLE MAPPING PERMISSION
  When selected, Tenant users with appropriate rights to view and edit Roles will have the ability to set role mapping for the Identity Source integration. This allows the Tenant user to edit only the role mappings without viewing or potentially editing the Identity Source configuration.
MANUAL ROLE ASSIGNMENT
  When selected, administrators can manually edit Roles for users created through this identity source integration from the user detail page (|AdmUse| > Selected user).

.. NOTE:: For more on Identity Source role mapping permissions, see the `associated guide <https://support.morpheusdata.com/s/article/How-to-enable-Subtenant-admins-to-edit-Identity-Source-role-mapping?language=en_US>`_ in our KnowledgeBase.

Now, allowed Okta users can log into |morpheus| via their Okta credentials and a user will be automatically generated within |morpheus| with matching metadata and mapped Role permissions.

.. NOTE:: If you've created multi-tenant roles, these will also appear here and can be mapped to Okta user groups allowing you to map users to equivalent user groups in |morpheus|.
