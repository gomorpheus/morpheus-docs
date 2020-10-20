Creating and Running Security Scan Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Security scan Jobs allow users to create and schedule SCAP program (Security Content Automation Program) scans for groups of managed systems. These Jobs can call in existing SCAP packages and checklists, which are used to scan the targeted systems on-demand or on a scheduled basis. Historical data for these scans is saved in the Job Execution list and in the software section of server detail pages. Detailed scan reports can also be viewed for each system as needed once the scan is complete. See the `SCAP documentation <https://csrc.nist.gov/CSRC/media/Projects/Security-Content-Automation-Protocol/documents/docs/scap-nistir-7343.pdf>`_ on the NIST website for information on developing your own scanning procedures.

.. NOTE:: Creating and editing Security Scan Jobs requires the "Security: Scanning" Role permission set to Full. Viewing Security Scan Jobs and seeing the results for scanned servers requires at least a Read-level permission.

Add a new Security Package
``````````````````````````

#. Navigate to Provisioning > Jobs > Security Packages Tab
#. Click :guilabel:`+ADD` > SCAP Package
#. Provide a name in addition to a URL to source the package
#. Click :guilabel:`SAVE CHANGES`

.. NOTE:: Currently URL is the only source option for security packages

.. image:: /images/provisioning/jobs/security/1add_package.png

Add a new Security Scan Job
```````````````````````````

#. Navigate to Provisioning > Jobs > Jobs Tab
#. Click :guilabel:`+ADD`
#. Set the Job type to "Security Scan Job" and provide a friendly name for the Job
#. Click:guilabel:`NEXT`

    .. image:: /images/provisioning/jobs/security/2new_job.png

#. Select a security package, see the previous section to add a new one
#. Enter your Scan Checklist (XML document) and Security Profile (XCCDF document), more information on these can be found in the SCAP documentation linked above
#. Set a schedule or leave as Manual to only run this scan on-demand (new execution schedules can be created in Provisioning > Automation if needed)
#. Set the context, can be Instance or Server. Select as many Instances or Servers as needed for this scanning run
#. Click :guilabel:`NEXT`
#. After final review, click :guilabel:`COMPLETE`

.. image:: /images/provisioning/jobs/security/3job_details.png

Running Security Scan Jobs
``````````````````````````

Once created, Security Scan Jobs will run based on the configured schedule. They can also be run on-demand when needed:

#. Navigate to Provisioning > Jobs > Jobs Tab
#. Click :guilabel:`MORE`
#. Click "Execute"

.. image:: /images/provisioning/jobs/security/4execute_scan.png

Viewing Completed Security Scan Jobs
````````````````````````````````````

To view a list of completed Security Scan Jobs (and Jobs of other types):

#. Navigate to Provisioning > Jobs > Job Executions Tab
#. Additional details can be viewed by clicking :guilabel:`(i)`

.. image:: /images/provisioning/jobs/security/5execution_list.png

To view scan results for specific servers:

#. Navigate to the server detail page (Infrastructure > Hosts > Virtual Machines tab > Selected server)
#. Click on the Software tab part way down the page, then click on the Security subtab
#. High level details on previous scans is viewable here

    .. image:: /images/provisioning/jobs/security/6server_results.png

#. To view the full report, click :guilabel:`(i)`

    .. image:: /images/provisioning/jobs/security/7scan_report.png
