Identity Sources
================
``Administration -> Tenants -> Select Tenant -> Identity Sources``

Overview
--------

There are several built in single sign-on integrations included with |morpheus| . These can be configured via the :guilabel:`+ IDENTITY SOURCES` button in ``Administration -> Accounts``. These integrations include linking
capabilities with LDAP, Active Directory, Okta, OneLogin and Jump Cloud. One can even map these sign on tools to equivalent roles in |morpheus| so at first log in users are assigned the appropriate role.

.. .image:: /images/administration/identity_sources.png

.. include:: tenants/ad.rst
.. include:: tenants/onelogin.rst
