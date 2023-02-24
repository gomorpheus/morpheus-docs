Requirements
````````````

Ensure the firewall (or security group) allows |morpheus| ``outbound`` access to the various backend services:

  - Amazon Aurora Ports
    
    - 3306/tcp
  
  - Amazon OpenSearch Port
    
    - 443/tcp
  
  - Amazon MQ Ports
    
    - 5671/tcp
    
    - 443/tcp (management API)
  
  - Amazon EFS Port
    
    - 2049/tcp

Ensure the firewall (or security group) allows |morpheus| ``inbound`` from agents and users:

  - HTTPS Port
    
    - 443/tcp

  Example commands to run in the OS, if needed.  By default, **|morpheus| will modify the OS firewall automatically**, if the firewall is enabled.  Usually, in public clouds, the firewall is **not** enabled.

    .. tabs::

      .. group-tab:: RHEL 8/9

        .. code-block:: bash

          firewall-cmd --zone=public --add-port={443/tcp,443/tcp} --permanent
          firewall-cmd --reload
                      
      .. group-tab:: Ubuntu

          .. code-block:: bash

            ufw allow 443/tcp

When installing |morpheus| on AWS, it is best to **not** use a burstable instance type (T2/T3), as these can run out of CPU credits and then run near 20% of the normal speed.
It would be recommended to choose an M4 or M5 family, with the CPU and memory requirements needed.  The M4 and M5 are general purpose, the same as the T2/T3 but **without** bursting.