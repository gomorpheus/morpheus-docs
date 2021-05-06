Getting Started with Terraform Instance Types
---------------------------------------------

`Terraform <https://www.terraform.io/intro/index.html>`_ is a common tool that allows IT administrators to map out infrastructure as code in configuration files and supports all of the popular providers used in the modern datacenter. Once configured, Terraform will plan, deploy, and manage the infrastructure as needed. Configuration files can be brought under version control so teams can easily make changes to environments. Infrastructure can also be monitored for drift and corrective action can easily be taken.

|morpheus| allows users to on-board or even draft Terraform spec directly. With the configuration on-board, we can begin to piece together infrastructure constructs into the |morpheus| Library as Layouts and Instance Types. With the Library items staged, users can deploy new infrastructure directly into the selected providers. Once deployed, infrastructure can be monitored for drift from within |morpheus| UI. When needed, we can plan and take corrective action easily from the detail page of a |morpheus| Terraform Instance.

In this section, we've discussed a high-level overview of Terraform and working with Terraform in the |morpheus| context. In the next section, we'll actually onboard Terraform spec, create Library items, and deploy real infrastructure to AWS with |morpheus|.

Terraform Instance Types in Action
----------------------------------

In this example, we're going to deploy a VPC and three subnets to AWS using Terraform and |morpheus|. I've created Spec Templates to onboard ``.tf`` configuration files which handle the AWS provider (with assume role for account flexibility), VPC creation, subnet creation, and variable injection.

We'll onboard the Terraform configuration files as modular Spec Templates, create new Instance Types with custom Layouts for the |morpheus| Library, and set up Option Types to inject variable values at provision time. Once deployed, we'll take a look at the new infrastructure in |morpheus| and go over the management capabilities for the new environment.

Spec Templates
--------------

Terraform configuration is stored as a Spec Template in |morpheus|. You can store your configuration as one monolithic file for each Instance Type you intend to create or you can create individual Spec Templates for modular pieces which can be reused across multiple Instance Types. When added to the Layout later, we'll be able to include as many Spec Templates as we wish which enables us to reuse smaller modular pieces if desired.

Spec Templates are added in the |morpheus| Library (Provisioning > Library > Spec Templates tab). We can pull in the template from some type of repository, such as through a Github integration, or write new spec directly into the New Spec Template modal. In most cases, the spec will be pre-existing and pulled in from a version-controlled repository so that is what I will do here as well. Click :guilabel:`+ ADD`, complete the fields as I've done in the example below and click :guilabel:`SAVE CHANGES`.

.. image:: /images/imtegration_guides/terr_inst_guide/1newSpec.png

- .. toggle-header:: :header: **AWS Subnet by Count**

    .. image:: /images/imtegration_guides/terr_inst_guide/2tfSubnetByCount.png

- .. toggle-header:: :header: **AWS Terraform Default Vars**

    .. image:: /images/imtegration_guides/terr_inst_guide/3tfDefaultVars.png

- .. toggle-header:: :header: **AWS Provider Role Assume**

    .. image:: /images/imtegration_guides/terr_inst_guide/4tfAssumeRole.png

- .. toggle-header:: :header: **AWS Terrform Locals**

    .. image:: /images/imtegration_guides/terr_inst_guide/5tfLocals.png

- .. toggle-header:: :header: **AWS VPC**

    .. image:: /images/imtegration_guides/terr_inst_guide/6tfVpc.png

Option Types and Option Lists
-----------------------------

In order to create the Layout later in the guide, I need to create four Option Types so the user can make certain selections at provision time. I wrote my Terraform Configuration with this flexibility in mind so that the same Instance Type can be reused in different scenarios. In this particular case, I'm populating the Option Types with manual Option Lists but they can also be populated through REST calls or calls to the |morpheus| API when needed.

Option Lists are created in the Library (Provisioning > Library) under the Option Lists tab. These are lists of items which will be used to create dropdown selections at provision time. Click :guilabel:`+ ADD`, complete the fields as I've done in the example below and click :guilabel:`SAVE CHANGES`. I've created one each for the AWS account selection, region selection, and CIDR mask input.

.. image:: /images/imtegration_guides/terr_inst_guide/7optionList.png

Option Types are also created in the Library under the Option Types tab. In this case, I'm creating four Option Types. Three of them will display as dropdown selections and will be tied to one of the Option Lists we just made. The other will be a simple text input where the user can indicate the total number of subnets that should be created. Click :guilabel:`+ ADD`, complete the fields as I've done in the example below and click :guilabel:`SAVE CHANGES`.

.. image:: /images/imtegration_guides/terr_inst_guide/8optionType.png

Instance Type
-------------

At this point we're ready to create a new Instance Type. We'll give the Instance Type a name, which users will use to identify the Instance Type from the list in the provisioning wizard. We don't need to set much else in this case, most of the pieces we've created in previous steps will be associated with the Layout that we create next. The Layout will also be tied to the Instance Type we're creating now. Instance Types are also created in the Library (Provisioning > Library) under the Instance Types tab. Click :guilabel:`+ ADD`, complete the fields as I've done in the example below and click :guilabel:`SAVE CHANGES`.

.. image:: /images/imtegration_guides/terr_inst_guide/9instanceType.png

Layout
------

The Layout will bring together everything we've made to this point, the Spec Templates, Option Types and the Instance Type. We can add a new one from the Instance Type detail page (Provisioning > Library > Instance Types > Selected Instance Type) by clicking :guilabel:`+ ADD LAYOUT`. We can also create one from the Layouts section (Provisioning > Library > Layouts tab) by clicking :guilabel:`+ ADD`.

First, change the TECHNOLOGY value to Terraform and the fields will change to allow proper configuration. Next, provide a name for your Layout. If you're creating the Layout through the Layout tab rather than from the Instance Type detail page, you'll need to identify the Instance Type the Layout goes with. Using the typeahead fields at bottom of the modal window, add our four Option Types and our five Spec Templates to the Layout. Finally, point the layout to a TFVAR SECRET from |morpheus| Cypher if needed. You can see a screenshot of my Layout configuration below

.. image:: /images/imtegration_guides/terr_inst_guide/10Layout.png

Provisioning
------------

Now, we're ready to provision new infrastructure into AWS using |morpheus| and Terraform. Just like any other Instance Type, we begin from the Instances list page (Provisioning > Instances) and click :guilabel:`+ ADD`. Select the Instance Type we've just created and move on to the GROUP tab of the wizard. Here you'll give the new instance a name and select your Group and Cloud. Once finished, you'll move on to the CONFIGURE tab where we'll see the Option Types we created and associated with the Layout. Once finished with this tab, step through the rest of the wizard to complete the process. You can see the options I've selected for this configuration in the image below.

.. image:: /images/imtegration_guides/terr_inst_guide/11configureTab.png

Review the New Instance
-----------------------

After completing the wizard, from the History tab of the Instance detail page users can review the Terraform plan being executed and see the output while the resources are still being provisioned.

.. image:: /images/imtegration_guides/terr_inst_guide/12historyTab.png

Once the provisioning process is complete, head to the State tab. Here we can see and link through to the associated Spec Templates. If needed, you can also edit the configuration spec by clicking on the pencil icon at the end of the row for any listed Spec Template.

By clicking :guilabel:`APPLY STATE`, the user can once again see the Option Type selections which were presented during the initial provisioning and make changes when needed. After making changes and clicking :guilabel:`NEXT`, |morpheus| will show the plan output no different than if you'd run ``terraform plan``. On clicking :guilabel:`COMPLETE`, the plan will be executed as if you'd run ``terraform apply``. Back on the State tab you will see the output from the Apply process as well as an indicator of the success or failure of the operation.

.. image:: /images/imtegration_guides/terr_inst_guide/13stateTab.png

|morpheus| will also regularly check for drift from the Terraform configuration. On the State tab near the top is a "Drift Status" indicator. This will either show Drift or No Drift depending on the situation. |morpheus| will automatically check for drift every few minutes but you can perform a manual check at any time by clicking :guilabel:`REFRESH STATE`. Drift can be corrected when needed by reapplying state (:guilabel:`APPLY STATE` button).
