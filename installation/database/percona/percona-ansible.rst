.. _Percona TLS Ansible:

Percona XtraDB Cluster with TLS (Ansible Deployment)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The prupose of this document is to provide a consistent way to deploy Percona using Ansible.  The Percona deployment is specifically setup for Morpheus,
it should not be used in conjunction with any other application.

.. tabs::

   .. group-tab:: RHEL

        .. code-block:: bash
    
            dnf install -y git sshpass
            python3 -m venv ~/percona
            source ~/percona/bin/activate
            python3 -m pip install ansible
            nano playbook.yml
                - hosts: db
                    gather_facts: true
                    become: true
                    roles:
                        - role: ansible-role-XtraDB-Cluster
                        xtradb_cluster_name: "prod-customer"
                        xtradb_root_password: yolo
                        xtradb_nodes_group: "db"
                        xtradb_bind_interface: eth0
                        xtradb_configure_firewalld: true
            nano hosts.yml
                [db]
                node1 ansible_host=192.168.100.104 ansible_ssh_common_args='-o StrictHostKeyChecking=no'
                node2 ansible_host=192.168.101.27 ansible_ssh_common_args='-o StrictHostKeyChecking=no'
                node3 ansible_host=192.168.100.197 ansible_ssh_common_args='-o StrictHostKeyChecking=no'
            mkdir .ansible/roles -p
            git clone https://github.com/tryfan/ansible-role-XtraDB-Cluster ~/.ansible/roles/ansible-role-XtraDB-Cluster
            export ANSIBLE_HOST_KEY_CHECKING=False
            ansible-playbook --inventory-file hosts.yml --user <username> --ask-pass --become --ask-become-pass playbook.yml
            deactivate
            rm ~/percona -rf

   .. group-tab:: Ubuntu

        TBD

.. tabs::

   .. group-tab:: RHEL

        TBD

   .. group-tab:: Ubuntu

        TBD
