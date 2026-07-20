cluster
-------

Show cluster state and quorum information.

Commands
````````

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Command
     - Description
   * - ``status``
     - Display cluster status and quorum information
   * - ``nodes``
     - List cluster nodes with status and role

cluster status
``````````````

Display the current cluster status including quorum state, active nodes, and health.

.. code-block:: bash

   sudo hvmcli cluster status

.. code-block:: bash

   sudo hvmcli cluster status --json

cluster nodes
`````````````

List all nodes in the cluster with their current status and role.

.. code-block:: bash

   sudo hvmcli cluster nodes --list

Options:

- ``--list`` — Display nodes in list format
