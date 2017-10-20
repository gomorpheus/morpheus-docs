Licenses

`Administration -> Provisioning -> Licenses`

Overview
--------

The License section is for automating the application of Licensee to Instances while provisioning. Licenses can be added to |morpheus| and then attached to images. |morpheus| will then apply the license to Instances provisioned using the images with license attached. Licenses can be configured for single or multiple Tenants.

Creating Licenses
-----------------

#. Select `+ Create License`
#. In the New License modal, enter the following:

   * License Type
      Windows
   * Name
      Name of the License in |morpheus| 
   * License Key
      Enter the License Key
   * Org Name
      The Organization Name (if applicable) related to the license key
   * Full Name
      The Full Name (if applicable) related to the license key
   * Version
      License Version
   * Copies
      The Number of copies available on the License
   * Description
      License description displayed in the Licenses list in |morpheus| . Helpful for identifying License after creation
   * Virtual Images
      Search for existing Virtual Images by name and select to attach the image to the license.
          .. NOTE:: Virtual Images are synced from Clouds or added in the `Provisioning -> Virtual Images` section.
   * Tenant Permissions
      Search for and select the Tenant(s) the License will be available for. Multiple Tenants can be added.

#. Save Changes

Provisioning with Licenses
--------------------------

When a Virtual Image is added to a license, |morpheus| will automatically apply the License to Instances configured with the Virtual Image during provisioning, including Instance Types with a Node Type that is configured with the Virtual Image, or if the image is selected when using generic Cloud Instances types (VMware, AWS, Nutanix, Openstack etc). Virtual Images can be removed from a License by editing the License.

Managing Licenses
-----------------

Created Licenses details are displayed in the License page, including the number of copies applied per License, the Tenants added to the License, and the Virtual Images attached to the License.

The Name, Version, Copies, Description, Virtual Images and Tenant Permissions are editable but selecting the `Actions` dropdown on a License.

.. NOTE:: License Types, Keys, Org Names and Full Names are not editable after a license has been created.

License can also be removed using the `Actions` dropdown on a License.
