Cannot Login
============

Forgot password
---------------

If a user forgets their password, they can use the `FORGOT PASSWORD?` link on the login page. They can then enter their username or email address to send a reset password email to the email address defined on the user.

If the default or user added SMTP server is not functioning or blocked, a System Admin user can impersonate that user and update their password.

If the System Admin user password needs to be reset and the default or user added SMTP server is not functioning or blocked, please contact Morpheus support for assistance.

Sub-Tenant user cannot login after 3.4.0 upgrade
------------------------------------------------

|morpheus| v3.4.0 added support for all subtenant users to login via the main tenant url using subtenant id or subdomain prefix, ie ``tenantId\username`` or ``subdomain\username``.

.. NOTE:: Tenant subdomains can be defined by editing Tenant settings and updating the `SUBDOMAIN` field.

.. IMPORTANT:: Subtenant local users will no longer be able to login from main login url without using their subtenant id or subdomain prefix.

The login requirements were added in v3.4.0 to allow subtenant users with identity source integration generated user accounts to be able to login to the master tenant, gain API and CLI access, and remove the requirement for usernames to be unique across all tenants.

Previously subtenant users that had local/morpheus generated user accounts could login to their tenant via the master tenant url, while subtenant users that had identity source integration generated user accounts had to use the subtenant specific login url.

In v3.4.0+ all subtenant users can login via the master tenant url by specifying their tenant id or subdomain prefix, ``\``, then username. Subtenants can still use the tenant specific login url as well.

Example:
  I have a username ``subuser`` that belongs to a tenant with the subdomain ``acme`` and tenant id ``58``. When logging in from the main login url, I now need to enter in: ``acme\subuser`` and the password. Alternatively the tenant ID can be used, ie ``58\subuser``

Active Directory user suddenly cannot Login
-------------------------------------------

In |morpheus| v3.4.0 and prior, OU changes in Active Directory can disable logins for AD users who had previously authenticated/have existing user accounts in |morpheus|. If an Active Directory user cannot login to |morpheus| after their OU was changed in AD, please contact Morpheus support for a resolution. The OU association for the user(s) can also be manually updated in the database. This issue is resolved in |morpheus| versions 3.4.1 and higher. 
