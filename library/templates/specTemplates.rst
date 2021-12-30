Spec Templates
--------------

Spec Templates allow |morpheus| users to leverage several major Infrastructure-as-Code solutions. These are typically JSON or YAML-based configuration files which make creating and managing multiple resource types easier. |morpheus| allows users to create and/or manage a collection of these templates for different solutions and from different sources.

|morpheus| currently supports Spec Templates of the following types:

- Kubernetes Spec
- Helm Chart
- Terraform
- ARM Template
- CloudFormation Template
- OneView Server Profile Template
- UCS Service Profile Template

|morpheus| also allows users to leverage templates pulled from URL sources, online repositories (such as GitHub), or you can write a template locally inside the "NEW SPEC TEMPLATE" modal.

.. TIP:: To see |morpheus| Spec Templates in action, take a look at our guide on `creating custom Instance Types using Terraform <https://docs.morpheusdata.com/en/latest/getting_started/guides/terraform_instances.html>`_ or see our `KnowledgeBase <https://support.morpheusdata.com/s/article/How-to-use-Spec-Templates-to-create-a-custom-instance-type?language=en_US>`_ for another example where a CloudFormation Spec Template is used to create a provisionable custom Instance Type.

Creating a Spec Template
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |LibTemSpe|
#. Click :guilabel:`+ ADD`
#. Complete the following fields, then click :guilabel:`SAVE CHANGES`:

  - **NAME**
  - **TYPE:** See the previous section for a complete list of Spec Template types
  - **SOURCE:** Local, Repository, or URL
  - **CONTENT:** If this is a local Spec Template, supply the template in this field. If the template is supplied through a URL or online repository, the CONTENT field will change to allow the user to point |morpheus| to that resource
  - **VERSION:** (Only displayed on Terraform Spec Templates) Enter a Terraform version number to force a specific version when provisioning your Terraform Instance Type or App, assuming your Terraform Runtime setting (|AdmSetPro| Tab) is "auto". If Terraform Runtime is set to "manual", |morpheus| will use the version of Terraform installed on the appliance box
