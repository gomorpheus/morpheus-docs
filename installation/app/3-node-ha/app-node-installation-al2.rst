App Node Installation
^^^^^^^^^^^^^^^^^^^^^

.. include:: /installation/app/3-node-ha/app-node-requirements-generic.rst

.. include:: /installation/app/3-node-ha/app-node-requirements-al2.rst

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

   .. include:: /installation/app/3-node-ha/3-node-ha-morpheus_rb-config-al2.rst

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