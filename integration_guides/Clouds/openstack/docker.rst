Docker
^^^^^^

So far this document has covered how to add the Openstack cloud integration and has described how to provision virtual machine-based Instances via the `Add Instance` catalog in `Provisioning`. Another great feature provided by |morpheus| out of the box is the ability to work with Docker containers and even support multiple containers per Docker host. To do this, a Docker host must first be provisioned into Openstack (multiple hosts are needed when dealing with horizontal scaling scenarios).

To provision a Docker Host, navigate to Infrastructure > Clusters and click :guilabel:`+ ADD CLUSTER`. Complete the provisioning wizard including selecting the appropriate Group and Cloud. Alternatively, you can navigate to the Clusters tab for a specific Cloud (Infrastructure > Clouds > Specific Cloud detail page > Clusters tab) and begin the process of provisioning a Docker host to that Cloud from there. Once completed, this host will show up in the Hosts sections (Infrastructure > Hosts OR Infrastructure > Clouds > Specific Cloud detail page > Hosts tab). |morpheus| views a Docker host just like any other Hypervisor with the caveat being that it is used for running containerized images instead of virtualized ones.

Once a Docker Host is successfully provisioned, a green checkmark will appear to the right of the host marking it as available for use. In the event of a failure, click into the relevant host that failed and an error explaining the failure will be displayed in red at the top.

Some common error scenarios include network connectivity. For a Docker Host to function properly, it must be able to resolve the |morpheus| appliance URL which can be configured in ``|AdmSet|``. If it is unable to resolve and negotiate with the appliance, the |morpheus| Agent installation will fail and provisioning instructions will not be able to be issued to the host.
