.. _upgrading:

Upgrading
---------

This is the starting point for upgrading |morpheus|. Pick your Manager topology, complete the appliance package upgrade, then finish any HVM Host Agent or cluster layout steps that apply.

.. tip:: For HVM deployments, see the :doc:`/getting_started/guides/hvm_upgrade_guide` for a cohesive end-to-end upgrade sequence covering Manager, cluster, and agent upgrades in the correct order.

.. important::

   Always back up the appliance database before upgrading. Confirm free space for new node and VM node packages (|morphver| needs about 3.5 GB under the package repo). After package install and before ``morpheus-ctl reconfigure``, you may reclaim space with::

      sudo rm -Rf /var/opt/morpheus/package-repos/*

   Application upgrades do not replace Ubuntu base-OS maintenance on the HPE Morpheus Manager QCOW2 image. See :doc:`manager_os_updates`.

.. toctree::
   :maxdepth: 2
   :caption: Upgrade procedures

   upgrades/overview.rst
   upgrades/single/singlenode.rst
   upgrades/3node/overview.rst
   upgrades/fullha/overview.rst
   upgrades/hvm_clusters.rst

Choose your path
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 28 42 30
   :header-rows: 1

   * - Deployment
     - What to follow
     - Typical package
   * - **Manager VM / AIO** (HPE Morpheus Manager QCOW2 or single appliance)
     - :ref:`singleUpgrade` — Debian/Ubuntu section first
     - ``.deb`` on the Manager VM
   * - **Single-node on your own guest OS**
     - :ref:`singleUpgrade` — Debian **or** RPM section for that OS
     - ``.deb`` or ``.rpm``
   * - **3-Node HA** (rolling across app nodes)
     - :doc:`upgrades/3node/overview`
     - ``.deb`` or ``.rpm`` per app node
   * - **Full HA** (external MySQL, RabbitMQ, search)
     - :doc:`upgrades/fullha/overview`
     - ``.deb`` or ``.rpm`` on app nodes only
   * - **HVM clusters** (after the Manager is upgraded)
     - :doc:`upgrades/hvm_clusters`
     - Layout/rolling update + Host Agent as needed

Recommended order
^^^^^^^^^^^^^^^^^

#. **Identify the topology** from the table above and open that procedure.
#. **Upgrade every Manager / app node** with the release package, then ``morpheus-ctl reconfigure``. For HA, use the rolling or coordinated sequence in the 3-Node or Full HA guide.
#. **Confirm the UI is healthy** — Refresh your browser and wait for the loading screen to finish. Only if the UI does not load or stalls, run ``morpheus-ctl tail morpheus-ui``.
#. **If you run HVM**, complete Host Agent and layout/rolling updates as described in :doc:`upgrades/hvm_clusters`.
#. **Optionally** apply Manager base-OS updates (:doc:`manager_os_updates`) in a separate maintenance window from the application package upgrade.

Packages and compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^^

Release packages are available from My HPE Software Center (and historically from Morpheus Hub package URLs). Minimum upgrade versions, rolling-upgrade eligibility, and component notes are in :doc:`/release_notes/compatibility` and the current release notes. High-level package and backup requirements are summarized in :doc:`upgrades/overview`.

After the Manager upgrade: Agents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do not treat a generic UI Agent notification as a requirement to upgrade every Agent type. Update only the Agents called out by the release or by a documented workflow.

**HVM Host Agents:** After Manager patch and minor releases that do **not** include an HVM layout update, manually upgrade Host Agents so Hosts receive quorum, health-check, and telemetry improvements. Use :guilabel:`Upgrade Agent` (or :guilabel:`Download Agent Script`) on each Host detail page. Details: :doc:`upgrades/hvm_clusters`.

**Layout-driven exception:** The HVM layout 1.2 → 1.3 cluster update requires Host Agent 3.2.7 or later and upgrades an older Host Agent automatically before layout scripts run. That minimum applies to that layout transition only; it is not a general requirement for every Manager upgrade. See :doc:`/infrastructure/clusters/hvm/upgrading`.

If the UI requests an Agent update but the component and required version are not identified by a release-specific workflow, preserve the notification and contact HPE Support rather than updating unrelated Agents.

Related maintenance
^^^^^^^^^^^^^^^^^^^

- :doc:`manager_os_updates` — Ubuntu base OS on the Manager image (separate from the ``morpheus-appliance`` package)
- :doc:`opensearch_migration` — Embedded search migration for appliances moving from Elasticsearch to OpenSearch (8.1.0+)
- :doc:`morpheus-ctl` — Service control during and after upgrades
- :doc:`db_migration` — Database migration topics when your topology requires them
