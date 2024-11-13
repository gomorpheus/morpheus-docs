Managing Instances
------------------

Instance actions allow you to perform numerous management tasks on instances. The actions available depend on the instance type, hypervisor, roles permissions, and instance state. Actions can be accessed from the Instances list page or from an Instance detail page.

Edit
  Edit the Name, Description, Environment, Group, Tags, and Owner for the Instance.
Delete
  Deletes the Instance.

.. IMPORTANT:: Deleting an Instance will delete the actual underlying VMs or Containers and cannot be undone.

.. TIP:: You can change the owner of an instance easily by selecting the edit button and entering a new owner in the corresponding field.

Actions
^^^^^^^

Available options in the Actions dropdown can include:

Suspend
  Puts the VM in a suspended state without shutting down the OS.
Stop/Start/Restart Server
  Stops, Starts or Restarts the Virtual Machine.
Import as Image
  Clones and exports VM in its current state to target Storage provider and adds a Virtual Image record with metadata matching the source Instance configuration.
Clone to Image
  Clones and converts VM in its current state to image in the source Cloud and adds a Virtual Image record with metadata matching the source Instance configuration.
Lock/Unlock Instance
  A locked Instance cannot be deleted until it is unlocked.
Reconfigure
  The Reconfigure action allows service plan, disk, CPU, memory, networks and storage controller changes. Available options depend on the type and Plan configuration. Some resize actions require an Instance restart.
Clone
  Creates a new Instance from the Instance at its current state.
Backup
  Immediately executes a backup of the Instance. This is only available for Instances with backups enabled.
Run Task
  Select a currently-configured Task to run against the Instance. Tasks can be created and edited in |LibAut|.
Add Node
  Adds an additional node to the configuration. Additional options and configurations are required in the add node wizard depending on Instance configuration and type.
Eject Disk
  Ejects attached disks (ISOs).
Clone to Template (VMware)
  Creates a new VMware Template from the Instance with corresponding |morpheus| Virtual Image record.

.. TIP:: Scrolling down in the Actions dropdown may be necessary to see all options.

Performing Instance Actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Select the Provisioning link in the navigation bar.
#. From the Instances list, select the desired Instance.
#. Click the Actions dropdown button and select an Action.

Notes
^^^^^

Every Instance has a Wiki section for adding useful information about the Instance. Wiki can be added by selecting the Wiki tab on the bottom of the Instance Detail page. Instances with associated VMware VMs will bi-directionally sync |morpheus| Wiki content and VMware VM Notes. See the :ref:`wiki` Section for more details.

.. TIP:: Markdown Syntax is supported in Wikis.
