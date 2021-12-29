Provisioning Concepts
=====================

|morpheus| is a powerful infrastructure-agnostic Cloud Application Management Platform. Compared to other CMP platforms in the space, some terminology and concepts may differ. These concepts are documented in this section along with places where terminology may be slightly different compared with other platforms or with common industry parlance.

|morpheus| refers to itself as a CAMP (Cloud Application Management Platform) as opposed to a (Cloud Management Platform). While that may seem minor, it actually is a big deal. Many CMP applications start at the IaaS layer and work up to the application layer (often needing additional PaaS architectures to fill out the model). |morpheus| was designed from a middle-ground perspective. As such, some concepts are a bit different. This provides a more complete platform that allows for greater capabilities out of the box as will be seen when these concepts are covered.

Instances
---------

<<<<<<< HEAD
|morpheus| starts with provisioning Instances. In some platforms an Instance is representative of a singular object like a "Virtual Machine" in Amazon. In |morpheus| , this concept was rethought. An Instance is more of a representation of a Resource or Service. This service may involve several virtual machines or even several docker containers.

For example, consider a Mongo is a full Mongo cluster consisting of either seven virtual machines or seven docker containers. Rather than representing these directly as seven individual "instances", |morpheus| groups them together into a singular instance of a service that contains multiple containers or virtual machines. This even allows for instance actions that can be performed to expand capacity on an instance (either horizontally or vertically). In the past, a database server may have been representative of a singular server, but this model has drastically changed in a big data world. This same concept also can apply to something like a simple Apache web server where there are 10 copies of a web server horizontally scaled out to handle traffic.
=======
|morpheus| starts with provisioning Instances. In some platforms, an Instance is representative of a singular object like a virtual machine in Amazon AWS. In |morpheus|, this concept was rethought. An Instance is more of a representation of a resource or service. This service may involve several virtual machines or several Docker containers.

For example, in the |morpheus| Instance wizard, MongoDB is an option and contains several Instance configurations. One of these configurations is a full MongoDB cluster consisting of either seven virtual machines or seven Docker containers. Rather than representing these directly as seven individual "instances", |morpheus| groups them together into a singular Instance of a service that contains multiple containers or virtual machines within it. This even allows for Instance actions that can be performed to expand capacity on an Instance (either horizontally or vertically). In the past, a database server may have been representative of a singular server, but this model has drastically changed in a big data world. This same concept also can apply to something like a simple Apache web server where there are 10 copies of a web server which are horizontally scaled out to handle traffic.
>>>>>>> 4cca5b2b... add more detail around plans and plan filtering

When viewing an Instance detail page, one is able to look at details and statistics specific to a virtual machine or container. |morpheus| simply helps simplify the management model for tracking these services.

Containers / Nodes / Virtual Machines
-------------------------------------

<<<<<<< HEAD
In relation to ``Instances``, an instance can have many nodes. A node is a generic representation of a container or a virtual machine. In most cases, |morpheus| will represent a node as a Container or Virtual Machine depending on the provisioning engine used for the instance. Node is just a generic naming representation when referring to these types of items. The public developer API, however, often refers to both virtual machines and docker containers as ``Containers``. The UI was since updated to better delineate this concept for easier understanding but In essence the name is valid for both concepts of containerized environments as well as Virtual Machines. In fact, one can even think of a Docker Host as a Hypervisor (which we do).
=======
In relation to Instances, an Instance can have many nodes. A node is a generic representation of a container or a virtual machine. In most cases, |morpheus| will represent a node as a Container or Virtual Machine depending on the provisioning engine used for the Instance. Node is just a generic naming representation when referring to these types of items. The public |morpheus| developer API, however, often refers to both virtual machines and Docker containers as "containers". The UI was since updated to better delineate this concept for easier understanding but, in essence, the name is valid for both concepts of containerized environments as well as Virtual Machines. In fact, one can even think of a Docker Host as a Hypervisor (which we do).
>>>>>>> 4cca5b2b... add more detail around plans and plan filtering

Hosts / Servers
---------------

<<<<<<< HEAD
This concept is mostly tailored to users of morpheus responsible for managing and maintaining the underlying infrastructure integrations. A Host typically refers to a Docker Host in which a container in an instance is running, or a hypervisor virtual machines can be provisioned onto. A Server is the underlying general representation of a physical or virtual server. It could be a Host representation , a Virtual Machine, or even a Bare Metal delineation.
=======
This concept is mostly tailored to users of |morpheus| who are responsible for managing and maintaining the underlying infrastructure integrations. A Host typically refers to a Docker Host in which a container (within an Instance) is running, or a hypervisor that virtual machines can be provisioned onto. A server is the underlying general representation of a physical or virtual server. It could be a Host representation, a Virtual Machine, or even a Bare Metal delineation.
>>>>>>> 4cca5b2b... add more detail around plans and plan filtering

When a user provisions a VM-based Instance, a corresponding server record is created to represent the link to the actual resource via the underlying provisioning engine. This may seem a bit odd but provides an aspect of |morpheus| that is quite powerful. This singular concept is what allows |morpheus| to ingest "brownfield" environments. We do not need to start clean. |morpheus| can be integrated into existing environments and manage existing virtual machines. The way |morpheus| does this is by periodically syncing existing VMs from the added cloud integrations. A server record will be created and periodically updated (every five minutes, by default) with realtime information and changes. This, in essence, provides CMDB-like capabilities as well. When a server is discovered, the user (given the appropriate access) can convert the virtual machine to a managed Instance. When this is done, a corresponding Instance is made in the provisioning section of |morpheus| and the |morpheus| Agent can optionally be installed to provide more refined guest operating system-level statistics and logging.

Apps
----

<<<<<<< HEAD
On top of all the previous concept, |morpheus| provides an Apps layer. An App is a collection of Instances linked together via application tiers. Tiers allow the user to define segregated sections of connectivity between the various elements / instances within an application. Once these instances are all linked together in an application concept, this may affect Instance environments and provide service discovery capabilities for them to cross connect. There are several service discovery aspects within morpheus as well as integrations with services like Consul.
=======
On top of all the previous concepts, |morpheus| provides an Apps layer. An App is a collection of Instances linked together via application tiers. Tiers allow the user to define segregated sections of connectivity between the various elements (Instances) within an application. Once these Instances are all linked together in an application concept, this may affect Instance environments and provide service discovery capabilities for them to cross connect. There are several service discovery aspects within |morpheus| as well as integrations with services.
>>>>>>> 4cca5b2b... add more detail around plans and plan filtering

App Blueprints
--------------

An App Blueprint allows a user to define an application structure for easy reproducibility and deployment into various environments. They can be used to mix and match various Instance types to provision an application dependent on multiple layers of services.
