Apps
====

Apps allow instances having general relationships to be grouped in a clean and organized manner. App functionality enables full control of which instances belong in an app as well setting Firewall and Access Control List (ACL) rules. Use Apps to structure all necessary components into a single place. Add checks and groups for web servers, database nodes, etc.

Apps can be created from Blueprints, which are made in |LibBluApp| or from Existing Apps.

Creating Apps from Blueprints
-----------------------------

#. Click :guilabel:`+ADD` on the right side of the main Apps section in Provisioning.
#. Select an existing App Blueprint and click :guilabel:`NEXT`.

   .. Note:: Blueprints must be created in in |LibBluApp|. to appear as options when creating an App.

#. Enter a Name for the App and select a Group. Default Cloud and Env can also be selected.
#. Click :guilabel:`NEXT`. Blueprint configurations matching the Group, Cloud and Environment selections will auto-populate the configurations of the Instances in the App.  If no Blueprint Configuration matched the Group, Cloud or Env selections, the Instances will have default configurations.
#. Configure your Instances. Depending on the Blueprint Configurations settings, instances may already be fully configured. Fields that are locked in a Blueprint cannot be edited when creating an App.

   .. Note:: Once an Instance is fully configured, a green checkmark will appear next to the Instance. Instances that have required fields that need populated will have a red X and must be completed. If your Blueprint is already fully configured you can simply select complete!

#. Select :guilabel:`COMPLETE` and the App will be created and the Instances will begin provisioning.

.. image:: /images/provisioning/apps_301_1.png

Creating Apps from Existing Instances
-------------------------------------

#. Click :guilabel:`+ADD` on the right side of the main Apps section in Provisioning.
#. Select ``APP FROM EXISTING INSTANCES`` from the Blueprints list and click :guilabel:`NEXT`.
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

#. Once all Existing Instances have been selected, click :guilabel:`COMPLETE`.
#. A new App will be created out of the Existing Instances.

.. image:: /images/provisioning/apps_301_2.png

Exporting Configuration JSON
----------------------------

To export a Blueprint as JSON:

#. Navigate to  |ProApp|
#. Select an App from the list to view the App detail page
#. Click the Actions button and select Export
#. The App export file will be downloaded to your computer as ``{app_name}.json``

Provisioning Apps via API
-------------------------

A quick example of how this work: https://d.pr/i/yxsW7t
