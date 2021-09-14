.. _Release Notes:

************************
|morphver| Release Notes
************************

.. No highlights this time, small update
  .. include:: highlights.rst

.. WARNING:: OpenStack v2 Identity API was deprecated in v5.2.9 and is removed in v5.3.3+

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

New Features
============

:Amazon: - Added Asia Pacific (Seoul) region support

:Pricing: - Added KRW (South Korean Won) currency support

:UI: - Help text added to Add Integration modals warning that HTTP URLs are insecure and not recommended :superscript:`5.3.3`

:vCD: - System administrator account credentials can now be provided to authenticate vCD Cloud integrations in Morpheus. Previously, only organization administrator credentials could be used. Keep in mind that you will need to set the system administrator account credentials appropriately, for example, to be able to see entities created by the organization administrator :superscript:`5.3.3`

|morpheus| API and CLI Improvements
===================================

:Checks: - The ``apiKey`` is now returned in GET calls for Push API-Type Monitoring Checks :superscript:`5.3.3`

Fixes
=====

:API: - Updated response for ``GET ... /api/zones`` when no clouds exist. :superscript:`5.3.3`
:Appliance: - Agent installation: Reconfigure process updated to add ``/var/opt/morpheus/package-repos/yum/el/8.2 -> /var/opt/morpheus/package-repos/yum/el/8`` symlink to handle agent installation requests for centos/rhel configurations version pinned to ``8.2`` :superscript:`5.3.3`
:Azure: - Costing: |morpheus| now stores the actual currency and conversion rates during cost syncs to address reporting, budget and analytic values of non-usd actuals when the tenants defined currency does not match actual cost currency :superscript:`5.3.3`
        - Fixed issue with record being association with the deleted record of a re-synced service plan :superscript:`5.3.3`
:KVM: - Fixed infrastructure deletion of discovered VMs on brownfield KVM clusters :superscript:`5.3.3`
:NSX: - Fix visibility of NSX-T Pools created in subtenants on master tenant NSX-T public integrations :superscript:`5.3.3`
      - Fixed NSX-V VMs added as a part of an app with a load balancer on 1 or more instances being added to pools :superscript:`5.3.3`
      - Fixed ui display issue updating NSX-V Firewall rule priority order after editing rule priority orders :superscript:`5.3.3`
:Provisioning: - ``Copies`` field now hidden when when a Load Balancer is configured :superscript:`5.3.3`
:Security: - Reconfigure and Library XSS vulnerabilities remediated :superscript:`5.3.3`
           - Updated request handling of user scoped policy creation during policy creation :superscript:`5.3.3`
:Terraform: - Fixed UI issue with ``NEXT`` and ``COMPLETE`` buttons becoming active before validation had completed :superscript:`5.3.3`
:vCloud Director: - Fixed issue with user-data iso attachment when provisioning cloudbase-init enabled Windows images :superscript:`5.3.3`
:VMware: - Fixed duplicate filename issue when adding multiple disks during reconfigure :superscript:`5.3.3`
         - Fixed storage volume values not updating on sync when volumes were removed in vCenter but the total number of volumes matches |morpheus| records. :superscript:`5.3.3`

.. Tagging Policy Does not Accept Morpheus Variables as valid input

Appliance & Agent Updates
=========================

:Appliance: - Agent installation: Reconfigure process updated to add ``/var/opt/morpheus/package-repos/yum/el/8.2 -> /var/opt/morpheus/package-repos/yum/el/8`` symlink to handle agent installation requests for centos/rhel configurations version pinned to ``8.2`` :superscript:`5.3.3`
