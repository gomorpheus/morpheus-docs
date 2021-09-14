CloudFormation Blueprints
--------------------------

CloudFormation Blueprints consume new or existing CloudFormation templates to create easily-deployable application stacks. CloudFormation templates in |morpheus| are JSON or YAML-formatted text documents that declare all relevant AWS resources needed for the provisioned application. They can be created directly in the New Blueprint modal or pulled in from existing Git repositories.

If needed, Amazon has educational resources available for getting started with CloudFormation. They can be found in the `AWS CloudFormation documentation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html>`_.

To create a new CloudFormation Blueprint, navigate to Provisioning > Blueprints. Click :guilabel:`+ ADD`.

On the Name tab of the New Blueprint modal, enter a name for your new Blueprint. In the Type dropdown menu, select CloudFormation. Click :guilabel:`NEXT`

In the Blueprint Summary section, complete the following fields as needed:

- **NAME:** Enter a name for this Blueprint as it will appear in the |morpheus| Blueprints list
- **DESCRIPTION:** An optional description field for your Blueprint
- **CATEGORY:** An optional category tag for your Blueprint, such as web, utility, or app
- **IMAGE:** An optional image icon to more easily identify your Blueprint from a list. If no image is uploaded, a default image will be used

Depending on whether we need the |morpheus| Agent installed and/or cloud-init enabled, mark the following boxes in the next section:

- **INSTALL AGENT**
- **CLOUD INIT ENABLED**

In some cases, you must explicitly acknowledge that your template contains certain capabilities in order for the application to successfully be deployed. There is more information on this in Amazon's documentation `here <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html>`_. If any of the following capabilities are contained in your application, acknowledge them by marking any of the following boxes that apply:

- **CAPABILITY_IAM**
- **CAPABILITY_NAMED_IAM**
- **CAPABILITY_AUTO_EXPAND**

Continuing on with the CloudFormation Configuration section, complete the following fields as needed when entering your configuration directly into the new Blueprint:

- **CONFIG TYPE:** "CloudFormation Template JSON (.json)"
- **CONFIG TYPE:** "CloudFormation Template YAML (.yaml)"
- **CONFIG:** Enter your configuration here

In the CloudFormation Configuration section, complete the following fields as needed when syncing in configuration from a Git repository:

- **CONFIG TYPE:** "Git Repository"
- **SCM INTEGRATION:** If a pre-existing SCM integration is selected here, the available selections in the "Repository" dropdown menu will be filtered to show only those associated with the chosen SCM integration
- **REPOSITORY:** Select the repository in which your configuration resides
- **BRANCH OR TAG:** The branch in which your configuration resides
- **WORKING PATH:** The path to your configuration files
- **CONFIG:** Your selected config file

Once finished, click :guilabel:`COMPLETE`.

Your new CloudFormation Blueprint is now saved and should be visible in the list of Blueprints. Blueprints are deployed in the Provisioning > Apps section of |morpheus|. See the Apps section of |morpheus| docs for more information on that process.
