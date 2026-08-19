iLO Information
^^^^^^^^^^^^^^^

The **iLO** menu option displays HPE Integrated Lights-Out (iLO) hardware and network information. This option is only available on HPE servers with ``ilorest`` installed.

.. note:: This menu item is hidden on non-HPE hardware or when the ``ilorest`` utility is not detected.

Displayed Information
`````````````````````

The iLO screen queries the local Redfish interface via ``ilorest`` and displays:

**Network:**

- IPv4 address, subnet mask, and gateway
- IPv6 address (if configured)
- MAC address

**Hardware:**

- Server model
- CPU count and model
- Total memory
- BIOS version
- Serial number

Data Collection
```````````````

When you open the iLO screen, ``hpe-vm`` runs ``ilorest`` to query the system and ethernet Redfish endpoints. Results are cached in ``/var/morpheus/ilo/`` for the duration of the session. A progress dialog is shown while data is being collected.
