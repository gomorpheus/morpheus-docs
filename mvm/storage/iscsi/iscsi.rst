.. _iscsi:

iSCSI
-----

Overview
^^^^^^^^

This document will provide commands an example for connecting an iSCSI initiator (clinet) to an iSCSI target (Server) on
an |mvm| host.  Untimately, it is up to the customer to connect their iSCSI devices to |morpheus| but this will help us help
them, in cases where there are issues and assistance is needed.

The below example does not use CHAP authentication.  The steps will vary if this is required.

Scripts with more advanced setups can be found here:

:ref:`iscsi_scripts`

Prerequisites
^^^^^^^^^^^^^

* Create iSCSI targets on a NAS/SAN/server (referred to as NAS from now on) to be used by the initiators on the |mvm| hosts
* Ensure network connectivity and firewall rules allow for the |mvm| hosts to access the iSCSI target/server

Connect iSCSI Target(s)
^^^^^^^^^^^^^^^^^^^^^^^

Overview
````````

There are a few steps to connecting an iSCSI initiator to a target.  In addition, there are different syntax to the commands,
which can connect just a single target from a server, multiple targets from a server, or the same (or multiple) targets from
different network adapters on the NAS to provide multipathing.

(Optional) Using Multipathing
`````````````````````````````

Multipathing allows your iSCSI attached block devices to use multiple paths to the targets, if the NAS has multiple NICs that
provide the target you wish to connect to.  More details of the process will be covered below.  However, if multipathing will
be utilized in |mvm|, it is recommended to update ``/etc/multipath.conf`` to disable ``user_friendly_names``

Example of the default:

    .. code-block:: bash
        defaults {
            user_friendly_names yes
        }

Update to be:

    .. code-block:: bash
        defaults {
            user_friendly_names no
        }

With this change, the disks added to the system will no longer be in the format of ``/dev/mapper/mpathX`` (X being a letter
such as "a", "b", etc.) but instead will be in the format of ``/dev/mapper/wwid`` (wwid being the World Wide Identifier), which
will be supplied from the NAS that contains the target.

Examples:

  ``/dev/mapper/mpatha`` vs ``/dev/mapper/36589cfc000000ce2c577a0a2e8ac7ac9``

Disabling ``user_friendly_names`` will ensure the device names are consistent accross the |mvm| hosts, where the previous method
could assign different device names across the hosts and cause issues when creating storage in |morpheus|

Ensure the Initiator is Unique
``````````````````````````````

Each server/vm that is created, that has the ``iscsid`` server installer/running will have an initiator name.  If the system was
cloned for an existing system/template, it may have the same as another system deployed.  It is important to ensure that the 
initiator names are unique on all the clients that will connected to the NAS that has targets.

* Verify or edit ``/etc/iscsi/initiatorname.iscsi``
* Example of what the initiator name may look like for Ubuntu:
  
  .. code-block:: bash
    InitiatorName=iqn.2004-10.com.ubuntu:01:c6b852bc3730

* The above is an iSCSI Qualified Name (IQN), which has the format of:

  ``iqn.yyyy-mm.naming-authority:unique name``

* The important thing is that the IQN is unique on each |mvm| host, less the various components.  In this example, changing
  ``c6b852bc3730`` to a unique value would be sufficient.  For example:

  * Host1 ``/etc/iscsi/initiatorname.iscsi``:
  
    .. code-block:: bash
        InitiatorName=iqn.2004-10.com.ubuntu:01:host1

  * Host2 ``/etc/iscsi/initiatorname.iscsi``:
    .. code-block:: bash
        InitiatorName=iqn.2004-10.com.ubuntu:01:host2

  * Other values separated by the colon (:) can be modified as well if needed, just depends on the complexity needed to ensure
    duplicate IQNs are not used in an environment connecting to an iSCSI NAS.

  * Additional information for IQN format:

    [https://blogs.virtualmaestro.in/2016/02/09/iscsi-naming-convention/](https://blogs.virtualmaestro.in/2016/02/09/iscsi-naming-convention/)

* Once the IQN has been configured to be unique, restart the ``iscsid`` service for it to take effect:

    .. code-block:: bash
        systemctl enable iscsid
        systemctl restart iscsid

Discover Targets
````````````````

Once the initiator IQNs are unique, it is time to locate targets from the NAS.  In these examples, it assumes that a portal or
[iSNS](https://docs.netapp.com/us-en/ontap/san-admin/isns-concept.html#what-an-isns-server-does) is available/created on the NAS, which will
help list the targets it is presenting.

* Discover targets using the following format:  ``iscsiadm -m discovery -t st -p ipOrHostname``
  * Example:

    .. code-block:: bash
        iscsiadm -m discovery -t st -p myname.example.local

  * The command will list the IP addresses and targets available on those IPs
  * The target may be listed multiple times if it is associated with multiple IP addresses, allowing for multipathing to be used
* (Optional) Once the targets have been discovered, you may want them to start automatically, once you have connected them (below).  If so,
  run the following commands.  Replace ``<targetIqn>`` and ``<ipAddress>`` accordingly:

  .. code-block:: bash
    iscsiadm -m node -T <targetIqn> -p <ipAddress> --op=update -n node.conn[0].startup -v automatic
    iscsiadm -m node -T <targetIqn> -p <ipAddress> --op=update -n node.startup -v automatic

  * Alternatively, if the same target is returned with multiple IP address and you want to apply to all more easily, run the following:
    
    .. code-block:: bash
        iscsiadm -m node -T <targetIqn> --op=update -n node.conn[0].startup -v automatic
        iscsiadm -m node -T <targetIqn> --op=update -n node.startup -v automatic

  * These settings, and others, can be confirmed in the following location, where the settings for discovered targets are stored:
    
    ``/etc/iscsi/nodes/``

Login to Targets
````````````````

* Once the targets are discovered, use the following to login to them.  Replace ``<targetIqn>`` and ``<ipAddress>`` accordingly:

  .. code-block:: bash
   	iscsiadm -m node -T <targetIqn> -p <ipAddress> -l

  * Alternatively, if the same target is returned with multiple IP address and you want to login to all more easily, run the following:

    .. code-block:: bash
        iscsiadm -m node -T <targetIqn> -l

  * Another alternernative, if you wish to login all connctions set to automatic (if performed above), the following can be used:

    .. code-block:: bash
        iscsiadm -m node --loginall=automatic

* If successful the device name (for example ``/dev/sdc``) can be located using the following command.  Looks for ``Disk model: iSCSI Disk``
  to idenfity the disks:

  .. code-block:: bash
    fdisk -l

* At this point, using GFS2 as an example, a datastore can be added using this disk

Cleanup iSCSI Target(s)
^^^^^^^^^^^^^^^^^^^^^^^

Once all storage devices have been deleted in |morpheus| for the |mvm| hosts, you can cleanup the iSCSI connections as needed.

* Find sessions currently established on the hosts, which will display the targets and IPs of currently logged in connections:

  .. code-block:: bash
    iscsiadm -m session

  * Alternatively, if you need to see non-logged in sessions, use the following:

    .. code-block::
        iscsiadm -m session -o show

* Logout of the session(s).  Replace ``<targetIqn>`` and ``<ipAddress>`` as needed:
  * Logout of a specific target on specific IP:

    .. code-block:: bash
        iscsiadm -m node -T <targetIqn> -p <ipAddress> -u

  * Logout of a specific target on **ALL** IPs:

    .. code-block:: bash
        iscsiadm -m node -T <targetIqn> -u

  * Logout of **ALL** Targets:

    .. code-block:: bash
        iscsiadm -m node -u

* To ensure not reconnection and fully deleting any entry of the iSCSI target, delete the discovered targets:

  .. code-block::
    iscsiadm -m node -o delete -T <targetIqn>