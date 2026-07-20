logs
----

View node, cluster, and Morpheus agent logs.

Commands
````````

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Command
     - Description
   * - ``node``
     - View node syslog
   * - ``cluster``
     - View cluster/pcs logs
   * - ``morpheus-agent``
     - View Morpheus agent logs

logs node
`````````

View the node's system log (syslog).

.. code-block:: bash

   sudo hvmcli logs node

Stream logs in real-time:

.. code-block:: bash

   sudo hvmcli logs node --live

Options:

- ``--live`` — Stream logs continuously (similar to ``tail -f``)

logs cluster
````````````

View cluster-related logs (Pacemaker/Corosync).

.. code-block:: bash

   sudo hvmcli logs cluster

Stream logs in real-time:

.. code-block:: bash

   sudo hvmcli logs cluster --live

logs morpheus-agent
```````````````````

View Morpheus agent logs.

.. code-block:: bash

   sudo hvmcli logs morpheus-agent

Stream logs in real-time:

.. code-block:: bash

   sudo hvmcli logs morpheus-agent --live
