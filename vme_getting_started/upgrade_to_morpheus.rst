Upgrading to |morphfirst|
^^^^^^^^^^^^^^^^^^^^^^^^^

This section of the guide goes over the process for upgrading a |firstuse| appliance to a full |morphfirst| appliance. |firstuse| and |morphfirst| are essentially the same product with |morpheus| focused specifically on management and consumption of |clusters| and |morph| adding on support for many other public and private Cloud types with a richer orchestration and automation experience (in addition to all features included with |morpheus|). |morph| requires separate licensing, reach out to your account manager if you're unsure which licensing entitlements you can access. This guide is intended for |morpheus| administrators to upgrade their existing appliances to |morph| and assumes a level of comfort with the Linux command line and the version upgrade process for |morpheus| and/or |morph|. After upgrading, refer to |morph| `documentation <https://docs.morpheusdata.com/en/latest/>`_ for use guides to consuming the full |morph| feature set.

Prerequisites
`````````````

- |manager| version 8.0.1+
- A bucket integrated with |manager| which can house an appliance database backup
- The |morph| upgrade package (version 8.0.4+)
- A |morph| license to add following the upgrade to enable the full feature set

Back Up the Appliance
`````````````````````

Start by taking a fresh backup of the appliance database. View the appliance backup job by navigating to |BacJob|. As in the screenshot, there should be a backup job named "Morpheus Appliance." If an appliance backup job is not shown, enable the "Backup Appliance" setting within global settings (|AdmSetBac|).

.. image:: /images/vmeInstall/upgradeCheckBackups.png

Click :guilabel:`Run Now` and wait for a new green checkmark to appear indicating a new run of the backup job was successful.

Package Installation
````````````````````

Upgrading the |manager| to a full |morph| appliance is as simple as installing the |morph| package over the existing |morpheus| package in a process very similar to version upgrades you may have done in the past. First, download the |morph| ``.deb`` package. The download URL shown below is a placeholder, reach out to your account manager if you're unsure where to find the download URL for the latest |morph| package.

.. code-block:: bash

  wget https://url.to.morpheus-appliance_x.x.x-x.deb

Next, stop the Morpheus UI.

.. code-block:: bash

  sudo morpheus-ctl stop morpheus-ui

Install the |morph| package and force it to overwrite.

.. code-block:: bash

  dpkg -i -force-overwrite morpheus-appliance_x.x.x-x.deb

Wait for the installation to complete. There will be warnings about conflicts which may be safely ignored. When installation is complete, you will see a message similar to the screenshot below:

.. image:: /images/vmeInstall/upgradeFinishInstall.png

Now, remove the |morpheus| package.

.. code-block:: bash

  sudo apt-get remove -y hpe-vm-essentials

Following removal, restart any recommended services if prompted.

.. image:: /images/vmeInstall/upgradeRemoveVme.png

We must now clean up OpenSearch directories. Currently, |morph| uses ElasticSearch while |manager| uses OpenSearch. Migration through snapshots is not supported due to this incompatibility. In general, OpenSearch and ElasticSearch contain VM performance metrics. This data can be considered ephemeral and safely deleted as the default retention is only 30 days. |morph| is planned to migrate to OpenSearch in the future and at that point, this cleanup step will not be required and metrics will persist across an upgrade to |morph|. Remove the following directories:

.. code-block:: bash

  rm -rf /var/run/morpheus/opensearch
  rm -rf /opt/morpheus/service/opensearch

Next, run the reconfigure command. This will configure ElasticSearch for use with the upgraded appliance.

.. code-block:: bash

  sudo morpheus-ctl reconfigure

Once the reconfigure is complete, make sure all |morph| services are started

.. code-block:: bash

  sudo morpheus-ctl status

If any services need started, use the following command:

.. code-block:: bash

  sudo morpheus-ctl start {service name}

You can watch the logs to see when the UI comes back up:

.. code-block:: bash

  sudo morpheus-ctl tail morpheus-ui

When the Morpheus ASCII logo appears, you should be able to reach the UI from a web browser.

Upgrading the License
`````````````````````

Now that |morph| UI is reachable, the license must be upgraded. Navigate to |AdmSetLic| where you'll see a field to paste in your license key. Once again, contact your account manager if you have questions on accessing your license key. Finally, make sure you select the appropriate option of either stacking the license onto an existing license or replacing it. Then, click :guilabel:`Update`.

At this point, the process is complete. Now that the full |morph| feature set is unlocked, refer to |morph| `documentation <https://docs.morpheusdata.com/en/latest/>`_ going forward.
