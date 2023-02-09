RabbitMQ
^^^^^^^^

This page is designed to help troubleshoot issues with RabbitMQ.  

Additional troubleshooting information:

    https://www.rabbitmq.com/troubleshooting.html

Log Locations
`````````````

    Embedded: ``/var/log/morpheus/rabbitmq/current``

    External cluster (default location): ``/var/log/rabbitmq/<rabbitNodeName>``

Using the rabbitmqctl Command
`````````````````````````````

    If RabbitMQ is embedded on the application nodes, then accessing ``rabbitmqctl`` can be call from the ``/opt/morpheus/embedded/bin/`` location:
    
    Example command:
    
        .. code-block:: bash
            
            /opt/morpheus/embedded/bin/rabbitmqctl report

    An alternative to having to use ``/opt/morpheus/embedded/bin/`` prior to the command, you can ``source`` the profile:

        .. code-block:: bash

            source /opt/morpheus/embedded/rabbitmq/.profile

        This will allow you to call the ``rabbitmqctl`` command without needing to use the full path.  For example:

            .. code-block:: bash

                rabbitmqctl report
        
        When sourced, you can also see the other environment variables available, to help locate other files and other configuration data:

            .. code-block:: bash

                env
    
    Additional information on the rabbitmqctl command can be found here:

        https://www.rabbitmq.com/rabbitmqctl.8.html


Common rabbitmqctl Commands
```````````````````````````

    **Enable the RabbitMQ UI**
	
        This will allow for the use of the web UI for external clusters, which can be navigated to via ``http://<nodeip/fqdn>:15672``

        .. code-block:: bash

            rabbitmq-plugins enable rabbitmq_management
    
    **Check the Status of the Service**

        Embedded Service:

            .. code-block:: bash

                morpheus-ctl status rabbitmq

        External Service:

            .. code-block:: bash

                morpheus-ctl status rabbitmq

    **Check the Cluster Status**

        .. code-block:: bash

            systemctl status rabbitmq-server

    **Generate a Report**

        .. code-block:: bash

            rabbitmqctl report | less -R

    **Lists All Policies**
	
        .. code-block:: bash

            rabbitmqctl -q -p / list_policies

    **Check Queue Quantity**
	
        .. code-block:: bash

            rabbitmqctl -q -p morpheus list_queues

    **Delete Queue via CLI**

        .. code-block:: bash

            rabbitmqadmin delete queue name='applianceJobLowQueue'

    **Remove Corrupted mnesia Database**

        The service may not start if the database is corrupted.  This process will clear the database and be rebuilt when the service starts again.

        Embedded example (folder names may vary):
        
            .. code-block:: bash

                morpheus-ctl stop rabbitmq
                # backup the database in case
                mv /var/opt/morpheus/rabbitmq/db/rabbit@app1/ /tmp
                morpheus-ctl start rabbitmq

        External cluster example (paths and hostname may vary):

            .. code-block:: bash

                systemctl stop rabbitmq-server
                # backup the database in case
                mv /var/lib/rabbitmq/mnesia/rabbit@app1/ /tmp
                systemctl start rabbitmq-server