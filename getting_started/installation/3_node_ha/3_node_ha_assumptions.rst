Assumptions
^^^^^^^^^^^

This guide assumes the following:

- App nodes can resolve each others short names 
- All app nodes have access to shared storage mounted at ``/var/opt/morpheus/morpheus-ui``. 
- This configuration is designed to tolerate the complete failure of a single node but not more. Specifically, the Elasticsearch tier requires MORE than 50% of the nodes to be up and clustered at all times. However, you can always add more nodes to increase resilience.
- You have a load balancer available and configured to distribute traffic between the app nodes. `Load Balancer Configuration <https://docs.morpheusdata.com/en/latest/getting_started/additional/additional_configuration.html#load-balancer-configuration>`_

.. thumbnail:: /images/arch/morpheus-3node-arch-2.png
   :alt: Morpheus 3-Node HA Architecture

   Morpheus 3-Node HA Architecture
