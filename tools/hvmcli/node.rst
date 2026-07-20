node
----

Manage the physical HVM host node configuration.

Commands
````````

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Command
     - Description
   * - ``list``
     - List node hardware, OS, and configuration summary
   * - ``show-config``
     - Show current NTP, DNS, and proxy configuration
   * - ``configure``
     - Configure node settings (NTP, DNS, hostname, proxy, locale, keymap, timezone, log-forwarding)
   * - ``list-locales``
     - List available system locales
   * - ``list-keymaps``
     - List available console keymaps
   * - ``list-timezones``
     - List available timezones
   * - ``backup``
     - Backup node configuration
   * - ``restore``
     - Restore node configuration from backup
   * - ``reboot``
     - Reboot the node
   * - ``shutdown``
     - Shut down the node
   * - ``events``
     - Query recent system journal events

node list
`````````

Display a summary of the node's hardware, operating system, and basic configuration.

.. code-block:: bash

   sudo hvmcli node list

.. code-block:: text

   Hostname            Vendor    Model  Serial        CPUs  CPU Model                       CPU MHz   Memory(GB)  OS                  Kernel             Uptime
   ------------------  --------  -----  -----------   ----  ------------------------------  --------  ----------  ------------------  -----------------  ------------------------
   hvm-node-01         HPE       DL360  MXQ123456     64    AMD EPYC 9334 32-Core           2695 MHz  512.0 GB    Ubuntu 24.04.4 LTS  6.8.0-134-generic  up 5 days, 12 hours

node show-config
````````````````

Display the current NTP, DNS, proxy, and search domain configuration.

.. code-block:: bash

   sudo hvmcli node show-config

.. code-block:: text

     NTP Servers         time.google.com, ntp.ubuntu.com
     DNS Servers         10.227.1.91, 10.227.1.92
     DNS Search Domains  example.com
     HTTP Proxy          -

node configure
``````````````

Configure various node settings. Each setting is specified with its own flag.

**NTP Configuration:**

.. code-block:: bash

   sudo hvmcli node configure --ntp "time.google.com,ntp.ubuntu.com"

**DNS Configuration:**

.. code-block:: bash

   sudo hvmcli node configure --dns "10.0.0.1,10.0.0.2" --dns-search "example.com"

**Hostname:**

.. code-block:: bash

   sudo hvmcli node configure --hostname hvm-node-01

**HTTP Proxy:**

.. code-block:: bash

   sudo hvmcli node configure --proxy "http://proxy.example.com:8080" --no-proxy "localhost,127.0.0.1"

**Locale, Keymap, and Timezone:**

.. code-block:: bash

   sudo hvmcli node configure --locale en_US.UTF-8
   sudo hvmcli node configure --keymap us
   sudo hvmcli node configure --timezone America/New_York

**Log Forwarding:**

.. code-block:: bash

   sudo hvmcli node configure --log-forwarding "syslog://logserver.example.com:514"

node list-locales
`````````````````

List all available system locales.

.. code-block:: bash

   sudo hvmcli node list-locales

node list-keymaps
`````````````````

List all available console keymaps.

.. code-block:: bash

   sudo hvmcli node list-keymaps

node list-timezones
```````````````````

List all available timezones.

.. code-block:: bash

   sudo hvmcli node list-timezones

node backup
```````````

Create a backup of the node's current configuration.

.. code-block:: bash

   sudo hvmcli node backup

node restore
````````````

Restore node configuration from a previously created backup.

.. code-block:: bash

   sudo hvmcli node restore

node reboot
```````````

Reboot the node.

.. code-block:: bash

   sudo hvmcli node reboot

.. warning:: This will restart the host and all running VMs will be interrupted. Ensure VMs are properly shut down or migrated before rebooting.

node shutdown
`````````````

Shut down the node.

.. code-block:: bash

   sudo hvmcli node shutdown

.. warning:: This will power off the host. All running VMs will be forcefully stopped.

node events
```````````

Query recent system journal events.

.. code-block:: bash

   sudo hvmcli node events
