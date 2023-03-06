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
Price Sets
  Associate a Price Set with the Instance Type, Price sets are created in |AdmPlaSet|. Price Sets which are added to Instance Types become additive with any pricing which may apply on the Service Plan. For example, a "fixed" Price Set of $1000/month has been associated with the Instance Type. If this Instance Type is provisioned to an Amazon AWS Cloud, the additional fixed price would be computed along with any Price which is pre-existing on the AWS Service Plan

  - .. toggle-header:: :header: **Instance Type Price Sets Demo**

      .. raw:: html

          <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
              <iframe src="//www.youtube.com/embed/V_ZoZBakAVM" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
          </div>

      |
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
