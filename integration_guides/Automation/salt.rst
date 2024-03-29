Salt
----

Overview
^^^^^^^^

|morpheus| integrates with an existing Salt Master for seamless deployment of Salt States to Minions provisioned from |morpheus| .

Add Salt Integration
^^^^^^^^^^^^^^^^^^^^

To get started browse to Admin > Integrations from within |morpheus| .

Once there simply add a New Integration

.. image:: /images/administration/salt-af3ca.png

And then scope the integration to your existing Salt Master by ip address.  Make sure that the username entered is one with proper escalation privileges for running Salt, and point the Working Directory at the directory on your Master where your States live.

.. NOTE:: |morpheus| will allow you to run States from a git backend, but in v2.10 you will not see states from a git backend within |morpheus|

.. image:: /images/administration/salt-a41c9.png

Scope Salt Integration to Group Or Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuration Management integrations like Saltstack apply to the Infrastructure Group abstraction in |morpheus| .  To ties yours in, browse to ``Infrastructure > Groups`` in |morpheus| and select the group that you would like to tie to your Salt Master.

From here select `Edit`

.. image:: /images/administration/salt-991dd.png

And from the options toggle Advanced Options and select your Saltstack integration in the Config Management dropdown.

.. image:: /images/administration/salt-be548.png

After a page refresh you should see your Saltstack tab in your group page

.. image:: /images/administration/salt-b5b6f.png

Clicking on it will reveal a page that includes:

#. An interface to run Salt Master commands

#. Parsed Top File

#. Available States

.. image:: /images/administration/salt-ccaca.png

The classic example of running

.. code-block:: bash

   salt '*' test.ping

will return empty unless there are existing Minions with accepted keys on the Master.  However, provisioning Minions via |morpheus| is extremely easy.

Provisioning with Saltstack
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To do so, provision as usual and Instances within the Group tied to the Saltstack Integration will now show additional options on the Configure pane

.. image:: /images/administration/salt-413c5.png

Minion ID defaults to the hostname, and a State can be applied directly at provision time.

.. NOTE:: Only States served from the Master's Working Directory can be applied at provision, not States from a git backend

Once your instance is provisioned and key negotiation has completed you will be able to access it and run commands via the integrated Salt command center in your Group.

.. image:: /images/administration/salt-f8e4e.png

If you did not apply a state at provision time now you will be able to run State commands through |morpheus| .

.. image:: /images/administration/salt-71b7c.png

In our example the Apache State from a git backend was applied successfully to our newly created vm.

.. image:: /images/administration/salt-bf299.png
