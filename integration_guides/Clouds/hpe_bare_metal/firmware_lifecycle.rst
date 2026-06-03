Firmware and Driver Lifecycle Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting with HPE BMaaS version 1.0.0,HPE |morpheus| Enterprise supports firmware and driver updates for HPE ProLiant bare-metal servers using preloaded tasks and workflows. This capability enables administrators to centrally manage server firmware and driver compliance using HPE Service Pack for ProLiant (SPP) images, executed directly from the HPE Morpheus appliance.

 Firmware and driver updates are performed through Jobs and Workflows in HPE Morpheus and can be run in Dry Run (inventory)or Deploy modes. Updates can target firmware only, drivers only, or both, depending on operational requirements. The update process supports multiple servers per job and provides detailed execution logs for auditing and troubleshooting.

  Prerequisites
 Before performing firmware and driver updates, ensure the following:

  
- HPE
- BM Plugin version 1.0.0 or later is installed.

 
- An appropriate
- HPE
- SPP ISO is available for each server generation (for example, Gen10 and Gen11 require different SPP ISOs).

 
- The
- HPE
- Morpheus appliance has access to the SPP ISO, either through:

  
  - A locally downloaded ISO file, or

 
  - A URL accessible without authentication.

  
- For driver inventory and updates within a deployed operating system:

  
  - iSUT (Integrated Smart Update Tools) and AMS (Agentless Management Service) must be installed and running on the target servers.

 
  - ESXi hosts are expected to already have iSUT installed.

Adding HPE SPP to Virtual Image Library
---------------------------------------

AddingHPE SPP to the Virtual Image Library
This procedure describes how to add an HPE Service Pack for ProLiant (SPP) ISO to the Morpheus Virtual Images library for use in firmware and driver update workflows.

  
#. Obtain the appropriate
#. HPE
#. SPP ISO for the target ProLiant server generation. 
#. NOTE
#. A separate ISO is required for each server generation (for example, Gen10 and Gen11). 
#. In the Morpheus appliance, navigate to
#. Library
#. >
#. Virtual Images.
#. Click
#. Add
#. >
#. SPP.
#. Enter a name for the image (for example,
#. HPE
#. Gen10 SPP 2025.09.00
#. ). 
#. From the
#. Operating System
#. drop-down list, select the appropriate
#. HPE
#. SPP for Gen…
#. entry. 
#. Add the SPP ISO using one of the following methods: 
  - Upload the locally downloaded ISO file, or 
  - Select
  - URL / PATH
  - and paste the full URL for the ISO.  
#. Leave all other properties at their default values. 
#. Click
#. Save Changes.
#. NOTE
#. When uploading a local file, wait for the upload to complete. 
#. In the
#. Virtual Images
#. list, wait until: 
  - Source
  - shows
  - Uploaded 
  - Status
  - shows
  - Active  
#. Record the
#. ID
#. of the Virtual Image entry. This ID is required when creating the update job.

Installing iSUT on Deployed Instances
-------------------------------------

(Optional)
To enable driver inventory and updates within the operating system, iSUT and AMS must be installed on each deployed instance.


#. Navigate to
#. Provisioning
#. >
#. Instances.
#. Select the target instance.   
#. NOTE
#. Since the workflow requires iLO credentials, only one instance can be selected at a time. Multiple instances cannot be targeted for a single iSUT/AMS install.  
#. Click
#. Actions
#. >
#. Run Workflow.
#. Select the appropriate workflow:  
  0. Download and Install iSUT and AMS (Linux), or 
  1. Download and Install iSUT and AMS (Windows)  
#. Enter the
#. iLO credentials
#. for the targeted bare metal server.   
#. NOTE
#. These are iLO credentials, not OS credentials.  
#. Click
#. Execute.
#. Monitor progress from the
#. History
#. tab until the workflow completes.

Creating and Running an SPP Update Job
--------------------------------------

  This procedure describes how to create and execute aHPE Morpheus Job to perform firmware and driver updates using an HPE SPP image.


#. Navigate to
#. Provisioning
#. >
#. Jobs.
#. Click
#. Add.
#. Enter a name for the job.   
#. NOTE  
  - Separate jobs are required for different server generations (for example, Gen10 vs Gen11).

 
  - Create separate jobs for
  - Dry Run
  - and
  - Deploy
  - executions.


#. Select
#. Workflow Job
#. as the
#. Job Type
#. and click
#. Next.
#. Select
#. Deploy SPP
#. as the
#. workflow.
#. Enter the
#. SPPVIRTUALIMAGE
#. value using the ID of the Virtual Image created earlier. 
#. Select a
#. DEPLOYMODE
#. :   
  - DryRun
  - : Performs inventory only

 
  - Deploy
  - : Applies firmware and/or driver updates


#. For
#. SPP Deploy Content
#. , choose one of the following:   
  - Firmware only

 
  - Drivers only

 
  - Firmware and Drivers

NOTEDriver inventory and updates require iSUT and AMS to be running on the target servers.
#. In the
#. Nodes
#. field, enter the iLO details for each target server in JSON format (minimum 1 server, maximum 30 servers). For example:  
#. [

#. {

#. \"ilo_ip\":\"1.2.3.4\",

#. \"ilo_user\":\"user1\",

#. \"ilo_password\":\"password1\"

#. },

#. {

#. \"ilo_ip\":\"1.2.3.5\",

#. \"ilo_user\":\"user2\",

#. \"ilo_password\":\"password2\"

#. }

#. ]
  
#. Optional: 
#. Create a schedule, or leave the job as
#. Manual.
#. Select
#. Run Now
#. if you want to execute the job immediately. 
#. Click
#. Next
#. , review the settings, and click
#. Complete.
#. If the job was not run immediately, click the
#. gear icon
#. next to the job and select
#. Execute.
Monitoring and Completion
-------------------------


#. Monitor job progress from the
#. Job Executions
#. tab. 
#. Execution time may range from
#. 15 minutes to over one hour
#. , depending on:  
  0. Number of servers 
  1. Deploy mode 
  2. Selected content 
  3. Firmware and driver versions on the target servers  
#. Upon completion, detailed logs are available in the
#. Job Executions
#. tab.   
  - Do not enter any values in
  - Custom Config
  - .

  
  - Servers are not automatically rebooted as part of the update process. 
    - If a reboot is required to complete updates, it must be performed manually at a time appropriate for the hosted services.

Post-SPP Firmware Update Cold Power Cycle
-----------------------------------------

Post-SPP Firmware Update - Mandatory Cold Power Cycle   After applying an HPE Service Pack for ProLiant (SPP) on Gen11 and Gen12 servers, a full cold power cycle is required to ensure proper initialization of updated firmware components.

 An iLO reset or standard operating system reboot is not sufficient after an SPP update.

 Failure to perform a cold power cycle may result in:

  
* Inconsistent Redfish storage inventory 
* Smart Array controller desynchronization 
* Missing or stale drive objects 
* Management platform initialization failures 
* Incomplete firmware activation  Perform the following steps for cold power cycle:

  
#. Power OFF the server
#. :Shut down gracefully through the operating system or iLO interface. Confirm the server is completely powered off. 
#. Disconnect AC Power
#. : Physically remove all power cables from the server power supplies. 
#. Wait for 60 Seconds
#. : Allow sufficient time for residual power to drain. This clears controller cache and resets hardware state.

 
#. Reconnect Power
#. : Reattach all power cables securely. 
#. Power ON the Server
#. : Boot the system normally.  A full AC power removal forces:

  
* Smart Array controller re-enumeration 
* PCI bus reinitialization 
* Storage firmware reload 
* Redfish object tree regeneration 
* Hardware state synchronization  This process resolves the majority of post-SPP Redfish storage inconsistencies observed on Gen11 and Gen12 platforms.

 HPEstrongly recommends performing a full cold power cycle after major firmware bundle updates to ensure all updated components are fully initialized.

