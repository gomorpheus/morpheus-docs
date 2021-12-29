Creating Instances
------------------

The Instance catalog is the one-stop shop for selecting items to be provisioned and pieced together. It contains not only basic container and VM options but also tailored services for SQL databases, NoSQL databases, cache stores, message busses, web servers, and even full-fledged apps. The list contains a lot of items to choose from and they are represented to the user based on what provisioning engines are enabled and integrated in the |morpheus| environment.

To get started, simply click the :guilabel:`+ Add` button in the upper right of the ``Provisioning -> Instances`` section. A modal will display allowing the catalog to be searched. Once an item is selected it is just a matter of following the steps through the wizard.

<<<<<<< HEAD
.. TIP:: The instance catalog can be customized via role based access control thereby restricting access to non sanctioned catalog items, as well as added to via the ``Provisioning -> Library`` section. It is completely customizable.

The next step will ask for a Group and Cloud to be selected. The Group is an abstract representation that can contain multiple cloud integrations. These cloud integrations can also be in multiple groups and is also useful for using role based access control to restrict provisioning access and set retainment policies. If the environment is new and these do not yet exist, It may be advisable to refer to the main section on Getting started by setting up some cloud integrations and infrastructure first. The wizard continues by allowing us to choose a name for the instance as well as an environment.
=======
.. TIP:: The Instance catalog can be customized via role-based access control (RBAC) thereby restricting access to non-sanctioned catalog items, as well as added to via the |Lib| section. It is completely customizable.

The next step will ask for a Group and Cloud to be selected. The Group is an abstract representation that can contain multiple cloud integrations. Clouds can be in multiple Groups and Groups are also useful for using RBAC to restrict provisioning access and set retainment policies. If the environment is new and these do not yet exist, it may be advisable to refer to one of our starter guides, such as the guide on getting started with |morpheus| and `VMware <https://docs.morpheusdata.com/en/latest/getting_started/guides/vmware_guide.html>`_. The wizard continues by allowing us to choose a name for the Instance as well as an environment.
>>>>>>> 4cca5b2b... add more detail around plans and plan filtering

.. NOTE:: Currently the Environment option is mostly useful for presenting the user with informative metadata around the Instance when coming back to it later.

Moving on, it is now time to configure the Instance. Depending on the Instance Configuration that is chosen, fields will change. This can include cloud-specific fields (i.e. Datastore for VMware or Network). There will also be options like setting an initial user account. Some of these fields are optional and will be represented as such.

Configuration options provided in this screen are very powerful. An example is MySQL where a Master/Slave or Master/Master layout can be selected. These configurations will automatically deploy two MySQL VMs or containers and link them together to provide replication. These types of configurations exist for a wide range of Instance types and are optimized for high performance and scale. It is even possible to provision entire sharded MongoDB clusters.

One last step before the Instance can be provisioned is the Automation step. This wizard step may or may not appear depending on the capabilities of the Instance type or previous configurations in the account. It is here one can easily select a post-provisioning workflow to run (see more on Tasks and Workflows elsewhere in |morpheus| documentation), assign a load balancer, or even configure the backup job that gets created.

<<<<<<< HEAD
Now that the steps are completed for provisioning the selected instance type , simply review your selections and complete. The instance will automatically show up in the instances list and its provisioning state will be represented. Depending on what was provisioned this step can range from seconds to minutes (typically a container configuration will be rather quick if the instance type has previously been provisioned before).
=======
Now that the steps are completed for provisioning the selected Instance type, simply review your selections and complete. The Instance will automatically show up in the Instances list and its provisioning state will be represented. Depending on what was provisioned this step can range from seconds to minutes (typically a container configuration will be rather quick if the Instance type has previously been provisioned before).

Converting Discovered Resources to Managed Instances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating new cloud integrations (or updating existing ones), users may opt for |morpheus| to onboard any existing resources that currently reside in the Cloud. For example, these may be virtual machines that exist on vCenter hosts prior to integration with |morpheus|, EC2 instances pre-existing on an Amazon AWS account, or virtual machines that are running on a KVM host. With the Add/Edit Cloud modal open, mark INVENTORY EXISTING INSTANCES for |morpheus| to automatically onboard these resources. Not only will |morpheus| inventory these instances at the time the cloud is integrated (or updated), it will also continue to poll the target cloud every five minutes (by default) for newly added or removed servers. Users can see these discovered servers by looking in |InfCom|. Depending on the type of resource, it may appear on the Virtual Machines tab, the Containers tab, or another tab. Additionally, we can see a list of discovered servers on Cloud detail pages (|InfClo| > Selected Cloud). Just click on the tabs for VMs, Containers or Hosts tab. Discovered resources will be indicated as such whereas containers which are associated with a managed Instance will be marked as a "Managed".

Additionally, |morpheus| allows users to convert discovered resources into managed Instances. Begin from the server detail page (|InfComVir| > selected machine) and from the ACTIONS menu select "Convert to Managed". At this point, we must make a number of selections:

- Assign to the primary Tenant or one of the Subtenants
- Select a Group (this dropdown contains a filtered list of Groups which the associated Cloud is in)
- Username and password for a seeded account
- Opt to install |morpheus| Agent or not (for more on |morpheus| Agent, click `here <https://docs.morpheusdata.com/en/latest/getting_started/functionality/agent/morpheus_agent.html>`_)
- Select the Instance Type which should be associated with the new Instance containing this VM
- Select a version number for the Instance (such as 20.04 for a basic Ubuntu Instance)
- Select a Layout, Instance Types often have multiple Layout configurations
- Identify the operating system
- Select a Plan (this dropdown contains a filtered list of plans which correlate to the size of the VM)

Finally, click :guilabel:`EXECUTE`. Once this process is completed, the server will be indicated as "Managed" in the servers list. Additionally, a new Instance will appear on the Instances List page (|ProIns|). We can now work with it in the same way we can work with any other Instance, such as by adding it to an App or expanding the Instance horizontally with added nodes.
>>>>>>> 4cca5b2b... add more detail around plans and plan filtering
