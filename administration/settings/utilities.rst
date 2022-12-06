System administrators have access to a utilities panel with the following options:

- **Reindex all searchable data:** Execute
- **Toggle Maintenance Mode:** Enable

.. NOTE:: Maintenance mode cleanly places |morpheus| into a state where maintenance can be performed on the appliance. This drains any active sessions and queues so an auto-scaling group can scale down. It also drains active sessions across services. Restarting |morpheus| UI disables maintenance mode.

.. NOTE:: When using |morpheus| in a Highly Available (HA) environment, it is important to navigate to a node directly and enable maintenance mode, as opposed to using the load balancer virtual IP (VIP).  A local host entry to the specific node may be required to access the specific node, this will ensure the correct node enters maintenance mode.  A |morpheus| node in maintenance mode can still be accessible through the load balancer VIP/target group and can queue requests but will not process anything in queue, while in maintenance mode.  A node can be removed/paused from the load balancer VIP or have VIP health checks implemented, if the node UI/API will become inaccessible due to maintenance.
