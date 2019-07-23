Jenkins
-------
The Morpheus Jenkins integration is easy to add and will allow you to see all jobs, builds, and statuses of those builds.


Adding Jenkins Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ```Administration -> integrations```
#. Select :guilabel:`+ NEW INTEGRATION`
#. Select Jenkins
#. Fill in the following:

  Name
     Name of the Integration in |morpheus|
  Enabled
     Enable the Integration
  Jenkins URL
     Jenkins URL or IP address.
  Username
    Username for Jenkins
  Password
     Password for Jenkins

#. :guilabel:`SAVE CHANGES`

.. IMAGE:: /images/integration_guides/build/Jenkins-add-modal.png

.. IMPORTANT::

    By default Jenkins is configured to run on port 8080.  If this has been modified you will need to update the URL to point to the new port.


Viewing Jobs in Jenkins Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the |morpheus| Jenkins integration you can view all of your jobs.

.. IMAGE:: /images/integration_guides/build/Jenkins-Jobs-View.png


Viewing Builds and Build Statuses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the |morpheus| Jenkins integration you can view all of your builds and statuses.

.. IMAGE:: /images/integration_guides/build/Jenkins-Builds-View.png
