Email Settings
^^^^^^^^^^^^^^

A default installation of Morpheus uses a online service called postmarkapp. Morpheus api requests to the postmarkapp service to send notification e-mails.

To add your own SMTP server you will need to go to the Administration and Settings of your Morpheus appliance. You will then need to provide Morpheus the following information, your mail server systems administrator should provide you with the below information and the preferred encryption method.

* From Address
* SMTP Server
* SMTP Port
* SSL Enabled
* TLS Encryption
* SMTP User
* SMTP Password

We recommend that you add your Morpheus server to your SMTP white list as well as using user authentication as an additional security measure.

Once you have added your SMTP server information into Morpheus scroll down the Administration and Settings page and press the blue save button which can be found under enabled clouds.

When you have saved your SMTP server settings in the Morpheus appliance you will then need to restart the Morpheus-ui. To restart the Morpheus-ui connection to your Morpheus server via ssh and run the below command.

``sudo morpheus-ctl restart morpheus-ui``

.. IMPORTANT:: If you do not restart the Morpheus-ui the notifications will be sent by the original notification service postmarkapp. Please note it can take up to 3 minutes for the ui to become reachable again.
 has a built in SMTP server for email notifications and alerts. An alternate SMTP server can be specified below:

Add an alternate SMTP Server:

* From Address
* SMTP Server
* SMTP Port
* SSL Enabled
* TLS Encryption
* SMTP User
* SMTP Password
