Jenkins
-------

The Morpheus Jenkins Integration is easy to add and will allow you to see all jobs, builds, statuses of those builds, commits notes, and links to artifacts.

Adding Jenkins Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /images/integration_guides/build-integrations/Jenkins-add-modal.png

#. Navigate to |AdmInt|
#. Select :guilabel:`+ NEW INTEGRATION`
#. Select Jenkins
#. Fill in the following:

   Name
      Name of the Integration in |morpheus|
   Enabled
      Enable the Integration. Uncheck to disable the Jenkins Integration sync Job.
   Jenkins URL
      Jenkins URL or IP address. ex: ``https://jenkins.morpheus.com``
   Username
     Jenkins service account username
   Password
     Jenkins service account password

#. :guilabel:`SAVE CHANGES`

   .. important::

       By default Jenkins is configured to run on port 8080.  If this has been modified you will need to append the alternate port to the the ``Jenkins URL``

Viewing Jobs in Jenkins Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the |morpheus| Jenkins integration you can view all of your jobs.

.. image:: /images/integration_guides/build-integrations/jenkinsJobsView.png
   :align: center

Viewing Builds and Build Statuses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the |morpheus| Jenkins integration you can view recent builds with ID, Status, Date, Duration, Artifacts, Commit Notes and Run By user data. Artifacts will automatically link to the Artifact url in Jenkins, and the urls can be used in Morpheus Deployments (dependent on Jenkins configuration).

.. image:: /images/integration_guides/build-integrations/jenkinsBuildView.png
   :align: center
