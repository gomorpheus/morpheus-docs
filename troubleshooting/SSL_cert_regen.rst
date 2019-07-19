SSL Cert Regeneration
========================

When Morpheus is deployed it generates a 10 year self signed non trusted ssl certificate.  Below details the process to regenerate this certificate.

#. Delete the files in ``/etc/morpheus/ssl/`` specifically the ``.crt`` and ``.key``
#. Run Reconfigure ``morpheus-ctl reconfigue``
#. Restart NGINX ``morpheus-ctl restart nginx``
