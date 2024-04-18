Packages
--------

Overview
^^^^^^^^

The ``/administration/packages`` is where |morpheus| packages (.morpkg, .mpkg, or .mopkg) can be uploaded to appliances. |morpheus| packages contain Library objects, such as Instance Types, Layouts, Node Types, Spec Temples and Cluster Layouts. |morpheus| packages consist of library objects as code compiled into a simple ``($.morpkg, $.mpkg, or $.mopkg)`` file, allowing for agile distribution, updating and sharing of Library configurations.

The addition of ``/administration/packages`` is primarily targeted for uploading future |morpheus|-provided packages, however users can create, distribute and/or import custom |morpheus| packages too. This section goes over the process for writing and preparing packages for upload to a |morpheus| appliance.

Role Permissions
^^^^^^^^^^^^^^^^

Access and capabilities for the **Packages** section is determined by the following role permissions:

Role: Feature Access: ``Admin: Plugins``
  - None: Cannot access Admin: Plugins section
  - Full: Access to Admin: Plugins and ability to upload |morpheus| packages (.morpkg, .mpkg, or .mopkg)

Uploading Packages
^^^^^^^^^^^^^^^^^^

``/administration/packages`` is targeted for uploading future |morpheus| provided packages's, however users will be able to create, distribute and/or import custom |morpheus| packages. Additional information on creating custom packages will be provided.
