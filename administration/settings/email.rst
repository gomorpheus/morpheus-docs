Email Settings
^^^^^^^^^^^^^^

In this section, you can configure an SMTP server for email notification delivery. You will need to provide |morpheus| the following information, your mail server systems administrator can assist you in filling these fields and with the preferred encryption method.

* From Address
* SMTP Server
* SMTP Port
* SSL Enabled
* TLS Encryption
* SMTP User
* SMTP Password

We recommend that you add the |morpheus| server to your SMTP whitelist as well as using user authentication as an additional security measure.

Once you have added your SMTP server information into |morpheus|, scroll down to the bottom of the page and press the blue SAVE button which can be found under the Enabled Clouds section.

When you have saved your SMTP server settings in the |morpheus| appliance you will then need to restart the UI. To restart the morpheus-ui, connect to your |morpheus| server via SSH and run the below command:

``sudo morpheus-ctl restart morpheus-ui``

.. IMPORTANT:: If you do not restart morpheus-ui, the notifications will not be sent. Please note it can take up to three minutes for the UI to become reachable again.
