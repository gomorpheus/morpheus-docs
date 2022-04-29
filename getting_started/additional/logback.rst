logback config
--------------

.. note:: This doc is for 5.4.4+ versions that use ``logback.xml``. 5.4.3 and earlier versions use ``logback.groovy`` with a different syntax that is not compatible with this doc. Please refer to 5.4.3 and earlier documentation for ``logback.groovy`` configuration details.

The log output for the morpheus-ui service is configured in the logback.xml file. Log output levels can be updated when more or less log output is desired.

Setting log levels
``````````````````
To change a log level, edit the logback configuration file in /opt/morpheus/conf/logback.xml and save. The changes will be reflected within the configured ``scanPeriod``, 30 seconds by default.

Levels:
 - **OFF** (no log output)
 - **ERROR** (includes error logs)
 - **WARN** (includes warn and error logs)
 - **INFO** (includes info, warn and error logs)
 - **DEBUG** (includes info, warn, error and debug logs)
 - **TRACE** (includes info, warn, error, debug and trace logs)

.. warning:: Use DEBUG and/or TRACE levels with caution. DEBUG & TRACE levels can produce many logs that can consume disk space quickly. Only use DEBUG and/or TRACE levels when needed and target them for specific services.

Example logback settings
````````````````````````
Below are sample log configuration settings. This is not a complete list. Additional log names/paths can typically be determined from the standard INFO, WARN and ERROR logs.

:ACI:
  .. code-block:: xml

     <logger name="com.morpheus.integration.NetworkServersController" level="DEBUG"/>
     <logger name="com.morpheus.network.AciNetworkService" level="DEBUG"/>
     <logger name="com.morpheus.network.AciUtility" level="DEBUG"/>
     <logger name="com.morpheus.network.NetworkService " level="DEBUG"/>

:Amazon:
  .. code-block:: xml
          
     <logger name="com.morpheus.compute.amazon.AmazonComputeService" level="DEBUG"/>
     <logger name="com.morpheus.compute.AmazonComputeUtility" level="DEBUG"/>
     <logger name="com.morpheus.provision.AmazonProvisionService" level="DEBUG"/>


:Azure:
  .. code-block:: xml
          
     <logger name="com.morpheus.Azure.ServersController" level="DEBUG"/>
     <logger name="com.morpheus.Azure.ServersController" level="DEBUG"/>
     <logger name="com.morpheus.AzureSqlServerProvisionService" level="DEBUG"/>
     <logger name="com.morpheus.compute.azure.AzureComputeService" level="DEBUG"/>
     <logger name="com.morpheus.compute.AzureComputeUtility" level="DEBUG"/>
     <logger name="com.morpheus.compute.AzureCostingService" level="DEBUG"/>

:DNS:
  .. code-block:: xml

     <logger name="com.morpheus.dns.MicrosoftDnsService" level="DEBUG"/>

:General:
  .. code-block:: xml

     <logger name="com.morpheus.InstanceService" level="DEBUG"/>
     <logger name="com.morpheus.util.ApiUtility" level="DEBUG"/>
     <logger name="com.morpheus.AppService" level="DEBUG"/>
     <logger name="com.morpheus.MorpheusComputeService" level="DEBUG"/>
     <logger name="com.morpheus.RpcService" level="DEBUG"/>
     <logger name="com.morpheus.network.NetworkService " level="DEBUG"/>
     <logger name="com.morpheus.provision.AbstractProvisionService" level="DEBUG"/>
     <logger name="com.morpheus.provision.AbstractBoxProvisionService" level="DEBUG"/>

:Google:
  .. code-block:: xml
 
     <logger name="com.morpheus.compute.google.GoogleComputeService" level="DEBUG"/>
     <logger name="com.morpheus.compute.GoogleComputeUtility" level="DEBUG"/>
     <logger name="com.morpheus.provision.GoogleProvisionService" level="DEBUG"/>


:IBM Cloud:
  .. code-block:: xml

     <logger name="com.morpheus.compute.softlayer.SoftlayerComputeService" level="DEBUG"/>
     <logger name="com.morpheus.compute.SoftlayerComputeUtility" level="DEBUG"/>

:Kubernetes:
  .. code-block:: xml
 
     <logger name="com.morpheus.app.KubernetesAppTemplateService" level="DEBUG"/>
     <logger name="com.morpheus.app.KubernetesResourceMappingService" level="DEBUG"/>
     <logger name="com.morpheus.compute.KubernetesComputeService" level="DEBUG"/>
     <logger name="com.morpheus.host.KubernetesHostService" level="DEBUG"/>
     <logger name="com.morpheus.provision.KubernetesProvisionService" level="DEBUG"/>
     <logger name="com.morpheus.storage.KubernetesStorageService" level="DEBUG"/>

:Nutanix:
  .. code-block:: xml
          
     <logger name="com.morpheus.compute.nutanix.NutanixComputeService" level="DEBUG"/>
     <logger name="com.morpheus.compute.NutanixComputeUtility" level="DEBUG"/>
     <logger name="com.morpheus.provision.NutanixProvisionService" level="DEBUG"/>

:Openstack:
  .. code-block:: xml
          
     <logger name="com.morpheus.compute.AbstractOpenStackComputeService" level="DEBUG"/>
     <logger name="com.morpheus.compute.AbstractOpenStackComputeUtility" level="DEBUG"/>
     <logger name="com.morpheus.provision.OpenStackProvisionService" level="DEBUG"/>
     <logger name="com.morpheus.storage.OpenStackSFSStorageService" level="DEBUG"/>

:Option Types:
  .. code-block:: xml

     <logger name="com.morpheus.OptionSourceService" level="DEBUG"/>
     <logger name="com.morpheus.OptionTypeListService" level="DEBUG"/>
     <logger name="com.morpheus.OptionTypeService" level="DEBUG"/>

:Remote Console:
  .. code-block:: xml

     <logger name="com.morpheus.remote.MorpheusGuacamoleWebsocketHandler" level="DEBUG"/>

:SCVMM:
  .. code-block:: xml

     <logger name="com.morpheus.compute.scvmm.ScvmmComputeService" level="DEBUG"/>
     <logger name="com.morpheus.compute.ScvmmComputeUtility" level="DEBUG"/>
     <logger name="com.morpheus.provision.ScvmmProvisionService" level="DEBUG"/>

:ServiceNow:
  .. code-block:: xml

     <logger name="com.morpheus.cmdb.ServiceNowCmdbService" level="DEBUG"/>

:Tasks:
  .. code-block:: xml

     <logger name="com.morpheus.task.WinrmTaskService" level="DEBUG"/>
     <logger name="com.morpheus.task.TaskService" level="DEBUG"/>

:Terraform:
  .. code-block:: xml

     <logger name="com.morpheus.app.AbstractResourceMappingService" level="DEBUG"/>
     <logger name="com.morpheus.app.TerraformAppTemplateService" level="DEBUG"/>
     <logger name="com.morpheus.app.TerraformAwsResourceMappingService" level="DEBUG"/>
     <logger name="com.morpheus.app.TerraformResourceMappingService" level="DEBUG"/>
     <logger name="com.morpheus.provision.TerraformProvisionService" level="DEBUG"/>

:Usage:
  .. code-block:: xml

     <logger name="com.morpheus.AccountPriceService" level="DEBUG"/>

:vCloud:
  .. code-block:: xml
 
     <logger name="com.morpheus.compute.vmware.VcloudDirectorComputeService" level="DEBUG"/>
     <logger name="com.morpheus.provision.VcloudDirectorProvisionService" level="DEBUG"/>
     <logger name="com.morpheus.compute.VcdComputeUtility" level="DEBUG"/>

:Veeam:
  .. code-block:: xml
      
     <logger name="com.morpheus.backup.VeeamBackupService" level="DEBUG"/>

:Vmware:
  .. code-block:: xml
          
     <logger name="com.morpheus.compute.VmwareComputeUtility" level="DEBUG"/>
     <logger name="com.morpheus.provision.VmwareProvisionService" level="DEBUG"/>

:vRO:
  .. code-block:: xml

     <logger name="com.morpheus.automation.VroService" level="DEBUG"/>

Audit logs
----------

#. To set up CEF/SIEM auditing export, add the below appender above or below the other appenders in the logback.xml configuration file:

   .. code-block:: xml

      <appender name="AUDIT" class="ch.qos.logback.core.rolling.RollingFileAppender">
          <file>/var/log/morpheus/morpheus-ui/audit.log</file>
          <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
              <fileNamePattern>audit_%d{yyyy-MM-dd}.%i.log</fileNamePattern>
                <maxFileSize>50MB</maxFileSize>
                <maxHistory>30</maxHistory>
          </rollingPolicy>
          <encoder>
              <pattern>[%d] [%thread] %-5level %logger{15} - %maskedMsg %n</pattern>
          </encoder>
      </appender>


    .. note:: ``maxFileSize`` and ``maxHistory`` values can be updated as needed.

#. Add the below logger above or below the other loggers in the logback.xml configuration file (make sure it is below, not above, the appender from the previous step or an error will occur):

   .. code-block:: xml

      <logger name="com.morpheus.AuditLogService" level="INFO" additivity="false">
          <appender-ref ref="AUDIT" />
      </logger>

#. Once you have done this, you need to restart the |morpheus| Application server:

   .. code-block:: bash

      morpheus-ctl stop morpheus-ui

   .. NOTE:: Please be aware this will stop the web interface for |morpheus|.

#. Once the service has stopped enter the following at the xml prompt to restart (if the service does not stop, replace stop with graceful-kill and retry)

   .. code-block:: bash

      morpheus-ctl start morpheus-ui

#. To know when the UI is up and running you can run the following command

   .. code-block:: bash

      morpheus-ctl tail morpheus-ui

   Once you see the ASCI art show up you will be able to log back into the User Interface. A new audit file will have been created called audit.log and will found in the default |morpheus| log path which is ``/var/log/morpheus/morpheus-ui/``

This is only an example and other configurations are possible, sucha as creating an appender definition for your SIEM audit database product.
