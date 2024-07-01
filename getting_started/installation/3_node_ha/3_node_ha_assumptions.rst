Assumptions
^^^^^^^^^^^

This guide assumes the following:

- Shortname versions of hostnames will be resolvable
- All app nodes have access to a shared storage mounted at ``/var/opt/morpheus/morpheus-ui``. 
- This configuration will support the complete loss of a single node, but no more. Specifically the Elasticsearch tier requires at least two of the three nodes to always be clustered.
- You have a load balancer available and configured to distribute traffic between the app nodes. `Load Balancer Configuration <https://docs.morpheusdata.com/en/latest/getting_started/additional/additional_configuration.html#load-balancer-configuration>`_

.. thumbnail:: /images/arch/morpheus-3node-arch-2.png
   :alt: Morpheus 3-Node HA Architecture

   Morpheus 3-Node HA Architecture
