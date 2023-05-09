Managing Instances
------------------

Instance actions allow you to perform numerous management tasks on instances. The actions available depend on the instance type, hypervisor, roles permissions, and instance state.

Edit
  Edit the Name, Display Name, Description, Environment, Group, Metadata, Tags, and Owner for the Instance.

  .. NOTE:: The Display Name is a friendly name used to identify the Instance in |morpheus|. You see this value in the Instances List Page and most other places throughout the UI. The Name and Display Name of Instances are initially the same after provisioning and may not ever need to be edited. The Name value for all Instances must be unique while the Display Name can take any value with no uniqueness requirement.
Delete
  Deletes the Instance.

.. IMPORTANT:: Deleting an Instance will delete the actual VM's or Containers and cannot be undone, unless a Delayed Removal policy has been applied prior to the Deletion. To delete Instances without deleting associated VM's, delete the Instances VM record(s) from the Infrastructure section with "Remove Infrastructure" deselected and select "Remove Associated Instances" in the VM delete modal options. This will delete the records in |morpheus| but leave the infrastructure in place.

.. TIP:: You can change the owner of an instance easily by selecting the edit button and entering a new owner in the corresponding field.

Actions
^^^^^^^

Available options in the Actions dropdown can include:

Suspend
  Puts the VM in a suspended state without shutting down the OS.
Stop/Start/Restart Service
  Stops, Starts or Restarts the service associated with the Instance Type.
Stop/Start/Restart Server
  Stops, Starts or Restarts the Virtual Machine.
Import as Image
  Clones and exports VM in its current state to target Storage provider and adds Virtual Image Record with metadata matching the source Instance's configuration.
Clone to Image
  Clones and converts VM in its current state to image in the source Cloud and adds Virtual Image Record with metadata matching the source Instance's configuration.
Lock/Unlock Instance
  A locked instance cannot be deleted until it is unlocked.
Reconfigure
  The Reconfigure action allows service plan, disk, cpu, ram, networks and storage controller changes. Available options depend on the instance type and service plan configuration. Some resize actions require an instance restart.
Clone
  Creates a new Instance from the Instance at its current state.
Backup
  Immediately executes a backup of the Instance. Only available for Instances with backups enabled.
Run Workflow
  Presents workflow options and then immediately runs selected Workflow on the Instance. Workflows can be created in the |LibAut| section.
Run Script
  Presents Script options and immediately executes selected Script on the Instance. Scripts can be created in the |Lib| section.
Apply Template
  Presents Template options and immediately applies selected Template to the Instance. Templates can be created in the |Lib| section.
Add Node
  Adds an additional node to the configuration. Additional options and configurations are required in the add node wizard depending on instance configuration and type.
Eject Disk
  Ejects attached disk/iso.
Add Slave
  Adds a database slave in the Instance.
Change Master
  Changes the database Master node in an Instance.
Clone to Template (VMware)
  Creates a new VMware Template from the Instance with corresponding |morpheus| Virtual Image record.


.. TIP:: Scrolling down in the Actions dropdown may be necessary to see all options.

Performing Instance Actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Select the Provisioning link in the navigation bar.
#. Click the Instance from the list of instances you wish to perform an action on.
#. Click the Actions drop down button and select an Action.

.. Instances___|morpheus| _Reconfigure.png

Notes
^^^^^

Every Instance has a Wiki section for adding useful information about the Instance. Wiki can be added by selecting the Wiki tab button on the bottom of Instance Detail pages. Instances with associated VMware VM's will bi-directionally sync |morpheus| Instance Wiki content and VMware VM Notes. See the :ref:`wiki` Section for more details.

.. TIP:: Markdown Syntax is supported in Wikis.
