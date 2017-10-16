Instances
=========

Instances is a great starting point for taking advantage of self service
features and spinning up both vms and containers. In |morpheus| it may
be advisable to cover the definition of a few terms used within the
application so as to reduce confusion.

-  *Instance* - A set of containers or virtual machines that can
   correlate to a single horizontally scalable entity or a service suite
   like a database. (It is important to note that an instance can
   contain one or more containers/vms depending on the instance type and
   configuration).
-  *Container* - Typically a docker container provisioned via a
   |morpheus| Docker host.
-  *Virtual Machine* - A virtualized compute server provisioned onto
   various hypervisor hosts.

The top of the main Instances page shows overall statistic for the
listed Instances, including count, status, and resource utilization.

Please note the instances listed are determined by group access and role
permissions. Also, certain features shown may be hidden or disabled
depending on user permissions.

You can search for instances by name, or filter by group, instance type,
or category.

The instance list contains important information about each instance,
including the instance name, environment tag, instance type icon, ip and
port info, instance version, the number of virtual machines or
containers in the instance, the group the instance is in, and the cloud
or clouds the instance is in.

.. include:: instance/creating_instances.rst
.. include:: instances/instance_details.rst
.. include:: instances/managing_instances.rst
