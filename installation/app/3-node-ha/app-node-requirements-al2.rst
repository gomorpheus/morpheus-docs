AL2 will have an issue with Elasticsearch starting its service during the reconfigure, it will sit at "wait".  Perform the following commands, which can also be found in the :ref:`app-troubleshooting` documentation.
If inspecting the Elasticsearch logs, you may see the following error:  ``max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]``

  .. code-block:: bash

    sysctl -w vm.max_map_count=262144
    echo 'vm.max_map_count = 262144' | sudo tee -a /etc/sysctl.conf

When installing |morpheus| on AWS, it is best to **not** use a burstable instance type (T2/T3), as these can run out of CPU credits and then run near 20% of the normal speed.
It would be recommended to choose an M4 or M5 family, with the CPU and memory requirements needed.  The M4 and M5 are general purpose, the same as the T2/T3 but **without** bursting.