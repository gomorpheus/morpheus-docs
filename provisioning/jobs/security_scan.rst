Creating and Running Security Scan Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Security Scan Jobs allow users to create and schedule SCAP program (Security Content Automation Program) scans for groups of managed systems. These Jobs can call in existing SCAP packages and checklists, which are used to scan the targeted systems on-demand or on a scheduled basis. Historical data for these scans is saved in the Job Execution list and in the software section of server detail pages. Detailed scan reports can also be viewed for each system as needed once the scan is complete. See the `SCAP documentation <https://csrc.nist.gov/CSRC/media/Projects/Security-Content-Automation-Protocol/documents/docs/scap-nistir-7343.pdf>`_ on the NIST website for information on developing your own scanning procedures.

.. NOTE:: Creating and editing Security Scan Jobs requires the "Security: Scanning" Role permission set to Full. Viewing Security Scan Jobs and seeing the results for scanned servers requires at least a Read-level permission.

Add a new Security Scan Job
```````````````````````````

.. NOTE:: New security scan packages are added in |morpheus| Library rather than here in the Jobs section. Ensure you have uploaded the desired security package in Library > Templates > Security Packages before proceeding with new security Job creation.

#. Navigate to |ProJob| > Jobs Tab
#. Click :guilabel:`+ADD`
#. Set the Job type to "Security Scan Job" and provide a friendly name for the Job
#. Click :guilabel:`NEXT`

    .. image:: /images/provisioning/jobs/security/2new_job.png
      :width: 50%

#. Select a security package, see the previous section to add a new one
#. Enter your Scan Checklist (XML document) and Security Profile (XCCDF document), more information on these can be found in the SCAP documentation linked above
#. Set a schedule or leave as Manual to only run this scan on-demand (new execution schedules can be created in |LibAut| if needed)
#. Set a specific power state target if desired. This indicates whether the Job should run against workloads having any power state, just an "on" power state, or just an "off" power state
#. Set the context, can be Instance or Server. Select as many Instances or Servers as needed for this scanning run
#. Click :guilabel:`NEXT`
#. After final review, click :guilabel:`COMPLETE`

    .. image:: /images/provisioning/jobs/security/3job_details.png
      :width: 50%

Running Security Scan Jobs
``````````````````````````

Once created, Security Scan Jobs will run based on the configured schedule. They can also be run on-demand when needed:

#. Navigate to |ProJob| > Jobs Tab
#. Click :guilabel:`MORE`
#. Click "Execute"

    .. image:: /images/provisioning/jobs/security/4execute_scan.png

Viewing Completed Security Scan Jobs
````````````````````````````````````

To view a list of completed Security Scan Jobs (and Jobs of other types):

#. Navigate to |ProJob| > Job Executions Tab
#. Additional details can be viewed by clicking :guilabel:`(i)`

    .. image:: /images/provisioning/jobs/security/5execution_list.png

To view scan results for specific servers:

#. Navigate to the server detail page (Infrastructure > Hosts > Virtual Machines tab > Selected server)
#. Click on the Software tab part way down the page, then click on the Security subtab
#. High level details on previous scans is viewable here

    .. image:: /images/provisioning/jobs/security/6server_results.png

#. To view the full report, click :guilabel:`(i)`

    .. image:: /images/provisioning/jobs/security/7scan_report.png

Security Drift
``````````````

In addition to tracking the scan results over time as described in the previous section, |morpheus| also provides detail into the change from the most recent scan to the one prior. This information is displayed in the Software tab (and Security subtab) of the detail page for the virtual machine (accessed from the associated Instance detail page or at Infrastructure > Hosts > Virtual Machines). The information surfaced by this view is listed below. If there is no change, you'll simply see a "No Drift" message.

- **Title:** The criteria for the test that has newly passed or failed
- **Severity:** The severity level for the indicated security requirement
- **Result:** The indicator for whether this test has newly passed or failed
- **New Pass:** The number of tests that have newly passed compared to the prior scan
- **New Fail:** The number of tests that have newly failed compared to the prior scan
- **Status:** An indicator of the change in security posture since the prior scan. A net gain in test failures will yield a negative status indicator while net gains in passed tests (or no change) will yield a positive status indicator

.. image:: /images/provisioning/jobs/security/8securityDrift.png
