SSL Self-signed Certificate Regeneration
========================================

When Morpheus is deployed it generates a 10 year self-signed non-trusted SSL certificate.  Below details the process to regenerate this certificate and key.

Replacing both the certificate and private key
----------------------------------------------

#. Delete the certificate and key files in ``/etc/morpheus/ssl/`` that end in ``.crt`` and ``.key``
#. Run Reconfigure ``morpheus-ctl reconfigure``
#. Restart NGINX ``morpheus-ctl restart nginx``

Replacing only the certificate
------------------------------

#. Delete the certificate file in ``/etc/morpheus/ssl/`` it ends in ``.crt``
#. Run Reconfigure ``morpheus-ctl reconfigure``
#. Restart NGINX ``morpheus-ctl restart nginx``
