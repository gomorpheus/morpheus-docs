Restarting the Morpheus Agent
==============================

In some situations, it may be necessary to restart the |morpheus| Agent on the host to re-sync communication from the Agent to the |morpheus| appliance.

Linux
-----

On the target host, run ``sudo morpheus-node-ctl restart morphd`` and the |morpheus| agent will restart. ``morpheus-node-ctl status`` will also show the agent status.

Windows
-------

The |morpheus| Windows Agent service can be restarted in Administrative Tools > Services.

.. tip:: The |morpheus| Remote Console is not dependent on Agent communication and can be used to install or restart the |morpheus| agent on an Instance.
