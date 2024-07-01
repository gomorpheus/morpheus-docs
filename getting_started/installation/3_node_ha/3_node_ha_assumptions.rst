Assumptions
^^^^^^^^^^^

This guide assumes the following:

- Shortname versions of hostnames will be resolvable
- All nodes have access to a shared storage mounted at ``/var/opt/morpheus/morpheus-ui``. This can be done as a post startup step.
- This configuration will support the complete loss of a single node, but no more.  Specifically the Elasticsearch tier requires at least two of the three nodes to always be clustered.

.. thumbnail:: /images/arch/morpheus-3node-arch-2.png
   :alt: Morpheus 3-Node HA Architecture

   Morpheus 3-Node HA Architecture

.. include:: 3_node_ha_paths.rst