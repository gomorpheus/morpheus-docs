.. _elasticsearch-tls-client:

(Optional) Client TLS
`````````````````````

.. toggle-header::
    :header: **Click to expand**

    In some cases, a cusomer may want to setup client TLS, to prevent the communication between |morpheus| and Elasticsearch on 9200 to be inspected.
    Although the data contained in the Elasticsearch logs is basically harmless, there are requirements from customers to secure
    communcation where possible.

    In this guide, we'll be configuring a locally-signed certificate.  A locally signed certificate is generated using a certificate
    authority (CA) that was also generated on the same node(s).  This is similar to a self-signed certificate, where it will not be trusted
    generally.  However, there will be a CA created in this process, which will sign the certificate and could be imported to be trusted.
    There may be a requirement to use internally generated certificates using a customers' PKI system, which can be used in lieu of many
    of the steps below.  This will not be covered in this document but providing the CA in a ``.p12`` to generate the certificates could be
    possible or certificate being provided in a ``.p12`` format, which would avoid any of the certificate generation.

    .. warning::
        It is best to ensure that DNS (or ``/etc/hosts``) is configured to resolve to hostnames to match to the certificates generated

    .. note::
        This is not the same as setting up inter-node TLS for the Elasticsearch nodes to communicate with each other.  See the :ref:`elasticsearch-tls-inter-node`
        section for more details.

    .. note::
        This guide will assume that Elasticsearch was installed in the default location of ``/usr/share/elasticsearch/`` and the configuration
        location is ``/etc/elasticsearch/``.  Modify the commands below as needed, if the installation or configuration locations are different.
        If certificates are created without the ``--out`` parameter the certificates will be generated in ``/usr/share/elasticsearch/``.

    - ``unzip`` is used in the steps, be sure to install it if needed

        .. tabs::

            .. group-tab:: RHEL

                .. code-block:: bash

                    dnf install unzip -y
                            
            .. group-tab:: Ubuntu

                .. code-block:: bash

                    apt install unzip -y

    Additional links used in this guide:

        - Encrypt HTTP CLient Communications:
        
            https://www.elastic.co/guide/en/elasticsearch/reference/7.17/security-basic-setup-https.html
        
        - elasticsearch-certutil:

            https://www.elastic.co/guide/en/elasticsearch/reference/current/certutil.html

        - elasticsearch-keystore

            https://www.elastic.co/guide/en/elasticsearch/reference/7.17/elasticsearch-keystore.html
    
    .. include::
        /installation/logs/tls-ca.rst

    #. On ``es-node-01``, run the following command, which will generate the certificates for all of your nodes

        - Ensure you have the short names, FQDNs available, and **static** IP addresses for each Elasticsearch node
        - The local path to the CA ``.p12`` certificate
        - Password for the CA ``.p12`` certificate        - 
       
        .. code-block:: bash

            /usr/share/elasticsearch/bin/elasticsearch-certutil http

        #. Generate a CSR? [y/N] **n**
        #. Use an existing CA? [y/N] **y**
        #. Enter the path to the CA certificate
            
            #. Enter the password, if necessary
        #. Enter an expiration length for the certificates
        #. Generate a certificate per node? [y/N] **y**

            #. node #1 name: **es-node-01**
            #. Enter all the shortnames and FQDNs, one per line.  If there is a load balancer for the cluster, this may be entered too if needed

                Examples:
                
                    es-node-01  
                    es-node-01.mydoamin.com  
                    loadbalancer.mydomain.com  

            #. Enter all IP addresses, one per line, if the nodes have **static** IP addresses
            #. Do you wish to change any of these options? [y/N] **n**
            #. Generate additional certificates? [Y/n] **y**
        #. Repeat the previous step for each node, until there are no more certificates to generate
        #. (Optional) Enter a password to secure the certificates
        #. What filename should be used for the output zip file? **/etc/elasticsearch/elasticsearch-ssl-http.zip**
    #. On ``es-node-01`` unzip the zip file created with all the certificate information
    
        .. code-block:: bash
            
            unzip /etc/elasticsearch/elasticsearch-ssl-http.zip -d /etc/elasticsearch/elasticsearch-ssl-http
            cp /etc/elasticsearch/elasticsearch-ssl-http/elasticsearch/es-node-01/http.p12 /etc/elasticsearch
            chmod 660 /etc/elasticsearch/http.p12

    #. On ``es-node-01``, copy the certificates to the remaining nodes

        .. code-block:: bash

            scp /etc/elasticsearch/elasticsearch-ssl-http/elasticsearch/es-node-02/http.p12 myusername@192.168.103.02:/home/myusername
            scp /etc/elasticsearch/elasticsearch-ssl-http/elasticsearch/es-node-03/http.p12 myusername@192.168.103.03:/home/myusername

    #. On ``es-node-02`` and ``es-node02`` copy the files to the appropriate path and set the permissions:

        .. code-block:: bash

            cp /home/myusername/http.p12 /etc/elasticsearch/
            chmod 660 /etc/elasticsearch/http.p12

    #. On ``All Nodes``, edit the Elasticsearch configuration file

        .. code-block:: bash

            vim /etc/elasticsearch/elasticsearch.yml

        #. Place the following in the ``/etc/elasticsearch/elasticsearch.yml`` file

            .. code-block:: yaml

                xpack.security.http.ssl.enabled: true
                xpack.security.http.ssl.keystore.path: http.p12

    #. On ``All Nodes``, if a password was set for the certificates, run the following command to set the password in Elasticsearch:

        .. code-block:: bash

            /usr/share/elasticsearch/bin/elasticsearch-keystore add xpack.security.http.ssl.keystore.secure_password
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

    #. The temporary zip files and certificates can be cleaned up as well.  You can back these up or generate new ones, as long as the CA certificate is backed up

        .. code-block:: bash

            rm /etc/elasticsearch/elasticsearch-ssl-http.zip
            rm /etc/elasticsearch/elasticsearch-ssl-http -rf

    #. Verify cluster health (**using HTTPS**)

        .. code-block:: bash

            curl https://node_ip:9200/_cluster/health -k
            
            or

            curl https://localhost:9200/_cluster/health -k