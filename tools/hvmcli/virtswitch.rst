virtswitch
----------

Manage Virtual Switches on the HVM host. Virtual Switches abstract host-level networking (bonds, bridges, VLANs) into a simple management model.

.. danger:: Direct use of ``hvmcli virtswitch`` commands can disrupt host networking and cause loss of connectivity. It is **highly recommended** to manage Virtual Switches through the Morpheus UI (Infrastructure > Clusters > Network > Virtual Switches) instead. Only use these CLI commands when directed by HPE support or when the Morpheus UI is unavailable.

.. important:: The ``virtswitch`` namespace is only available on **HVM OS Ubuntu 26.04+** with **Cluster Layout 2.0**. On HVM OS Ubuntu 24.04, this namespace is hidden and unavailable.

Commands
````````

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Command
     - Description
   * - ``list``
     - List managed Virtual Switch configurations
   * - ``list-route``
     - List Virtual Switch routes and default route mappings
   * - ``create``
     - Create a new Virtual Switch
   * - ``import``
     - Import an existing network interface into a managed Virtual Switch
   * - ``edit``
     - Edit Virtual Switch configuration
   * - ``add-segment``
     - Add a VLAN segment to an existing Virtual Switch
   * - ``edit-segment``
     - Edit a segment or manage static routes
   * - ``delete-segment``
     - Delete a VLAN segment from a Virtual Switch
   * - ``delete``
     - Delete a Virtual Switch and its associated metadata
   * - ``rename``
     - Rename a Virtual Switch (metadata only)
   * - ``export``
     - Export Virtual Switch config as YAML or JSON
   * - ``show``
     - Show detailed Virtual Switch view
   * - ``status``
     - Show real-time operational status

virtswitch list
```````````````

List all managed Virtual Switches on the host.

.. code-block:: bash

   sudo hvmcli virtswitch list

Use ``--filter`` to show specific Virtual Switch types:

.. code-block:: bash

   sudo hvmcli virtswitch list --filter general
   sudo hvmcli virtswitch list --filter data
   sudo hvmcli virtswitch list --filter sdn

virtswitch list-route
`````````````````````

List routes and default route mappings for managed Virtual Switches.

.. code-block:: bash

   sudo hvmcli virtswitch list-route

virtswitch create
`````````````````

Create a new Virtual Switch with specified uplinks and traffic configuration.

.. code-block:: bash

   sudo hvmcli virtswitch create \
     --virtswitch-name virtSwitch0 \
     --type general \
     --uplink-name eth0 \
     --traffic-type management \
     --ip 10.0.0.10 \
     --netmask 24 \
     --gateway 10.0.0.1

**Create with bonded uplinks:**

.. code-block:: bash

   sudo hvmcli virtswitch create \
     --virtswitch-name virtSwitch0 \
     --type general \
     --uplink-name eth0,eth1 \
     --uplink-mode active-backup

Options:

- ``--virtswitch-name <name>`` — Name for the Virtual Switch (max 12 characters)
- ``--type <general|iscsi|sdn>`` — Virtual Switch type
- ``--uplink-name <nic>[,<nic>]`` — Physical NIC(s) to use as uplinks
- ``--uplink-mode <active-backup|802.3ad>`` — Bond mode when using two uplinks
- ``--traffic-type <management|vm|data-nfs|live-migration|iscsi|sdn>`` — Traffic type for the segment
- ``--ip <address>`` — IP address for the host interface
- ``--netmask <prefix>`` — Subnet mask or prefix length
- ``--gateway <address>`` — Default gateway
- ``--mtu <1500|9000>`` — MTU size
- ``--vlan-id <2-4094>`` — VLAN ID for tagged traffic

virtswitch import
`````````````````

Import an existing network interface (e.g., a pre-configured bridge) into a managed Virtual Switch.

.. code-block:: bash

   sudo hvmcli virtswitch import --interface br-mgmt

This is used during cluster creation to adopt existing management bridges without disrupting connectivity.

virtswitch edit
```````````````

Edit an existing Virtual Switch configuration.

.. code-block:: bash

   sudo hvmcli virtswitch edit --virtswitch-name virtSwitch0 --mtu 9000 --force

Options:

- ``--virtswitch-name <name>`` — Name of the Virtual Switch to edit (required)
- ``--mtu <1500|9000>`` — New MTU value
- ``--uplink-mode <active-backup|802.3ad>`` — Change bond mode
- ``--force`` — Skip confirmation prompts

virtswitch add-segment
``````````````````````

Add a VLAN segment to an existing general or iSCSI Virtual Switch.

.. code-block:: bash

   sudo hvmcli virtswitch add-segment \
     --virtswitch-name virtSwitch0 \
     --vlan-id 100 \
     --traffic-type data-nfs \
     --ip 172.16.0.10 \
     --netmask 24

Options:

- ``--virtswitch-name <name>`` — Target Virtual Switch (required)
- ``--vlan-id <2-4094>`` — VLAN ID for the segment
- ``--traffic-type <data-nfs|live-migration|iscsi|sdn>`` — Traffic type
- ``--ip <address>`` — IP address for this segment
- ``--netmask <prefix>`` — Subnet mask or prefix length
- ``--gateway <address>`` — Gateway for this segment

virtswitch edit-segment
```````````````````````

Edit a segment or manage static routes on an existing Virtual Switch.

.. code-block:: bash

   sudo hvmcli virtswitch edit-segment \
     --virtswitch-name virtSwitch0 \
     --traffic-type data-nfs \
     --ip 172.16.0.20 \
     --force

Options:

- ``--virtswitch-name <name>`` — Target Virtual Switch (required)
- ``--traffic-type <type>`` — Traffic type of the segment to edit (required)
- ``--force`` — Skip confirmation prompts

virtswitch delete-segment
`````````````````````````

Remove a VLAN segment from a Virtual Switch.

.. code-block:: bash

   sudo hvmcli virtswitch delete-segment \
     --virtswitch-name virtSwitch0 \
     --traffic-type data-nfs

Options:

- ``--virtswitch-name <name>`` — Target Virtual Switch (required)
- ``--traffic-type <type>`` — Traffic type of the segment to delete (required)

virtswitch delete
`````````````````

Delete a Virtual Switch and all associated host networking configuration.

.. code-block:: bash

   sudo hvmcli virtswitch delete --virtswitch-name virtSwitch0 --force

Options:

- ``--virtswitch-name <name>`` — Virtual Switch to delete (required)
- ``--force`` — Skip confirmation prompts

.. warning:: Deleting a Virtual Switch removes all associated bridges, bonds, and VLAN configurations from the host.

virtswitch rename
`````````````````

Rename a Virtual Switch. This only updates metadata — no network changes are applied.

.. code-block:: bash

   sudo hvmcli virtswitch rename --virtswitch-name virtSwitch0 --new-name mySwitch

Options:

- ``--virtswitch-name <name>`` — Current Virtual Switch name (required)
- ``--new-name <name>`` — New name (max 12 characters, required)

virtswitch export
`````````````````

Export a Virtual Switch configuration as YAML or JSON.

.. code-block:: bash

   sudo hvmcli virtswitch export --virtswitch-name virtSwitch0 --format json
   sudo hvmcli virtswitch export --virtswitch-name virtSwitch0 --format yaml

Options:

- ``--virtswitch-name <name>`` — Virtual Switch to export (required)
- ``--format <yaml|json>`` — Output format (default: yaml)

virtswitch show
```````````````

Show a detailed view of a Virtual Switch including segments, uplinks, and bridge information.

.. code-block:: bash

   sudo hvmcli virtswitch show --virtswitch-name virtSwitch0

virtswitch status
`````````````````

Show real-time operational status of Virtual Switches including link state and sync status.

.. code-block:: bash

   sudo hvmcli virtswitch status
   sudo hvmcli virtswitch status --virtswitch-name virtSwitch0 --json
