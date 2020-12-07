Splunk
------

Overview
^^^^^^^^

The |morpheus| Splunk Integration allows forwarding logs from managed Linux hosts and vm's to a target Splunk listener by changing the rsyslogd config on linux vm's to point to Splunk forwarders. The logs will be forwarded from the clients, not from the |morpheus| Appliance.

Adding Splunk Integration
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Add a syslog listener configuration in Splunk.
#. Navigate to ``Administration > Settings > Logs``
#. Expand the Splunk section
#. Enable the integration
#. Fill in the following:

    Enabled
      Enable the Splunk integration
    Host
      IP or Hostname of the Splunk server.
    Port
      Port configured to access the Splunk server.

#. :guilabel:`SAVE`

Once added, syslogs from managed Linux hosts and vm's will be forwards from the clients to the target Splunk listener.
