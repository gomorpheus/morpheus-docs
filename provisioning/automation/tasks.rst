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


Overview
^^^^^^^^

Task Types
^^^^^^^^^^

.. list-table:: **Available Task Types**
   :header-rows: 1

   * - Logo
     - Task Type
     - Description
     - Target
   * - |ansible|
     - Ansible
     - Runs an Ansible playbook. Ansible Integration required
     - Instance or Host
   * - |chef|
     - Chef bootstrap
     - Executes Chef bootstrap and run list. Chef Integration required
     - Instance or Host
   * - |groovy|
     - Groovy script
     - Executes Groovy Script locally (on |morpheus| app node)
     - Local
   * - |http|
     - HTTP
     - Executes REST call for targeting external API's.
     - URL specified in Task
   * - |javascript|
     - Javascript
     - Executes Javascript locally (on |morpheus| app node)
     - Local
   * - |jruby|
     - jRuby Scirpt
     - Executes Ruby script locally (on |morpheus| app node)
     - Local
   * - |libraryscript|
     - Library Script
     - Allows using an existing script from ``Provisioning -> Library-> Scripts``
     - Instance or Host
   * - |template|
     - Library Template
     - Allows using an existing file Template from ``Provisioning -> Library-> Templates``
     - Instance or Host
   * - |shellscript|
     - Local Shell Script
     - Executes Bash script locally (on |morpheus| app node)
     - Local
   * - |puppet|
     - Puppet Agent Install
     - Executes Puppet Agent bootstrap, writes ``puppet.conf`` and triggers agent checkin. Puppet Integration required
     - Instance or Host
   * - |jython|
     - Python Script (jython)
     - Executes Python script locally (on |morpheus| app node)
     - Local
   * - |shellscript|
     - Remote Shell Task
     - Executes Bash script against the Instance or Host the Task or Workflow is ran on
     - Instance or Host
   * - |restart|
     - Restart
     - Restarts target VM/Host/Container and confirms status before executing next task
     - Instance or Host
   * - |ssh|
     - SSH Script
     - Execute Bash script against IP specified in Task.
     - IP specified in Task
   * - |winrm|
     - WinRM Script
     - Execute Powershell script against IP specified in Task.
     - Instance or Host



Ansible Playbook
`````````````````

Chef Bootstrap
``````````````

Groovy script
``````````````

HTTP
`````

Javascript
```````````

jRuby Script
``````````````

Library Script
``````````````
Adds an existing script from the Library section as a task

Library Template
`````````````````
Adds an existing script from the Library section as a task
Puppet Agent Install
````````````````````

Python Script (jython)
``````````````````````

Shell Script
````````````

SSH Script
``````````

WinRM Script
````````````

Restart
```````
Executes a restart on the Instance. Morpheus will wait until the restart is complete to execute the next task in the workflow phase.


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
