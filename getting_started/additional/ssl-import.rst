Import Trusted Certificates
---------------------------

Use this procedure to add a certificate authority that the |morpheus| application must trust, such as the CA for a ServiceNow endpoint. Reconfigure imports certificates from the trusted-certificate directory into both the appliance OpenSSL trust path and the embedded JRE truststore. Reconfigure does not restart a running ``morpheus-ui`` JVM, so the UI must be restarted to load the updated JRE truststore.

#. Obtain the full SSL certificate chain in PEM format.

#. Copy them to each appliance and place them in the ``/etc/morpheus/ssl/trusted_certs`` directory.

#. Run ``morpheus-ctl reconfigure`` on the appliance. Reconfigure can run while the UI is active.

#. Verify that each certificate is present in the embedded JRE truststore. Reconfigure uses the certificate filename as its alias:

   .. code-block:: bash

      /opt/morpheus/embedded/java/jre/bin/keytool -list -cacerts -storepass changeit -alias root_ca.pem

#. Verify the remote endpoint and chain with the appliance OpenSSL client, replacing the host and port:

    .. code-block:: bash

       openssl s_client -connect host:port -showcerts -tls1_2

#. You should get an output similar to:

    .. code-block:: bash

        New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-GCM-SHA384
        Server public key is 2048 bit
        Secure Renegotiation IS supported
        No ALPN negotiated
        SSL-Session:
        Protocol : TLSv1.2
        Cipher  : ECDHE-RSA-AES256-GCM-SHA384
        Session-ID: 5D9E820E4FF2A73A9977BA663E6029AA5415FEE85F49D8B1E541F5997C8E1FB2
        Session-ID-ctx:
        Master-Key: 29EEC2E7750C659AECB9942902D9A87B824E571522812B718420FC08F8D2ACE68CB16EC812A7D90B12A86D1970FFD81C
        Key-Arg  : None
        PSK identity: None
        PSK identity hint: None
        SRP username: None
        Start Time: 1547219217
        Timeout  : 7200 (sec)
        Verify return code: 0 (ok) #<----------------

#. If the certificates are installed correctly you should see ``Verify return code: 0 (ok)``.  If they were not installed correctly then you will see a return similar to: ``Verify return code: 21 (unable to verify the first certificate)``

#. Restart the UI so its JVM loads the updated truststore:

   .. code-block:: bash

      morpheus-ctl restart morpheus-ui

#. Repeat the copy, reconfigure, truststore verification, and UI restart on every application node. In an HA deployment, process one application node at a time and confirm it is healthy before proceeding to the next node.

#. Retry the integration without disabling certificate verification. A successful connection confirms that the application JVM trusts the endpoint; ``openssl`` success alone does not verify the trust state of the already-running JVM.
