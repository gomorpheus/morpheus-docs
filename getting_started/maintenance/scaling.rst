Scaling Morpheus Nodes
-----------------------

Morpheus App nodes can be scaled to accommodate additional load. Appliance nodes can be scaled vertically in centralized architectures, and both vertically and horizontally in distributed architectures.

Vertical Scaling
^^^^^^^^^^^^^^^^

In all Appliance Architectures, Application nodes can be vertically scaled at any time, however a reconfigure must be performed for additional resources to be utilized bu Morpheus on a node, which will result in the ``morpheus-ui`` restarting on the reconfiguring node.

Morpheus configures memory/ram utilization for services during the ``reconfigure`` process. If additional memory/ram is added to a Host or VM running the Morpheus App, the additional memory/ram will not be utilized by the Morpheus Application until a ``morpheus-ctl reconfigure`` command is ran and the additional memory/ram is recognized.

When the ``morpheus-ctl reconfigure`` command detects changes on available memory/ram, it will trigger a ``morpheus-ui`` service restart.

.. important:: When the ``morpheus-ctl reconfigure`` command detects changes on available memory/ram, it will restart the ``morpheus-ui`` service.






The impact on Availability depends on the Morpheus Appliance Architecture.



- Centralized Appliances
    Morpheus will be unavailable while the ``morpheus-ui`` restarts.
- Distributed Appliances
    Zero-down time can be achieved by Reconfiguring one App Node at a time, with proper Front-End Load Balancer configuration.
