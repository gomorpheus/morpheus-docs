Scaling Morpheus Nodes
----------------------

Morpheus App nodes can be scaled to accommodate additional load. Appliance nodes can be scaled vertically in centralized architectures, and both vertically and horizontally in distributed architectures.

Vertical Scaling
^^^^^^^^^^^^^^^^

In all Appliance Architectures, Application nodes can be vertically scaled at any time, however a reconfigure must be performed for additional resources to be utilized by |morpheus| on a node, which will result in the ``morpheus-ui`` restarting on the reconfiguring node.

Morpheus configures memory/ram utilization for services during the ``reconfigure`` process. If additional memory/ram is added to a Host or VM running the Morpheus App, the additional memory/ram will not be utilized by the Morpheus Application until a ``morpheus-ctl reconfigure`` command is ran and the additional memory/ram is recognized.

.. important:: When the ``morpheus-ctl reconfigure`` command detects changes on available memory/ram, it will restart the ``morpheus-ui`` service.

The impact on Availability depends on the Morpheus Appliance Architecture.

- Centralized Appliances
    Morpheus will be unavailable while the ``morpheus-ui`` restarts.
- Distributed Appliances
    Zero-down time can be achieved by Reconfiguring one App Node at a time, with proper Front-End Load Balancer configuration.

Horizontal Scaling
^^^^^^^^^^^^^^^^^^

Additional Morpheus App Nodes can be added at any time to Fully Distributed Architectures.

- Configure Shared Storage paths for the new App Node(s)
- Install, but do not run the ``morpheus-ctl reconfigure`` command on the new App Node(s), using the same Morpheus version as the existing Appliance nodes.
- Copy the ``morpheus.rb`` from an existing App Node to the new App Node(s)
- Ensure permissions and network configuration for the new App Node(s) to access all MySQL and Elasticsearch nodes, and the RabbitMQ VIP.
- Ensure permissions and network configuration for all required UI services and Integrations, such as network access to ESXi hosts over 443 for Hypervisor console and/or image transfers.
- Add associated SSL files and configuration which is not on shared storage.
- Reconfigure the new App Node(s) via ``morpheus-ctl reconfigure``
- Verify UI startup succeeded
- Add New App Node(s) to Front End Morpheus UI Load Balancer pool.

During ``morpheus-ctl reconfigure``, the new App Node(s) will validate and be configured to use the existing tiers for the UI service. Upon successful reconfigure, the Morpheus service will be available on the App Node(s) with consistent data and capabilities.

.. note:: No services, including ``morpheus-ui``, are required to be shut down on existing nodes when adding new App Nodes
