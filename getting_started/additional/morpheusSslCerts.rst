SSL Certificates
----------------

The default installation generates a self-signed SSL certificate. To implement a third-party certificate:

#. Copy the private key and certificate to ``/etc/morpheus/ssl/your_fqdn_name.key`` and ``/etc/morpheus/ssl/your_fqdn_name.crt`` respectively.

#. Edit the configuration file ``/etc/morpheus/morpheus.rb`` and add the following entries:

   .. code-block:: bash

    nginx['ssl_certificate'] = 'path to the certificate file'
    nginx['ssl_server_key'] = 'path to the server key file'

   .. NOTE:: Both files should be owned by root and only readable by root, also if the server certificate is signed by an intermediate then you should include the signing chain inside the certificate file. The key file needs to decrypted for Morpheus to install it properly.

#. Next simply reconfigure the appliance and restart nginx:

   .. code-block:: bash

    sudo morpheus-ctl reconfigure
    sudo morpheus-ctl restart nginx

SSL Self-signed Certificate Regeneration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When Morpheus is deployed it generates a 10 year self-signed non-trusted SSL certificate.  Below details the process to regenerate this certificate and key.

Replacing both the certificate and private key
*************************************************

#. Delete the certificate and key files in ``/etc/morpheus/ssl/`` that end in ``.crt`` and ``.key``
#. Run Reconfigure ``morpheus-ctl reconfigure``
#. Restart NGINX ``morpheus-ctl restart nginx``

Replacing only the certificate
********************************

#. Delete the certificate file in ``/etc/morpheus/ssl/`` it ends in ``.crt``
#. Run Reconfigure ``morpheus-ctl reconfigure``
#. Restart NGINX ``morpheus-ctl restart nginx``
