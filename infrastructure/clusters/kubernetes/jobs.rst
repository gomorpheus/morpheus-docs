.. _k8s-jobs:

Kubernetes Jobs
===============

Overview
--------

|morpheus| supports three distinct job types within Kubernetes clusters: **Jobs**, **CronJobs**, and **Deploy Jobs**. These are managed through the cluster Workloads tab and can be created, monitored, and deleted from the |morpheus| UI.

Jobs are executed via the ``KubernetesJobExecutorService`` and can be run on-demand or scheduled.

Job Types
---------

Job
^^^

A Kubernetes Job creates one or more Pods and ensures a specified number of them successfully terminate. Jobs are useful for batch processing, data migrations, and one-off tasks.

Key characteristics:

- Runs to completion (not continuously)
- Tracks successful and failed Pod completions
- Supports parallelism and completion count configuration
- Automatically cleaned up based on TTL settings

CronJob
^^^^^^^

A CronJob creates Jobs on a repeating schedule defined by a cron expression. Useful for periodic tasks such as backups, report generation, and cleanup operations.

Key characteristics:

- Schedule defined in standard cron format (e.g., ``0 */6 * * *`` for every 6 hours)
- Creates a new Job object on each scheduled run
- Configurable concurrency policy (Allow, Forbid, Replace)
- History limits for successful and failed Jobs

Deploy Job
^^^^^^^^^^

Deploy Jobs are |morpheus|-specific job types that execute deployment operations against Kubernetes clusters. They combine the deployment workflow with job semantics, allowing deployment operations to be tracked as discrete units of work.

Creating Jobs
-------------

Via Cluster ACTIONS Menu
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Clusters > [cluster name]``
#. From the ACTIONS menu, select **Run Workload**
#. Select the workload type: **Job**, **Deployment**, **StatefulSet**, or **DaemonSet**
#. Configure:

   NAME
     Name for the Job
   NAMESPACE
     Target namespace
   IMAGE
     Container image to run
   COMMAND
     Command to execute in the container (optional)
   ARGS
     Arguments to pass to the command (optional)
   COMPLETIONS
     Number of successful completions required (Jobs only)
   PARALLELISM
     Number of Pods to run concurrently (Jobs only)
   RESTART POLICY
     ``Never`` or ``OnFailure``

#. Select :guilabel:`RUN`

Via Provisioning Jobs
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Provisioning > Jobs``
#. Select :guilabel:`+ ADD`
#. Configure the job targeting a Kubernetes cluster
#. Set the schedule (for CronJob behavior) or run on-demand

Monitoring Jobs
---------------

Active and completed Jobs are visible on the cluster Workloads tab:

- **STATUS** — Running, Succeeded, Failed
- **COMPLETIONS** — Progress toward completion count (e.g., ``2/3``)
- **DURATION** — Time since Job creation
- **AGE** — Time since the Job was created

For detailed information:

- Click on a Job to see its Pods and their statuses
- View Pod logs for debugging failed Jobs
- Check events for scheduling or resource issues

Deleting Jobs
-------------

To delete a Job from |morpheus|:

#. Navigate to the cluster Workloads tab > Jobs subtab
#. Select the Job to delete
#. Click :guilabel:`DELETE`
#. Confirm deletion

When deleting a Job, |morpheus| uses a ``Background`` propagation policy, which means:

- The Job object is deleted immediately
- Associated Pods are garbage collected asynchronously by Kubernetes
- Pod logs remain accessible briefly until Pods are fully terminated

.. NOTE:: Deleting a CronJob also removes all Jobs it has created that are still running.

Job Templates
-------------

|morpheus| tracks Jobs internally as ``JobTemplate`` records linked to their parent cluster (``ComputeServerGroup``). Each Job template stores:

- The Job name (``internalId``)
- The namespace (``organizationId``)
- Reference to the parent cluster

This allows |morpheus| to manage the full lifecycle of Jobs across the cluster.

Best Practices
--------------

- **Set TTL for finished Jobs:** Use ``ttlSecondsAfterFinished`` to auto-clean completed Jobs
- **Use resource limits:** Always set CPU and memory limits on Job Pods to prevent resource starvation
- **Monitor CronJob history:** Review failed Job history regularly; configure ``failedJobsHistoryLimit`` appropriately
- **Use restart policies wisely:** ``OnFailure`` retries the container in-place; ``Never`` creates a new Pod on failure
- **Namespace isolation:** Run batch Jobs in dedicated namespaces to avoid impacting production workloads
