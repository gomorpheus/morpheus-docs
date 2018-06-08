Export Morpheus Logs
=====================

Log Settings
-------------

There are three main log areas in Morpheus

Agent Logs

Morpheus Server Logs

Activity / Audit Logs 

Agent Logs
-----------

When instances are deployed through Morpheus, the agent that is installed, captures Application logs and sends them back to the Morpheus Server.

While the built-in logging solution provided by Morpheus is sufficient for most, there are some scenarios in which a more advanced logging system may be desired or already in place. To facilitate this Morpheus makes it easy to add custom syslog rules as well as built in direct integrations with Splunk and LogRhythm. All integrations pertaining to logging can be configured in the Administration -> Logging section.

Splunk
To configure Splunk simply create a syslog listener configuration in Splunk. Then it is simply a matter of expanding the section in Logging settings pertaining to Splunk and filling out the host and port of the appender. Once saved, all hosts managed by Morpheus will be configured to forward logs to the target Splunk listener.

LogRhythm
Configuring LogRhythm is much like configuring Splunk. Simply toggle the enabled flag in the LogRhythm section to enabled and fill in the Host, and Port information for the LogRhythm listener.

Morpheus Server Logs
--------------------

The main Morpheus server log is in /var/log/morpheus/Morpheus-ui and the latest log file is named current. This log is archived every 24hrs. There are a number of other log files for the individual infrastructure components as well.

If you wish to export these to an external syslog platform, do the following:

Once you have configured your syslog destination (edit rsyslog.conf), create a Morpheus-syslog.conf file in the ``/etc/rsyslog.d`` directory and add the following entries


module(load="imfile" PollingInterval="50")
input(type="imfile" File="/var/log/morpheus/morpheus-ui/current" Tag="morpheus-ui" ReadMode="2" Severity="info" StateFile="morpheus-ui")
input(type="imfile" File="/var/log/morpheus/check-server/current" Tag="check-server" ReadMode="2" Severity="info")
input(type="imfile" File="/var/log/morpheus/guacd/current" Tag="guacd" ReadMode="2" Severity="info")
input(type="imfile" File="/var/log/morpheus/elasticsearch/current" Tag="elasticsearch" ReadMode="2")
input(type="imfile" File="/var/log/morpheus/mysql/current" Tag="mysql" ReadMode="2" Severity="info")
input(type="imfile" File="/var/log/morpheus/nginx/current" Tag="nginx" ReadMode="2" Severity="info")
input(type="imfile" File="/var/log/morpheus/rabbitmq/current" Tag="rabbitmq" ReadMode="2" Severity="info")
input(type="imfile" File="/var/log/morpheus/redis/current" Tag="redis" ReadMode="2" Severity="info")

Restart rsyslog

The logfiles will now be to the destination you have defined.

This configuration is valid for an ‘all-in-one’ Morpheus server. If the infrastructure components are running on separate servers /clusters, you will need to create the relevant redirects for the logs on those boxes.

Activity Log
-------------

The final log type that may require export is the Morpheus Activity log. This tracks system changes made by users, for example create and delete instances etc.

To set up CEF/SIEM auditing export, you should edit the following file: logback.groovy
It can be located in the following directory:

``/opt/morpheus/conf/logback.groovy``

Copy the below configuration to the bottom of the logback.groovy configuration file, save and then exit.

appender("AUDIT", RollingFileAppender) {
  file = "/var/log/morpheus/morpheus-ui/audit.log"
  rollingPolicy(TimeBasedRollingPolicy) {
    fileNamePattern = "/var/log/morpheus/morpheus-ui/audit_%d{yyyy-MM-dd}.%i.log"
    timeBasedFileNamingAndTriggeringPolicy(SizeAndTimeBasedFNATP) {
      maxFileSize = "50MB"
    }
    maxHistory = 30
  }
  encoder(PatternLayoutEncoder) {
    pattern = "[%d] [%thread] %-5level %logger{15} - %maskedMsg %n"
  }
}

logger("com.morpheus.AuditLogService", INFO, ['AUDIT'], false)

Once you have done this, you need to restart the Morpheus Application server. To do this, do the following:  **please be aware this will restart the web interface for Morpheus.**

.. code-block:: bash

Morpheus-ctl stop morpheus-ui

Once the service has stopped enter the following at the shell prompt to restart (if the service does not stop, replace stop with graceful-kill and retry)

.. code-block:: bash

Morpheus-ctl start moprheus-ui

To know when the UI is up and running you can run the following command

.. code-block:: bash

Morpheus-ctl tail moprheus-ui

Once you see the ASCI art show up you will be able to log back into the User Interface. A new audit file will have been created called audit.log and will found in the default Morpheus log path which is ``/var/log/morpheus/morpheus-ui/``

Instead of writing the output to a logile, you could create an Appender definition for your SIEM audit database product
