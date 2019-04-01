Import Trusted Certificates to Morpheus
------------------------------------------

#. Obtain the full SSL certificate chain in PEM format. How you get this just depends on how your organization distributes the internal CA certificate and if it has an intermediate CA or not. I can help you figure out how to get the right format or you can Google the ways to convert what you have into a PEM formatted certificate chain.

#. Once you have the certificates, copy them to each appliance and place them in the /etc/morpheus/ssl/trusted_certificates directory.

#. Run morpheus-ctl reconfigure on each appliance, note you don’t need to stop Morpheus before you run this.

#. Run the following commands as root:

.. code-block:: bash

    export PATH=/opt/morpheus/sbin:/opt/morpheus/sbin:/opt/morpheus/embedded/sbin:/opt/morpheus/embedded/bin:$PATH

.. code-block:: bash

   /opt/morpheus/embedded/java/bin/keytool -import -keystore /opt/morpheus/embedded/java/lib/security/cacerts -trustcacerts -file /etc/morpheus/ssl/trusted_certs/root_ca.pem -alias some_alias -keypass changeit

Do this command for each certificate in the chain adjust the file and alias name as needed. Answer yes for the root certificate when asked it you want to trust it.

If you run the command openssl s_client -connect host:port -showcerts -tls1_2 you should get an output that looks like something like this:`

.. code-block:: bash

    New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-GCM-SHA384
    Server public key is 2048 bit
    Secure Renegotiation IS supported
    No ALPN negotiated
    SSL-Session:
    Protocol : TLSv1.2
    Cipher  : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 5D9E820E4FF2A73A9977BA663E6029AA5415FEE95F49D8B1E541F5997C8E1FB2
    Session-ID-ctx:
    Master-Key: 29EEC2E7750C659AECB9942902D9A87B824E571522112B718420FC08F8D2ACE68CB16EC812A7D90B12A86D1970FFD81C
    Key-Arg  : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1547219217
    Timeout  : 7200 (sec)
    Verify return code: 0 (ok)

If the certificates are installed correctly you should see Verify return code: 0 (ok) if not then you get something like Verify return code: 21 (unable to verify the first certificate)
