Key Pairs & Certificates
========================

Key Pairs
---------

The key pairs section enables the following actions: Add and Delete key pairs. Key pairs are commonly used by |morpheus| for accessing instances via SSH. |morpheus| stores key pairs to simplify administration and access across both private and public clouds.

|morpheus| only accepts key pairs in PEM format (for example, a private key beginning with ``-----BEGIN RSA PRIVATE KEY-----``). If you have a key in another format, such as OpenSSH, convert the key:

.. code-block:: bash

  #No passphrase
  ssh-keygen -m pem -f /path/to/key

  #With passphrase
  ssh-keygen -p -P "old passphrase" -N "new passphrase" -m pem -f path/to/key

Add Key Pair
------------

To Add Key Pair:

#. Navigate to Infrastructure > Keys & Certs
#. On the Key Pairs tab, click :guilabel:`+ ADD`
#. From the Add Key Pair wizard input the following as needed:

   * Name
   * Public Key
   * Private Key
   * Passphrase

   .. NOTE:: Certain features do not require storage of the private key.

Delete Key Pair
---------------

To Delete Key Pair:

#. Navigate to Infrastructure > Keys & Certs
#. On the Key Pairs tab, select the trash can icon at the end of any row
#. Acknowledge that you wish to delete the selected key pair

SSL Certificates
----------------

SSL certificates authenticate the identity of web servers and encrypt the data being transmitted. |morpheus| stores SSL certificates to simplify administration and application of SSL certificates to |morpheus|-managed resources.

Add SSL Certificate
-------------------

#. Navigate to Infrastructure > Keys & Certs
#. On the SSL Certificates tab, click :guilabel:`+ ADD`
#. From the Add SSL Certificate wizard input the following as needed:

   * Name
   * Domain Name
   * Key File
   * Cert File
   * Root Cert

Delete SSL Certificate
----------------------

To Delete SSL Certificate:

#. Navigate to Infrastructure > Keys & Certs
#. On the SSL Certificates tab, select the trash can icon at the end of any row
#. Acknowledge that you wish to delete the selected SSL Certificate

Trust Integrations
------------------

Some organizations may use outside technologies to manage their key and certificates. |morpheus| allows users to integrate with Venafi for trust management. Trust management integrations can be managed from the Integrations tab on the Infrastructure > Keys & Certs page. Additionally, they can be managed in |AdmInt|.

Currently, |morpheus| supports trust integration Venafi. For more detailed information on integrating Venafi with |morpheus|, take a look at our `integration guide <https://docs.morpheusdata.com/en/latest/integration_guides/KeysCertificates/keysandcerts.html>`_.
