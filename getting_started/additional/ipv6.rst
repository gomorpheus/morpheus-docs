IPv6
-------

Overview
^^^^^^^^

There may be situations where instances only have IPv6 routing available.  |morpheus| fully supports IPv6 for the appliance and agent comms.

To enable IPv6 listener on the |morpheus| appliance, you must modify the NGINX listeners.

Configuring NGINX Listeners
^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Confirm IPv6 is enabled and IP address is applied within the Morpheus underlying OS.

#. Modify the `/opt/morpheus/embedded/nginx/conf/sites-available/morpheus.conf` file, and add the following listerning under the server block at the top:

    .. code-block:: bash

        listen [::]:80;

#. Modify the `/opt/morpheus/embedded/nginx/conf/sites-available/morpheus-ssl.conf` file, and add the following listerning under the server block at the top:

    .. code-block:: bash

        listen [::]:443 ssl;

#. Restart the NGINX service:

    .. code-block:: bash
        morpheus-ctl restart nginx
        
        ok: run: nginx: (pid 47868) 0s

#. The site should now be resolvable via IPv6. To test you should be able to do the following:

    .. code-block:: bash
        curl -k -6 https://[<IPv6 Address>]/ping

        MORPHEUS PING