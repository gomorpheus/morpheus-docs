Advanced
^^^^^^^^

There are a few advanced features when it comes to provisioning on top of Openstack. Most of these present themselves in the provisioning wizard. This includes OS Volume Type (Local or Volume) which dictates whether the main OS disk is copied and run off the hypervisor or remotely mounted as a volume via Glacier. Some Openstack setups only configure hypervisors with minimal local disks so volume type is needed.

Another option during provisioning is "Assign Floating IP". This option does exactly what it says and is similar to the feature on the Openstack instance dashboard itself. It should be noted that this will attempt to acquire a floating IP from the project and, if out of capacity, will attempt to increase capacity to the project if the cloud credentials provided have sufficient administrative privileges to do so.
