Tasks
-----

.. |ansible| image:: /images/automation/tasks/ansible-e488f61cefa223236abd1b40af950439.png
.. |chef| image:: /images/automation/tasks/chef-66ca1aef7d659471d9219530dd576ce9.png
.. |groovy| image:: /images/automation/tasks/groovy-3ae2a0a8a649cf64717fc8b159d6836b.png
.. |http| image:: /images/automation/tasks/http-2d0ab035cb2ee622c520ad3e013e959d.png
.. |javascript| image:: /images/automation/tasks/javascript-1b4151066591cf1150ce76904e63dd04.png
.. |jruby| image:: /images/automation/tasks/jruby-3de7c63116cea7cce4116db537ac2458.png
.. |jython| image:: /images/automation/tasks/jython-842a43046c24ba18f4d78088bce6105f.png
.. |restart| image:: /images/automation/tasks/restart-9fefb1980aa7ff8ecd7f782f19376cda.png
.. |shellscript| image:: /images/automation/tasks/script-501d006c699c8ffbb471e05e1b975005.png
.. |template| image:: /images/automation/tasks/containerTemplate-cd1594dec2fd11d5709e12cb94e22d68.png
.. |ssh| image:: /images/automation/tasks/ssh-ab1b26b75b17c3ef85f99afdadeb0371.png
.. |winrm| image:: /images/automation/tasks/winrm-944c5bdddc2dc53b1c32dda533a09ee8.png
.. |libraryscript| image:: /images/automation/tasks/containerScript-5ec043b7a9611549f58ae27d9e9aa88a.png
.. |puppet| image:: /images/automation/tasks/puppet-d39e3a20a47d04a44d6d2a854b2acd65.png
.. |localscript| image:: /images/automation/tasks/localScript-bfbe0063e4e6c35ed1c4e5898c88e007.png

Overview
^^^^^^^^

There are many Task Types available, including scripts added directly, scripts and templates from the Library section, recipes, playbooks, salt states, puppet agent installs, and http (api) calls. Tasks are primarily created for use in Workflows, but a single Task can be executed on an existing instance via ``Actions -> Run Task``.

Role Permissions
^^^^^^^^^^^^^^^^^

The User Role Permission 'Provisioning: Tasks  FULL' is required to create, edit and delete tasks.

Tasks Types that can execute locally against the |morpheus| Appliance have an additional Role Permission: ``Tasks - Script Engines``. Script Engine Task Types will be hidden for users without ``Tasks - Script Engines`` role permissions.

Task Types
^^^^^^^^^^

.. list-table:: **Available Task Types**
   :header-rows: 1

   * -
     - Task Type
     - Task Description
     - Task Target
     - Configuration Requirements
     - Role Permissions Requirements
   * - |ansible|
     - Ansible
     - Runs an Ansible playbook. Ansible Integration required
     - Instance or Host
     - Existing Ansible Integration
     - Provisioning: Tasks
   * - |chef|
     - Chef bootstrap
     - Executes Chef bootstrap and run list. Chef Integration required
     - Instance or Host
     - Existing Chef Integration
     - Provisioning: Tasks
   * - |groovy|
     - Groovy script
     - Executes Groovy Script locally (on |morpheus| app node)
     - Local
     - None
     - Provisioning: Tasks, Tasks - Script Engines
   * - |http|
     - HTTP
     - Executes REST call for targeting external API's.
     - URL specified in Task
     - None
     - Provisioning: Tasks
   * - |javascript|
     - Javascript
     - Executes Javascript locally (on |morpheus| app node)
     - Local
     - None
     - Provisioning: Tasks, Tasks - Script Engines
   * - |jruby|
     - jRuby Scirpt
     - Executes Ruby script locally (on |morpheus| app node)
     - Local
     - None
     - Provisioning: Tasks, Tasks - Script Engines
   * - |libraryscript|
     - Library Script
     - Creates a Task from an existing Library Script (``Provisioning -> Library -> Scripts``)
     - Instance or Host
     - Existing Library Script
     - Provisioning: Tasks
   * - |template|
     - Library Template
     - Creates a Task from an existing Library Template (``Provisioning -> Library-> Templates``)
     - Instance or Host
     - Existing Library Templates
     - Provisioning: Tasks
   * - |localscript|
     - Local Shell Script
     - Executes Bash script locally (on |morpheus| app node)
     - Local
     - None
     - Provisioning: Tasks, Tasks - Script Engines
   * - |puppet|
     - Puppet Agent Install
     - Executes Puppet Agent bootstrap, writes ``puppet.conf`` and triggers agent checkin. Puppet Integration required
     - Instance or Host
     - Existing Puppet Integration
     - Provisioning: Tasks
   * - |jython|
     - Python Script (jython)
     - Executes Python script locally (on |morpheus| app node)
     - Local
     - None
     - Provisioning: Tasks, Tasks - Script Engines
   * - |shellscript|
     - Remote Shell Script
     - Executes Bash script against the Instance or Host the Task or Workflow is ran on
     - Instance or Host
     - None
     - Provisioning: Tasks
   * - |restart|
     - Restart
     - Restarts target VM/Host/Container and confirms status before executing next task in Workflow
     - Instance or Host
     - None
     - Provisioning: Tasks
   * - |ssh|
     - SSH Script
     - Execute Bash script against IP specified in Task.
     - IP specified in Task
     - None
     - Provisioning: Tasks
   * - |winrm|
     - WinRM Script
     - Execute Powershell script against IP specified in Task.
     - IP specified in Task
     - None
     - Provisioning: Tasks


|ansible| Ansible Playbook
``````````````````````````````````
:Description:
       Runs an Ansible playbook. Ansible Integration required
:Target:
       Instance or Host
:Role Permissions:
       Provisioning: Tasks
:Task Configuration:
   NAME
     Name of the Task
   CODE
     Unique code name for api, cli, and variable reference
   ANSIBLE REPO
    Select existing Ansible Integration
   GIT REF
    Specify tag or branch (Option, blank assumes default)
   PLAYBOOK
    Name of playbook to execute
       Both ``playbook`` and ``playbook.yml`` format supported
   TAGS
    Enter comma separated tags to filter executed tasks by (ie ``--tags``)
   SKIP TAGS
    Enter comma separated tags to run the playbook without matching tagged tasks (ie ``--skip-tags``)

   .. IMPORTANT:: Using different Git Ref's for multiple Ansible Tasks in same Workflow is not supported. Git Refs can vary between Workflows, but Tasks in each workflow must use the same Git Ref.

|chef| Chef Bootstrap
````````````````````````````
:Description:
  Executes Chef bootstrap and run list. Chef Integration required
:Target:
  Instance or Host
:Role Permissions:
  Provisioning: Tasks
:Task Configuration:
  NAME
   Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  CHEF SERVER
    Select existing Chef Integration
  ENVIRONMENT
    Populate Chef environment, or leave as ``_default``
  RUN LIST
    Enter Run List, eg ``role[web]``
  DATA BAG KEY
    Enter data bag key (will be masked uon save)
  DATA BAG KEY PATH
    Enter data bag key path, eg ``/etc/chef/databag_secret``
  NODE NAME
    Defaults to instance name, configurable.
  NODE ATTRIBUTES
    Specify attributes inside the ``{}``


|groovy| Groovy script
```````````````````````
:Description:
  Executes Groovy Script locally (on app node)
:Target:
  Local App Node
:Role Permissions:
  Provisioning: Tasks, Tasks - Script Engines
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  RESULT TYPE
    - Single Value
    - Key/Value Pairs
    - JSON
  SCRIPT
    Contents of Groovy Script to execute


|http| HTTP (api)
```````````````````
:Description:
  Executes REST call for targeting external API's.
:Target:
  URL specified in Task
:Role Permissions:
  Provisioning: Tasks
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  RESULT TYPE
    - Single Value
    - Key/Value Pairs
    - JSON
  URL
    http or https url for http task target
  HTTP METHOD
    GET (default), POST, PUT, PATCH, HEAD, or DELETE
  AUTH USER
    Username for username/password authentication
  PASSWORD
    Password for username/password authentication
  BODY
    Request Body
  HTTP HEADERS
    Enter requests headers
      .. list-table:: **Http Header examples**

         * - Authorization
           - Bearer `token`
         * - Content-Type
           - application/json

|javascript| Javascript
```````````````````````
:Description:
  Executes Javascript locally (on app node)
:Target:
  Local App Node
:Role Permissions:
  Provisioning: Tasks, Tasks - Script Engines
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  RESULT TYPE
    - Single Value
    - Key/Value Pairs
    - JSON
  SCRIPT
    Contents of Javascript to execute


|jruby| jRuby Script
````````````````````````````
:Description:
  Executes Ruby script locally (on app node)
:Target:
  Local App Node
:Role Permissions:
  Provisioning: Tasks, Tasks - Script Engines
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  RESULT TYPE
    - Single Value
    - Key/Value Pairs
    - JSON
  SCRIPT
    Contents of jRuby Script to execute


|libraryscript| Library Script
```````````````````````````````
:Description:
  Creates a Task for an existing Library Script (``Provisioning -> Library -> Scripts``)
:Target:
  Instance or Host
:Role Permissions:
  Provisioning: Tasks
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  RESULT TYPE
    - Single Value
    - Key/Value Pairs
    - JSON
  SCRIPT
    Search for and select existing Library Script

|template| Library Template
```````````````````````````````
:Description:
  Creates a Task for an existing Library Template (``Provisioning -> Library-> Templates``)
:Target:
  Instance or Host
:Role Permissions:
  Provisioning: Tasks
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  TEMPLATE
    Search for and select existing Library Template

|localscript| Local Shell Script
`````````````````````````````````
:Description:
  Executes Bash script locally (on |morpheus| app node)
:Target:
  Local App Node
:Role Permissions:
  Provisioning: Tasks, Tasks - Script Engines
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  RESULT TYPE
    - Single Value
    - Key/Value Pairs
    - JSON
  GIT REPO
    Select a Git Repo which can be referenced in the Script.
  GIT REF
    Specify git ref such as branch
  SCRIPT
    Bash Script to execute. If a Git Repo is specified, files in the repo can be called in the script.

|puppet| Puppet Agent Install
```````````````````````````````````
:Description:
  Executes Puppet Agent bootstrap, writes ``puppet.conf`` and triggers agent checkin. Puppet Integration required
:Target:
  Instance or Host
:Role Permissions:
  Provisioning: Tasks
:Task Configuration:
  NAME
    Name of the Task
  PUPPET MASTER
    Select Puppet Master from existing Puppet Integration
  PUPPET NODE NAME
    Enter Puppet Node Name. Variables supported eg. ``"<%= instance.name %>"``
  PUPPET ENVIRONMENT
    Enter Puppet Env. eg. ``production``


|jython| Python Script (jython)
`````````````````````````````````````
:Description:
  Executes Python script locally (on app node)
:Target:
  Local App Node
:Role Permissions:
  Provisioning: Tasks, Tasks - Script Engines
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  TYPE
    Python Script (jython)
  RESULT TYPE
    - Single Value
    - Key/Value Pairs
    - JSON
  SCRIPT
    Python Script (jython) Script to execute

|shellscript| Remote Shell Script
``````````````````````````````````
:Description:
  Executes Bash script against the Instance or Host the Task or Workflow is ran on
:Target:
  Instance or Host
:Role Permissions:
  Provisioning: Tasks
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  RESULT TYPE
    - Single Value
    - Key/Value Pairs
    - JSON
  SCRIPT
    Enter Bash Script to execute

|restart| Restart
``````````````````````
:Description:
  Specifically for use in Workflows after a task that requires a restart, the Restart task executes a restart on the target Instance or Host. Morpheus will wait until the restart is complete to execute the next task in the workflow phase.
:Target:
  Instance or Host
:Role Permissions:
  Provisioning: Tasks
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference

|ssh| SSH Script
`````````````````````````
:Description:
  Execute Bash script against IP specified in Task.
:Target:
  IP specified in Task
:Role Permissions:
  Provisioning: Tasks
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  RESULT TYPE
    - Single Value
    - Key/Value Pairs
    - JSON
  IP ADDRESS
    IP Address of the ssh task target
  PORT
    SSH port for ssh task target (22 default)
  KEY
    Select existing Keypair for key auth
  USERNAME
    Username for ssh task target
  PASSWORD
    Password for ssh task target
  SCRIPT
    Enter Bash Script to execute


|winrm| WinRM Script
```````````````````````````
:Description:
  Execute Powershell script against IP specified in Task.
:Target:
  IP specified in Task
:Role Permissions:
  Provisioning: Tasks
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  RESULT TYPE
    - Single Value
    - Key/Value Pairs
    - JSON
  IP ADDRESS
    IP Address of the WinRM task target
  PORT
    SSH port for WinRM task target (5985 default)
  USERNAME
    Username for WinRM task target
  PASSWORD
    Password for WinRM task target
  SCRIPT
    Enter Script to execute

To Add Tasks:
^^^^^^^^^^^^^

#. Select the Provisioning link in the navigation bar.
#. Select Automation from the sub-navigation menu.
#. Click the :guilabel:`Add` button.
#. From the New Task Wizard input a name for the task.
#. Select the type of task from from the type dropdown.
#. Input the appropriate details dependent on the task type you selected from the dropdown.
#. Save

Edit Task
^^^^^^^^^

#. Select the Provisioning link in the navigation bar.
#. Select Automation from the sub-navigation menu.
#. Click the Edit icon on the row of the task you wish to edit.
#. Modify information as needed.
#. Click the Save Changes button to save.

Delete Task
^^^^^^^^^^^

#. Select the Provisioning link in the navigation bar.
#. Select Automation from the sub-navigation menu.
#. Click the Delete icon on the row of the task you wish to delete.
