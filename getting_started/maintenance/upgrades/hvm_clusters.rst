.. _hvm-cluster-upgrades:

HVM Clusters After Manager Upgrade
----------------------------------

Upgrade the |morpheus| Manager (or HA app nodes) **first**, using the topology procedure under :doc:`/getting_started/maintenance/upgrading`. Only after the UI is on the target release should you update HVM Hosts and cluster layouts. The Manager publishes the cluster update definitions and Agent packages those steps use.

End-to-end sequence
^^^^^^^^^^^^^^^^^^^

#. **Upgrade the appliance** — Manager VM (Debian ``.deb``), single-node on your own OS, 3-Node HA, or Full HA. Start at :doc:`/getting_started/maintenance/upgrading`.
#. **Verify Manager and Host connectivity** — UI available; Hosts show recent Agent contact; Quorum ACHIEVED where applicable.
#. **Upgrade HVM Host Agents when there is no layout update** — On Manager patch/minor releases that do not ship a layout or rolling cluster update, manually run :guilabel:`Upgrade Agent` (or :guilabel:`Download Agent Script`) on **each** HVM Host so quorum, health-check, and telemetry Agent improvements take effect.
#. **Run layout or rolling cluster updates when offered** — For example layout 1.2 → 1.3, or rolling Host updates on layouts 1.3 and 2.0. Layout-driven updates upgrade the Host Agent automatically when ``minAgentVersion`` requires it.
#. **Verify the cluster** — Quorum, Corosync/DLM, datastores, and VM health using the post-upgrade checks in the detailed guide.

What lives where
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Topic
     - Location
   * - Manager / app-node package upgrade
     - :doc:`/getting_started/maintenance/upgrading` and the topology pages linked from there
   * - HVM layout 1.2 → 1.3, rolling updates, failure/rollback, checklists
     - :doc:`/infrastructure/clusters/hvm/upgrading`
   * - Host maintenance mode (used during rolling updates)
     - :doc:`/infrastructure/clusters/hvm/host_maintenance`
   * - Layout vs HVM OS vs Manager version policy
     - :doc:`/release_notes/lifecycle`

.. important::

   A layout upgrade and an HVM OS update are separate operations. Layout 1.3 uses HVM OS/Ubuntu 24.04; layout 2.0 uses HVM OS 26.04. Do not change layout or HVM OS outside a documented product workflow. Rolling cluster updates run layout-supplied scripts; they are not approval for an arbitrary base-OS release upgrade on the Host.

Continue to the full HVM procedures
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For layout transition details, rolling update behavior, Agent automation during updates, and pre/post checklists, see:

:doc:`/infrastructure/clusters/hvm/upgrading`
