Morpheus UI war files
---------------------

Pre-release or patched versions of the |morpheus| UI are sometimes provided. To deploy the ui war on a |morpheus| Appliance:

#. Download the war file to the target appliance

   .. code-block:: bash

    wget https://url/war_file

   .. note:: If the war file is provided via a droplr link, ensure a ``+`` is added to end of droplr url or the file will not download

#. Backup current war file

   .. code-block:: bash

    sudo mv /opt/morpheus/lib/morpheus/morpheus-ui.war /opt/morpheus/lib/morpheus/morpheus-ui.bak.`date +"%m-%d-%Y"`

#. Move and rename new war file

   .. code-block:: bash

    sudo mv <file> /opt/morpheus/lib/morpheus/morpheus-ui.war 

#. Ensure war is owned by ``morpheus-app``

   .. code-block:: bash

    sudo chown morpheus-app.morpheus-app /opt/morpheus/lib/morpheus/morpheus-ui.war

#. Restart the |morpheus| UI

   .. code-block:: bash

    sudo morpheus-ctl restart morpheus-ui

The new ui war will load on startup!
