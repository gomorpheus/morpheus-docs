3.2.0+ Upgrades
---------------

Overview
^^^^^^^^

Upgrading from previous versions of Morpheus to 3.2.0 or later requires upgrading ElasticSerach to 5.4.1 or 5.x. We do not support ElasticSearch 6.x at this time.  This upgrade requires an export and import of Morpheus ElasticSearch data if you want to retain logs, backup history, statistics, and check history of your instances. If you do not need to retain that data you can skip the ElasticSearch migration.  Upgrading to 3.2.0 will create a blank ElasticSearch node with no data. Your Morpheus layout configuration will determine how to migrate your ElasticSearch data: all-in-one or distributed high availability.

Morpheus All-In-One
^^^^^^^^^^^^^^^^^^^

This deployment configuration is the default mode for Morpheus and contains a single ElasticSearch instance on the appliance.  The migration steps are as follows:

#. Login to your appliance as a user that has sudo privileges and can switch to the root user sudo su -.  You can run the following commands under sudo, but you will need to pass the PATH to the Morpheus embedded directory. Export the Morpheus embedded path to your environment by executing: ``export PATH=/opt/morpheus/sbin:/opt/morpheus/sbin:/opt/morpheus/embedded/sbin:/opt/morpheus/embedded/bin:$PATH``

#. Verify that you are using the Morpheus embedded gem by executing the command: which gem. You should see the path ``/opt/morpheus/embedded/bin/gem``

#. Install the elastic-util gem by executing: ``gem install elastic-util`` if you don't want the documentation then execute ``gem install elastic-util --no-ri --no-rdoc``

#. Stop the Morpheus application by executing ``morpheus-ctl stop morpheus-ui``, this will stop creating new documents in ElasticSearch.

#. Create a backup of the ElasticSearch indices by executing: ``elastic-util backup http://localhost:9200 /root/es_backup``, you can change the location of the backup to any file location. You can also pass the ``--force`` argument to overwrite the existing location if you are repeating the backup.

#. Upgrade Morpheus as usual by executing the package upgrade command ``dpkg -i morpheus-appliance_3.2.0-1_amd64.deb`` or ``rpm -U morpheus-appliance-3.2.0-1.el7.x86_64.rpm``, and run ``morpheus-ctl reconfigure`` to complete the upgrade process.

#. You can start Morpheus at this point to bring up the Morpheus application by executing: ``morpheus-ctl start morpheus-ui``.

.. NOTE:: Make sure that Morpheus is fully started before moving on to the next step.

Once the application has started, a new ElasticSearch node is created with default data, to import your data from the backup execute: ``morpheus-ctl elastic-util restore http://localhost:9200 /root/es_backup``, substitute the path you used during the backup if different from above.

.. NOTE:: The restore may take several hours depending on the amount of data to restore. You can run this while running Morpheus.

Morpheus Distributed High Availability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This deployment configuration assumes that you manage an ElasticSearch cluster externally from Morpheus.  The steps for upgrading ElasticSearch from 1.x to 5.x are located on the ElasticSearch website. Run the following from a "master" appliance, it has the required Ruby installed in the Morpheus full stack directory. Ensure that the appliance can reach at least one ElasticSearch node over port 9200 (http). Also, make sure thre is enough disk space to hold the exported data on the appliance.

#. Login to the master appliance as a user that has sudo privileges and can switch to the root user ``sudo su -``.  You can run the following commands under sudo, but you will need to pass the PATH to the Morpheus embedded directory.

#. Export the Morpheus embedded path to your environment by executing: export ``PATH=/opt/morpheus/sbin:/opt/morpheus/sbin:/opt/morpheus/embedded/sbin:/opt/morpheus/embedded/bin:$PATH``

#. Verify that you are using the Morpheus embedded gem by executing the command: which gem. You should see the path ``/opt/morpheus/embedded/bin/gem``

#. Install the elastic-util gem by executing: ``gem install elastic-util`` if you don't want the documentation then execute ``gem install elastic-util --no-ri --no-rdoc``

#. Stop all the Morpheus application instances by executing ``morpheus-ctl stop morpheus-ui`` on each appliance node, this will stop creating new documents in ElasticSearch.

#. Create a backup of the ElasticSearch indices by executing: ``elastic-util backup http://xxx.xxx.xxx.xxx:9200 /root/es_backup``, you can change the location of the backup to any file location. You can also pass the ``--force`` argument to overwrite the existing location if you are repeating the backup.

   .. NOTE:: The next steps are done on the ElasticSearch node(s).

#. Stop ElasticSearch on each node.

#. Backup the ElasticSearch config directory for each node, normally located at ``/etc/elasticsearch/``.

#. Since the index data between 1.x and 5.x is incompatible, delete the data from the data directory normally located at ``/var/lib/elasticsearch``. To prepare for future upgrades make sure that you delete the cluster name directory as well, ie morpheus.

#. Upgrade ElasticSearch, use the method that best fits your situation ie pkg, tar, or zip.

#. Remove unsupported configuration from the existing ElasticSearch configuration

   - ``index.number_of_shards``
   - ``index.number_of_replicas``
   - ``discovery.zen.ping.multicast``

#. Replace or update the package installed configuration with your existing configuration if it was overwritten.

   - Set ``network.host`` or ``network.bind_ip`` and ``network.publish_ip`` accordingly to your network configuration.

#. Start ElasticSearch on each node and form a new cluster.

#. Verify you have a good cluster by executing: ``curl http://xxx.xxx.xxx.xxx:9200/_cluster/health?pretty``, check for the number of nodes and that you have a green status.

   .. NOTE:: The next steps are done on the Morpheus "master" node.

#. Upgrade Morpheus as usual by executing the package upgrade command ``dpkg -i morpheus-appliance_3.2.0-1_amd64.deb`` or ``rpm -U morpheus-appliance-3.2.0-1.el7.x86_64.rpm``, and run ``morpheus-ctl reconfigure`` to complete the upgrade process.

#. You can start Morpheus on the master node only at this point to bring up the Morpheus application by executing:    ``morpheus-ctl start morpheus-ui``.

   .. NOTE:: Make sure that Morpheus is fully started before moving on to the next step.

#. Once the application has started, a new ElasticSearch node is created with default data, to import your data from the backup execute: ``morpheus-ctl elastic-util restore http://xxx.xxx.xxx.xxx:9200 /root/es_backup``, substitute the path you used during the backup if different from above.

   .. NOTE:: The restore may take several hours depending on the amount of data to restore. You can run this while running Morpheus.

#. Move to the next Morpheus appliance and upgrade it by executing the package upgrade command ``dpkg -i morpheus-appliance_3.2.0-1_amd64.deb`` or ``rpm -U morpheus-appliance-3.2.0-1.el7.x86_64.rpm``, and run ``morpheus-ctl reconfigure`` to complete the upgrade process.

#. Start Morpheus by executing: ``morpheus-ctl start morpheus-ui``.

#. Upgrade the rest of the Morpheus appliances in your environment.
