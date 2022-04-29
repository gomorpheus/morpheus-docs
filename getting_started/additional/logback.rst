logback config
--------------

.. note:: This doc is for 5.4.3 versions and earlier that use logback.groovy. 5.4.4+ versions use logback.xml with a different syntax that is not compatible with this doc. Please refer to 5.4.4 and later documentation for logback.xml configuration details.

The log output for the morpheus-ui service is configured in the logback.groovy file. Log output levels can be updated when more or less log output is desired.

Setting log levels
``````````````````
To change a log level, edit the logback configuration file in /opt/morpheus/conf/logback.groovy and save. The changes will be reflected within the configured scan period, 30 seconds by default.

Levels:
 - OFF (no log output)
 - ERROR (includes error logs)
 - WARN (includes warn and error logs)
 - INFO (includes info, warn and error logs)
 - DEBUG (includes info, warn, error and debug logs)
 - TRACE (includes info, warn, error, debug and trace logs)

.. warning:: Use DEBUG and/or TRACE levels with caution. DEBUG & TRACE levels can produce many logs that can consume disk space quickly. Only use DEBUG and/or TRACE levels when needed and target them for specific services.

Example logback settings
````````````````````````
Below are sample log configuration settings. This is not a complete list. Additional log names/paths can typically be determined from the standard INFO, WARN and ERROR logs.

:ACI:
  .. code-block:: groovy

     logger("com.morpheus.integration.NetworkServersController", DEBUG)
     logger("com.morpheus.network.AciNetworkService", DEBUG)
     logger("com.morpheus.network.AciUtility", DEBUG)
     logger("com.morpheus.network.NetworkService ", DEBUG)

:Amazon:
  .. code-block:: groovy
          
     logger("com.morpheus.compute.amazon.AmazonComputeService", DEBUG)
     logger("com.morpheus.compute.AmazonComputeUtility", DEBUG)
     logger("com.morpheus.provision.AmazonProvisionService", DEBUG)


:Azure:
  .. code-block:: groovy
          
     logger("com.morpheus.Azure.ServersController", DEBUG)
     logger("com.morpheus.Azure.ServersController", DEBUG)
     logger("com.morpheus.AzureSqlServerProvisionService", DEBUG)
     logger("com.morpheus.compute.azure.AzureComputeService", DEBUG)
     logger("com.morpheus.compute.AzureComputeUtility", DEBUG)
     logger("com.morpheus.compute.AzureCostingService", DEBUG)

:DNS:
  .. code-block:: groovy

     logger("com.morpheus.dns.MicrosoftDnsService", DEBUG)

:General:
  .. code-block:: groovy

     logger("com.morpheus.InstanceService" level=
     logger("com.morpheus.util.ApiUtility", DEBUG)
     logger("com.morpheus.AppService", DEBUG)
     logger("com.morpheus.MorpheusComputeService", DEBUG)
     logger("com.morpheus.RpcService", DEBUG)
     logger("com.morpheus.network.NetworkService ", DEBUG)
     logger("com.morpheus.provision.AbstractProvisionService", DEBUG)
     logger("com.morpheus.provision.AbstractBoxProvisionService", DEBUG)

:Google:
  .. code-block:: groovy
 
     logger("com.morpheus.compute.google.GoogleComputeService", DEBUG)
     logger("com.morpheus.compute.GoogleComputeUtility", DEBUG)
     logger("com.morpheus.provision.GoogleProvisionService", DEBUG)


:IBM Cloud:
  .. code-block:: groovy

     logger("com.morpheus.compute.softlayer.SoftlayerComputeService", DEBUG)
     logger("com.morpheus.compute.SoftlayerComputeUtility", DEBUG)

:Kubernetes:
  .. code-block:: groovy
 
     logger("com.morpheus.app.KubernetesAppTemplateService", DEBUG)
     logger("com.morpheus.app.KubernetesResourceMappingService", DEBUG)
     logger("com.morpheus.compute.KubernetesComputeService", DEBUG)
     logger("com.morpheus.host.KubernetesHostService", DEBUG)
     logger("com.morpheus.provision.KubernetesProvisionService", DEBUG)
     logger("com.morpheus.storage.KubernetesStorageService", DEBUG)

:Nutanix:
  .. code-block:: groovy
          
     logger("com.morpheus.compute.nutanix.NutanixComputeService", DEBUG)
     logger("com.morpheus.compute.NutanixComputeUtility", DEBUG)
     logger("com.morpheus.provision.NutanixProvisionService", DEBUG)

:Openstack:
  .. code-block:: groovy
          
     logger("com.morpheus.compute.AbstractOpenStackComputeService", DEBUG)
     logger("com.morpheus.compute.AbstractOpenStackComputeUtility", DEBUG)
     logger("com.morpheus.provision.OpenStackProvisionService", DEBUG)
     logger("com.morpheus.storage.OpenStackSFSStorageService", DEBUG)

:Option Types:
  .. code-block:: groovy

     logger("com.morpheus.OptionSourceService", DEBUG)
     logger("com.morpheus.OptionTypeListService", DEBUG)
     logger("com.morpheus.OptionTypeService", DEBUG)

:Remote Console:
  .. code-block:: groovy

     logger("com.morpheus.remote.MorpheusGuacamoleWebsocketHandler", DEBUG)

:SCVMM:
  .. code-block:: groovy

     logger("com.morpheus.compute.scvmm.ScvmmComputeService", DEBUG)
     logger("com.morpheus.compute.ScvmmComputeUtility", DEBUG)
     logger("com.morpheus.provision.ScvmmProvisionService", DEBUG)

:ServiceNow:
  .. code-block:: groovy

     logger("com.morpheus.cmdb.ServiceNowCmdbService", DEBUG)

:Tasks:
  .. code-block:: groovy

     logger("com.morpheus.task.WinrmTaskService", DEBUG)
     logger("com.morpheus.task.TaskService", DEBUG)

:Terraform:
  .. code-block:: groovy

     logger("com.morpheus.app.AbstractResourceMappingService", DEBUG)
     logger("com.morpheus.app.TerraformAppTemplateService", DEBUG)
     logger("com.morpheus.app.TerraformAwsResourceMappingService", DEBUG)
     logger("com.morpheus.app.TerraformResourceMappingService", DEBUG)
     logger("com.morpheus.provision.TerraformProvisionService", DEBUG)

:Usage:
  .. code-block:: groovy

     logger("com.morpheus.AccountPriceService", DEBUG)

:vCloud:
  .. code-block:: groovy
 
     logger("com.morpheus.compute.vmware.VcloudDirectorComputeService", DEBUG)
     logger("com.morpheus.provision.VcloudDirectorProvisionService", DEBUG)
     logger("com.morpheus.compute.VcdComputeUtility", DEBUG)

:Veeam:
  .. code-block:: groovy
      
     logger("com.morpheus.backup.VeeamBackupService", DEBUG)

:Vmware:
  .. code-block:: groovy
          
     logger("com.morpheus.compute.VmwareComputeUtility", DEBUG)
     logger("com.morpheus.provision.VmwareProvisionService", DEBUG)

:vRO:
  .. code-block:: groovy

     logger("com.morpheus.automation.VroService", DEBUG)
