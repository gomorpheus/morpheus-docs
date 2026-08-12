.. _upgrading:

Upgrading
---------

.. warning:: |morpheus| |morphver| contains new node and VM node packages that require 3.5GB of storage. It is safe to run ``sudo rm -Rf /var/opt/morpheus/package-repos/*`` after |morphver| package installation and before reconfigure to clean old node and vm node packages from the package-repo when room is needed. 

Morpheus application upgrades do not replace maintenance of the Ubuntu operating system included in the HPE Morpheus Manager QCOW2 image. For the HPE validation boundary, connected APT workflow, and Canonical-aligned air-gapped repository models, see :doc:`manager_os_updates`.

VME 8.1.1 Agent Follow-up
^^^^^^^^^^^^^^^^^^^^^^^^^

The available release data does not establish a general requirement to update every Agent type after a VME Manager 8.1.1 upgrade. Do not apply a generic Agent update sequence based only on an update notification. Review the release-specific update offered for each managed component and update only the Agent identified by that workflow.

The documented exception is the HVM layout 1.2-to-1.3 cluster update: its released update definitions require HVM Host Agent 3.2.7 or later and upgrade an older Host Agent automatically before layout scripts run. After that operation, verify the Host reconnects at the required Agent version and confirm the cluster state and Quorum panel under :menuselection:`Infrastructure --> Clusters`. See :doc:`/infrastructure/clusters/hvm/upgrading`. This exception does not establish a version requirement for appliance, VM, container, or other Agent types.

If the UI requests an Agent update but the component and required version are not identified by its release-specific workflow, the supported requirement is not established in this documentation; preserve the notification and contact HPE Support rather than updating unrelated Agents.

	
.. toctree::
   :maxdepth: 4

   upgrades/overview.rst
   upgrades/single/singlenode.rst
   upgrades/3node/overview.rst
   upgrades/fullha/overview.rst
