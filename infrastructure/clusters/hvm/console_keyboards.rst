Hypervisor Console Keyboards
============================

HVM VMs support guest console access as well as hypervisor console access. For each HVM VM, users can set a keyboard layout configuration which will then be set for use on each session.

.. IMPORTANT:: This feature requires |host| agent version 3.0.3 or greater. Upgrade the host agent from the host detail page for **each** host by expanding the ACTIONS menu and clicking "Upgrade Agent." Alternatively, select "Download Agent Script" to download a script to run against the host manually from a terminal session. These scripts are specific to each host so you must download a script for each host and run the correct script against the correct host.

Supported Keyboard Layouts
--------------------------

- Dutch (Belgium)
- French (Belgium)
- German
- Italian
- English (United Kingdom)
- English (United States)
- French
- Spanish
- German (Switzerland)
- Finnish
- French (Switzerland)
- Icelandic
- Norwegian
- Portuguese
- Danish

Setting the Keyboard Layout
----------------------------

#. Navigate to :menuselection:`Infrastructure --> Clusters`
#. From the list of Clusters, select the appropriate HVM Cluster
#. Click on the VMs tab
#. Click on the hyperlinked "name" value of the appropriate HVM VM
#. Click :guilabel:`EDIT`
#. Expand the Advanced Options section
#. In the KEYBOARD LAYOUT field, select the desired keyboard localization
#. Click :guilabel:`SAVE CHANGES`

Using the Configured Keyboard Layout
--------------------------------------

#. Navigate to :menuselection:`Infrastructure --> Clusters`
#. From the list of Clusters, select the appropriate HVM Cluster
#. Click on the VMs tab
#. Click on the hyperlinked "name" value of the appropriate HVM VM
#. Click on the Console tab
#. Click on the dropdown labeled :guilabel:`GUEST` and change the selection to :guilabel:`Hypervisor`
#. Click on the keyboard icon and see the keyboard layout has changed to the selected layout
