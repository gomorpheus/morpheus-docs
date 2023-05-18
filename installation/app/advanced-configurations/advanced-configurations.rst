Advanced Configurations
=======================

Introduction
^^^^^^^^^^^^

    All of these configurations are altering the normal installation of |morpheus|.  Some customers have requirements from an installation or security perspective, which
    we may be asked to follow in the installation.  However, note that changing these items could affect future predictability with upgrades, causing issues.  Any issues
    that arise would be out of scope of support, unless they are configured to the recommended default settings.

    .. important:: Be sure to share the warning with the customers looking to make any such changes


Create Symbolic link (symlink) for |morpheus| Installations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    A customer may wish to install |morpheus| to a different mount point, which may be a different disk presented to the OS.  Generally, this is to ensure the data does not
    fill up the OS drive, then crashing the system.  Below is a process to create symlinks for |morpheus|, assuming a 3-Node-HA embedded configuration

    .. note:: ``/etc/morpheus/`` is not included in this list.  When symlink'd, SELinux (RHEL/CentOS) has issues with the firewall settings that are applied.  Either the firewall configuration can be disabled in the ``/etc/morpheus/morpheus.rb`` file and done manually, or SELiniux must be disabled/permissive.

    #. **(Optional)** Create the directories the symlinks will be pointed to.  Customers will usually already have this in place, so this may not be required:

        .. code-block:: bash

            mkdir /apps/opt/morpheus/ -p
            mkdir /apps/tmp/morpheus/ -p
            mkdir /logs/var/log/morpheus/ -p
            mkdir /apps/var/opt/morpheus/ -p
        
    #. Create the symlinks from the Morpheus locations to the customer preferred mount points:
        
        .. code-block:: bash
    
            ln -s /apps/opt/morpheus/ /opt/morpheus
            ln -s /apps/tmp/morpheus/ /tmp/morpheus
            ln -s /logs/var/log/morpheus/ /var/log/morpheus
            ln -s /apps/var/opt/morpheus/ /var/opt/morpheus

    #. RabbitMQ does not like symlinks, their script tend to fail.  The ``morpheus.rb`` file must be altered as well, to ensure functionality.  Ensure the following lines are included, modifing the targetpaths as needed:

        .. code-block:: ruby

            rabbitmq['home'] = '/apps/opt/morpheus/embedded/rabbitmq'
            rabbitmq['schema_dir'] = '/apps/opt/morpheus/embedded/rabbitmq/priv/schema'

    Additional information:

        https://docs.morpheusdata.com/en/latest/getting_started/additional/morpheusRb.html

        https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/

        https://www.tecmint.com/disable-selinux-in-centos-rhel-fedora/

Convert 3-node Elasticsearch from Non-Secure to Secure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    This section assumes that a previous deployment has been completed, which did not specify ``elasticsearch['secure_mode'] = true`` in the ``/etc/morpheus/morpheus.rb`` file.  It is possible to create three new nodes
    that are configured to be secure and replace the non-secure nodes.  This section will assume that the original appliances will want to be kept, instead of being replaced.

    For more info on creating secure 3-node appliances during the initial installation, see the following page:
    :ref:`3nodeinstall-rhel8-secure`

    #. Begin by backing up the Chef recipe that configures Elasticsearch on reconfigure
    
        .. content-tabs::

            .. tab-container:: tab1
                :title: All Nodes

                .. code-block:: bash

                    cp /opt/morpheus/embedded/cookbooks/morpheus-solo/recipes/elasticsearch.rb /opt/morpheus/embedded/cookbooks/morpheus-solo/recipes/elasticsearch.rb.bak

    #. Edit the original Chef recipe

        .. content-tabs::

            .. tab-container:: tab1
                :title: All Nodes

                .. code-block:: bash

                    vim /opt/morpheus/embedded/cookbooks/morpheus-solo/recipes/elasticsearch.rb

        #. In the recipe, locate the following ``execute`` blocks:

            * execute 'update elastic user password'
            * execute 'create morpheus role'
            * execute 'create morpheus user'

        #. Once located, delete the entire block of each one.  Alternatively, they can be commented out, whichever is easiest.
        #. Once the three blocks are removed, this will only leave the following ``execute`` block in the parent block

            * execute 'remove keystore.seed in elasticsearch keystore'

        #. Save the file and close it
    
    #. Create the directory structure and generate the needed Certificate Authority (CA) certificate
   
        .. note::
            The UID/GID ``896`` is used for the ``es-morpheus`` user, which will be configured in the configuration file example.
            If the UID/GID will be different, be sure to change it in the example below.

        .. note::
            The version of Elasticsearch included may be different, which may change the directory ``elasticsearch-7.17.5`` to a different path,
            be sure to modify the command as needed.

        .. content-tabs::

            .. tab-container:: tab1
                :title: Node 1

                .. code-block:: bash

                    mkdir /var/opt/morpheus/certs/ -p
                    export ES_JAVA_HOME=/opt/morpheus/embedded/java/jdk
                    /opt/morpheus/embedded/elasticsearch-7.17.5/bin/elasticsearch-certutil ca --out /var/opt/morpheus/certs/elastic-stack-ca.p12
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

        .. note::
            The UID/GID ``896`` is used for the ``es-morpheus`` user, which will be configured in the configuration file example.
            If the UID/GID will be different, be sure to change it in the example below.

        .. content-tabs::

            .. tab-container:: tab1
                :title: Node 2

                .. code-block:: bash

                    mkdir /var/opt/morpheus/certs/ -p
                    cp /home/username/elastic-stack-ca.p12 /var/opt/morpheus/certs/
                    chown 896:896 /var/opt/morpheus/certs/elastic-stack-ca.p12
                    chmod u=rw,g=r /var/opt/morpheus/certs/elastic-stack-ca.p12
                    chmod -R o+x /var/opt/morpheus/certs/

            .. tab-container:: tab2
                :title: Node 3

                .. code-block:: bash

                    mkdir /var/opt/morpheus/certs/ -p
                    cp /home/username/elastic-stack-ca.p12 /var/opt/morpheus/certs/
                    chown 896:896 /var/opt/morpheus/certs/elastic-stack-ca.p12
                    chmod u=rw,g=r /var/opt/morpheus/certs/elastic-stack-ca.p12
                    chmod -R o+x /var/opt/morpheus/certs/

    #. At this point, all three nodes should have the same CA certificate file located at ``/var/opt/morpheus/certs/elastic-stack-ca.p12``

        #. This file should at least allow ``read (r)`` to the UID/GID set (the ``es-morpheus`` user once created)
        #. Be sure the parent directories have at least ``execute (x)`` for other users, which will let the ``es-morpheus`` user traverse the directoires
        #. This file is very important and the least permissions possible is the best, in case of a system compromise

    #. Using `Node 1`, display the passwords in the ``/etc/morpheus/morpheus-secrets.json``

        .. content-tabs::

            .. tab-container:: tab1
                :title: Node 1

                .. code-block:: bash

                    vim /opt/morpheus/embedded/cookbooks/morpheus-solo/recipes/elasticsearch.rb
    
        * Be sure to note the ``elastic_password`` and ``morpheus_password`` values

    #. Modify the ``/etc/morpheus/morpheus.rb`` file to add our configuration

        .. content-tabs::

            .. tab-container:: tab1
                :title: All Nodes

                .. code-block:: bash

                    vim /etc/morpheus/morpheus.rb
        
        #. Add the following to the configuration file, replacing the values as needed.  Then save and exit it.

            .. code-block:: ruby

                elasticsearch['secure_mode'] = true
                elasticsearch['use_tls'] = true
                elasticsearch['truststore_path'] = '/var/opt/morpheus/certs/elastic-stack-ca.p12'
                elasticsearch['truststore_password'] = '<<CA Password>>'
                elasticsearch['morpheus_password'] = '<<password from node 1 morpheus-secrets.json>>'
                elasticsearch['elastic_password'] = '<<password from node 1 morpheus-secrets.json>>'
        
        #. Now reconfigure |morpheus| and restart the Elasticsearch service

            .. tab-container:: tab1
                :title: All Nodes

                .. code-block:: bash

                    morpheus-ctl reconfigure
                    morpheus-ctl restart elasticsearch

        #. After the reconfigure and service restart is complete, generate a new set of passwords for the built-in users of Elasticsearch

            .. tab-container:: tab1
                :title: Node 1

                .. code-block:: bash

                    /opt/morpheus/embedded/elasticsearch/bin/elasticsearch-setup-passwords auto

            * Ignore any critical errors about certificate trust
            * Locate the ``elastic`` password that is generated, it is usually the last one listed
            * Be sure to note the password for later

        #. Verify that TLS and authentication is working

            .. tab-container:: tab1
                :title: Node 1

                .. code-block:: bash

                    curl -X GET "https://localhost:9200/_security/_authenticate" -k -u elastic:<<new elastic password>>

            * Details about the ``elastic`` user should be returned
            * If an error is returned, investigate the cause, such as a bad password or a missed step
            * Errors for the service can be seen in ``/var/log/morpheus/elasticsearch/current``

        #. Restore the original Chef recipe file that we backed up previously.  Reconfigure and restart the service once more, just for peace of mind

            .. tab-container:: tab1
                :title: All Nodes

                .. code-block:: bash

                    cp /opt/morpheus/embedded/cookbooks/morpheus-solo/recipes/elasticsearch.rb elasticsearch.rb.secure.bak
                    cp /opt/morpheus/embedded/cookbooks/morpheus-solo/recipes/elasticsearch.rb.bak /opt/morpheus/embedded/cookbooks/morpheus-solo/recipes/elasticsearch.rb
                    morpheus-ctl reconfigure
                    morpheus-ctl restart elasticsearch
        
        #. Update the temporary ``elastic`` password to match the ``elastic_password`` located on node 1's ``/etc/morpheus/morpheus-secrets.json`` file (also set in each ``/etc/morpheus/morpheus.rb`` file).  Be sure to replace the password values in the command

            .. tab-container:: tab1
                :title: Node 1

                .. code-block:: bash

                    curl \
                        -s \
                        -X POST \
                        --insecure \
                        --header "Content-Type: application/json" \
                        --user elastic:'<<temp_password>>' \
                        --data '{"password": "<<password from morpheus-secrets.json>>"}' \
                        https://localhost:9200/_security/user/elastic/_password

            * With the new password set for the ``elastic`` user, the new password will be used instead of the temporary password

        #. Create the |morpheus| role and user.  The user will be used by |morpheus| when connecting with the ``morpheus-ui`` service.  Be sure to replace the password values in the command.

            .. tab-container:: tab1
                :title: Node 1

                .. code-block:: bash

                    curl \
                        -s \
                        -X POST \
                        --insecure \
                        --header "Content-Type: application/json" \
                        --user elastic:'<<password from morpheus-secrets.json>>' \
                        --data '{
                            "cluster": [
                            "manage_index_templates",
                            "monitor"
                            ],
                            "indices": [
                                {
                                    "names": [
                                        "activities*",
                                        "azure-marketplace*",
                                        "backup_results",
                                        "check_history*",
                                        "logs*",
                                        "morpheus*",
                                        "stats*"
                                    ],
                                    "privileges": [
                                        "all"
                                    ]
                                }
                            ]
                        }' \
                        https://localhost:9200/_security/role/morpheus

                    curl \
                        -s \
                        -X POST \
                        --insecure \
                        --header "Content-Type: application/json" \
                        --user elastic:'<<password from morpheus-secrets.json>>' \
                        --data '{
                            "password" : "abb797ea7b72fff13aaebe6c",
                            "roles" : [ "morpheus" ],
                            "full_name" : "Morpheus User"
                        }' \
                        https://localhost:9200/_security/user/morpheus
        
        #. Finally, restart the ``morpheus-ui`` service on all of the nodes, to ensure that it connects using TLS and authentication correctly

            .. tab-container:: tab1
                :title: All Nodes

                .. code-block:: bash

                    morpheus-ctl restart morpheus-ui

        #. You can ``tail`` the ``morpheus-ui`` logs and note any errors as needed

            .. code-block:: bash

                    morpheus-ctl tail morpheus-ui

Pre-Create |morpheus| OS Users (deprecated)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. important:: 
        This section is being kept for reference purposes.  All HA configurations provide examples to create the users with the same
        UID/GID, to ensure there are not issues with the shared storage.  This will ensure the users are created by the installer and
        provides consistency.

    |morpheus| has a few local users that are created when installed, depeneding on the services that are embedded.  These users run the services and need to be created in a
    specific way.  The installer will normally create the users automatically but there are some cases where the users need to be pre-created.  Specifically, in a 3-node-ha or distributed
    configuration, different UIDs/GIDs could be chosen for the users and groups.  If the systems are exactly the same, this may not happen but it could if someone has created
    a user on one of the systems without your knowledge.

    If a user is created on a system without your knowledge, |morpheus| will create its users looking for then next available UIDs/GIDs.  One one node, the ``morpheus-app`` user
    could get a UID of 999 and, on a different node, the user could get a UID of 998.  The primary issue becomes that when a ``morpheus-ctl reconfigure`` is performed, the
    permissions on the shared storage (and all other |morpheus| directories) are updated.  When the shared storage permissions are updated, each node uses the UID and GID that it
    knows for that users.  This will cause the permissions to mismatch for some or all of the nodes, causing issues for uploaded images and plugins.

    Pre-creating the users ensure the UIDs/GIDs are consistent across all the nodes.

    #. Before the installation, find a range of UIDs and GIDs that all node have available.  See the UIDs and GIDs by inspecting the following files:

        .. code-block:: bash
            
            cat /etc/passwd
            cat /etc/group

    #. Next, run the following commands to create the groups, users, and associations.  Be sure to replace the UIDs and GIDs with the ones you found available:

        .. code-block:: bash

            groupadd -g 899 morpheus-app
			groupadd -g 898 morpheus-local
			groupadd -g 896 es-morpheus
			groupadd -g 895 rabbitmq-morpheus
			groupadd -g 894 guac-morpheus
			useradd -u 899 -g 899 -d /opt/morpheus -s /bin/bash morpheus-app
			useradd -u 898 -g 898 -d /opt/morpheus/.local -s /bin/bash morpheus-local
			useradd -u 896 -g 896 -d /opt/morpheus/embedded/elasticsearch -s /sbin/nologin es-morpheus
			useradd -u 895 -g 895 -d /opt/morpheus/embedded/rabbitmq -s /sbin/nologin rabbitmq-morpheus
			useradd -u 894 -g 894 -d /opt/morpheus/embedded/guac -s /sbin/nologin guac-morpheus
            usermod -G 898 morpheus-app
    
    All users will now be created.  When performing a ``morpheus-ctl reconfigure``, the users will be located based on their names.  When located, the UID and the GID found will
    be used through the reconfigure process to set all of the permissions needed.  This will keep the permissions consistent on all the nodes, including the shared storage.