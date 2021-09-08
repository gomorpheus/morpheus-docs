.. _Release Notes:

************************
|morphver| Release Notes
************************

.. No highlights this time, small update
  .. include:: highlights.rst

.. WARNING:: OpenStack v2 Identity API was deprecated in v5.2.9 and is removed in v5.3.3+

.. NOTE:: Items appended with :superscript:`5.3.3` are also included in that version

New Features
============

:Amazon:
- Added Asia Pacific (Seoul) region support

:Pricing:
- Added KRW (South Korean Won) currency support

:UI:
- Help text added to Add Integration modals warning that HTTP URLs are insecure and not recommended :superscript:`5.3.3`

:vCD:
- System administrator account credentials can now be provided to authenticate vCD Cloud integrations in Morpheus. Previously, only organization administrator credentials could be used. Keep in mind that you will need to set the system administrator account credentials appropriately, for example, to be able to see entities created by the organization administrator :superscript:`5.3.3`

|morpheus| API and CLI Improvements
===================================

:Checks:
- The ``apiKey`` is now returned in GET calls for Push API-Type Monitoring Checks :superscript:`5.3.3`

Fixes
=====

:Terraform:
- Fixed an issue where Terraform App and Instance wizard :guilabel:`NEXT` buttons would not deactivate once clicked, allowing multiple submissions for validation. In some scenarios, this could cause the Morpheus app node to run out of memory :superscript:`5.3.3`

Appliance & Agent Updates
=========================
