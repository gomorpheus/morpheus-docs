Instances
=========

..
  .. container:: left-col

Instances is a great starting point for taking advantage of self service features and spinning up both VM's and containers. In |morpheus| it may be advisable to cover the definition of a few terms used within the application so as to reduce confusion.

Instance
  A set of containers or virtual machines that can correlate to a single horizontally scalable entity or a service suite like a database. (It is important to note that an instance can contain one or more containers/vms depending on the instance type and configuration).
Container
  Typically a docker container provisioned via a |morpheus| Docker host.
Virtual Machine
  A virtualized compute server provisioned onto various hypervisor hosts.

The top of the main Instances page shows overall statistic for the listed Instances, including count, status, and resource utilization. You can search for instances by name, or filter by group, instance type, or category.

.. NOTE:: Instances listed are determined by group access and role permissions.

The Instance list contains important information about each instance, including the instance name, environment tag, instance type icon, ip and port info, instance version, the number of virtual machines or containers in the instance, the group the instance is in, and the cloud or clouds the instance is in.

.. include:: creating_instances.rst
.. include:: instance_details.rst
.. include:: managing_instances.rst
.. .. include:: /troubleshooting/Remote_Console.rst

..
  .. container:: right-col

      .. content-tabs::

          .. tab-container:: tab1
              :title: CLI

              .. include:: /provisioning/instances/instancecli.rst

          .. tab-container:: tab2
              :title: API

              in progress...
