.. _Percona TLS Ansible:

Percona XtraDB Cluster with TLS (Ansible Deployment)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The prupose of this document is to provide a consistent way to deploy Percona using Ansible.  The Percona deployment is specifically setup for Morpheus,
it should not be used in conjunction with any other application.

#. Install the necessary requirements on the OS using the package manager

    .. tabs::

        .. group-tab:: RHEL 8/9

                .. code-block:: bash
            
                    dnf install -y git sshpass
                        
        .. group-tab:: Ubuntu

            apt-get install -y python3-venv sshpass

#. Setup a virtual environment, this will help prevent modifications to the OS and provide an easy way to cleanup the environment when complete

    .. code-block:: bash

        python3 -m venv ~/percona
        source ~/percona/bin/activate

#. Install Ansible and create the playbook/host files

    Examples of the playbooks and additional information can be found in the readme of the `ansible-role-XtraDB-Cluster <https://github.com/tryfan/ansible-role-XtraDB-Cluster>`_ role,
    which will be used later

    #. Install Ansible using ``pip``

        .. code-block:: bash
    
            python3 -m pip install ansible

    #. Create and input the configuration into ``~/playbook.yml``

        .. code-block:: bash
            
            vim ~/playbook.yml
    
        Example file below, be sure to modify the contents as needed following the documentation above

        .. code-block:: yaml

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
    
    #. Create and input the configuration into ``~/hosts.yml``

        .. code-block:: bash

            vim ~/hosts.yml
    
        Example file below, be sure to modify the contents as needed following the documentation above

        .. code-block:: ini

            [db]
            node1 ansible_host=192.168.100.104
            node2 ansible_host=192.168.101.27
            node3 ansible_host=192.168.100.197
                    
#. Download the Ansible role needed for the playbook

    .. code-block:: bash
                
        mkdir .ansible/roles -p
        git clone https://github.com/tryfan/ansible-role-XtraDB-Cluster ~/.ansible/roles/ansible-role-XtraDB-Cluster
                
                
#. Disable ``StrictHostKeyChecking`` via an environment variable

    If this is not disabled, the Ansible will fail unless the target hosts' key is added to ``~/.ssh/known_hosts``

    .. code-block:: bash

        export ANSIBLE_HOST_KEY_CHECKING=False

#. Run the ``ansible-playbook`` command

    Ensure the inventory and playbook file name match what was created previously.  Also be sure to replace <username> with the username of the target host

    .. code-block:: bash

        export ANSIBLE_HOST_KEY_CHECKING=False
        ansible-playbook --inventory-file hosts.yml --user <username> --ask-pass --become --ask-become-pass playbook.yml
                
#. Finally, cleanup the environment

    .. code-block:: bash
        
        deactivate
        rm ~/percona -rf