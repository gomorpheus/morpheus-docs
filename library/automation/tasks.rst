.. role:: raw-html(raw)
    :format: html

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
.. |wa| image:: /images/automation/tasks/writeAttributes.png

Overview
^^^^^^^^

There are many Task Types available, including scripts added directly, scripts and templates from the Library section, recipes, playbooks, salt states, puppet agent installs, and http (api) calls. Tasks are primarily created for use in Workflows, but a single Task can be executed on an existing instance via ``Actions > Run Task``.

Role Permissions
````````````````

The User Role Permission 'Provisioning: Tasks  FULL' is required to create, edit and delete tasks.

Tasks Types that can execute locally against the |morpheus| Appliance have an additional Role Permission: ``Tasks - Script Engines``. Script Engine Task Types will be hidden for users without ``Tasks - Script Engines`` role permissions.

Common Options
^^^^^^^^^^^^^^

When creating a Task, the required and optional inputs will vary significantly by the Task type. However, there are options which are common to Tasks of all types.

Target Options
``````````````

When creating a Task, users can select a target to perform the execution. Some Task types allow for any of the three execution targets listed below and some will limit the user to two or just one. The table in the next section lists the available execution targets for each Task type.

- **Resource:** A |morpheus|-managed Instance or server is selected to execute the Task
- **Local:** The Task is executed by the |morpheus| appliance node
- **Remote:** The user specifies a remote box which will execute the Task

Execute Options
```````````````

- **Retryable:** When marked, this Task can be configured to be retried in the event of failure
- **Retry Count:** The maximum number of times the Task will be retried when there is a failure
- **Retry Delay:** The length of time (in seconds) |morpheus| will wait to retry the Task
- **Allow Custom Config:** When marked, a text area is provided at Task execution time to allow the user to pass extra variables or specify extra configuration. See the next section for an example.

Allow Custom Config
```````````````````

When "Allow Custom Config" is marked on a Task, the user is shown a text area for custom configuration when the Task is executed manually from the Tasks List Page. If the Task is to be part of an Operational Workflow, mark the same box on the Workflow rather than on the Task to see the text area at execution time. This text area is inside the "Advanced Options" section, which must be expanded in order to reveal the text area. Within the text area, add a JSON map of key-value pairs which can be resolved within your automation scripts. This could be used to pass extra variables that aren't always needed in the script or for specifying extra configuration.

**Example JSON Map:**

.. code-block::

  {"key1": "value1",
  "key2": "value2",
  "os": "linux",
  "foo": "bar"}

When the Task is executed, these extra variables would be resolved where called into the script such as in the following simple BASH script example:

.. code-block:: bash

  echo "<%=customOptions.os%>"
  echo "<%=customOptions.foo%>"

The above example would result in the following output:

.. code-block::

  linux
  bar

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
     - Creates a Task from an existing Library Script (|LibTemScr|)
     - Library Script
     - Resource
     - Existing Library Script
     - Provisioning: Tasks
   * - |template|
     - Library Template
     - Creates a Task from an existing Library Template (|LibTemSpe|)
     - Library Template
     - Resource
     - Existing Library Templates
     - Provisioning: Tasks
   * - |powershell|
     - PowerShell Script
     - Execute PowerShell Script on the Target Resource
     - Local, Repository, Url
     - Remote, Resource, Local
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
     - ``virtualenv`` installed on Appliance Nodes
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
     - Executes Bash script on the target resource
     - Local, Repository, Url
     - Local, Remote, Resource
     - None
     - Provisioning: Tasks
   * - |vro|
     - vRealize Orchestrator Workflow
     - Executes vRO Workflow on the Target Resource
     - vRO Integration
     - Local, Resource
     - Existing vRO Integration
     - Provisioning: Tasks
   * - |wa|
     - Write Attributes
     - Add arbitrary values to the Attributes map of the target resource
     - N/A
     - Local
     - Provide map of values as valid JSON
     - Provisioning: Tasks

Task Configuration
^^^^^^^^^^^^^^^^^^

- .. toggle-header:: :header: **Ansible Playbook**

    |ansible|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **ANSIBLE REPO:** Select existing Ansible Integration
    - **GIT REF:** Specify tag or branch (Option, blank assumes default)
    - **PLAYBOOK:** Name of playbook to execute, both ``playbook`` and ``playbook.yml`` format supported
    - **TAGS:** Enter comma separated tags to filter executed tasks by (ie ``--tags``)
    - **SKIP TAGS:** Enter comma separated tags to run the playbook without matching tagged tasks (ie ``--skip-tags``)

    .. IMPORTANT:: Using different Git Refs for multiple Ansible Tasks in same Workflow is not supported. Git Refs can vary between Workflows, but Tasks in each Workflow must use the same Git Ref.

- .. toggle-header:: :header: **Ansible Tower Job**

    |ansibletower|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **TOWER INTEGRATION:** Select an existing Ansible Tower integration
    - **INVENTORY:** Select an existing Inventory, when bootstrapping an Instance, |morpheus| will add the Instance to the Inventory
    - **GROUP:** Enter a group name, when bootstrapping an Instance, |morpheus| will add the Instance to the Group if it exists. If it does not exist, |morpheus| will create the Group
    - **JOB TEMPLATE:** Select an existing job template to associate with the Task
    - **SCM OVERRIDE:** If needed, specify an SCM branch other than that specified on the template
    - **EXECUTE MODE:** Select Limit to Instance (template is executed only on Instance provisioned), Limit to Group (template is executed on all hosts in the Group), Run for all (template is executed on all hosts in the Inventory), or Skip Execution (to skip execution of the template on the Instance provisioned)

- .. toggle-header:: :header: **Chef bootstrap**

    |chef|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **CHEF SERVER:** Select existing Chef integration
    - **ENVIRONMENT:** Populate Chef environment, or leave as ``_default``
    - **RUN LIST:** Enter Run List, eg ``role[web]``
    - **DATA BAG KEY:** Enter data bag key (will be masked upon save)
    - **DATA BAG KEY PATH:** Enter data bag key path, eg ``/etc/chef/databag_secret``
    - **NODE NAME:** Defaults to Instance name, configurable
    - **NODE ATTRIBUTES:** Specify attributes inside the ``{}``

- .. toggle-header:: :header: **Groovy script**

    |groovy|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **RESULT TYPE:** Single Value, Key/Value Pairs, or JSON
    - **CONTENT:** Contents of the Groovy script if not sourcing it from a repository

- .. toggle-header:: :header: **Email**

    |email|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **SOURCE:** Choose local to draft or paste the email directly into the Task. Choose Repository or URL to bring in a template from a Git repository or another outside source
    - **EMAIL ADDRESS:** Email addresses can be entered literally or |morpheus| automation variables can be injected, such as ``<%=instance.createdByEmail%>``
    - **SUBJECT:** The subject line of the email, |morpheus| automation variables can be injected into the subject field
    - **CONTENT:** The body of the email is HTML. |morpheus| automation variables can be injected into the email body when needed
    - **SKIP WRAPPED EMAIL TEMPLATE:** The |morpheus|-styled email template is ignored and only HTML in the Content field is used

    .. TIP:: To whitelabel email sent from Tasks, select SKIP WRAPPED EMAIL TEMPLATE and use an HTML template with your own CSS styling

- .. toggle-header:: :header: **HTTP (API)**

    |http|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **RESULT TYPE:** Single Value, Key/Value Pairs, or JSON
    - **URL:** An HTTP or HTTPS URL as the HTTP Task target
    - **HTTP METHOD:** GET (default), POST, PUT, PATCH, HEAD, or DELETE
    - **AUTH USER:** Username for username/password authentication
    - **PASSWORD:** Password for username/password authentication
    - **BODY:** Request Body
    - **HTTP HEADERS:** Enter requests headers, examples below:

    .. list-table::

      * - Authorization
        - Bearer `token`
      * - Content-Type
        - application/json

    - **IGNORE SSL ERRORS:** Mark when making REST calls to systems without a trusted SSL certificate

- .. toggle-header:: :header: **Javascript**

    |javascript|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **RESULT TYPE:** Single Value, Key/Value Pairs, or JSON
    - **SCRIPT:** Javascript contents to execute

- .. toggle-header:: :header: **jRuby Script**

    |jruby|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **RESULT TYPE:** Single Value, Key/Value Pairs, or JSON
    - **CONTENT:** Contents of the jRuby script is entered here if it's not being called in from an outside source

- .. toggle-header:: :header: **Library Script**

    |libraryscript|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **RESULT TYPE:** Single Value, Key/Value Pairs, or JSON
    - **SCRIPT:** Search for an existing script in the typeahead field

- .. toggle-header:: :header: **Library Template**

    |template|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **TEMPLATE:** Search for an existing template in the typeahead field

- .. toggle-header:: :header: **Powershell Script**

    |powershell|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **RESULT TYPE:** Single Value, Key/Value Pairs, or JSON
    - **ELEVATED SHELL:** Run script with administrator privileges
    - **IP ADDRESS:** IP address of the PowerShell Task target
    - **PORT:** SSH port for PowerShell Task target (5985 default)
    - **USERNAME:** Username for PowerShell Task target
    - **PASSWORD:** Password for PowerShell Task target
    - **Content:**  Enter script to execute if not calling the script in from an outside source

    .. NOTE:: Setting the execution target to local requires Powershell to be installed on the |morpheus| appliance box(es). `Microsoft Documentation <https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-linux?view=powershell-7.2>`_ contains installation instructions for all major Linux distributions and versions.



- .. toggle-header:: :header: **Puppet Agent Install**

    |puppet|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **PUPPET MASTER:** Select Puppet Master from an existing Puppet integration
    - **PUPPET NODE NAME:** Enter Puppet node name. Variables supported eg. ``<%= instance.name %>``
    - **PUPPET ENVIRONMENT:** Enter Puppet environment, eg. ``production``

- .. toggle-header:: :header: **Python Script**

    |python|

    .. IMPORTANT:: Beginning with |morpheus| version 4.2.1, Python Tasks use virtual environments. For this reason, ``virtualenv`` must be installed on your appliances in order to work with Python Tasks. See the information below for more detailed steps to install ``virtualenv`` on your |morpheus| appliance node(s).

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **RESULT TYPE:** Single Value, Key/Value Pairs, or JSON
    - **CONTENT:** Python script to execute is entered here if not pulled in from an outside repository
    - **COMMAND ARGUMENTS:** Optional arguments passed into the Python script. Variables supported eg. ``<%= instance.name %>``
    - **ADDITIONAL PACKAGES:** Additional packages to be installed after ``requirements.txt`` (if detected). Expected format for additional packages: 'packageName==x.x.x packageName2==x.x.x', the version must be specified
    - **PYTHON BINARY:** Optional binary to override the default Python binary

    :raw-html:`<br />`

    Python and |morpheus|
    `````````````````````

    **Enterprise Proxy Considerations**

    Additional considerations must be made in enterprise proxy environments where Python Tasks are run with additional package download requirements. These additional packages are downloaded using ``pip`` and may not obey global |morpheus| proxy rules. To deal with this, create or edit the pip configuration file at ``/etc/pip.conf``. Your configuration should include something like the following:

    .. code-block:: bash

      [global]
      proxy = http://some-proxy-ip.com:8087

    For more information, review the Pip documentation on using proxy servers `here <https://pip.pypa.io/en/stable/user_guide/#using-a-proxy-server>`_.

    **CentOS 7 / Python 2.7 (RHEL system Python)**

    With a fresh install of |morpheus| on a default build of CentOS 7, Python Tasks will not function due to the missing requirement of ``virtualenv``.

    If you attempt to run a python task, you will get an error similar to the following:

    .. code-block:: bash

      Task Execution Failed on Attempt 1
      sudo: /tmp/py-8ae51ebf-749c-4354-b6e4-11ce541afad5/bin/python: command not found

    In order to run |morpheus| Python Tasks in CentOS 7, install ``virtualenv``: ``yum install python-virtualenv``

    If you require ``python3``, you can specify the binary to be used while building the virtual environment. In a default install, do the following: ``yum install python3``. Then, in your |morpheus| Python Task, specify the binary in the PYTHON BINARY field as "/bin/python3". This will build a virtual environment in ``/tmp`` using the ``python3`` binary, which is equivalent to making a virtual environment like so: ``virtualenv ~/venv -p /bin/python3``.

    If you wish to install additional Python packages into the virtual environment, put them in ``pip`` format and space-separated into the ADDITIONAL PACKAGES field on the Python Task. Use the help text below the field to ensure correct formatting.

    **CentOS 8 and Python**

    In CentOS 8, Python is not installed by default. There is a ``platform-python`` but that should not be used for anything in userland. The error message with a default install of CentOS 8 will be similar to this:

    .. code-block:: bash

      Task Execution Failed on Attempt 1
      sudo: /tmp/py-cffc9a8f-c40d-451d-956e-d6e9185ade33/bin/python: command not found

    The default ``virtualenv`` for CentOS 8 is the python3 variety, for |morpheus| to use Python Tasks, do the following: ``yum install python3-virtualenv``

    If Python2 is required, do the following: ``yum install python2`` and specify ``/bin/python2`` as the PYTHON BINARY in your |morpheus| Task.

    This will build a ``virtualenv`` in ``/tmp`` using the ``python2`` binary, which is equivalent to making a ``virtualenv`` like so: ``virtualenv ~/venv -p /bin/python2``

    If you wish to install additional Python packages into the virtual environment, put them in ``pip`` format and space-separated into the ADDITIONAL PACKAGES field on the Python Task. Use the help text below the field to ensure correct formatting.

- .. toggle-header:: :header: **Restart**

    |restart|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references

- .. toggle-header:: :header: **Shell Script**

    |shellscript|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **RESULT TYPE:** Single Value, Key/Value Pairs, or JSON
    - **SUDO:** Mark the box to run the script as ``sudo``
    - **CONTENT:** Script to execute is entered here if not pulled in from an outside repository

    |

    .. TIP:: When the EXECUTE TARGET option is set to "Local" (in other words, the Task is run on the appliance itself), two additional fields are revealed: GIT REPO and GIT REF. Use GIT REPO to set the PWD shell variable (identifies the current working directory) to the locally cached repository (ex. /var/opt/morpheus-node/morpheus-local/repo/git/76fecffdf1fe96516e90becdab9de) and GIT REF to identify the Git branch the Task should be run from if the default (typically main or master) shouldn't be used. If these options are not set, the working folder will be /opt/morpheus/lib/tomcat/temp which would not allow scripts to reference file paths relative to the repository (if needed).

- .. toggle-header:: :header: **vRealize Orchestrator Workflow**

    |vro|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **RESULT TYPE:** Single Value, Key/Value Pairs, or JSON
    - **vRO INTEGRATION:** Select an existing vRO integration
    - **WORKFLOW:** Select a vRO workflow from the list synced from the selected integration
    - **PARAMETER BODY (JSON):**

- .. toggle-header:: :header: **Write Attributes**

    |wa|

    - **NAME:** Name of the Task
    - **CODE:** Unique code name for API, CLI, and variable references
    - **ATTRIBUTES:** A JSON map of arbitrary values to write to the attributes property of the target resource

    |

    .. TIP:: This is often useful for storing values from one phase of a Provisioning Workflow for access in another phase. See the video demo below for a complete example.

    .. raw:: html

        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
            <iframe src="//www.youtube.com/embed/7b_HQTRMR2Y" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
        </div>

    |

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
