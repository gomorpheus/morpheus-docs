Script Templates
----------------

Scripts are bash and Powershell scripts that can be attached to Node Types to always execute at the selected phase when that Node Type is provisioned, added to Workflows as Library Script Tasks, and/or executed ad-hoc on Instances.

Creating Scripts
^^^^^^^^^^^^^^^^

#. Navigate to |LibTemScr|
#. Select :guilabel:`+ ADD`
#. Enter the Following:

   NAME
     Name of the Script in |morpheus|
   SCRIPT TYPE
     - Bash
     - Powershell
   PHASE
     Select which phase the Script will execute when attached to a Node Type. When a script is attached to a Node Type, it will execute according to the selcted phase:

     Start Service
       Any time the Instance action ``Start Service`` is executed
     Stop Service
       Any time the Instance action ``Stop Service`` is executed
     Pre-Provision
       - Containers: Script will execute against the container host before the container is provisioned
       - Virtual Machines: Script will execute before any provision phase Scripts or Tasks
     Provision
       Script will execute once per new Instance node during the provision Phase. Provisioning will not be considered complete until all scripts and tasks in the provisioning phase are completed

       .. NOTE:: Any Script or Task set to the provision phase will be included in the total provision time and impact success/warn/failure provisioning status messages. As an example, your VM could be up and running but if your Script is in the provision phase and fails, provisioning will be marked as a failure.

      Post-Provision
       Script will execute once per new Instance node after the provision phase is completed. Scripts and Tasks in the Post-Provision phase will show execution status and history, but are not considered part of the provision and do not impact provisioning status.
      Pre-Deploy
       Script will execute on target Instance any time a deployment is run against the Instance. The Script will run prior to the deployment file(s) being written
      Deploy
       Script will execute on target Instance any time a deployment is run against the Instance. The script will run after the deployment file(s) are written
      Reconfigure
       Script will execute on target Instance any time a reconfigure is executed against the Instance.
      Teardown
       Script will execute on target Instance upon Instance deletion. Script will execute against target Instance prior to the deletion/removal of resources.

   SCRIPT
     Enter Bash or Powershell script.

     .. note:: |morpheus| variables are supported in Library Scripts using ``<%= variable.var %>`` format

   RUN AS USER
     By default Scripts are execute as ``morpheus-node``. To execute as another User, populate ``RUN AS USER`` and ensure proper user permissions & group access
   SUDO
     Flag ``SUDO`` if sudo is required to execute the Script


To attach Scripts and templates that have been added to the Library to a Node Type, start typing the name and then select the script(s) and/or template(s).

* Multiple scripts and templates can be added to a Node Type
* Scripts and Templates can be added/shared among multiple Node Types
* The execution phase can be set for Scripts in the Scripts section
* Search will populate Scripts or Templates containing the characters entered anywhere in their name, not just the first letter(s) of the name
