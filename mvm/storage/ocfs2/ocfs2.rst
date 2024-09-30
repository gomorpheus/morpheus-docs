.. _ocfs2:

OCFS2
-----

Overview
^^^^^^^^

This document will illustrate how to connect an existing iSCSI target to the |mvm| hosts and utilize it with OCFS2.
Preparing the iSCSI targets are out-of-scope of this document but attaching them and creating a file system to support
|mvm| will be include, as well as the creation of the storage objects in |mvm| to deploy instance to.

The below example does not use CHAP authentication.  The steps will vary if this is required.

Prerequisites
^^^^^^^^^^^^^

* Create iSCSI targets to be used by the initiators on the |mvm| hosts
* Ensure network connectivity and firewall rules allow for the |mvm| hosts to access the iSCSI target/server

Connect iSCSI Target(s)
^^^^^^^^^^^^^^^^^^^^^^^

.. important::
  All commands in this section should be run on all nodes.  The iSCSI disks need to be mounted to each |mvm| node to be
  utilized successfully.

* Verify each |mvm| node has a unique initiator name by viewing/editing ``/etc/iscsi/initiatorname.iscsi``
  
  * Example of ``host1`` and ``host2``, these no not need to match the hostnames but it may be less confusing:

    ``iqn.2004-10.com.ubuntu:01:host1``

    ``iqn.2004-10.com.ubuntu:01:host2``

* Discover the available targets from the iSCSI target/server:

  ``iscsiadm -m discovery -t st -p <ip address>``

* Set automatic login for the target that you intend to connect, replacing ``<target iqn>`` and ``<ip address>``
  with the appropriate values.  This will ensure the iSCSI connections are reconnected after a host restart:

  ``iscsiadm -m node -T <target iqn> -p <ip address> --op=update -n node.conn[0].startup -v automatic``

  ``iscsiadm -m node -T <target iqn> -p <ip address> --op=update -n node.startup -v automatic``

  .. note::
    These values can be verified by navigating to ``/etc/iscsi/nodes/``, which is where the database of connections
    are stored.
  
* Login to the specific target:

  ``iscsiadm -m node -T <target iqn> -p <ip address> -l`` 

* Verify the device name (``/dev/sd*``) for the newly added disk with the ``Disk model`` of ``iSCSI Disk``: 

  ``fdisk -l``

  .. note::
    Alternatively, the following command can be used as well, which will list recent disk operations and grab the device name:
    ``dmesg | grep -oP 'sd[a-z]+\b' | tail -1``

Install and Initialize OCFS2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::
  With the exception of creating the file system (noted below), all of the commands should be run on all nodes.

* Install OCFS2 packages
  
  ``apt install ocfs2-tools ocfs2-tools-dev -y``

* (**RUN ON ONE NODE ONLY**) Create the OCFS2 file system on the disks added previously, replacing ``<device>`` with
  the device name (``/dev/sd*``) noted above for the iSCSI disk:

  ``mkfs.ocfs2 -b 4K -C 4K -J size=4M -N 4 -L ocfs2vol1 --cluster-name=ocfs2 --cluster-stack=o2cb --global-heartbeat <device>``

  .. important::
    The ``--cluster-name`` should match the value that will be found in ``/etc/default/o2cb`` (edited later) and the ``o2cb`` commands
    set to configure the cluster below.  Just make sure the cluster name is consistent with all commands and locations.

* After the file system is created, obtain the UUID for the file system by running the below command and replacing ``<device>``,
  which will be used for the heartbeat region below:
  
  ``mounted.ocfs2 -d | grep <device> | awk '{print $5}'``

* Run the following commands on each node:
  
  .. ::note::
    Alternatively, they can be ran on one node but make sure to copy ``/etc/ocfs2/cluster.conf`` from that node to all others

  .. important::
    If the ``--cluseter-name`` was not kept to the default of ``ocfs2`` when creating the file system, be sure to use the correct
    cluster name in these commands.

  .. ::important::
    The hostnames used in the ``o2cb add-node`` commands **MUST** match the hostnames of the |mvm| nodes when checking ``hostname``

  .. code-block:: bash
  
    o2cb add-cluster ocfs2
    o2cb add-node ocfs2 <hostname1> --ip <ip>
    o2cb add-node ocfs2  <hostname2> --ip <ip>
    o2cb add-heartbeat ocfs2 <region>
    o2cb heartbeat-mode ocfs2 global

* Edit the ``/etc/default/o2cb`` to ensure the the OCFS2 cluster will start automatically after a host restart:
  
  ``sed -i 's/O2CB_ENABLED=false/O2CB_ENABLED=true/' /etc/default/o2cb``

  .. important::
    If the ``--cluseter-name`` was not kept to the default of ``ocfs2`` when creating the file system, the ``O2CB_BOOTCLUSTER``
    will need to be updated to the correct value as well.

* Reload the settings just modified:
  
  ``DEBIAN_FRONTEND=noninteractive dpkg-reconfigure ocfs2-tools``

* Ensure the OCFS2 services are set to start after a restart:
  
  .. code-block:: bash
    
    systemctl enable o2cb
    systemctl enable ocfs2

* Start the cluster:
  
  ``service o2cb enable``

* Ensure the services are started and check the status:

  .. code-block:: bash

    service o2cb start
	  service ocfs2 start
    service o2cb status

* Optional but recommended values to set for OCFS2:
  
  .. code-block:: bash

    sysctl kernel.panic=30
    sysctl kernel.panic_on_oops=1

  * To keep the above settings persistent, also run the following:

    .. code-block:: bash
      
      echo "kernel.panic=30" >> /etc/sysctl.conf
      echo "kernel.panic_on_oops=1" >> /etc/sysctl.conf

Add OCFS2 as a Datastore
^^^^^^^^^^^^^^^^^^^^^^^^

* Login to your |morpheus| appliance
* Navigate to your |morpheus| Cloud that contains your |mvm| Cluster
* Click the |mvm| Cluster hyperlink
* Click the ``Storage`` tab on the cluster
* Click the ``ADD`` button
* Enter a ``Name`` for the datastore
* Choose ``OCFS2`` for the ``Type``
* Enter the device name (``/dev/sd*``) into the ``Block Device``
* Click ``SAVE``
* The datastore should show ``ONLINE`` of ``Yes`

Optional/Additional
^^^^^^^^^^^^^^^^^^^

Mounting the File System
````````````````````````

It is not necessary to mount the file system for |mvm| to use it.  However, to do troubleshooting, you may want to mount the disk to a know location.
It is important to note that a mount is created automatically by |mvm| when a datastore is added, which will be located under `/mnt/`

* Create a directory to mount the file system to:

  ``mkdir /ocfs2``

* Edit ``/etc/fstab`` and add the following, while replacing ``<device>`` below:
  
  ``/dev/<device> /ocfs2 ocfs2     _netdev,defaults   0 0

* Mount the file system using the following command, which will use ``/etc/fstab``:
  
  ``mount -a``

* Unmounting can be performed using the following:

  ``umount /ocfs2``

Cleanup OCFS2
`````````````

* Delete the datastore in |morpheus| from ``Infrastructure > Clusters > your cluster > Storage``
* Disable the cluster on each host:

  ``service o2cb disable``

.. warning::
  This next command is destructive, it will wipe your file system, only perform it if you are positive you wish to clear it

* (**DESTRUCTIVE**) Clear the file system using the following:
  
  * Check if the file system is the one you expect, this is not descructive as long as you do not use ``-a`` in the command:

    ``wipefs <device>``
  
  * Once you are satisifed with the disk you wish to **ERASE**, run the following from just one node:
  
    ``wipefs -a <device>``

Remove iSCSI Targets
````````````````````

* Locate any open session:

  ``iscsiadm -m session``

* Logout of any targets:

  ``iscsiadm -m node -T <target iqn> -p <ip address> -u``

* Delete the discovery entry, so login is not possible accidentlly:

  ``iscsiadm -m node -o delete -T <target iqn>``