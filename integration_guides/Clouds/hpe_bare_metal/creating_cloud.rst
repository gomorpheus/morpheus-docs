Creating an HPE BMaaS Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

About this task
```````````````

Creating an HPE BMaaS Cloud integrates physical infrastructure into the |morpheus| management plane, establishing a logical boundary for bare-metal resources to enable group-based policies and proxy configurations. This setup allows for onboarding HPE ProLiant servers for automated provisioning and lifecycle management.

To create an **HPE BMaaS Cloud** in |morpheus| for HPE ProLiant bare-metal operations, follow this procedure:

Procedure
`````````

#. Navigate to :menuselection:`Infrastructure --> Clouds` in the |morpheus| interface.
#. Click the :guilabel:`+ Add` button.
#. Locate and select the HPE BMaaS Cloud type as **HPE Bare Metal (BMaaS)**, and then click :guilabel:`Next`.
#. Enter the name, code, Labels, Location, and complete any additional required details for the cloud.
#. (Optional) In :guilabel:`Provisioning Command`, select a Proxy for provisioned bare metal instances if required, then click :guilabel:`Next`.
#. For the group, you may either select **Use Existing** or **Create New**:

   - To use an existing group, choose :guilabel:`Use Existing` and select the desired group from the drop-down list.
   - To create a new group, select :guilabel:`Create New` and enter a group name.

#. Click :guilabel:`Complete` to finish creating the HPE BMaaS Cloud.

After completing these steps, the HPE BMaaS Cloud appears in the Infrastructure > Clouds list and is ready to have bare-metal servers imported.
