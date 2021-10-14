Helm Blueprints
---------------

If you're using Helm Charts to manage Kubernetes applications, |morpheus| allows you to bring them in from a Git repository as a Blueprint. The selected repository must be integrated with |morpheus| before creating the Blueprint.

To create a new Helm Blueprint, navigate to Provisioning > Blueprints. Click :guilabel:`+ ADD`.

On the Name tab of the New Blueprint modal, enter a name for your new Blueprint. In the Type dropdown menu, select Helm. Click guilabel:`NEXT`.

In the Blueprint Summary section, complete the following fields as needed:

- **NAME:** Enter a name for this Blueprint as it will appear in the |morpheus| Blueprints list
- **DESCRIPTION:** An optional description field for your Blueprint
- **CATEGORY:** An optional category tag for your Blueprint, such as web, utility, or app
- **IMAGE:** An optional image icon to more easily identify your Blueprint from a list. If no image is uploaded, a default image will be used

In the Helm Configuration section, complete the following fields as needed to sync in configuration from a Git repository:

- **CONFIG TYPE:** "Git Repository"
- **SCM INTEGRATION:** If a pre-existing SCM integration is selected here, the available selections in the "Repository" dropdown menu will be filtered to show only those associated with the chosen SCM integration
- **REPOSITORY:** Select the repository in which your configuration resides
- **BRANCH OR TAG:** The branch in which your configuration resides
- **CHART PATH:** The path to the folder within the repository containing your configuration files, enter "./" if this is the top level folder within the repository
- **CONFIG:** Config files within your selected folder are displayed here for confirmation

Once finished, click :guilabel:`COMPLETE`.

Your new Helm Blueprint is now saved and should be visible in the list of Blueprints. Blueprints are deployed in the Provisioning > Apps section of |morpheus|. See the Apps section of |morpheus| docs for more information on that process.
