.. _Release Notes:

************************
|morphver| Release Notes
************************

Release Dates:

- |morphver| |releasedate|

New Features
============


Fixes
=====


Appliance & Agent Updates
=========================


Known Issues
============

:Alletra MP Storage Plugin: - VM creation with specific ISO virtual images could fail volume creation. Recommendation is to use Qcow2 based images in case the error is seen. Fix will be available in 8.0.7 release.
                            - No support for iface for Software iSCSI
                            - VM Migration to other hosts may fail under heavy write-iops load on the VM. Recommendation is to reduce write-iops prior to migration
                            - Virtual images created without a specified disk capacity will fail to provision if the associated disk size is smaller than the minimum required
                            - VM in shutdown state will not migrate to the new node until it's powered on
                            - If the default image store is created after the virtual image is uploaded, it may cause issues with VM provisioning. Workaround is to ensure the store is created prior to virtual image creation
                            - Reconfigure Instance with HPE Alletra MP datastore fails if there is an attached CD ROM. Workaround is to delete the CD Drive before performing any subsequent actions for reconfigure
                            - Mixed datastore type is not supported for snapshot related features. Workaround is to specify the Alletra datastore by changing the disk type to Standard, selecting the datastore, and changing back to CD ROM
