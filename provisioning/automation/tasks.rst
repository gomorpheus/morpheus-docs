Tasks
-----

.. |ansible| image:: /images/automation/tasks/ansible-e488f61cefa223236abd1b40af950439.png
.. |ansibletower| image:: /images/automation/tasks/ansible_tower_logo.png
.. |chef| image:: /images/automation/tasks/chef-66ca1aef7d659471d9219530dd576ce9.png
.. |email| image:: /images/automation/tasks/email_logo.png
.. |groovy| image:: /images/automation/tasks/groovy-3ae2a0a8a649cf64717fc8b159d6836b.png
.. |http| image:: /images/automation/tasks/http-2d0ab035cb2ee622c520ad3e013e959d.png
.. |javascript| image:: /images/automation/tasks/javascript-1b4151066591cf1150ce76904e63dd04.png
.. |jruby| image:: /images/automation/tasks/jruby-3de7c63116cea7cce4116db537ac2458.png
.. |python| image:: /images/automation/tasks/jython-842a43046c24ba18f4d78088bce6105f.png
.. |restart| image:: /images/automation/tasks/restart-9fefb1980aa7ff8ecd7f782f19376cda.png
.. |shellscript| image:: /images/automation/tasks/script-501d006c699c8ffbb471e05e1b975005.png
.. |template| image:: /images/automation/tasks/containerTemplate-cd1594dec2fd11d5709e12cb94e22d68.png
.. |ssh| image:: /images/automation/tasks/ssh-ab1b26b75b17c3ef85f99afdadeb0371.png
.. |powershell| image:: /images/automation/tasks/winrm-944c5bdddc2dc53b1c32dda533a09ee8.png
.. |libraryscript| image:: /images/automation/tasks/containerScript-5ec043b7a9611549f58ae27d9e9aa88a.png
.. |puppet| image:: /images/automation/tasks/puppet-d39e3a20a47d04a44d6d2a854b2acd65.png
.. |localscript| image:: /images/automation/tasks/localScript-bfbe0063e4e6c35ed1c4e5898c88e007.png
.. |vro| image:: /images/automation/tasks/vro_logo.png

Overview
^^^^^^^^

There are many Task Types available, including scripts added directly, scripts and templates from the Library section, recipes, playbooks, salt states, puppet agent installs, and http (api) calls. Tasks are primarily created for use in Workflows, but a single Task can be executed on an existing instance via ``Actions -> Run Task``.

Role Permissions
````````````````

The User Role Permission 'Provisioning: Tasks  FULL' is required to create, edit and delete tasks.

Tasks Types that can execute locally against the |morpheus| Appliance have an additional Role Permission: ``Tasks - Script Engines``. Script Engine Task Types will be hidden for users without ``Tasks - Script Engines`` role permissions.

Task Types
^^^^^^^^^^

.. list-table:: **Available Task Types**
   :header-rows: 1

   * -
     - Task Type
     - Task Description
     - Source Options
     - Execute Target Options
     - Configuration Requirements
     - Role Permissions Requirements
   * - |ansible|
     - Ansible
     - Runs an Ansible playbook. Ansible Integration required
     - Ansible Repo (Git)
     - Local, Resource
     - Existing Ansible Integration
     - Provisioning: Tasks
   * - |ansibletower|
     - Ansible Tower
     - Relays Ansible calls to Ansible Tower
     - Tower Integration
     - Local, Remote, Resource
     - Existing Ansible Tower Integration
     - Provisioning: Tasks
   * - |chef|
     - Chef bootstrap
     - Executes Chef bootstrap and run list. Chef Integration required
     - Chef Server
     - Resource
     - Existing Chef Integration
     - Provisioning: Tasks
   * - |Email|
     - Email
     - Send an email from a Workflow
     - Task Content
     - Local
     - SMTP Configured
     - Provisioning: Tasks
   * - |groovy|
     - Groovy script
     - Executes Groovy Script locally (on |morpheus| app node)
     - Local, Repository, Url
     - Local
     - None
     - Provisioning: Tasks, Tasks - Script Engines
   * - |http|
     - HTTP
     - Executes REST call for targeting external API's.
     - Local
     - Local
     - None
     - Provisioning: Tasks
   * - |javascript|
     - Javascript
     - Executes Javascript locally (on |morpheus| app node)
     - Local
     - Local
     - None
     - Provisioning: Tasks, Tasks - Script Engines
   * - |jruby|
     - jRuby Scirpt
     - Executes Ruby script locally (on |morpheus| app node)
     - Local, Repository, Url
     - Local
     - None
     - Provisioning: Tasks, Tasks - Script Engines
   * - |libraryscript|
     - Library Script
     - Creates a Task from an existing Library Script (``Provisioning -> Library -> Scripts``)
     - Library Script
     - Resource
     - Existing Library Script
     - Provisioning: Tasks
   * - |template|
     - Library Template
     - Creates a Task from an existing Library Template (``Provisioning -> Library-> Templates``)
     - Library Template
     - Resource
     - Existing Library Templates
     - Provisioning: Tasks
   * - |powershell|
     - PowerShell Script
     - Execute PowerShell Script on the Target Resource
     - Local, Repository, Url
     - Remote, Resource
     - None
     - Provisioning: Tasks
   * - |puppet|
     - Puppet Agent Install
     - Executes Puppet Agent bootstrap, writes ``puppet.conf`` and triggers agent checkin. Puppet Integration required
     - Puppet Master
     - Resource
     - Existing Puppet Integration
     - Provisioning: Tasks
   * - |Python|
     - Python Script
     - Executes Python Script locally
     - Local, Repository, Url
     - Local
     - ``virtualenv`` installed on Appliance Nodes (``pip install virtualenv``)
     - Provisioning: Tasks, Tasks - Script Engines
   * - |restart|
     - Restart
     - Restarts target VM/Host/Container and confirms startup status before executing next task in Workflow
     - System
     - Resource
     - None
     - Provisioning: Tasks
   * - |shellscript|
     - Shell Script
     - Executes Bash script on the Target Resource
     - Local, Repository, Url
     - Local, Remote, Resource
     - None
     - Provisioning: Tasks
   * - |vro|
     - vRealize Orchestrator Workflow
     - Executes vRO Workflow on the Target Resource
     - vRO Integraiton
     - Local, Resource
     - Existing vRO Integration
     - Provisioning: Tasks

|ansible| Ansible Playbook
``````````````````````````
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
`````````````````````
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
``````````````````````
:Description:
  Executes Groovy Script locally (on app node)
:Target:
  Local App Node
:Role Permissions:
  Provisioning: Tasks
  Provisioning: Tasks - Script Engines
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

Email
`````
:Description:
  Allows for sending of email via Workflows
:Target:
  Local
:Role Permissions:
  Provisioning: Tasks
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
:Source:
  Choose local to draft or paste the email directly into the Task. Choose Repository or URL to bring in a template from a Git repository or an outside source
:Email Address:
  Email addresses can be entered literally or Morpheus automation variables can be injected, such as ``<%=instance.createdByEmail%>``
:Subject:
  Morpheus automation variables can be injected into the subject field when needed
:Content:
  The body of the email is HTML. Morpheus automation variables can be injected into the email body when needed
:Skip Wrapped Email Template:
  The |morpheus| email template is ignored and only HTML in the Content field is used

|http| HTTP (api)
`````````````````
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
  IGNORE SSL ERRORS
    Mark when making REST calls to systems without a trusted SSL certificate

|javascript| Javascript
```````````````````````
:Description:
  Executes Javascript locally (on app node)
:Target:
  Local App Node
:Role Permissions:
  Provisioning: Tasks
  Provisioning: Tasks - Script Engines
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
````````````````````
:Description:
  Executes Ruby script locally (on app node)
:Target:
  Local App Node
:Role Permissions:
  Provisioning: Tasks
  Provisioning: Tasks - Script Engines
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
``````````````````````````````
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
```````````````````````````
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

PowerShell Script
`````````````````

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
    IP Address of the PowerShell task target
  PORT
    SSH port for PowerShell task target (5985 default)
  USERNAME
    Username for PowerShell task target
  PASSWORD
    Password for PowerShell task target
  SCRIPT
    Enter Script to execute


|puppet| Puppet Agent Install
`````````````````````````````
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


|python| Python Script
``````````````````````

.. IMPORTANT:: Beginning with |morpheus| version 4.2.1, Python Tasks use virtual environments. For this reason, "virtualenv" must be installed on your appliances in order to work with Python tasks. Connect to the appliance node(s) and run "pip install virtualenv".

:Description:
  Executes Python script locally (on app node)
:Target:
  Local App Node
:Role Permissions:
  Provisioning: Tasks
  Provisioning: Tasks - Script Engines
:Task Configuration:
  NAME
    Name of the Task
  CODE
    Unique code name for api, cli, and variable reference
  TYPE
    Python Script
  RESULT TYPE
    - None
    - Single Value
    - Key/Value Pairs
    - JSON
  SCRIPT
    Python Script Script to execute


|restart| Restart
`````````````````
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

|shellscript| Shell Script
``````````````````````````
:Description:
  Executes Bash script locally (on |morpheus| app node), against the Instance or Host the Task or Workflow is run on, or against the IP specified in the Task
:Target:
  Instance or Host, specified IP, or the local app node
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

Task Management
^^^^^^^^^^^^^^^

Adding Tasks
````````````

#. Select the Provisioning link in the navigation bar.
#. Select Automation from the sub-navigation menu.
#. Click the :guilabel:`Add` button.
#. From the New Task Wizard input a name for the task.
#. Select the type of task from from the type dropdown.
#. Input the appropriate details dependent on the task type you selected from the dropdown.
#. Save

Editing Tasks
`````````````

#. Select the Provisioning link in the navigation bar.
#. Select Automation from the sub-navigation menu.
#. Click the Edit icon on the row of the task you wish to edit.
#. Modify information as needed.
#. Click the Save Changes button to save.

Deleting Tasks
``````````````

#. Select the Provisioning link in the navigation bar.
#. Select Automation from the sub-navigation menu.
#. Click the Delete icon on the row of the task you wish to delete.

.. include:: tasks/taskResults.rst
