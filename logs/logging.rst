Logs
====

Overview
--------

The logging architecture backing |morpheus| uses the latest and greatest technologies and standards to be able to service large amounts of log traffic as well as facilitate easy viewing. Utilizing elasticsearch behind the scenes and buffered log transmission protocols |morpheus| provides a highly efficient and highly scalable solution for capturing log data from anything provisioned via the system. By utilizing common formats (syslog) it is also very easy to forward logs to external third party log services.

Configuration
^^^^^^^^^^^^^

Logging configuration can be setup in the Administration > Settings > Logs section. There are useful settings here, including customizing the retainment policy (7 days by default). This could be expanded to years for PCI compliance purposes or other requirements an organization might have.

.. NOTE:: When increasing the retainment policy of the logging system, it may be necessary to scale out the elasticsearch cluster. Please refer to the relevant information with regards to scaling elasticsearch and advanced installation options for externalizing the elasticsearch cluster.

The Log administration section also provides options for setting custom syslog forward rules. These rules are applied on each individual host therefore keeping the |morpheus| appliance itself out of the data plane. For information on different syslog formatting rules please refer to the http://www.rsyslog.com/sending-messages-to-a-remote-syslog-server/[rsyslog] documentation.

Usage
^^^^^^^^

|morpheus| automatically sets up and configures logging for all of the standard catalog items provisioned through morpheus. This includes both Docker containers as well as virtual machines. Simply view instance-specific logs in instance detail via the "Logs" tab.

There are several filtering capabilities built into the logging UI with more being added continually. Easily toggle log level filters from the dropdown or change the date range filter using the handy date filter component. A chart is also displayed above logs representing the log counts by level over the selected time range (default last 24 hours). A handy pattern search is also available with some rather capable features based on Lucene search syntax.

.. TIP:: It may be useful to review the Lucene search query syntax for powerful use cases: https://lucene.apache.org/core/2_9_4/queryparsersyntax.html[Syntax Guide]

There are several other places logs can be viewed. Not only can they be viewed across an application in app detail but also across all instances in the account. The main level ``Logs`` section provides an ability to query all logs produced by the system. It is also possible to view host-specific logs on a docker host by viewing the host detail page via ``Infrastructure``.

.. NOTE:: New features are on the roadmap for the main logs section including saved searches, and handy charting dashboards for garnering insights out of log data.

Exporting Logs
---------------

Log Settings
^^^^^^^^^^^^^
There are three main log areas in |morpheus|

* Agent Logs

* |morpheus| Server Logs

* Activity / Audit Logs

Agent Logs
-----------

When Instances are deployed through |morpheus|, the installed Agent captures application logs and sends them back to the |morpheus| server.

In most cases, the built-in |morpheus| logging features are sufficient for tracking and reviewing Agent logs. However, if needed, |morpheus| supports integration with advanced logging systems. See the `log integration section <https://docs.morpheusdata.com/en/4.2.0/logs/logging.html#integrations>`_ above for more information.

|morpheus| Server Logs
----------------------

The main |morpheus| server log is in ``/var/log/morpheus/morpheus-ui`` and the latest log file is named current. This log is archived every 24hrs. There are a number of other log files for the individual infrastructure components as well.

If you wish to export these to an external syslog platform, do the following:

#. Once you have configured your syslog destination (edit rsyslog.conf), create a morpheus-syslog.conf file in the ``/etc/rsyslog.d`` directory and add the following entries

   .. code-block:: bash

     module(load="imfile" PollingInterval="10")
     input(type="imfile" File="/var/log/morpheus/morpheus-ui/current" Tag="morpheus-ui" ReadMode="2" Severity="info" StateFile="morpheus-ui")
     input(type="imfile" File="/var/log/morpheus/check-server/current" Tag="check-server" ReadMode="2" Severity="info" StateFile="check-server")
     input(type="imfile" File="/var/log/morpheus/guacd/current" Tag="guacd" ReadMode="2" Severity="info" StateFile="guacd")
     input(type="imfile" File="/var/log/morpheus/elasticsearch/current" Tag="elasticsearch" ReadMode="2" Severity="info" StateFile="elasticsearch")
     input(type="imfile" File="/var/log/morpheus/mysql/current" Tag="mysql" ReadMode="2" Severity="info" StateFile="mysql")
     input(type="imfile" File="/var/log/morpheus/nginx/current" Tag="nginx" ReadMode="2" Severity="info" StateFile="nginx")
     input(type="imfile" File="/var/log/morpheus/rabbitmq/current" Tag="rabbitmq" ReadMode="2" Severity="info" StateFile="rabbitmq")

#. Restart rsyslog

The logfiles will now be forwarded to the destination you have defined.

This configuration is valid for an ‘all-in-one’ |morpheus| server. If the infrastructure components are running on separate servers /clusters, you will need to create the relevant redirects for the logs on those boxes.

Activity Log
-------------

The final log type that may require export is the |morpheus| Activity log. This tracks system changes made by users, for example create and delete instances etc.

#. To set up CEF/SIEM auditing export, you should edit the following file: ``logback.groovy`` located at ``/opt/morpheus/conf/logback.groovy``.

#. Copy the below configuration to the bottom of the logback.groovy configuration file, save and then exit.

   .. code-block:: javascript

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

#. Once you have done this, you need to restart the |morpheus| Application server. To do this, do the following:

   .. code-block:: bash

      morpheus-ctl stop morpheus-ui

   .. NOTE:: Please be aware this will stop the web interface for |morpheus|.

#. Once the service has stopped enter the following at the shell prompt to restart (if the service does not stop, replace stop with graceful-kill and retry)

   .. code-block:: bash

      morpheus-ctl start morpheus-ui

#. To know when the UI is up and running you can run the following command

   .. code-block:: bash

      morpheus-ctl tail morpheus-ui

Once you see the ASCI art show up you will be able to log back into the User Interface. A new audit file will have been created called audit.log and will found in the default |morpheus| log path which is ``/var/log/morpheus/morpheus-ui/``

Instead of writing the output to a log file, you could create an Appender definition for your SIEM audit database product


morpheus-ssl nginx logs
------------------------

.. NOTE:: Morpheus does not put a logrotate in for Morpheus-ssl access logs

svlogd will only rotate the current file, nginx is setup to write the access logs to separate files and not stdout.

Implementation of a log rotate is left up to up to end users for files outside of the services.  This is done in case end users have a log management solution.


Below is what a suggested configuration looks like for the file ``/etc/logrotate.d/morpheus-nginx``:

     .. code-block:: bash

       /var/log/morpheus/nginx/morpheus*access.log {
               daily
               rotate 14
               compress
               delaycompress
               missingok
               notifempty
               create 644 morpheus-app morpheus-app
               postrotate
                       [ ! -f /var/run/morpheus/nginx/nginx.pid ] || kill -USR1 `cat /var/run/morpheus/nginx/nginx.pid`
               endscript
       }
