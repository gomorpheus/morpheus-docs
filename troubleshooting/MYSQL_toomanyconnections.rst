MySQL Too many connections error
================================

If you see the following error in the |morpheus| UI logs:

.. code-block:: bash

   SqlExceptionHelper - Data source rejected establishment of connection,  message from server: "Too many connections"

it means the number connections between |morpheus| application and mysql have reached the `max_connections` limit set in mysql (default is 151), or the `max_active` setting, which limits the number of connections on the |morpheus| end (default is 150), and the limit needs to be raised, either in |morpheus| or mysql, or both depending on the number of connections and configuration.

.. note:: The `max_connections` setting in mysql and the maximum used connections between an app node and mysql can be viewed in the |morpheus| ui in the `Administration - Health` section under Database.

.. important:: In Single |morpheus| app node configurations, the ``max_active`` setting on the app node must be less than the ``max_connections`` setting in mysql.

.. important:: In HA configurations, the ``max_active`` setting is per app node, and the ``max_connections`` setting in mysql must be greater than all app nodes ``max_active`` values combined, ie ``(max_active`` * $number_of_app_nodes) <= max_connections``.

|morpheus| ``max_active`` setting
---------------------------------

Edit ``/etc/morpheus/morpheus.rb`` and add ``mysql[‘max_active’] = $value`` replacing ``$value`` with desired desired number of maximum connections allowed by |morpheus| to mysql. For example, to set max_active at 150:

.. code-block:: bash

   mysql[‘max_active’] = 150

Replacing 100 with the desired number of maximum connections allowed by |morpheus| to mysql.

Run ``morpheus-ctl reconfigure`` for the setting to be applied. Reconfigure will not restart the ui unless additional ram has been added to the appliance host since the previous reconfigure. To edit the max_active without a reconfigure, update the ``max_active`` setting in ``/opt/morpheus/conf/application.yml``. Please note the default setting of 150 will be applied upon the next reconfigure unless ``max_active`` is defined as instructed above in the ``morpheus.rb`` file.

mysql ``max_connections`` setting
---------------------------------

.. important:: Customers are responsible for configuring and maintaining external databases used by |morpheus|. This explains how to set the ``max_connections`` setting, but the value for the setting needs to be established by a customers qualified db admin.

In mysql prompt,

run ``mysql> SET GLOBAL max_connections = $value;``

This will immediately write the variable, however it is only a temporary setting that will be overwritten upon restart of the mysql service.

To persist the ``max_connections`` setting, edit my.cnf, and add ``max_connections = $value`` replacing ``$value`` with desired value, ie to set max_connections at 300 in in my.cnf, add:

.. code-block:: bash

   max_connections = 300
