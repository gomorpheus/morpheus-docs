Instance Types
--------------

.. image:: /images/provisioning/library/Types_Library_Morpheus_salt_library_item.png

Adding an Instance Type creates a new Library Item category. Multiple layouts can be added to an instance type, and these layout can have different nodes attached. The instance wizard will present the layout options compatible with the selected cloud. If cloud selection is turned off, all layouts will be presented for all cloud types accessible by the user.

Name
  Name of the Instance Type in the Provisioning Library
Code
  Useful shortcode for provisioning naming schemes and export reference.
Description
  The description of the Instance Type shown in the Provisioning Library. (255 characters max)
Category
  For filtering in Instance sections and Provisioning Wizard

  * Web
  * SQL
  * NoSLQ
  * Apps
  * Network
  * Messaging
  * Cache
  * OS
  * Cloud
  * Utility

Icon
  Suggested Dimensions: 150 x 51
Visibility
  * Private- Only accessibly by assigned Accounts/Tenants
  * Public- accessible by all Accounts/Tenants
Environment Prefix
  Used for exportable environment variables when tying instance types together environment Variables in app contexts. If not specified a name will be generated
Enable Scaling (Horizontal)
  Enables load balancer assignment and auto-scaling features
Supports Deployments
  Enables deployment features (Requires a data volume be configured on each version. Files will be copied into this location)

Upon saving, this Instance Type will be available in the Provisioning Catalog, per user role access. However we still need to add layouts to the Instance Type, and prior to creating a layout, we will add a node type.
