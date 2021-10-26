Kubernetes Blueprints
---------------------

|morpheus| allows you to store Kubernetes configuration YAML files for easy deployment on-demand. Kubernetes Blueprints can be built by pulling in Kubernetes spec stored as a |morpheus| Spec Template object, those tracked under version control in a Git repository, or you can write them directly in the New Blueprint modal.

To create a new Kubernetes Blueprint, navigate to |LibBluApp|. Click :guilabel:`+ ADD`.

On the Name tab of the New Blueprint modal, enter a name for your new Blueprint. In the Type dropdown menu, select Kubernetes. :guilabel:`NEXT`

In the Cluster Summary section, complete the following fields as needed:

- **NAME:** Enter a name for this Blueprint as it will appear in the |morpheus| Blueprints list
- **DESCRIPTION:** An optional description field for your Blueprint
- **CATEGORY:** An optional category tag for your Blueprint, such as web, utility, or app
- **IMAGE:** An optional image icon to more easily identify your Blueprint from a list. If no image is uploaded, a default image will be used

Complete the Kubernetes Configuration section as follows depending on your Config Type selection.

To consume a |morpheus| Spec Template containing Kubernetes spec:

- **CONFIG TYPE:** "Kubernetes Spec"
- **SPEC TEMPLATE:** Use the typeahead field to locate the desired Spec Template

To draft or paste configuration directly in the New Blueprint modal:

- **CONFIG TYPE:** "Kubernetes Yaml Spec"
- **CONFIG:** Enter your YAML configuration template here

To consume YAML configuration files tracked in a Git repository:

- **CONFIG TYPE:** "Git Repository"
- **SCM INTEGRATION:** If a pre-existing SCM integration is selected here, the available selections in the "Repository" dropdown menu will be filtered to show only those associated with the chosen SCM integration
- **REPOSITORY:** Select the repository in which your configuration resides
- **BRANCH OR TAG:** The branch in which your configuration resides
- **WORKING PATH:** The path to your configuration files
- **CONFIG:** Your selected config file

Once finished, click :guilabel:`COMPLETE`.

Your new Kubernetes Blueprint is now saved and should be visible in the list of Blueprints. Blueprints are deployed in the |ProApp| section of |morpheus|. See the Apps section of |morpheus| docs for more information on that process.
