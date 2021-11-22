Apps
====

Apps allow instances having general relationships to be grouped in a clean and organized manner. App functionality enables full control of which instances belong in an app as well setting Firewall and Access Control List (ACL) rules. Use Apps to structure all necessary components into a single place. Add checks and groups for web servers, database nodes, etc.

Apps can be created from Blueprints, which are made in ``Provisioning -> Blueprints`` or from Existing Apps.


Creating Apps
-------------

New Apps can be created from Blueprints or using existing Instances. 


Creating Apps from Blueprints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Click :guilabel:`+ADD` on the right side of the main Apps section in Provisioning.
#. Select an existing App Blueprint and click :guilabel:`NEXT`.

   .. Note:: Blueprints must be created in in ``Provisioning -> Blueprints``. to appear as options when creating an App.

#. Enter a Name for the App and select a Group. Default Cloud and Env can also be selected.
#. Click :guilabel:`NEXT`. Blueprint configurations matching the Group, Cloud and Environment selections will auto-populate the configurations of the Instances in the App.  If no Blueprint Configuration matched the Group, Cloud or Env selections, the Instances will have default configurations.
#. Configure your Instances. Depending on the Blueprint Configurations settings, instances may already be fully configured. Fields that are locked in a Blueprint cannot be edited when creating an App.

   .. Note:: Once an Instance is fully configured, a green checkmark will appear next to the Instance. Instances that have required fields that need populated will have a red X and must be completed. If your Blueprint is already fully configured, you can simply select :guilabel:`COMPLETE`!

#. Select :guilabel:`COMPLETE` and the App will be created, and the Instances will begin provisioning.

.. image:: /images/provisioning/apps_301_1.png

Creating Apps from Existing Instances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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



Managing Apps
-------------

App Status
^^^^^^^^^^

App Status is determined by the status of the Instances within the App or by the :redguilabel:`DELETE` action. All Instances in an App must be in 'Running' status for the App status to equal 'Running'.


.. list-table:: **App Statuses**
  :widths: auto
  :header-rows: 1

   * - Status Icon
     - App Status
     - Status Reason 
   * - .. image:: /images/provisioning/instances/status/running_icon.svg  
          :width: 25px
     - Running 
     - All Instance Statuses = Running      
   * - .. image:: /images/provisioning/instances/status/failed_icon.svg
          :width: 25px
     - Failed 
     - Any Instance Status = Failed 
   * - .. image:: /images/provisioning/instances/status/pending_icon.svg
          :width: 25px
     - Pending 
     - Any Instance Status = Pending 
   * - .. image:: /images/provisioning/instances/status/pendingRemoval_icon.svg
          :width: 25px
     - Pending Removal 
     - Any Instance Status = Pending Removal 
   * - .. image:: /images/provisioning/instances/status/deploying_icon.svg
          :width: 25px
     - Provisioning 
     - Any Instance Status = Provisioning 
   * - .. image:: /images/provisioning/instances/status/removing_icon.svg
          :width: 25px
     - Removing 
     - The :redguilabel:`DELETE` action was trigger on the App 
   * - .. image:: /images/provisioning/instances/status/unknown_icon.svg
          :width: 25px
     - Unknown 
     - Any Instance Status = Unknown, or the App is empty      

An App will be in "Removing Status" when the :redguilabel:`DELETE` action is trigger on the App and no Delayed Removal Policies are enforced


Editing an App
^^^^^^^^^^^^^^

The :guilabel:`EDIT` action allows permissioned users to update an Apps metadata, Environment, Group and Owner. 

#. Navigate to |ProApp|
#. Select an App from the list to view the App detail page
#. Select :guilabel:`EDIT`
#. Update the following 

   :NAME: App Name 
   :DESCRIPTION: App Description 
   :ENVIRONMENT: App Environment
   :GROUP: App Group assignment
   :OWNER: User assigned as Owner of the App

#. Select :guilabel:`SAVE CHANGES`

Deleting an App
^^^^^^^^^^^^^^^

The :guilabel:`DELETE` action allows permissioned users to delete an App and, by default, all Instances within the App. 

#. Navigate to |ProApp|
#. Select an App from the list to view the App detail page
#. Select :redguilabel:`DELETE`
#. The DELETE APP? confirmation modal will be displayed: 

   :Remove Instances: Deletes all Instances associated with the App
                      - Enabled by Default
   :Preserve Backups: Preserves Backups of the Instances associated with the App
                     - Disabled by Default
   :Preserve Volumes: Preserves Storage Volumes of the Instances associated with the App
                     - Disabled by Default
   :Force Delete: Forces deletion of the App
                  - Required when any Instances associated with the App are in "provisioning" state
                  - WARNING Force deleting may cause orphaned infrastructure or resources.
                  - Disabled by Default

#. Select :guilabel:`DELETE` to proceed with deleting the App, or :guilabel:`CANCEL` to abort the delete action.



Exporting Configuration JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To export a Blueprint as JSON:

#. Navigate to |ProApp|
#. Select an App from the list to view the App detail page
#. Select :guilabel:`ACTIONS` > Export
#. The App export file will be downloaded to your computer as ``{app_name}.json``

