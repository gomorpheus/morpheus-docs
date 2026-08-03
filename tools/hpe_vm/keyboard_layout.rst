Keyboard Layout / TimeZone
^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Keyboard Layout / TimeZone** menu option configures the host's locale, virtual console keymap, and timezone.

Settings
````````

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Setting
     - Description
   * - **Locale**
     - System locale (e.g., ``en_US.UTF-8``, ``fr_FR.UTF-8``)
   * - **VC Keymap**
     - Virtual console keyboard layout (e.g., ``us``, ``fr``, ``de``)
   * - **Timezone**
     - System timezone (e.g., ``America/New_York``, ``Europe/Paris``)

How It Works
````````````

- Current settings are read from ``localectl status`` and ``timedatectl``
- Changes are applied immediately using:

  - ``localectl set-locale`` — for locale
  - ``localectl set-keymap`` — for keyboard layout
  - ``timedatectl set-timezone`` — for timezone

- If keyboard maps are not installed on the system, ``hpe-vm`` offers to download and install the KBD keymaps package

.. note:: Keyboard layout changes affect the local console immediately. SSH sessions use the client's keyboard settings and are not affected.
