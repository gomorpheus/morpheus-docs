ARM Blueprints
--------------

ARM Blueprints provide a simple and repeatable way of deploying infrastructure-as-code to Azure Clouds. Objects and properties are defined in a JSON file and are provisionable on-demand in *|ProApp|*

To create a new ARM Blueprint, navigate to |LibBluApp|. Click :guilabel:`+ ADD`.

On the Name tab of the New Blueprint modal, enter a name for your new Blueprint. In the Type dropdown menu, select ARM. :guilabel:`NEXT`

In the Blueprint Summary section, complete the following fields as needed:

- **NAME:** Enter a name for this Blueprint as it will appear in the |morpheus| Blueprints list
- **DESCRIPTION:** An optional description field for your Blueprint
- **CATEGORY:** An optional category tag for your Blueprint, such as web, utility, or app
- **IMAGE:** An optional image icon to more easily identify your Blueprint from a list. If no image is uploaded, a default image will be used

The ARM template itself is defined in the ARM Configuration section. Using the Config Type dropdown menu, we can opt to write or paste JSON configuration directly into this modal, or we can choose to bring in a JSON which we're keeping under version control in a Git repository.

Depending on whether we need the |morpheus| Agent installed and/or cloud-init enabled, mark the following boxes in the next section:

- **INSTALL AGENT**
- **CLOUD INIT ENABLED**

If writing or pasting your configuration JSON directly into the modal, fill out the following fields:

- **OS TYPE:** Identify the resources to be created as Linux or Windows
- **CONFIG TYPE:** ARM Template JSON (.json)
- **CONFIG:** Your JSON configuration template

If bringing in a template from a Git repository, fill out the following fields:

- **OS TYPE:** Identify the resources to be created as Linux or Windows
- **CONFIG TYPE:** "Git Repository"
- **SCM INTEGRATION:** If a pre-existing SCM integration is selected here, the available selections in the "Repository" dropdown menu will be filtered to show only those associated with the chosen SCM integration
- **REPOSITORY:** Select the repository in which your configuration resides
- **BRANCH OR TAG:** The branch in which your configuration resides
- **WORKING PATH:** The path to your configuration files
- **CONFIG:** Your selected config file

Once finished, click :guilabel:`COMPLETE`.

Your new ARM Blueprint is now saved and should be visible in the list of Blueprints. Blueprints are deployed in the |ProApp| section of |morpheus|. See the Apps section of |morpheus| docs for more information on that process.
