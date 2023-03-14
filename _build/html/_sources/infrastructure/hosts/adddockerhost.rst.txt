Docker Hosts
------------

Overview
^^^^^^^^

Morpheus can provision Docker Hosts into any cloud, convert existing Hosts to Docker Hosts, or even make itself a Docker Host.

.. image:: /images/infrastructure/add_docker.gif

To add a Docker Host to any cloud:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Navigate to Infrastructure -> Hosts
2. Click the +CONTAINER HOST button
3. Select a container host type

.. image:: /images/infrastructure/add_docker.png

4. Select a Group

.. image:: /images/infrastructure/select_group.png

.. [caption="Figure 3: ", title="Select Group", alt="Select Group"]

5. Enter the following:
  * Name
  * Description
  * Visibility
  * Select a Cloud
  * Enter tags (optional)

Then click NEXT.

.. image:: /images/infrastructure/create_host.png

.. [caption="Figure 4: ", title="Create Host", alt="Create Host"]

6. Configure the host options

Select a Service Plan (Volume, Memory and CPU count fields may not be shown if selected service plan does not have custom options enabled).
  * Add and set size the volumes
  * Set memory size
  * Set the CPU count
  * Select a network

Optionally configure the following:
  * OS username
  * OS password
  * Domain name
  * Hostname (default is the name previously provided for the container host)

. Then click the NEXT button


image::infrastructure/create_host_2.png[caption="Figure 5: ", title="Create Host", alt="Create Host"]

7. Optionally add any Automation Workflows and configure for Backups.

.. image:: /images/infrastructure/docker_host_automation.png

[caption="Figure 6: ", title="Docker Host Automation", alt="Automation"]

8. Review and click Complete to save

.. image:: /images/infrastructure/save_docker_host.png

.. [caption="Figure 7: ", title="Save Docker Host", alt="Save"]

Your new container host will begin provisioning, and soon be running and ready for containers.
