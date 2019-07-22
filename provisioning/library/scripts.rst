Scripts
-------

Scripts are bash and powershell scripts that can be attached to node types to always execute at the set phase when that node type is provisioned, added to Workflows as Library Script Tasks, and/or execute ad-hoc on Instances.

Creating Scripts
^^^^^^^^^^^^^^^^

#. Navigate to ``Provisioning -> Library -> Scripts``
#. Select :guilabel:`+ ADD`
#. Enter the Following:

   NAME
     Name of the Script in |morpheus|
   SCRIPT TYPE
     - Bash
     - Powershell
   PHASE
     Select which phase the Script will execute when attached to a Node Type. When a script is attached to a Node Type, it will execute according to the set Phase:

     Start Service
       Any time the Instance action ``Start Service`` is executed.
     Stop Service
       Any time the Instance action ``Stop Service`` is executed.
     Pre-Provision
       Containers
         Script will execute agains the container host before the container is provisioned
       Virtual Machines
         Script will execute before any Provision phase scripts or Tasks
     Provision
         Script will execute once per new Instance node during the Provision Phase. Provisioning will not be considered complete until all scripts and tasks in the Provisioning Phase are completed.

         .. NOTE:: Any Script or Task set to Provision Phase will be included in the total Provision Time and impact success/warn/failure Provision status. Aka your VM could be up and running but if your Script is in the Provision phase and fails, provisioning will be marked as a failure.

       Post-Provision
           Script will execute once per new Instance node after the Provision phase is completed. Scripts and Tasks in the Post-Provision phase will show Execution Status and History, but are not considered part of the Provision and do not impact Provisioning Status.
       Pre-Deploy
           Script will execute on Target Instance any time a Deployment is ran against the Instance. The script will run prior to the Deployment file(s) being written.
       Deploy
           Script will execute on Target Instance any time a Deployment is ran against the Instance. The script will run after the Deployment file(s) are written.
       Reconfigure
           Script will execute on Target Instance anytime a Reconfigure is executed against the Instance.
       Teardown
           Script will execute on Target Instance upon Instance deletion. Script will execute against Target Instance prior to the deletion/removal of resources.

   SCRIPT
     Enter bash or powershell script.

     .. note:: |morpheus| variables are supported in Library Scripts using ``<%= variable.var %>`` format

   RUN AS USER
     By default script are execute as ``morpheus-node``. To execute as another User, populate ``RUN AS USER`` and ensure proper user permissions & group access.
   SUDO
     Flag ``SUDO`` if sudo is required to execute the Script


To attach scripts and templates that have been added to the Library to a node type, start typing the name and then select the script(s) and/or template(s).

* Multiple scripts and templates can be added to a node type
* Scripts and Templates can be added/shared among multiple node types
* The Execution Phase can be set for scripts in the Scripts section.
* Search will populate Scripts or Templates containing the characters entered anywhere in their name, not just the first letter(s) of the name.
