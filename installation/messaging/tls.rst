.. rabbitmq-tls:

(Optional) Enable TLS
`````````````````````

.. toggle-header::
    :header: **Click to expand**

    In some cases, a cusomer may want to setup TLS, to prevent the communication between |morpheus| and RabbitMQ on 5672 to be inspected.
    Although the data contained in the RabbitMQ logs is basically harmless, there are requirements from customers to secure
    communcation where possible.

    In this guide, we'll be configuring a locally-signed certificate.  A locally signed certificate is generated using a certificate
    authority (CA) that was also generated on the same node(s).  This is similar to a self-signed certificate, where it will not be trusted
    generally.  However, there will be a CA created in this process, which will sign the certificate and could be imported to be trusted.
    There may be a requirement to use internally generated certificates using a customers' PKI system, which can be used in lieu of many
    of the steps below.  This will not be covered in this document but providing the CA in a ``.pem`` to generate the certificates could be
    possible or certificate being provided in a ``.pem`` format, which would avoid any of the certificate generation.

    .. warning::
        It is best to ensure that DNS (or ``/etc/hosts``) is configured to resolve to hostnames to match to the certificates generated

    Additional links used in this guide:

        - RabbitMQ TLS Support:
        
            https://www.rabbitmq.com/ssl.html
        
        - RabbitMQ Ports:
        
            https://www.rabbitmq.com/networking.html#ports

    #. On a single node, generate a CA certificate

        .. content-tabs::

            .. tab-container:: tab1
                :title: Node 1

                .. code-block:: bash

                    openssl genrsa -out /etc/pki/tls/private/rabbitmq-ca-key.pem
                    openssl req -new -key /etc/pki/tls/private/rabbitmq-ca-key.pem -x509 -days 1825 -out /etc/pki/tls/certs/rabbitmq-ca-cert.pem

    #. Using the generated CA, generate certificates for each RabbitMQ node.  These will all use their own private keys for the certificate signing request (CSR).  Be sure to enter appropriate information
       when prompted, specifically the Common Name, which should contain the server hostname that will be connected to
    
        .. content-tabs::

            .. tab-container:: tab1
                :title: Node 1
        
                .. code-block:: bash
                    
                    openssl genrsa -out /etc/pki/tls/private/rabbit-1-key.pem
                    openssl req -new -key /etc/pki/tls/private/rabbit-1-key.pem -out ~/rabbit-1.csr
                    openssl x509 -req -days 365 -in ~/rabbit-1.csr -CA /etc/pki/tls/certs/rabbitmq-ca-cert.pem -CAkey /etc/pki/tls/private/rabbitmq-ca-key.pem -CAcreateserial -out /etc/pki/tls/certs/rabbit-1-cert.pem

                .. code-block:: bash
                    
                    openssl genrsa -out /etc/pki/tls/private/rabbit-2-key.pem
                    openssl req -new -key /etc/pki/tls/private/rabbit-2-key.pem -out ~/rabbit-2.csr
                    openssl x509 -req -days 365 -in ~/rabbit-2.csr -CA /etc/pki/tls/certs/rabbitmq-ca-cert.pem -CAkey /etc/pki/tls/private/rabbitmq-ca-key.pem -CAcreateserial -out /etc/pki/tls/certs/rabbit-2-cert.pem

                .. code-block:: bash
                    
                    openssl genrsa -out /etc/pki/tls/private/rabbit-3-key.pem
                    openssl req -new -key /etc/pki/tls/private/rabbit-3-key.pem -out ~/rabbit-3.csr
                    openssl x509 -req -days 365 -in ~/rabbit-3.csr -CA /etc/pki/tls/certs/rabbitmq-ca-cert.pem -CAkey /etc/pki/tls/private/rabbitmq-ca-key.pem -CAcreateserial -out /etc/pki/tls/certs/rabbit-3-cert.pem

    #. Once all of the certificates have been generated, copy the respective certificates, private keys, and the CA public certificate to the other nodes

        .. content-tabs::

            .. tab-container:: tab1
                :title: Node 1
        
                .. code-block:: bash

                    scp /etc/pki/tls/certs/rabbit-2-cert.pem /etc/pki/tls/private/rabbit-2-key.pem /etc/pki/tls/certs/rabbitmq-ca-cert.pem username@rabbit-2:~
                    scp /etc/pki/tls/certs/rabbit-3-cert.pem /etc/pki/tls/private/rabbit-3-key.pem /etc/pki/tls/certs/rabbitmq-ca-cert.pem username@rabbit-3:~

    #. After the certificates have been copied to the other nodes, they need to be moved to the same location as ``Node 1``

        .. content-tabs::

            .. tab-container:: tab1
                :title: Node 2 and 3
        
                .. code-block:: bash

                    mv /home/username/rabbitmq-ca-cert.pem /etc/pki/tls/certs/
                    mv /home/username/rabbit-*-cert.pem /etc/pki/tls/certs/
                    mv /home/username/rabbit-*-key.pem /etc/pki/tls/private/

    #. On all of the nodes, be sure to set the permissions for the rabbitmq user to be able to access the appropriate certificates and private keys

        .. content-tabs::

            .. tab-container:: tab1
                :title: All Nodes

                .. code-block:: bash
                    
                    chown rabbitmq:rabbitmq /etc/pki/tls/private/rabbit-*-key.pem
                    chmod u=rw,g=r /etc/pki/tls/private/rabbit-*-key.pem

    #. Edit/create the ``/etc/rabbitmq/rabbitmq.conf`` configuration on all of the nodes with the following

        .. content-tabs::

            .. tab-container:: tab1
                :title: Node 1

                .. code-block:: bash
                    
                    ssl_options.cacertfile               = /etc/pki/tls/certs/rabbitmq-ca-cert.pem
                    ssl_options.certfile                 = /etc/pki/tls/certs/rabbit-1-cert.pem
                    ssl_options.keyfile                  = /etc/pki/tls/private/rabbit-1-key.pem
                    ssl_options.verify                   = verify_none
                    ssl_options.fail_if_no_peer_cert     = false
                    ssl_options.versions.1               = tlsv1.2
                    listeners.tcp                        = none
                    stomp.listeners.tcp                  = none
                    listeners.ssl.default                = 5671
                    stomp.listeners.ssl.default          = 61614

            .. tab-container:: tab2
                :title: Node 2

                .. code-block:: bash
                    
                    ssl_options.cacertfile               = /etc/pki/tls/certs/rabbitmq-ca-cert.pem
                    ssl_options.certfile                 = /etc/pki/tls/certs/rabbit-2-cert.pem
                    ssl_options.keyfile                  = /etc/pki/tls/private/rabbit-2-key.pem
                    ssl_options.verify                   = verify_none
                    ssl_options.fail_if_no_peer_cert     = false
                    ssl_options.versions.1               = tlsv1.2
                    listeners.tcp                        = none
                    stomp.listeners.tcp                  = none
                    listeners.ssl.default                = 5671
                    stomp.listeners.ssl.default          = 61614

            .. tab-container:: tab3
                :title: Node 3

                .. code-block:: bash
                    
                    ssl_options.cacertfile               = /etc/pki/tls/certs/rabbitmq-ca-cert.pem
                    ssl_options.certfile                 = /etc/pki/tls/certs/rabbit-3-cert.pem
                    ssl_options.keyfile                  = /etc/pki/tls/private/rabbit-3-key.pem
                    ssl_options.verify                   = verify_none
                    ssl_options.fail_if_no_peer_cert     = false
                    ssl_options.versions.1               = tlsv1.2
                    listeners.tcp                        = none
                    stomp.listeners.tcp                  = none
                    listeners.ssl.default                = 5671
                    stomp.listeners.ssl.default          = 61614


    #. Now restart the RabbitMQ service on all of the nodes

        .. content-tabs::

            .. tab-container:: tab1
                :title: All Nodes

                .. code-block:: bash
                    
                    systemctl restart rabbitmq-server

    #. Once the service is started on all of the nodes, be sure to backup the following CA files on ``Node 1`` to an external location,
       in case it is needed at another time.  If this CA file is compromised, a new CA and certificate should be generated
       and implemented.  If a node certificates is compromised, the CA can be reused to generate new certificates.  The files could remain on
       the node but can present a security risk to the RabbitMQ communication, if discovered.

       - ``/etc/pki/tls/private/rabbitmq-ca-key.pem``
       - ``/etc/pki/tls/certs/rabbitmq-ca-cert.pem``
       - ``/etc/pki/tls/certs/rabbitmq-ca-cert.srl``

    #. **Once the CA is backed-up**, delete the following files from ``Node 1`` to cleanup extra files:

        .. content-tabs::

            .. tab-container:: tab1
                :title: All Nodes
        
                .. code-block:: bash

                    rm /etc/pki/tls/private/rabbitmq-ca-key.pem
                    rm /etc/pki/tls/certs/rabbitmq-ca-cert.srl

                    rm /etc/pki/tls/certs/rabbit-2-cert.pem
                    rm /etc/pki/tls/private/rabbit-2-key.pem

                    rm /etc/pki/tls/certs/rabbit-3-cert.pem
                    rm /etc/pki/tls/private/rabbit-3-key.pem

                    rm ~/rabbit-1.csr
                    rm ~/rabbit-2.csr
                    rm ~/rabbit-3.csr

    Below is an example of how the ``/etc/morpheus/morpheus.rb`` file would be configured:

        .. code-block:: ruby

            rabbitmq['enable'] = false
            rabbitmq['vhost'] = 'morpheus'
            rabbitmq['queue_user'] = '<<admin username>>'
            rabbitmq['queue_user_password'] = '<<password>>'
            rabbitmq['host'] = 'RabbitMQ VIP'
            rabbitmq['port'] = '5671'
            rabbitmq['stomp_port'] = '61614'
            rabbitmq['use_tls'] = true
            rabbitmq['heartbeat'] = 50