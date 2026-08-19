.. _manager-os-updates:

Morpheus Manager Base OS Updates
--------------------------------

The HPE Morpheus Manager QCOW2 image includes an Ubuntu base operating system. Maintaining this operating system is separate from upgrading the |morpheus| application package:

- A **Morpheus application upgrade** installs a new HPE-provided ``morpheus-appliance`` package and runs ``morpheus-ctl reconfigure``. Follow :doc:`upgrading`.
- A **Manager base-OS update** installs Ubuntu packages from APT repositories. Follow this page and the update guidance published by HPE for the applicable Manager release.
- An **Ubuntu release upgrade** changes the Ubuntu release, such as Ubuntu 22.04 LTS to 24.04 LTS. Do not perform an Ubuntu release upgrade on a Manager appliance unless HPE provides a procedure for the exact source and target releases.

.. important::

   Do not run an unrestricted ``apt upgrade``, ``apt full-upgrade``, or unattended upgrade on a production Manager based only on package availability from Canonical. Before updating, obtain the HPE guidance for the installed Manager release. It must identify the validated Ubuntu series, repository pockets, components, architecture, and any required snapshot date, package holds, exclusions, or sequencing. If those inputs are not published, contact HPE Support.

Update Models
^^^^^^^^^^^^^

Choose the model that matches the Manager appliance's network access. All models must expose the same HPE-validated package set to the appliance.

Connected
.........

The Manager reaches the HPE-approved Canonical repositories directly or through an HTTP proxy. Restrict outbound access according to organizational policy and the repository endpoints identified in the applicable HPE guidance.

Restricted Network
..................

The Manager reaches an internal APT repository, but not Canonical repositories. Canonical recommends a repository mirror such as self-hosted Landscape. The mirror synchronizes the HPE-approved Ubuntu series, pockets, components, and ``amd64`` architecture from the upstream archive and serves them inside the restricted network.

For the Landscape workflow, see `Canonical's repository mirroring documentation <https://documentation.ubuntu.com/landscape/how-to-guides/repository-mirrors/>`_. Configure the Manager to trust the repository signing key and use only the internal repository URL. If the internal publication is re-signed, distribute its public key through the site's approved trust process; do not bypass APT signature verification.

Fully Disconnected
..................

Canonical's fully disconnected Landscape model uses an online Landscape server outside the air gap and an offline Landscape server inside it:

#. Create identical repository structures and profiles on both servers, including the same signing key.
#. On the online server, synchronize only the Ubuntu content identified by the HPE update guidance.
#. Transfer the repository data through the site's approved removable-media process, including integrity and malware checks.
#. Place the data in the corresponding repository location on the offline Landscape server.
#. Publish the internal repository and verify its metadata and signatures before pointing the Manager at it.

See `Canonical's air-gapped repository procedure <https://documentation.ubuntu.com/landscape/how-to-guides/repository-mirrors/manage-repositories-in-an-air-gapped-or-offline-environment/>`_ for the version-specific Landscape steps and repository paths.

.. warning::

   Canonical states that its fully disconnected Landscape workflow cannot produce a delta containing only changes since the previous transfer. Refreshing the offline server can require transferring the complete repository contents. Ubuntu repositories can require hundreds of GB, so size the mirror and transfer media before approving this design. Limit architectures, components, series, and pockets only as allowed by the HPE update guidance.

Prepare the Update
^^^^^^^^^^^^^^^^^^

#. Record the Manager and Ubuntu versions:

   .. code-block:: bash

      sudo morpheus-ctl version
      . /etc/os-release && printf '%s %s (%s)\n' "$NAME" "$VERSION_ID" "$VERSION_CODENAME"
      dpkg --print-architecture

#. Obtain the HPE update guidance for this Manager release and record its repository inputs and package restrictions in the change record.
#. Confirm the appliance resolves and reaches only the intended repository, whether direct, proxied, or internal.
#. Create and verify a recoverable appliance backup. If the virtualization platform provides a supported VM snapshot workflow, take a snapshot in accordance with the site's recovery policy. A snapshot is not a substitute for an application and database backup.
#. Confirm adequate free space in ``/``, ``/boot``, and ``/var`` and resolve any interrupted package operation before the maintenance window.
#. Test the exact repository state and update sequence on a representative non-production Manager before production rollout. Canonical recommends staged testing for production server updates.

Validate the Repository State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On Ubuntu 24.04 LTS and later, Ubuntu repository definitions normally use the deb822-formatted ``/etc/apt/sources.list.d/ubuntu.sources`` file. Earlier Ubuntu releases commonly use ``/etc/apt/sources.list``. Compare the configured URIs, suites, components, signing key, and optional snapshot with the HPE update guidance.

Refresh metadata and review the proposed change without installing packages:

.. code-block:: bash

   sudo apt update
   apt list --upgradable
   sudo apt-get --simulate upgrade

Use ``apt-cache policy <package>`` to verify the candidate version and source of a package. Stop if APT reports signature errors, unreachable sources, unexpected repositories, removals, held-package conflicts, or candidate versions outside the HPE-approved update set.

Canonical's `Ubuntu snapshot service <https://documentation.ubuntu.com/server/how-to/software/snapshot-service/>`_ can reproduce a dated archive state. Use a snapshot identifier only when HPE publishes or approves it for the Manager release. A snapshot is not independently evidence of HPE compatibility.

Apply the Update
^^^^^^^^^^^^^^^^

#. Schedule a maintenance window. Base-OS updates can restart services, and kernel or low-level library updates can require an appliance reboot.
#. Stop or drain user activity according to the topology's maintenance procedure.
#. Run the exact APT command and package sequence from the applicable HPE update guidance. Do not substitute ``full-upgrade`` or add packages that were not included in the validated procedure.
#. Review the command result and ``/var/log/apt/`` and ``/var/log/dpkg.log`` for failures.
#. If ``/var/run/reboot-required`` exists, reboot within the maintenance window. Do not enable automatic reboot unless HPE explicitly supports it for this appliance and the deployment topology.

Canonical enables automatic security updates on standard Ubuntu Server installations through ``unattended-upgrades``. Before relying on that behavior for a Manager appliance, confirm the HPE policy for the image and release. An internal mirror alone does not ensure that ``unattended-upgrades`` selects the intended origins, and Ubuntu 24.04 can restart affected services through ``needrestart``.

Validate the Manager
^^^^^^^^^^^^^^^^^^^^

After package installation and any required reboot:

#. Confirm that APT and dpkg completed successfully and no reboot remains pending.
#. Confirm ``morpheus-ctl status`` reports the expected services running.
#. Sign in to the Manager UI and verify the appliance version, system health, and expected integrations.
#. For an HVM deployment, confirm managed hosts and clusters reconnect and report their expected state. A Manager base-OS update does not update the HVM host OS.
#. Record installed package versions, update logs, reboot time, and health-check results in the change record.

Recovery and Escalation
^^^^^^^^^^^^^^^^^^^^^^^

Do not attempt an Ubuntu release downgrade or ad hoc package downgrade after a failed update. Preserve ``/var/log/apt/``, ``/var/log/dpkg.log``, ``journalctl`` output for the affected boot, the repository configuration, and the simulated or actual package transaction.

If the Manager does not recover after standard service or appliance restart checks, use the previously validated recovery procedure to restore the appliance and database, then contact HPE Support with the preserved evidence. For an air-gapped environment, also preserve the transferred repository manifest, signing-key fingerprint, and integrity-verification results.
