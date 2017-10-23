Apps
====

Apps allow instances having general relationships to be grouped in a clean and organized manner. App functionality enables full control of which instances belong in an app as well setting Firewall and Access Control List (ACL) rules. Use Apps to structure all necessary components into a single place. Add checks and groups for web servers, database nodes, etc.

Apps can be created from Templates, which are made in ``Provisioning -> Templates`` or from Existing Apps.

Creating Apps from Templates
----------------------------

#. Click "+ADD APP" on the right side of the main Apps section in Provisioning.
#. Select an existing App Template and click NEXT.

   .. Note:: Templates must be created in in ``Provisioning -> Templates``. to appear as options when creating an App.

#. Enter a Name for the App and select a Group. Default Cloud and Env can also be selected.
#. Click NEXT. Template configurations matching the Group, Cloud and Environment selections will auto-populate the configurations of the Instances in the App.  If no Template Configuration matched the Group, Cloud or Env selections, the Instances will have default configurations.
#. Configure your Instances. Depending on the Template Configurations settings, instances may already be fully configured. Fields that are locked in a Template cannot be edited when creating an App.

   Note:: Once an Instance is fully configured, a green checkmark will appear next to the Instance. Instances that have required fields that need populated will have a red X and must be completed. If your Template is already fully configured you can simply select complete!

#. Select COMPLETE and the App will be created and the Instances will begin provisioning.

.. image:: /images/provisioning/apps_301_1.png

Creating Apps from Existing Instances
-------------------------------------

#. Click "+ADD APP" on the right side of the main Apps section in Provisioning.
#. Select APP FROM EXISTING INSTANCES from the Templates list and click NEXT.
#. Enter a Name for the App and select a Group. Default Cloud and Env can also be selected.

   .. Note:: Only instances within the selected Group and Cloud will be available to be added to the App.

#. In the STRUCTURE section, select + to add a Tier
#. Select or enter a Tier Name.
#. Select the Tier to set Boot Order, rename, or once multiple Tiers are added, connect the Tier to other Tiers.
#. In the STRUCTURE section, select + in a Tier to add an Instance
#. Select the Instance Type of the Existing Instance to be added to the App.
#. In the STRUCTURE section, select the Instance.
#. In the CONFIGURATION section, select the Cloud the Existing Instance is in. Existing INSTANCES that match the Group, Cloud and Instance Types set will populate.
#. Select the desired Instance from the INSTANCES list. Selected instance will show in the SELECTED INSTANCE section.

   .. Note:: Only one existing Instance can be added per Instance. To add multiple Existing Instances, repeat the step above including adding an Instance for each Existing Instance to be added to the App.

#. Once all Existing Instances have been selected, click COMPLETE.
#. A new App will be created out of the Existing Instances.

.. image:: /images/provisioning/apps_301_2.png
