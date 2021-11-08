Unable to Provision a Custom Image
==================================

Prior to provisioning an custom image, the image must be configured in the |LibVir| section by selecting Edit on the Actions dropdown of the Virtual Image.

In the Edit Virtual Image pane:

#. Select "Cloud Init Enabled?" only if the Virtual Image is a linux image with cloud init installed.

#. Enter the username and password that are set on the Virtual Image.

.. NOTE:: When using Static IP's or IP Pools in VMware, VMware tools must also be installed on the template in order for |morpheus| to set the static IP address when provisioning.

.. NOTE:: |morpheus| agents only support 64-bit vm's prior to versions 2.12.3 and 3.0.2
