.. _elasticsearch-inter-node-tls:

(Optional) Inter-node TLS
`````````````````````````

.. toggle-header::
    :header: **Click to expand**

    In some cases, a cusomer may want to setup inter-node TLS, to prevent the communication between nodes on 9300 to be inspected.
    Although the data contained in the Elasticsearch logs is basically harmless, there are requirements from customers to secure
    communcation where possible.

    In this guide, we'll be configuring a locally-signed certificate.  A locally signed certificate is generated using a certificate
    authority (CA) that was also generated on the same node(s).  This is similar to a self-signed certificate, where it will not be trusted
    generally.  However, there will be a CA created in this process, which will sign the certificate and could be imported to be trusted.
    There may be a requirement to use internally generated certificates using a customers' PKI system, which can be used in lieu of many
    of the steps below.  This will not be covered in this document but providing the CA in a ``.p12`` to generate the certificates could be
    possible or certificate being provided in a ``.p12`` format, which would avoid any of the certificate generation.

    .. note::
        This is not the same as setting up TLS for the |morpheus| nodes to connect via TLS to the cluster.  See the ``<inputlinklater>``
        section for more details.

    .. note::
        This guide will assume that Elasticsearch was installed in the default location of ``/usr/share/elasticsearch/`` and the configuration
        location is ``/etc/elasticsearch/``.  Modify the commands below as needed, if the installation or configuration locations are different.
        If certificates are created without the ``--out`` parameter the certificates will be generated in ``/usr/share/elasticsearch/``.

    Additional links used in this guide:

        - Encrypt Internode Communication:
        
            https://www.elastic.co/guide/en/elasticsearch/reference/7.17/security-basic-setup.html
        
        - elasticsearch-certutil:

            https://www.elastic.co/guide/en/elasticsearch/reference/current/certutil.html

        - elasticsearch-keystore

            https://www.elastic.co/guide/en/elasticsearch/reference/7.17/elasticsearch-keystore.html

    #. Begin by generating a Certificate Authority (CA) on ``es-node-01``, which will be used to generate all the certificates needed for all the nodes:
       
        .. code-block:: bash

            /usr/share/elasticsearch/bin/elasticsearch-certutil ca --out /etc/elasticsearch/elastic-stack-ca.p12

        #. During the CA creation process, you will be prompted to create a password to secure the CA.  Although it is not required, it is
           recommended and this guide will assume that a password was created.  If one was not created, ignore any steps related to passwords on the CA
        #. If a CA has been created previously, that can be used instead of generating a new one.  Using a single CA makes implementations less complex
    #. Next, generate the certificate on ``es-node-01``, which a single one will be used across all the nodes
       
        .. code-block:: bash

            /usr/share/elasticsearch/bin/elasticsearch-certutil cert --ca /etc/elasticsearch/elastic-stack-ca.p12 --out /etc/elasticsearch/elastic-certificates.p12

        #. Enter the password created for the CA
        #. (optional) Enter a password for the certificate.  This guide will assume a password was entered
    #. With the certificate generated on ``es-node-01``, modify the permissions on ``es-node-01``:
        
        .. code-block:: bash

            chmod 660 /etc/elasticsearch/elastic-certificates.p12

    #. From ``es-node-01``, copy the certificate to the other nodes:

        .. code-block:: bash

            scp /usr/share/elasticsearch/elastic-certificates.p12 myusername@192.168.103.02:/home/myusername
            scp /usr/share/elasticsearch/elastic-certificates.p12 myusername@192.168.103.03:/home/myusername
    
    #. On ``es-node-02`` and ``es-node02`` copy the files to the appropriate path and set the permissions:

        .. code-block:: bash

            cp /home/myusername/elastic-certificates.p12 /etc/elasticsearch/
            chmod 660 /etc/elasticsearch/elastic-certificates.p12

    #. On ``All Nodes``, edit the Elasticsearch configuration file

        .. code-block:: bash

            vim /etc/elasticsearch/elasticsearch.yml

        #. Place the following in the ``/etc/elasticsearch/elasticsearch.yml`` file

            .. code-block:: yaml

                xpack.security.transport.ssl.enabled: true
                xpack.security.transport.ssl.verification_mode: certificate
                xpack.security.transport.ssl.client_authentication: required
                xpack.security.transport.ssl.keystore.path: elastic-certificates.p12
                xpack.security.transport.ssl.truststore.path: elastic-certificates.p12

    #. On ``All Nodes``, if a password was set for the certificate, run the following commands to set the passwords in Elasticsearch:

        .. code-block:: bash

            /usr/share/elasticsearch/bin/elasticsearch-keystore add xpack.security.transport.ssl.keystore.secure_password
                # Enter the password when prompted
            /usr/share/elasticsearch/bin/elasticsearch-keystore add xpack.security.transport.ssl.truststore.secure_password
                # Enter the password when prompted

    #. On ``All Nodes``, restart the Elasticsearch service to enable the changes:

        .. code-block:: bash

            systemctl restart elasticsearch

        #. Startup errors can be investigated in the default Elasticsearch log location (replacing ``clustername``):

            .. code-block:: bash

                tail -100 /var/log/elasticsearch/clustername.log

    #. Once the service is started, on ``es-node-01``, be sure to backup the CA file (``/etc/elasticsearch/elastic-stack-ca.p12``) to an external location,
       in case it is needed at another time.  If this CA file is compromised, a new CA and certificate should be generated
       and implemented.
    #. **Once it is backed-up**, remove the CA file  from ``es-node-01``:

        .. code-block:: bash

            rm /etc/elasticsearch/elastic-stack-ca.p12