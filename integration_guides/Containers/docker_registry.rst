Docker Registry
---------------

Overview
^^^^^^^^

Without any additional configuration, |morpheus| can provision images from Docker's public hub at https://hub.docker.com/ using their public API.

However, many organizations maintain private Docker registries for security measures. Additional public and private Docker registries can be added to Morpheus.

Adding a Docker Registry Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmInt|
#. Click "New Integration"
#. Select the `Docker Repository` Type
#. Add the following:

   Name
    Name for the Registry in |morpheus|
   Repository url
    Docker Registry url or IP address
   Username
    Username if private registry
   Password
    Password if private registry

#. Save Changes

.. NOTE:: You must either have signed certificates for your registry or configure your docker host(s) to accept insecure registries

Provisioning an Instance from Docker Registry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Docker images from the Integrated Registry can be provisioned using the generic `Docker` Instance Type, or by adding images to Node Types for custom Library Instance Types.

.. //add provisioning info and creating docker node types
