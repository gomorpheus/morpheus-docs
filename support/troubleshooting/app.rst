App
===

VMware
^^^^^^

Guest Customization Fails
`````````````````````````

    **Issue**

        After deploying a |morpheus| instance, the instance's hostname and other items are not modified and/or provisioning fails due to timeout.  After inspecting vCenter, it is noticed the 
        **Guest Customization** task has failed.  The following error is seen in the Guest Customization failure:

            ``A specified parameter was not correct: spec.identity.hostName``
        
    **Resolution**

        When this error is seen, it means the Guest Customization does not like the hostname that was inputted for it.  VMware does not support some special characters, such as:

            - Underscores ( ``_`` )
            - White space ( ``" "`` )
            - Periods     ( ``.`` )

        The name can contain letters, numbers, and hyphens.  This is also consistent with some OSs like Windows, which allows hyphens but underscores are no longer allowed.

            .. image:: /images/support/troubleshooting/app_guest_cust_hostname_failure.png

        Verify these characters are not being entered at the time of deployment or specified in a Catalog Item's code.  It has been seen that an extra space might be before or after an input variable 
        in a Catalog Item, which is added to the hostname during deployment.  It would be best to place a RegEx filter on any inputs that might be used for hostnames, to ensure users do not use the 
        restricted characters.

    Additional information:

        https://github.com/ansible/ansible/issues/24225
        
        https://docs.morpheusdata.com/en/latest/library/options/option_types.html#create-input

Reconfigure Virtual Machine Fails
`````````````````````````````````

    **Issue**

        After deploying a |morpheus| instance, the instance displays a **Failed to create server** error message.  After inspecting vCenter, it is noticed the **Reconfigure Virtual Machine** task has 
        failed.  The following error is seen in the Reconfigure Virtual Machine failure:

            ``Invalid virtual machine configuration. Nested Hardware-Assisted``
        
    **Resolution**

        Some operating systems, such as Windows Server 2022, require **Nested Virtualization** to be enabled in the **Advanced** section during provisioning.  In the case for Windows Server 2022, it has 
        `Virtualization-based Security (VBS) <https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs>`_ enabled by default, which requires Nested Virtualization to be enabled.

            - Underscores ( ``_`` )
            - White space ( ``" "`` )
            - Periods     ( ``.`` )

        Additional information:

            https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-2A98801C-68E8-47AF-99ED-00C63E4857F6.html