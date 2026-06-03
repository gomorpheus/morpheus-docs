Migrations Plans
----------------

Migration plans are created and run from the Migrations section of the Tools menu (:menuselection:`Tools --> Migrations`). Migrations happen by creating and running Migration Plans. Plans are created in a pending state, meaning an additional action must be undertaken to set the plan in motion. Thus, Plans may be created which are intended to be run at a later time. Once finished, completed Plans remain on the Migrations list page for later review and, if desired, deletion.

Creating Migration Plans
^^^^^^^^^^^^^^^^^^^^^^^^

Begin creating a Migration Plan from the Migrations list page (:menuselection:`Tools --> Migrations`). This page contains a list of all Migrations already created, including those completed, currently running, and available to be run (pending). To start a new Migration, click :guilabel:`+ ADD`.

From the SETUP tab of the CREATE MIGRATION PLAN modal, configure the following:

- **NAME:** A name to identify the Migration
- **SOURCE:** The source VMware vCenter Cloud
- **TARGET:** The target Cloud containing the HVM Cluster
- **RESOURCE POOL:** The selected destination HVM Cluster
- **GROUP:** The Group which should own the migrated VMs

When finished, click :guilabel:`NEXT`.

The next step is to choose VMs from the selected VMware source Cloud to migrate. Select as many as desired given current recommendations regarding the maximum size due to storage space and available bandwidth (see the previous section). Selected VMs will form a list at the bottom of the modal. When finished, click :guilabel:`NEXT`.

The next tab establishes resource mapping. Listed, you will see the current networks and storage locations for the selected VMs. Choose destination networks and destination storage locations for each. Optionally, enter existing Linux or Windows user credentials and choose if prechecks or guest tools installation should be skipped. Click :guilabel:`NEXT`.

The final tab is a review tab where all current selections can be checked. Return to any previous tabs, if necessary, to update selections.

Running Migration Plans
^^^^^^^^^^^^^^^^^^^^^^^

At this point, the Migration is created but will not run without additional input. The Migration is in a "Pending" state. All selections made when configuring the Migration are shown here. To execute the Migration, click :guilabel:`RUN`. The length of time it will take for the Migration to run depends on many factors. Once run, the Migration detail page will provide status updates on VMs currently being migrated, which have completed successfully, and if any have failed. The History tab provides greater detail on current and past migration actions taken. The Destination tab includes details on VMware VMs which have successfully been migrated to the HVM Cluster. Migrations are run just once and may be kept indefinitely after for review. When a Migration is no longer needed, click :guilabel:`DELETE`.
