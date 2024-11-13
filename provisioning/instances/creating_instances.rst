Creating Instances
------------------

The Instance catalog is where you will create new workloads targeting the |clusters| and/or VMware vCenter Clouds available to the |morpheus| environment. The list contains only Instance Types relevant to the provisioning engines which enabled and integrated in the current appliance.

To get started, simply click the :guilabel:`+ Add` button in the upper right of the |ProIns| page. A modal will display allowing the catalog to be searched. Once an item is selected, it is just a matter of following the steps through the wizard.

.. TIP:: The Instance catalog can be customized via role-based access control (RBAC) to restrict provision types only to certain Roles. It is completely customizable.

The next step will ask for a Group and Cloud to be selected. The Group is an abstract representation that can contain multiple |clusters| or VMware vCenter integrations. Clouds can be in multiple Groups and Groups are also useful for using RBAC to restrict provisioning access and set retainment policies. The wizard continues by allowing us to choose a name for the Instance as well as an environment.

.. NOTE:: Currently the Environment option is most useful for presenting the user with informative metadata around the Instance when coming back to it later.

Moving on, it is now time to configure the Instance. Depending on the Instance Configuration that is chosen, fields will change. This can include cloud-specific fields (i.e. target hosts for |clusters| or datastores for VMware Clouds). There will also be options like setting an initial user account. Some of these fields are optional and will be represented as such in the wizard.

One last step before the Instance can be provisioned is the Automation step. It is here that you can select Tasks which will run during the provision process and these Tasks must complete successfully in order for the Instance status to be reported as successful. Tasks are either Bash or Powershell scripts which can be configured in the |LibAut| section.

Now that the steps are completed for provisioning the selected Instance type, simply review your selections and complete. The Instance will automatically show up in the Instances list and its provisioning state will be represented. Depending on what was provisioned this step can range from seconds to minutes.

Converting Discovered Resources to Managed Instances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating new cloud integrations (or updating existing ones), users may opt for |morpheus| to onboard any existing resources that currently reside in the Cloud. For example, these may be virtual machines that exist on vCenter hosts prior to integration with |morpheus|. With the Add/Edit Cloud modal open, mark INVENTORY EXISTING INSTANCES for |morpheus| to automatically onboard these resources. Not only will |morpheus| inventory these hosts at the time the cloud is integrated (or updated), it will also continue to poll the target cloud every five minutes (by default) for newly added or removed servers. Users can see these discovered servers by looking in |InfCom|. Depending on the type of resource, it may appear on the Virtual Machines tab, the Containers tab, or another tab. Additionally, we can see a list of discovered servers on Cloud detail pages (|InfClo| > Selected Cloud). Just click on the tabs for VMs, Containers or Hosts tab. Discovered resources will be indicated as such whereas containers which are associated with a managed Instance will be marked as a "Managed".

Additionally, |morpheus| allows users to convert discovered resources into managed Instances. Begin from the server detail page (|InfComVir| > selected machine) and from the ACTIONS menu select "Convert to Managed". At this point, we must make a number of selections:

- Select a Group (this dropdown contains a filtered list of Groups in which the associated Cloud resides)
- Username and password for a seeded account
- Opt to install |morpheus| Agent or not
- Select the Instance Type which should be associated with the new Instance containing this VM
- Identify the operating system
- Select a Plan (this dropdown contains a filtered list of plans which correlate to the size of the VM)

Finally, click :guilabel:`EXECUTE`. Once this process is completed, the server will be indicated as "Managed" in the servers list. Additionally, a new Instance will appear on the Instances List page (|ProIns|). We can now work with it in the same way we can work with any other Instance, such as by expanding the Instance horizontally with added nodes.
