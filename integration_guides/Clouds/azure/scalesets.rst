Azure Scale Sets
^^^^^^^^^^^^^^^^

Auto-scaling Azure instances can be done with the native Morpheus scaling service or Azure Scale Sets. When using Azure Scale Sets, Morpheus will configure the scale sets and thresholds, but Azure will be responsible for scaling the instances. The Instances nodes that are added and removed by Azure will be synced in by Morpheus as the instance scales up and down.

.. NOTE:: Instances can only be added to Azure Scale Sets at provision time.

Adding an Instance to a Scale Set
`````````````````````````````````

#. In ``Provisioning - Instances`` select :guilabel:`+ ADD`
#. Select an Instance Type that has scaling enabled (Advanced section when editing an Instance Type in `Provisioning - Library`)
#. Configure the Instance as desired
#. In the `AUTOMATION` section under `Scale - Scale Type` select `Azure Scale Set`
#. Select a default Threshold. Threshold pre-sets can be added in `Provisioning - Automation- Scale Thresholds` (requires Instances - Thresholds permission)

   .. image:: /images/clouds/azure/azure_scale_sets1.png

#. Complete the instance configuration and provision the instance.

A Virtual Machine scale set will be created in Azure with the selected threshold and min/max node settings.

Create Threshold Presets
````````````````````````


#. In ``Provisioning - Automation`` select the `SCALE THRESHOLDS` tab

   .. NOTE:: Access to the SCALE THRESHOLDS section requires `Instances - Thresholds` Role permissions.

   .. image:: /images/provisioning/scalethresholds.png
#. Select :guilabel:`+ ADD`
#. Configure Threshold settings.

   .. image:: /images/provisioning/scalethresholds1.png

#. Select :guilabel:`SAVE CHANGES`

The new Threshold will be available for selection in the SCALE section during provisioning or when configuring an App Blueprint.


Edit Thresholds on an Instance
``````````````````````````````

#. In ``Provisioning - Instances`` select the target Instance.
#. Select the `SCALE` tab below the VM's section
#. In the `THRESHOLDS` section of the SCALE tab, click :guilabel:`EDIT`
#. Update the threshold settings.
#. Select :guilabel:`APPLY`

   .. NOTE:: Morpheus will sync in changes to a scale sets threshold settings if the settings are edited in Azure.
