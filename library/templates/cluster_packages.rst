Cluster Packages
----------------

Cluster Packages are created and can then be associated with Cluster Layouts. Cluster Packages themselves are created from Spec Templates. The Spec Templates and Cluster Layouts sections of |morpheus| docs include more information on creating those constucts and show the steps to deploy sample builds.

Creating a Cluster Package
^^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to the Cluster Packages List page (|LibTemClu|). System Cluster Packages are listed here. These are included as part of |morpheus| pre-built Cluster Layouts and cannot be edited or viewed. User-created Cluster Layouts are also listed here and these may be edited. To begin creating a new Cluster Package, click :guilabel:`+ ADD` and configure the following:

- **NAME:** A friendly name for the Cluster Package in |morpheus|
- **CODE:** An identifying code for the Cluster Package for use with |morpheus| API and CLI
- **DESCRIPTION:** An optional description for the Cluster Package
- **PACKAGE VERSION:** A version designation for the Cluster Package
- **ICON:** An identifying icon for the Cluster Package, this will appear in a list with other packages associated with a Cluster Layout
- **DARK MODE IMAGE:** An alternate icon for the Cluster Package used when the dark theme is enabled on the |morpheus| appliance
- **TYPE:** A type selection for the package, see dropdown for options
- **PACKAGE TYPE:** A one-word descriptor for the package such as "calico", "prometheus", etc.
- **ENABLED:** When marked, this Cluster Package is available to be set on Cluster Layouts
- **REPEAT INSTALL:**
- **SPEC TEMPLATES:** Use the Typeahead field to select relevant Spec Templates to build the Cluster Package

.. image:: /images/templates/cluster-packages/cluster-packages.png
