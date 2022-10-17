Labels
======

Labels are a categorization feature designed to allow easier filtering of list views in the |morpheus| Library. The following library constructs can be labeled:

- Tasks
- Workflows
- Jobs
- Instance Types
- Layouts
- Node Types
- Virtual Images
- Inputs
- Option Lists

Labels are visible from the list views of any constructs listed above. By default, labels are turned on in the list view but if they aren't showing, click the gear icon (|gear|) and then click Labels to enable them.

The list view contains a row of filters above the list, one of which is Labels. Enter a search string to find an existing label or click the dropdown button within the field to select an existing label. This will filter the list to show only constructs which have the selected label.

.. NOTE:: Any list may be filtered by any label which exists anywhere in the current Tenant. When a label is removed from a construct and no other constructs also have that label, |morpheus| will remove the label from the list during its nightly sync. It is normal for a label to continue to exist in this list, even if it's not currently applied to any constructs, until the next nightly sync has taken place.

.. image:: /images/provisioning/library/labels/labels.png

Adding and Removing Labels
--------------------------

Labels can be created when adding or edited any of the supported constructs listed above. When adding or editing the object, enter or edit the comma-separated list of labels you wish to apply.

.. image:: /images/provisioning/library/labels/labeladd.png
  :width: 50%
