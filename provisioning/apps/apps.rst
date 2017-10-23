Apps
====

Apps allow instances having general relationships to be grouped in a clean and organized manner. App functionality enables full control of which instances belong in an app as well setting Firewall and Access Control List (ACL) rules. Use Apps to structure all necessary components into a single place. Add checks and groups for web servers, database nodes, etc.

Apps can be created from Templates, which are made in ``Provisioning -> Templates`` or from Existing Apps.

Creating an App from a Template
-------------------------------

#. Click "+ADD APP" on the right side of the main Apps section in Provisioning.
#. Select an existing App Template.

   .. Note:: Templates must be created in in ``Provisioning -> Templates``. to appear as options when creating an App.

#. Name the App and select a Group. Default Cloud and Env can also be selected.
#. Click NEXT. Template configurations matching the Group, Cloud and Environment selections will auto-populate the configurations of the Instances in the App.  If no Template Configuration matched the Group, Cloud or Env selections, the Instances will have default configurations.
#. Configure your Instances. Depending on the Template Configurations settings, instances may already be fully configured. Fields that are locked in a Template cannot be edited when creating an App.

   Note:: Once an Instance is fully configured, a green checkmark will appear next to the Instance. Instances that have required fields that need populated will have a red X and must be completed.

#. Select COMPLETE and the App will be created and the Instances will begin provisioning.
