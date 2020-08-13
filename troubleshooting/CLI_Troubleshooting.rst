CLI Troubleshooting
===================

If you have installed the |morpheus| CLI successfully and get a successful login but see this error ``Error Communicating with the Appliance. SSL_connect returned=1 errno=0 state=error: certificate verify failed``

run the command

  .. code-block:: bash

    morpheus remote update {appliancename} --insecure
