Key Pairs & Certificates
========================

Key Pairs
---------

The Key Pairs section enables the following actions: Add and Delete key pairs. Key Pairs are commonly used by |morpheus| for accessing instances via SSH. |morpheus| stores key pairs to simplify administration and access across both private and public clouds.

To navigate to the Key Pairs section:

#. Select the Infrastructure link in the navigation bar.
#. Select the Key Pairs link in the sub navigation bar.

Add Key Pair
------------

.. IMPORTANT::  Keys need to be RSA format, OpenSSH format is not accepted. Some operating systems, such as Mac OS X, default to OpenSSH. When generating keys in these operating systems, `we must specify generation in RSA format <https://support.morpheusdata.com/s/article/ssh-key-not-showing-new-integration?language=en_US>`_. 

To Add Key Pair:

#. Select the Infrastructure link in the navigation bar.
#. Select the Key Pairs link in the sub navigation bar.
#. Click the Add Key Pair button.
#. From the Add Key Pair Wizard input the following:
  * Name
  * Public Key
  * Private Key

.. NOTE:: Certain features do not require storage of the private key.

Delete Key Pair
---------------

To Delete Key Pair:

#. Select the Infrastructure link in the navigation bar.
#. Select the Key Pairs link in the sub navigation bar.
#. Click the Delete icon on the row of the Key Pair to delete.

.. ==Certificates
