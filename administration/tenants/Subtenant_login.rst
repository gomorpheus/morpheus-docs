Subtenant Login
================

Subusers can have the same username as the user on the master tenant or any other tenant. Subusers will now have to login using the subdomain prefix. 

.. important::

  Subtenant users will no longer be able to login from the main login page without specifying their subdomain.


Example:
  I have a username ``subuser`` that belongs to a tenant with the subdomain ``subaccount``.
  When logging in from the main login url, I would now need to enter in: ``subaccount\subuser``
