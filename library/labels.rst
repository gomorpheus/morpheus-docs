Labels
======

- .. toggle-header:: :header: Labels Video Demo

    .. raw:: html

        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
            <iframe src="//www.youtube.com/embed/igdLB7fbv6g" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
        </div>

    |

Labels are a categorization feature designed to allow easier filtering of list views in the |morpheus| Library. The following library constructs can be labeled:

- Tasks
- Workflows
- Jobs
- Instance Types
- Instances
- Layouts
- Node Types
- Servers
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

Running Automation Against Label Targets
----------------------------------------

The |morpheus| automation constructs Jobs, Tasks, and Workflows can be run against Instance Labels or Server Labels. When creating the Job or executing the Task or Workflow, select either Server Label or Instance Label. After specifying the Label, the automation will be run against all Instances or Servers which have the indicated Label. Currently, only one Label may be selected and users cannot enter multiple Labels in the field. If a non-existent Label is entered, the automation simply will not run against any Workloads since the Label does not match any.

.. NOTE:: Instance and server Labels are separate. Even if some Instances or servers have the same Label, the automation is only run against the selected construct (Instance Labels or Server Labels).

.. image:: /images/automation/executeLabel.png
