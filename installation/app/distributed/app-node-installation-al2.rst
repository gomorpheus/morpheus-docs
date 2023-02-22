App Node Installation
^^^^^^^^^^^^^^^^^^^^^

Requirements
````````````

When installing |morpheus| on AWS, it is best to not use a burstable instance tupe (T2/T3), as these can run out of CPU credits and then run near 20% of the normal speed.
It would be recommended to choose an M4 or M5 family, with the CPU and memory requirements needed.  The M4 and M5 are general purpose, the same as the T2/T3 but **without** bursting.

Ensure the firewall (or security group) allow |morpheus| ``outbound`` access to the various backend services:

  - Amazon Aurora Ports
    - 3306/tcp
  - Amazon OpenSearch Port
    - 443/tcp
  - Amazon MQ Ports
    - 5671/tcp
    - 443/tcp (management API)
  - Amazon EFS Port
    - 2049/tcp

Ensure the firewall (or security group) allows |morpheus| ``inbound`` from agents and users:

  - HTTPS Port
    - 443/tcp

  Example commands to run in the OS, if needed.  By default, **|morpheus| will modify the OS firewall automatically**, if the firewall is enabled.  Usually, in public clouds, the firewall is **not** enabled.

    .. tabs::

      .. group-tab:: RHEL 8/9

        .. code-block:: bash

          firewall-cmd --zone=public --add-port={443/tcp,443/tcp} --permanent
          firewall-cmd --reload
                      
      .. group-tab:: Ubuntu

          .. code-block:: bash

            ufw allow 443/tcp

Installation
````````````

#. First begin by downloading and installing the requisite |morpheus| packages to the |morpheus| nodes.

   .. note:: For offline or nodes that cannot reach |repo_host_url|, both the standard and supplemental packages will need to be transferred and then installed on the |morpheus| nodes.

   .. note:: |morpheus| packages can be found in the Downloads section of the `Morpheus Hub <https://morpheushub.com/download>`_

   .. content-tabs::

      .. tab-container:: tab1
         :title: All Nodes

         .. include:: /installation/app/morpheus-install-al2.rst

#. Do NOT run reconfigure yet. The |morpheus| configuration file must be edited prior to the initial reconfigure.

#. Next you will need to edit the |morpheus| configuration file ``/etc/morpheus/morpheus.rb`` on each node.

   .. include:: /installation/app/distributed/distributed-morpheus_rb-config-al2.rst

#. Reconfigure on all nodes

   .. content-tabs::

      .. tab-container:: tab1
         :title: All Nodes

         .. code-block:: bash

            [root@node-[1/2/3] ~] morpheus-ctl reconfigure

   |morpheus| will come up on all nodes.

#. After the reconfigure is complete, tail the morpheus-ui logs:

    .. content-tabs::

      .. tab-container:: tab1
         :title: All Nodes

         .. code-block:: bash

            [root@node-[1/2/3] ~] morpheus-ctl tail morpheus-ui