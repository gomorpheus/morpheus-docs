network
-------

List virtual networks and run connectivity tests.

Commands
````````

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Command
     - Description
   * - ``list``
     - List configured libvirt networks
   * - ``test``
     - Run connectivity tests for gateways, DNS, and NTP

network list
````````````

List all configured virtual networks (libvirt networks) on the host.

.. code-block:: bash

   sudo hvmcli network list

.. code-block:: text

   Name     State   Autostart  Persistent  Type   virtSwitch   Interface  Managed
   -------  ------  ---------  ----------  -----  ----------   ---------  -------
   default  active  yes        yes         other  -            -          no
   vs0      active  yes        yes         bridge virtSwitch0  vs0-br     yes

network test
````````````

Run connectivity tests to verify gateway, DNS, and NTP reachability.

.. code-block:: bash

   sudo hvmcli network test

Test specific targets:

.. code-block:: bash

   sudo hvmcli network test --target 8.8.8.8 --target time.google.com

Options:

- ``--target <host>`` — Specific host or IP to test connectivity to (can be specified multiple times)
