.. _helm-charts:

Helm Chart Provisioning
=======================

Overview
--------

|morpheus| provides native Helm chart provisioning support for deploying applications to Kubernetes clusters. Helm charts are provisioned through the App (Blueprint) provisioning workflow and are managed via the ``HelmProvisionService``. Helm charts allow users to define, install, and upgrade complex Kubernetes applications using templated manifests and configurable values.

.. NOTE:: Helm chart provisioning requires an active Kubernetes cluster managed by or integrated with |morpheus|. The Helm binary is managed internally by |morpheus| and does not need to be installed separately.

Prerequisites
-------------

- A Kubernetes cluster provisioned or imported in |morpheus| (see :ref:`k8s`)
- A Helm chart stored in a Git repository integration or accessible Helm repository
- Role permission ``Provisioning: Apps > Full`` for creating Helm-based Apps
- Network access from the |morpheus| appliance to the target cluster API server

Creating a Helm App Blueprint
-----------------------------

Helm charts are provisioned as App-type blueprints in |morpheus|. To create a Helm blueprint:

#. Navigate to |LibBlu| (Library > Blueprints)
#. Select :guilabel:`+ ADD`
#. Choose **Helm** as the blueprint type
#. Configure the blueprint:

   NAME
     A friendly name for the blueprint
   DESCRIPTION
     Optional description
   CATEGORY
     Optional category for organization
   SOURCE
     Select the source for the Helm chart:

     - **Repository** — Select a Git repository integration containing the chart
     - **Path** — Specify the subdirectory path within the repository to the chart root (where ``Chart.yaml`` resides)

#. Select :guilabel:`SAVE`

Provisioning a Helm App
------------------------

To provision a Helm chart as an App:

#. Navigate to ``Provisioning > Apps``
#. Select :guilabel:`+ ADD`
#. Choose the Helm blueprint
#. Select :guilabel:`NEXT`
#. Configure the App:

   APP NAME
     Name for the deployed release. This becomes the Helm release name.
   GROUP
     Select the target Group
   DEFAULT CLOUD
     Select the Cloud containing the target Kubernetes cluster
   RESOURCE POOL
     Select the Kubernetes namespace for deployment. The namespace dropdown is populated from available namespaces on the selected cluster.

#. Select :guilabel:`NEXT`
#. Configure Helm-specific options:

   TEMPLATE PARAMETERS
     Override chart values using key-value pairs. These correspond to ``values.yaml`` entries in the chart. Values are passed via ``-f`` flag to the ``helm install`` command.
   ADDITIONAL HELM ARGS
     Specify additional Helm CLI arguments to append to the install command (e.g., ``--timeout 600s``, ``--wait``, ``--atomic``).

#. Select :guilabel:`NEXT`
#. Review the configuration and select :guilabel:`COMPLETE`

|morpheus| will:

1. Clone the chart from the configured repository
2. Run ``helm template`` to preview generated manifests
3. Execute ``helm install <release-name> --namespace=<namespace> --kube-apiserver <cluster-api-url>`` with configured values
4. Create corresponding resource records in |morpheus| for deployed Kubernetes objects

Helm Values and Configuration
------------------------------

Template Parameters
^^^^^^^^^^^^^^^^^^^

Template parameters map directly to Helm chart values. When configuring an App from a Helm blueprint, |morpheus| runs ``helm inspect values`` against the chart to discover available parameters. Users can override any value by providing key-value pairs in the configuration step.

Values are written to a temporary YAML file and passed to Helm via the ``-f`` flag, ensuring proper handling of complex nested values.

Custom Values Files
^^^^^^^^^^^^^^^^^^^

For advanced use cases, custom values YAML can be provided directly. This is particularly useful during :ref:`helm-upgrades` where multiple value sources may need to be merged.

Additional Helm Arguments
^^^^^^^^^^^^^^^^^^^^^^^^^

The **Additional Helm Args** field allows passing arbitrary flags to the Helm CLI. Common uses include:

- ``--timeout 600s`` — Extend timeout for long-running deployments
- ``--wait`` — Wait for all resources to be ready
- ``--atomic`` — Roll back on failure
- ``--set key=value`` — Override individual values inline
- ``--version 1.2.3`` — Pin a specific chart version

.. WARNING:: Use caution with additional arguments. Invalid flags will cause the deployment to fail.

Managing Helm Apps
------------------

Once deployed, Helm Apps appear in ``Provisioning > Apps`` with their associated Kubernetes resources. The App detail page shows:

- All deployed Kubernetes resources (Pods, Services, Deployments, etc.)
- Current release status
- Helm release history

Actions available on deployed Helm Apps:

- **Upgrade** — Apply new values or chart versions (see :ref:`helm-upgrades`)
- **Delete** — Runs ``helm uninstall`` to remove the release and all associated resources
- **Refresh** — Sync the current state from the cluster

Helm Version Management
------------------------

|morpheus| automatically manages Helm binary versions. The system caches available Helm releases from the official GitHub repository and selects the appropriate version based on the target cluster's Kubernetes version. Multiple Helm versions can coexist, ensuring compatibility across clusters running different Kubernetes versions.

Troubleshooting
----------------

- **Chart not found:** Verify the Git repository integration is active and the path to the chart root is correct
- **Namespace errors:** Ensure the target namespace exists or that the cluster allows automatic namespace creation
- **Timeout errors:** Increase the timeout via Additional Helm Args (``--timeout``)
- **Permission denied:** Verify the cluster service account has sufficient RBAC permissions for the resources defined in the chart
- **Values not applied:** Check that template parameter keys match the chart's ``values.yaml`` structure exactly
