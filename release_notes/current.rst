.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. important:: Updates to many plugins have been timed for the release of |morpheus| 5.5.2. After completing an appliance upgrade, see share.morpheusdata.com and apply any plugin updates which may be available. Those using a previous version of the Infoblox plugin (prior to 1.1.0) should note that the new version of the plugin will not directly upgrade an existing version. This is because previous versions had an identification code of ``infoblox2`` whereas all future versions will have an identification code of ``infoblox``. This was done to prevent conflicts with the embedded Infoblox integration during early testing which has now concluded. The best upgrade approach is to remove any existing integrations and earlier versions of the plugin, apply the new plugin, and re-create your integrations. If this is not possible, there is a method by which existing pool server entries in the database can be updated for the new version of the plugin. Please contact |morpheus| support for assistance with this process and reference this note in your case.

.. important:: |morpheus| |morphver| requires Morpheus Worker |workerVer|. Please upgrade any existing Morpheus Workers to the |workerVer| Worker package to ensure compatibility with Morpheus |morphver|.

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

Release Dates
  - 5.5.2 |releasedate|

- .. toggle-header:: :header: **5.5.2 RBAC Changes**

    |morpheus| 5.5.2 includes changes to Role permissions UI, improvements to make permissions more granular, and changes to make Tenant management easier for Primary Tenant administrators. See the embedded video below for a walkthrough of the changes.

    .. raw:: html

        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
            <iframe src="//www.youtube.com/embed/752-Bnu0f30" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
        </div>

|

New Features
============



Fixes
=====



Appliance & Agent Updates
=========================
