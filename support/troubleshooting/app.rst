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
        
        Additional information:

            https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-2A98801C-68E8-47AF-99ED-00C63E4857F6.html

Morpheus App
^^^^^^^^^^^^

OutOfMemoryError: Java heap space
`````````````````````````````````

    **Issue**

        Encountering the error ``OutOfMemoryError: Java heap space`` in the logs.  The source of the ``OutOfMemoryError`` needs to be located.

    **Resolution**

        #. Add the following to ``/opt/morpheus/sv/morpheus-ui/run`` JAVA_OPTS:
	
	        ``-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=<path>`` (path needs lots of space, prof file written to path can be huge (like 50GB each))
	
            ie change
                ``export JAVA_OPTS="-Xms12882m -Xmx45089m -XX:+UseG1GC"``
            to
                ``export JAVA_OPTS="-Xms12882m -Xmx45089m -XX:+UseG1GC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/a/path/with/lots/of/space"``
	
        #. Restart morpheus-ui to pick up the changes:  ``morpheus-ctl restart morpheus-ui``
                
        #. On the next ``OutOfMemoryError``, a ``java_pidxxx.hprof`` file will be written to the specified path
                
        #. Remove the heap dump config from ``/opt/morpheus/sv/morpheus-ui/run`` to prevent additional .hprof files being generated and filling disk

            ``export JAVA_OPTS="-Xms12882m -Xmx45089m -XX:+UseG1GC"``

        #. Restart the morpheus-ui to pickup the changes:  ``morpheus-ctl restart morpheus-ui``
                
        #. zip ``java_pidxxx.hprof`` file
                
        #. scp or transfer the ``java_pidxxx.hprof.gz`` to local machine
                
        #. Use a heap dump analytics tool to analyze the hprof file
                
            #. Eclipse Memory Analyzer (https://www.eclipse.org/mat/) as an example
                    
                .. important:: Warning - This takes a ton of local RAM depending on size of hprof file. If needed, edit the eclipse.ini to increase the available ram to -Xmx30720m (30GB)
                
        #. Example stack track the analysis uses:

            .. toggle-header:: :header: **Click to expand**
            
                .. image:: /images/support/troubleshooting/leak_stack_trace.png
        
        #. Analysis identifies leak suspect(s):
            
            .. toggle-header:: :header: **Click to expand**
                
                .. image:: /images/support/troubleshooting/leak_suspects.png

General Toubleshooting

    **Missing Agent Installer**

        This is most likely caused with newer OS releases, due to a missing symlink on the Morpheus app nodes

        .. code-block:: bash

            # All App Nodes (Example)
            ln -s /var/opt/morpheus/package-repos/yum/el/9 /var/opt/morpheus/package-repos/yum/el/9.1