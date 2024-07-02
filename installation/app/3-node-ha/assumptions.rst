Assumptions
^^^^^^^^^^^

This guide assumes the following:

- The Baremetal nodes cannot access the public internet
- Shortname versions of hostnames will be resolvable
- All nodes have access to a shared volume for ``/var/opt/morpheus/morpheus-ui``. This can be done as a post startup step.
- This configuration is designed to tolerate the complete failure of a single node but not more. Specifically, the Elasticsearch tier requires MORE than 50% of the nodes to be up and clustered at all times. However, you can always add more nodes to increase resilience.
- You have a load balancer available and configured to distribute traffic between the app nodes. `Load Balancer Configuration <https://docs.morpheusdata.com/en/latest/getting_started/additional/additional_configuration.html#load-balancer-configuration>`_

.. thumbnail:: /images/arch/morpheus-3node-arch-2.png
   :alt: Morpheus 3-Node HA Architecture

   Morpheus 3-Node HA Architecture