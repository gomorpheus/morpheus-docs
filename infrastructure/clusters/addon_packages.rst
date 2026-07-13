Addon Packages
==============

Overview
^^^^^^^^

Addon Packages extend the functionality of |morpheus| clusters by installing additional software components, services, or capabilities on cluster nodes. Packages are available for MVM (Morpheus Virtual Machine) clusters and provide a plugin-based mechanism to add features such as storage drivers, network plugins, monitoring agents, and other operational tools.

Addon Packages are managed at the cluster level and can be installed, configured, upgraded, and removed.

Role Requirements
^^^^^^^^^^^^^^^^^

- ``Infrastructure: Clusters`` role permission at **Full** level is required to install, update, upgrade, or remove addon packages.
- ``Infrastructure: Clusters`` role permission at **Read** level allows viewing installed packages only.

Viewing Installed Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Clusters``
#. Click the name of a Cluster
#. Select the **PACKAGES** tab

The Packages tab displays all installed addon packages with:

- **Name** — Package name
- **Description** — Package description
- **Version** — Currently installed version
- **Status** — Package status (installed, installing, error)
- **Upgradeable** — Indicates if a newer version is available

Installing an Addon Package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Clusters``
#. Click the name of a Cluster
#. Select the **PACKAGES** tab
#. Click :guilabel:`+ ADD`
#. The Add Package wizard will guide you through two steps:

   **Step 1: Select Package Type**

   Choose from available package types that are not already installed on the cluster. Only packages compatible with the cluster type (MVM) are shown.

   **Step 2: Configure Package**

   Configure package-specific settings. The available configuration options depend on the selected package type and may include:

   - Connection endpoints
   - Authentication credentials
   - Resource allocation settings
   - Feature toggles

   .. NOTE:: Some packages provide custom configuration forms defined by plugin providers. These forms are dynamically rendered based on the package type.

#. Click :guilabel:`SAVE`

The package installation runs asynchronously. Progress can be monitored in the cluster's History tab.

Editing Package Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the Cluster's **PACKAGES** tab
#. Click the edit icon next to the installed package
#. Modify the configuration settings
#. Click :guilabel:`SAVE CHANGES`

Configuration updates are applied asynchronously to the cluster nodes.

Upgrading a Package
^^^^^^^^^^^^^^^^^^^

When a newer version of an installed package is available, the package is marked as upgradeable:

#. Navigate to the Cluster's **PACKAGES** tab
#. Click the upgrade icon next to the package (shown when an upgrade is available)
#. Review the upgrade details:

   - **Current Version** — The version currently installed
   - **Upgrade Version** — The version that will be installed

#. Confirm the upgrade

The upgrade runs asynchronously. The package status will update to reflect the new version upon completion.

Removing a Package
^^^^^^^^^^^^^^^^^^

#. Navigate to the Cluster's **PACKAGES** tab
#. Click the delete icon next to the package
#. Review the deletion confirmation showing the package name and description
#. Confirm the removal

.. WARNING:: Removing a package will uninstall its components from all cluster nodes. Ensure no workloads depend on the package's services before removing it.

Package removal runs asynchronously and is tracked in the cluster's History tab.

Package Status Values
^^^^^^^^^^^^^^^^^^^^^

- **Installed** — Package is active and functioning normally
- **Installing** — Package installation is in progress
- **Upgrading** — Package upgrade is in progress
- **Removing** — Package removal is in progress
- **Error** — Package encountered an error during installation or operation
