Creating Instances
------------------

The Instance catalog is the one-stop shop for selecting items to be provisioned and pieced together. It contains not only basic container and VM options but also tailored services for SQL databases, NoSQL databases, cache stores, message busses, web servers, and even full-fledged apps. The list contains a lot of items to choose from and they are represented to the user based on what provisioning engines are enabled and integrated in the |morpheus| environment.

To get started, simply click the :guilabel:`+ Add` button in the upper right of the :menuselection:`Provisioning --> Instances` section. A modal will display allowing the catalog to be searched. Once an item is selected it is just a matter of following the steps through the wizard.

.. TIP:: The Instance catalog can be customized via role-based access control (RBAC) thereby restricting access to non-sanctioned catalog items, as well as added to via the |Lib| section. It is completely customizable.

.. NOTE:: For storage-specific provisioning workflows, see the integration guide for your storage platform. For example, :doc:`/integration_guides/storage/hpe-alletra-mp` includes a walkthrough of creating Instances on HPE Alletra MP datastores.

The next step will ask for a Group and Cloud to be selected. The Group is an abstract representation that can contain multiple cloud integrations. Clouds can be in multiple Groups and Groups are also useful for using RBAC to restrict provisioning access and set retainment policies. If the environment is new and these do not yet exist, it may be advisable to refer to one of our starter guides, such as the :doc:`/getting_started/guides/vmware_guide` guide. The wizard continues by allowing us to choose a name for the Instance as well as an environment.

For cluster-backed provisioning, cluster Group permissions filter the targets available after the Group is selected. Cluster Service Plan permissions then filter plan choices for that target; role access, plan active state, provision type, and layout or image minimums also apply. **Default** permission behavior is not an explicit allow-list and does not mean the cluster is preselected. See :ref:`hvm-cluster-permissions`.

.. NOTE:: Currently the Environment option is mostly useful for presenting the user with informative metadata around the Instance when coming back to it later.

The Environment value is stored as the Instance context and can be displayed and filtered as metadata. Administrators can require a value through Provisioning Settings, and naming policies can reference it as ``${instance.instanceContext}``. The Environment record itself does not grant access; use Roles and resource permissions for access control.

Moving on, it is now time to configure the Instance. Depending on the Instance Configuration that is chosen, fields will change. This can include cloud-specific fields (i.e. Datastore for VMware or Network). There will also be options like setting an initial user account. Some of these fields are optional and will be represented as such.

For VMware Clouds, storage-type and network-interface-type selectors are shown only when the corresponding Cloud settings are enabled and the provider exposes choices. See :doc:`/integration_guides/Clouds/vmware/advanced`. Selector availability is provider-specific and can differ between initial provisioning and reconfiguration.

For HVM VMs, expand **Advanced Options** on the Configure step to set provider-specific firmware, boot, security, graphics, memory, identity, and virtualization controls. The fields shown depend on the selected layout and whether the VM is being provisioned or reconfigured. See :doc:`/infrastructure/clusters/hvm/vm_advanced_options` for the current field inventory, defaults, dependencies, and availability matrix. In particular, :guilabel:`QEMU Arguments` is available during provisioning and reconfiguration; its value is tokenized and passed to QEMU when the VM definition is generated, so invalid or conflicting arguments can prevent startup.

There is no universal Instance :guilabel:`Port` field. A field with that label is supplied by a selected Instance type or connection workflow and its meaning follows that context. For example, the MySQL **Existing** layout uses :guilabel:`Host` and :guilabel:`Port` to connect to the existing MySQL service; the default port is ``3306``. A Windows server connection form can also label its WinRM connection port as :guilabel:`Port` and defaults it to ``5985``. Neither field opens a guest firewall port or publishes an application endpoint. Confirm the selected layout and the field group before setting it; do not apply a port value from one Instance type to another.

Configuration options provided in this screen are very powerful. An example is MySQL where a Master/Slave or Master/Master layout can be selected. These configurations will automatically deploy two MySQL VMs or containers and link them together to provide replication. These types of configurations exist for a wide range of Instance types and are optimized for high performance and scale. It is even possible to provision entire sharded MongoDB clusters.

One last step before the Instance can be provisioned is the Automation step. This wizard step may or may not appear depending on the capabilities of the Instance type or previous configurations in the account. It is here one can easily select a post-provisioning workflow to run (see more on Tasks and Workflows elsewhere in |morpheus| documentation), assign a load balancer, or even configure the backup job that gets created.

Now that the steps are completed for provisioning the selected Instance type, simply review your selections and complete. The Instance will automatically show up in the Instances list and its provisioning state will be represented. Depending on what was provisioned this step can range from seconds to minutes (typically a container configuration will be rather quick if the Instance type has previously been provisioned before).

Converting Discovered Resources to Managed Instances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating new cloud integrations (or updating existing ones), users may opt for |morpheus| to onboard any existing resources that currently reside in the Cloud. For example, these may be virtual machines that exist on vCenter hosts prior to integration with |morpheus|, EC2 instances pre-existing on an Amazon AWS account, or virtual machines that are running on a KVM host. With the Add/Edit Cloud modal open, mark INVENTORY EXISTING INSTANCES for |morpheus| to automatically onboard these resources. Not only will |morpheus| inventory these instances at the time the cloud is integrated (or updated), it will also continue to poll the target cloud every five minutes (by default) for newly added or removed servers. Users can see these discovered servers by looking in :menuselection:`Infrastructure --> Compute`. Depending on the type of resource, it may appear on the Virtual Machines tab, the Containers tab, or another tab. Additionally, we can see a list of discovered servers on Cloud detail pages (|InfClo| > Selected Cloud). Just click on the tabs for VMs, Containers or Hosts tab. Discovered resources will be indicated as such whereas containers which are associated with a managed Instance will be marked as a "Managed".

Additionally, |morpheus| allows users to convert discovered resources into managed Instances. Begin from the server detail page (:menuselection:`Infrastructure --> Compute --> Virtual Machines` > selected machine) and from the ACTIONS menu select "Convert to Managed". At this point, we must make a number of selections:

- Assign to the primary Tenant or one of the Subtenants
- Select a Group (this dropdown contains a filtered list of Groups which the associated Cloud is in)
- Username and password for a seeded account
- Opt to install |morpheus| Agent or not (:doc:`/getting_started/functionality/agent/features`)
- Select the Instance Type which should be associated with the new Instance containing this VM
- Select a version number for the Instance (such as 20.04 for a basic Ubuntu Instance)
- Select a Layout, Instance Types often have multiple Layout configurations
- Identify the operating system
- Select a Plan (this dropdown contains a filtered list of plans which correlate to the size of the VM)

Finally, click :guilabel:`EXECUTE`. Once this process is completed, the server will be indicated as "Managed" in the servers list. Additionally, a new Instance will appear on the Instances List page (:menuselection:`Provisioning --> Instances`). We can now work with it in the same way we can work with any other Instance, such as by adding it to an App or expanding the Instance horizontally with added nodes.
