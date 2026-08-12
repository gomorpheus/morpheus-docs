Okta
----

Overview
^^^^^^^^

|morpheus| allows users to integrate an Okta deployment for user management and authentication. In |morpheus|, identity sources are added on a per-Tenant basis and Morpheus allows you to map Okta user groups to |morpheus| user groups. User accounts are automatically created with matching metadata and role permissions when users are authenticated.

Adding an Okta Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmTen|
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
  The Okta group that users must be in to have access. If left empty, all Okta users who can authenticate will be allowed to log in and a local user account will be created automatically. It is strongly recommended to set this field in enterprise environments to restrict access to authorized users only.
Default Role
  The default role applied to all users who pass the Required Group check. This role is always assigned in addition to any roles granted through role mappings below.
ENABLE ROLE MAPPING PERMISSION
  When selected, Tenant users with appropriate rights to view and edit Roles will have the ability to set role mapping for the Identity Source integration. This allows the Tenant user to edit only the role mappings without viewing or potentially editing the Identity Source configuration.
MANUAL ROLE ASSIGNMENT
  When selected, administrators can manually edit Roles for users created through this identity source integration from the user detail page (|AdmUse| > Selected user).

.. NOTE:: For more on Identity Source role mapping permissions, see the `associated guide <https://support.morpheusdata.com/s/article/How-to-enable-Subtenant-admins-to-edit-Identity-Source-role-mapping?language=en_US>`_ in our KnowledgeBase.

Now, allowed Okta users can log into |morpheus| via their Okta credentials and a user will be automatically generated within |morpheus| with matching metadata and mapped Role permissions.

For Okta applications using the SAML SSO identity-source type, each configured Role mapping is compared with one complete SAML attribute value. Comma- or space-separated role names inside a single value are not parsed. Emit the group/role attribute as a multi-value SAML attribute, with one exact value for each desired mapping. This limitation applies to SAML attribute mapping; it does not mean that every Okta identity-source mapping mechanism is limited to one Role.

.. NOTE:: If you've created multi-tenant roles, these will also appear here and can be mapped to Okta user groups allowing you to map users to equivalent user groups in |morpheus|.
