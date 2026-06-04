.. _helm-upgrades:

Helm Upgrade Workflow
=====================

Overview
--------

|morpheus| supports in-place upgrades of Helm-deployed applications. The upgrade workflow uses ``helm upgrade --install`` semantics, allowing users to update chart values, apply new chart versions, or modify configurations without redeploying from scratch. This is handled internally by the ``upgradeOrInstallApp`` method which ensures idempotent operations.

.. NOTE:: Helm upgrades preserve release history, enabling rollback if needed.

Upgrade Methods
---------------

|morpheus| supports several upgrade operation types:

Values Override Upgrade
^^^^^^^^^^^^^^^^^^^^^^^

Update the deployed release with new Helm ``--set`` values:

#. Navigate to ``Provisioning > Apps``
#. Select the Helm App to upgrade
#. From the ACTIONS menu, select **Upgrade**
#. Modify the **Override Values** field with new ``key=value`` pairs (comma-separated)
#. Select :guilabel:`APPLY`

Custom YAML Upgrade
^^^^^^^^^^^^^^^^^^^

Provide a complete custom ``values.yaml`` to apply:

#. Navigate to ``Provisioning > Apps``
#. Select the Helm App to upgrade
#. From the ACTIONS menu, select **Upgrade**
#. Enter or paste custom values YAML in the **Custom Values YAML** field
#. Select :guilabel:`APPLY`

Combined Upgrade
^^^^^^^^^^^^^^^^

Apply both a custom values file and individual set overrides in a single operation. When both are provided, |morpheus| auto-detects the combined operation type:

- Custom YAML values are applied first (via ``-f``)
- Individual ``--set`` values take precedence and override matching keys

This is useful for applying a base configuration file while overriding specific environment-specific values.

How Upgrades Work
-----------------

When an upgrade is triggered, |morpheus| executes the following:

1. **Resolves the chart source** — Locates the chart from the configured Git repository or cached chart path
2. **Processes namespace** — Uses the existing release namespace or the resource pool namespace as fallback
3. **Builds the Helm command** — Constructs ``helm upgrade --install <release-name>`` with:

   - ``--namespace=<namespace>``
   - ``--kube-apiserver <cluster-api-url>``
   - Values file (``-f values.yaml``) if template parameters exist
   - Custom values file (``-f custom-values.yaml``) if provided
   - ``--set`` overrides if provided
   - Any additional Helm arguments configured on the App

4. **Executes against the cluster** — Runs the command against the target cluster's API server
5. **Updates resource records** — Syncs the new state of Kubernetes resources back to |morpheus|

Upgrade vs Install Behavior
----------------------------

The ``helm upgrade --install`` flag ensures:

- If the release **exists**, it is upgraded with the new configuration
- If the release **does not exist**, it is installed fresh

This makes the operation idempotent and safe to retry on failure.

Monitoring Upgrade Status
--------------------------

After initiating an upgrade:

- Progress is tracked in the App's History tab
- Process output is available by clicking the info icon on the target process
- Logs are also available in ``Operations > Activity > History``

If an upgrade fails, the release retains its previous state (unless ``--atomic`` was specified, in which case Helm auto-rolls back).

Configuration Persistence
--------------------------

|morpheus| tracks chart configuration across upgrades:

- **Chart path** — Stored in the App config and reused on subsequent upgrades
- **Git path** — The repository path to the chart is persisted for the release
- **Release name** — Defaults to the App name and remains consistent across upgrades

Rolling Back
-------------

To roll back a failed upgrade, you can:

1. Re-run the upgrade with the previous values configuration
2. Use the ``kubectl`` command line on the Cluster Control tab to run ``helm rollback <release> <revision>``
3. Delete and re-provision the App from the original blueprint

.. TIP:: Check the release history with ``helm history <release-name>`` from the cluster Control tab to identify the target revision number for rollback.

Best Practices
--------------

- **Test with --dry-run:** Add ``--dry-run`` to Additional Helm Args during testing to preview changes without applying them
- **Use --wait:** Include ``--wait`` to ensure the upgrade only reports success after all resources are ready
- **Pin chart versions:** Specify explicit chart versions to avoid unexpected changes from upstream
- **Incremental changes:** Make small, focused value changes per upgrade rather than large configuration shifts
- **Monitor pod status:** After upgrade, verify pod health on the cluster Workloads tab
