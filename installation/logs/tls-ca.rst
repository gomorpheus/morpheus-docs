#. Generate a Certificate Authority (CA) on ``es-node-01``, which will be used to generate all the certificates needed for all the nodes:
       
    .. code-block:: bash

        /usr/share/elasticsearch/bin/elasticsearch-certutil ca --out /etc/elasticsearch/elastic-stack-ca.p12

    #. If a CA has been created previously for other TLS certificates, that can be used instead of generating a new one.  Using a single CA makes implementations less complex
    #. During the CA creation process, you will be prompted to create a password to secure the CA.  Although it is not required, it is
        recommended and this guide will assume that a password was created.  If one was not created, ignore any steps related to passwords on the CA