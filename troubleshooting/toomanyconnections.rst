mysql Too many connections error
================================

If you see the following error in the |morpheus| UI logs:

.. code-block:: bash

   SqlExceptionHelper - Data source rejected establishment of connection,  message from server: "Too many connections"

it means the number connections between |morpheus| application and mysql have reached the `max_connections` limit set in mysql (default is 151), or the `max_active` setting, which limits the number of connections on the |morpheus| end (default is 100), and the limit needs to be raised, either in |morpheus| or mysql, or both depending on the number of connections and configuration.

.. note:: The `max_connections` setting in mysql and the maximum used connections between an app node and mysql can be viewed in the |morpheus| ui in the `Operations - Health` section under Database.
