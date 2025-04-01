Securing Elasticsearch
``````````````````````
.. Content-Begin

#. Using ``Node 1``, create the directory structure and generate the needed Certificate Authority (CA) certificate

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 1

         .. code-block:: bash

            mkdir /var/opt/morpheus/certs/ -p
            export ES_JAVA_HOME=/opt/morpheus/embedded/java/jdk
            /opt/morpheus/embedded/elasticsearch/bin/elasticsearch-certutil ca --days 1826 --out /var/opt/morpheus/certs/elastic-stack-ca.p12
               # Be sure to enter a password for the CA
            chown 896:896 /var/opt/morpheus/certs/elastic-stack-ca.p12
            chmod u=rw,g=r /var/opt/morpheus/certs/elastic-stack-ca.p12
            chmod -R o+x /var/opt/morpheus/certs/

#. Copy the CA certificate from ``Node 1`` to the other nodes, replacing the hostnames and usernames as needed

   .. content-tabs::

     .. tab-container:: tab1
        :title: Node 1

        .. code-block:: bash

           scp /var/opt/morpheus/certs/elastic-stack-ca.p12 username@es-node-02:/home/username
           scp /var/opt/morpheus/certs/elastic-stack-ca.p12 username@es-node-03:/home/username

#. Create the same directory structure on ``Node 2`` and ``Node 3``, then copy the CA certificate from the ``/home/username`` directory to the same location as ``Node 1``

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 2

         .. code-block:: bash

            mkdir /var/opt/morpheus/certs/ -p
            cp /home/username/elastic-stack-ca.p12 /var/opt/morpheus/certs/

      .. tab-container:: tab2
         :title: Node 3

         .. code-block:: bash

            mkdir /var/opt/morpheus/certs/ -p
            cp /home/username/elastic-stack-ca.p12 /var/opt/morpheus/certs/

.. note::
      The UID/GID ``896`` is used for the ``es-morpheus`` user, which will be configured in the configuration file example.
      If the UID/GID will be different, be sure to change it in the example below.

#. On ``All Nodes``, modify the permissions for the generated CA

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 1

         .. code-block:: bash
      
            chown 896:896 /var/opt/morpheus/certs/elastic-stack-ca.p12
            chmod u=rw,g=r /var/opt/morpheus/certs/elastic-stack-ca.p12
            chmod -R o+x /var/opt/morpheus/certs/

      .. tab-container:: tab2
         :title: Node 2

         .. code-block:: bash
      
            chown 896:896 /var/opt/morpheus/certs/elastic-stack-ca.p12
            chmod u=rw,g=r /var/opt/morpheus/certs/elastic-stack-ca.p12
            chmod -R o+x /var/opt/morpheus/certs/

      .. tab-container:: tab3
         :title: Node 3

         .. code-block:: bash
      
            chown 896:896 /var/opt/morpheus/certs/elastic-stack-ca.p12
            chmod u=rw,g=r /var/opt/morpheus/certs/elastic-stack-ca.p12
            chmod -R o+x /var/opt/morpheus/certs/

#. At this point, all three nodes should have the same CA certificate file located at ``/var/opt/morpheus/certs/elastic-stack-ca.p12``

   #. This file should at least allow ``read (r)`` to the UID/GID set (the ``es-morpheus`` user once created)
   #. Be sure the parent directories have at least ``execute (x)`` for other users, which will let the ``es-morpheus`` user traverse the directoires
   #. This file is very important and the least permissions possible is the best, in case of a system compromise

#. On ``All Nodes``, extract the certificate for the generated CA and place it in the |morpheus| ``trusted_certs``

   .. content-tabs::

      .. tab-container:: tab1
         :title: Node 1

         .. code-block:: bash
      
            openssl pkcs12 -in /var/opt/morpheus/certs/elastic-stack-ca.p12 -out /etc/morpheus/ssl/trusted_certs/elastic-stack-ca.pem -clcerts -nokeys

      .. tab-container:: tab2
         :title: Node 2

         .. code-block:: bash
      
            openssl pkcs12 -in /var/opt/morpheus/certs/elastic-stack-ca.p12 -out /etc/morpheus/ssl/trusted_certs/elastic-stack-ca.pem -clcerts -nokeys

      .. tab-container:: tab3
         :title: Node 3

         .. code-block:: bash
      
            openssl pkcs12 -in /var/opt/morpheus/certs/elastic-stack-ca.p12 -out /etc/morpheus/ssl/trusted_certs/elastic-stack-ca.pem -clcerts -nokeys
.. Content-Begin