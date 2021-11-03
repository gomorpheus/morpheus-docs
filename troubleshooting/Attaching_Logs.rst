Attaching Logs to Case
======================

When submitting a case it is critical to attach the relevant logs. The logs can be found at ``/var/log/morpheus/morpheus-ui/current``.  Logs can be attached to the case at anytime.

When submitting logs please reproduce the error right before capturing and sending the log file.  This will ensure the activity that took place and resulted in an error is contained in the logs.

Log rotation takes the current file each night or after it's a certain size and compresses them. The ``*.s`` files in the current directory are rotated and zipped logs that can be sent as is.

The logs can also be captured from the Morpheus UI.  Under ``Administration -> Health -> Morpheus Logs``.  Please copy relevant logs and add to case as an attachment.

.. image:: /images/troubleshooting/Morpheus-Health-Logs.png
