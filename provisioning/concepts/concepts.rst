Provisioning Concepts
=====================

|morpheus| is a powerful provisioning and management platform for |clusters| and VMware vCenter private cloud. Compared to other CMP platforms in the space, some terminology and concepts may differ. These concepts are documented in this section along with places where terminology may be slightly different compared with other platforms or with common industry parlance.

Instances
---------

|morpheus| starts with provisioning Instances. In some platforms, an Instance is representative of a singular object like a virtual machine in VMware vCenter. In |morpheus|, this concept was rethought. An Instance is more of a representation of a resource or service. This service may involve several virtual machines, as in the case of a database cluster or horizontally-scaled web servers.

When viewing an Instance detail page, one is able to look at details and statistics specific to a virtual machine or container. |morpheus| simply helps simplify the management model for tracking these services.

Containers / Nodes / Virtual Machines
-------------------------------------

In relation to Instances, an Instance can have many nodes. A node is a generic representation of a container or a virtual machine. In most cases, |morpheus| will represent a node as a Container or Virtual Machine depending on the provisioning engine used for the Instance (workload provisioned to a |cluster| as opposed to a Docker cluster, for example). Node is just a generic naming representation when referring to these types of items. The public |morpheus| developer API, however, often refers to both virtual machines and Docker containers as "containers". The UI was updated to better delineate this concept for easier understanding but, in essence, the name is valid for both concepts of containerized environments as well as virtual machines.

Hosts / Servers
---------------

This concept is mostly tailored to users of |morpheus| who are responsible for managing and maintaining the underlying infrastructure integrations. A Host typically refers to a Docker Host in which a container (within an Instance) is running, or a hypervisor that virtual machines can be provisioned onto. A server is the underlying general representation of a physical or virtual server. It could be a Host representation, a Virtual Machine, or even a Bare Metal delineation.

When a user provisions a VM-based Instance, a corresponding server record is created to represent the link to the actual resource via the underlying provisioning engine. This may seem a bit odd but provides an aspect of |morpheus| that is quite powerful. This singular concept is what allows |morpheus| to ingest "brownfield" environments. We do not need to start clean. |morpheus| can be integrated into existing environments and manage existing virtual machines. The way |morpheus| does this is by periodically syncing existing VMs from the added cloud integrations. A server record will be created and periodically updated (every five minutes, by default) with realtime information and changes. This, in essence, provides CMDB-like capabilities as well. When a server is discovered, the user (given the appropriate access) can convert the virtual machine to a managed Instance. When this is done, a corresponding Instance is made in the provisioning section of |morpheus| and the |morpheus| Agent can optionally be installed to provide more refined guest operating system-level statistics and logging.
