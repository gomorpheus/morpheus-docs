.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. Small Update, omitting highlights this time
  .. include:: highlights.rst

New Features
============

- Amazon: AWS Instances can now be cloned to AWS Clouds associated with a different account from the source Cloud. This is currently only supported by single-disk VMs as the image to be cloned is created from the root disk only
- Ansible Tower: Updated Ansible Tower integration to make full payload of |morpheus| variables available to Ansible Tower Tasks bringing this integration in line with what is currently available to Ansible Tasks
- Backups: Azure VMs can now be restored to a current Instance, previously they needed to be restored to a new Instance
- CloudFormation: YAML templates now accepted in addition to JSON for CF Blueprints and Spec Templates both entered locally and ingested through integration with a Git repository
- Clouds: Grant read-level access to Clouds for Tenants through the applied Tenant Role
- Huawei Cloud: Improved filtering to show only plan sizes which are currently available during provisioning
- Open Telekom Cloud: Improved filtering to show only plan sizes which are currently available during provisioning
- Oracle Cloud: Instance reconfigure support added for Oracle Cloud plan change and boot volume resizing
- Policies: Policy types including budget, max cores, max hosts, max memory, and max storage are now considered when provisioning a new cluster or when adding a new host to an existing cluster
- Policies: When provisioning Apps, Instance types containing multiple nodes (such as Redis master/replica) or Instances with scale factor are considered against policy types including budget, max containers, max cores, max memory, max storage, and max VM
- Policies: When completing cart checkout in the Service Catalog Persona view, the sum of all ordered items within the cart are considered against any policies that may be in place
- Policies: Improved handling for budget, max containers, max cores, max hosts, max memory, and max storage policies when adding nodes to Instances (manually or through auto-scaling and thresholds)
- Policies: Improved policy handling when provisioning Instances as it relates to specific handling of copy and scale scenarios, friendlier policy warning messages, and other improvements
- Storage: Added support for SMB2 file shares
- Terraform: Support added for Terraform v0.14
- UI: Executions list page (Automation > Executions) now automatically refreshes to display new executions
- Whitelabel: Set your own "Terms and Privacy String" to be displayed on the login page. This field takes HTML markup allowing administrators to link to an outside Terms and Conditions page, Privacy Policy page, or anything else

|morpheus| API & CLI Improvements
=================================

- API/CLI: "Clone To Image" action added for API/CLI
- API/CLI: User Sources metadata can now be accessed through either |morpheus| API or CLI, User Sources information has been moved from the Users section of |morpheus| API docs to the `Identity Sources <https://apidocs.morpheusdata.com/#identity-sources>`_ section
- API/CLI: Calls to the ``api/invoices`` endpoint no longer return the list of ``lineItems`` for each Invoice by default as, in some cases, this list could be very large. Instead, a call to ``api/invoices`` now returns the new property ``lineItemCount``. Invoices has a new parameter, ``includeLineItems=true``, which can be used when needed. GET calls for a specific Invoice (``/api/invoices/:id``) will still return ``lineItems``
- API/CLI: The ``rawData`` parameter for the ``invoices`` and ``invoices-line-items`` API is now deprecated

Fixes
=====

- Backup: Fixed an issue that could cause Hyper-V Instance restore not to complete when restoring to a new Instance

Appliance Updates
=================

- Installer: Improved RAM validation handling on FIPS-compliant installer to prevent unwanted validation fails in certain cases
- Installer: Java upgrade to 8u282-b08

..
  Morpheus Hub
  ============

  Agent/Node Package Updates
  ==========================
