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