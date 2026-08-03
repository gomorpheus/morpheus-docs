Configure Network
^^^^^^^^^^^^^^^^^

The **Configure Network** menu option provides a graphical editor for the host's netplan configuration. It allows you to manage network interfaces, bonds, VLANs, and bridges without manually editing YAML files.

How It Works
````````````

- Reads the current netplan configuration and network device status
- Displays devices in a table with their type, name, addresses, and status
- Supports adding, editing, and removing network devices
- Generates and previews the resulting netplan YAML before applying

Supported Device Types
``````````````````````

The editor supports all device types defined in netplan:

- **Ethernet** — Physical network interfaces
- **Bond** — Link aggregation (active-backup, balance-rr, 802.3ad/LACP)
- **VLAN** — 802.1Q tagged interfaces
- **Bridge** — Linux bridge devices

Workflow
````````

1. Select **Configure Network** from the main menu
2. The current network devices are listed in a table
3. Use the buttons to:

   - **Add** — Create a new device definition
   - **Edit** — Modify the selected device
   - **Remove** — Delete a device definition
   - **Preview** — View the generated netplan YAML

4. When ready, select **Save** to apply changes

Applying Changes
````````````````

When you save:

1. The existing netplan YAML is backed up
2. A new configuration is written to ``/etc/netplan/60-mvm.yaml``
3. ``netplan apply`` is executed to activate the changes
4. If the network becomes unreachable, an automatic rollback restores the previous configuration

.. warning:: Network configuration changes can cause loss of connectivity. Ensure you have physical or iLO console access before modifying network settings.

Validation
``````````

- IP addresses must be in CIDR notation (e.g., ``192.168.1.10/24``)
- Device names must reference existing physical interfaces or previously defined virtual devices
