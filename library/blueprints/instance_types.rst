Instance Types
--------------

Adding an Instance Type creates a new Library item category. Multiple Layouts can be added to an Instance Type and these Layouts can have different Nodes attached. The Instance provisioning wizard will present the Layout options compatible with the selected Cloud. If Cloud selection is turned off, all Layouts will be presented for all Cloud types accessible by the User.

.. image:: /images/provisioning/library/Types_Library_Morpheus_salt_library_item.png

Name
  Name of the Instance Type in the provisioning Library
Code
  A useful shortcode for provisioning naming schemes and export reference
Description
  The description of the Instance Type shown in the Provisioning Library. (255 characters max)
Category
  For filtering in Instance sections and provisioning wizard

  * Web
  * SQL
  * NoSQL
  * Apps
  * Network
  * Messaging
  * Cache
  * OS
  * Cloud
  * Utility

Icon
  An identifiable icon to display in-line with your Instance Type in the provisioning wizard (Suggested dimensions: 150 x 51)
Visibility
  * Private: Only accessible by assigned Accounts/Tenants
  * Public: Accessible by all Accounts/Tenants
Inputs
  Custom options presented to the user at provision time, Inputs are also created and stored in Morpheus Library
Environment Prefix
  Used for exportable environment variables when tying Instance Types together in App contexts. If not specified, a name will be generated
Environment Variables
  Name and value pairs for environment variables to be loaded on initialization
Enable Settings
  Allows for attachment of modifiable file templates to Node Types in a settings tab of the Instance after deployment
Enable Scaling (Horizontal)
  Enables load balancer assignment and auto-scaling features
Support Deployments
  Enables deployment features (Requires a data volume be configured on each version. Files will be copied into this location)

Upon saving, this Instance Type will be available in the provisioning catalog, per User Role access. However, we still need to add Layouts to the Instance Type, and prior to creating a Layout, we will add a Node Type.
