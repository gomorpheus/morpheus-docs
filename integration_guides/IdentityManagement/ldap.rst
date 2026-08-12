LDAP
----

Overview
^^^^^^^^

The LDAP identity source authenticates users against an LDAP directory and creates or updates the corresponding |morpheus| user at login. Identity sources are configured per Tenant under |AdmTen| > selected Tenant > :guilabel:`IDENTITY SOURCES`.

Before configuring the source, obtain a directory URL, a least-privilege bind account, the user distinguished-name (DN) pattern, user attribute names, and the DNs of any groups used to restrict access or map Roles. The appliance must be able to reach the directory endpoint. Use an ``ldaps://`` URL and a certificate issued for the directory hostname whenever the directory supports TLS. Do not place production credentials in examples, tickets, or screenshots.

Adding an LDAP Identity Source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmTen| and select a Tenant.
#. Select :guilabel:`IDENTITY SOURCES`, then :guilabel:`+ ADD IDENTITY SOURCE`.
#. Select ``LDAP`` and configure the following fields:

   URL
     LDAP endpoint, including the scheme and port, for example ``ldaps://ldap.example.com:636``.
   Binding Username
     DN or username for an account that can read the required users, attributes, and groups.
   Binding Password
     Password for the binding account. The value is stored as a secured field.
   User DN Expression
     Template used to construct the authenticating user's DN. ``$username`` is replaced with the supplied login name, for example ``uid=$username,ou=people,dc=example,dc=com``.
   Required Group DN
     Optional group DN that a user must match before login is authorized. Leaving it empty removes this group gate; successful directory authentication can then create or synchronize a user.
   LDAP Attribute Names
     Attribute names used to read the username, common name, first name, last name, email, group members, and user group memberships. The implementation defaults to ``uid``, ``cn``, ``givenName``, ``sn``, ``mail``, ``uniqueMember``, and ``memberOf`` respectively when a value is not supplied.

#. Set the Default Role and map additional |morpheus| Roles to LDAP group DNs. At login, group membership is tested against the configured user membership attribute (and then ``uniqueMemberOf``). Each matching mapping adds its Role; the Default Role is also assigned. With Manual Role Assignment disabled, these identity-source Roles are recalculated on login.
#. Save the source. Saving validates the URL, bind credentials, user DN expression, Required Group DN, and mapped group DNs.

Testing and troubleshooting
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test with a non-administrative directory user that is in the required and mapped groups, then with a user outside the Required Group. Confirm the resulting local profile attributes and Roles. If saving or login fails:

* Verify DNS, routing, and the LDAP/LDAPS port from every appliance application node.
* Verify the bind account can read the generated user DN and every configured group DN.
* Check that the User DN Expression produces the user's exact DN and that attribute names match the directory schema.
* Confirm group mapping values are full DNs and match the values returned by the user's membership attribute.
* For LDAPS, verify the endpoint hostname and certificate chain. Do not bypass certificate checks in external diagnostic clients or replace LDAPS with clear-text LDAP as a production workaround.

.. NOTE:: The fields and defaults above describe the current LDAP implementation. Directory schemas vary; use the attribute names and DN syntax returned by your directory rather than assuming Active Directory conventions.
