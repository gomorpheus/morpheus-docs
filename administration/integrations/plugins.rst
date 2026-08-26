Plugins
-------

Overview
^^^^^^^^

|morpheus| is extendable with custom plugins for Task types, UI tabs, reports, approvals, cypher, and more. Plugins are added from the Plugins tab of the Integration page under Administration (|AdmIntPlu|). Simply browse for a local plugin file (.jar) to add it to the UI. Custom plugins can also be edited or deleted by clicking on the pencil or trash can icons in the corresponding row.

|morpheus| maintains a repository of internally-developed and vetted plugins at |morpheus| `Exchange <https://share.morpheusdata.com/>`_. These plugins can be downloaded and added to |morpheus| using the instructions in the prior paragraph. Alongside the download link, you can also find helpful readme information that discusses how the plugin can be used and which versions of |morpheus| it's compatible with.

Marketplace Search
^^^^^^^^^^^^^^^^^^

The Plugins page includes an integrated search interface for browsing the |morpheus| Exchange marketplace directly from the UI. Plugins listed in the marketplace are automatically filtered to show only those compatible with the current appliance version, eliminating the risk of installing incompatible plugins.

From the Plugins page, use the marketplace search to:

- Browse available plugins by name or description
- View plugin details including version, compatibility, and description
- Download compatible plugins directly for installation

.. note::

   The appliance must have outbound HTTPS access to ``share.morpheusdata.com`` (port 443). Environments with restricted outbound access must configure a proxy or allowlist this endpoint. If the marketplace is unreachable, the search returns a connection error but local plugin management remains unaffected.

With at least one plugin integrated, |morpheus| will show details on each plugin from the Plugins List View. The following information is displayed:

- **NAME:** The name given to the plugin
- **DESCRIPTION:** A description value (if any) coded into the plugin
- **FILE NAME:** The .jar filename
- **VERSION:** The plugin version number
- **STATUS:** The status of the plugin, such as "loaded" when the plugin is ready for use
- **STATUS MESSAGE:** A status message (if any) for the plugin
- **ENABLED:** If the plugin is enabled, a check mark appears here. Disabled plugins are also grayed out

Additional information about each plugin can be viewed by clicking on the pencil (edit) icon. Most of the information in this modal is read-only but you can enable or disable plugins from this pane.

Please visit the `Morpheus Developer Portal <https://developer.morpheusdata.com>`_ for Plugin Architecture SDK documentation and help getting started with custom Plugin development.

.. image:: /images/administration/plugins_new.png
