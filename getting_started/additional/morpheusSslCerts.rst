SSL Certificates
----------------

By default |morpheus| generates a Self-Signed SSL Certificate. The Self-Signed SSL Certificate can be replaced with a Trusted CA Signed SSL Certificate.

Trusted CA Signed SSL Certificate Implementation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. If you don't already have your certificate, run an OpenSSL command to generate an SSL certificate request (.csr) and private key (.key). If you need help formatting the command, `DigiCert provides a helpful tool <https://www.digicert.com/easy-csr/openssl.htm>`_

#. Submit your certificate request (.csr) and await approval of the request and return of the certificate (.crt)

#. Copy the private key and certificate to ``/etc/morpheus/ssl/your_fqdn_name.key`` and ``/etc/morpheus/ssl/your_fqdn_name.crt`` respectively

    - .. toggle-header:: :header: **Extracting Certificates in PFX Format**

       .. code-block:: bash

         # Extract the private key
         openssl pkcs12 -in example.pfx -nocerts -nodes -out priv.key
         # Extract the public key
         openssl pkcs12 -in example.pfx -clcerts -nokeys -out pub.crt
         # Extract the CA cert chain
         openssl pkcs12 -in example.pfx -cacerts -nokeys -chain -out ca.crt

    - .. toggle-header:: :header: **Extracting Certificates in PEM Format**

       .. code-block:: bash

         # Extract the private key
         openssl x509 -outform der -in your-cert.pem -out your-cert.key
         # Extract the public key
         openssl x509 -outform der -in your-cert.pem -out your-cert.key

#. Edit the configuration file ``/etc/morpheus/morpheus.rb`` and add the following entries:

   .. code-block:: bash

    nginx['ssl_certificate'] = 'path to the certificate file'
    nginx['ssl_server_key'] = 'path to the server key file'

   .. NOTE:: Both files should be owned by root and only readable by root, also if the server certificate is signed by an intermediate then you should include the signing chain inside the certificate file. The key file needs to be decrypted for Morpheus to install it properly.

#. Next simply reconfigure the appliance and restart nginx:

   .. code-block:: bash

    sudo morpheus-ctl reconfigure
    sudo morpheus-ctl restart nginx

Self-Signed SSL Certificate Regeneration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When Morpheus is deployed it generates a 10 year Self-Signed SSL Certificate.  Below details the process to regenerate the Certificate and Key files.

Regenerate both the Certificate and Key
```````````````````````````````````````

#. Delete the certificate and key files in ``/etc/morpheus/ssl/``.
#. Run Reconfigure ``morpheus-ctl reconfigure``.
#. Restart NGINX ``morpheus-ctl restart nginx``.

Regenerate only the Certificate
```````````````````````````````

#. Delete the certificate file in ``/etc/morpheus/ssl/``.
#. Run Reconfigure ``morpheus-ctl reconfigure``.
#. Restart NGINX ``morpheus-ctl restart nginx``.
