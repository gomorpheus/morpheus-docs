Percona XtraDB
^^^^^^^^^^^^^^

This page is designed to help troubleshoot issues with Percona XtraDB.  

Additional information:

    https://docs.percona.com/percona-xtradb-cluster/8.0/index.html

Log Locations
`````````````

    RHEL (default location): ``/var/log/mysqld.log``
    
    Ubuntu (default location): ``/var/log/mysql/error.log``

Common Percona Commands
```````````````````````

    **Recover Offline Cluster**
        
        #. Check all nodes to see if the mysql service is started on any of the nodes

            .. code-block:: bash

                systemctl status mysql

        #. If the service is started on any of the nodes, you should be able to start the service on all the other nodes

            .. code-block:: bash

                systemctl start mysql

        #. If the service is not started on any of the nodes, check the ``seqno`` in ``/var/lib/mysql/grastate.dat`` on each server and find the one with the highest number

            .. code-block:: bash

                cat /var/lib/mysql/grastate.dat

        #. After locating the node with the highest number, it needs to be bootstrapped.  Bootstrapping a node will make it authoritative and the data from it will be replicated to all the nodes

            #. On the node with the highest ``seqno``, verify if ``safe_to_bootstrap`` is ``1`` in ``/var/lib/mysql/grastate.dat``
            
                .. code-block:: bash

                    cat /var/lib/mysql/grastate.dat

            #. If ``safe_to_bootstrap`` is not ``1``, then modify the file so it is ``1``

                .. code-block:: bash

                    # Alternatively, you can use vi/vim/nano to do the same
                    sed -i 's/safe_to_bootstrap: 0/safe_to_bootstrap: 1/g' /var/lib/mysql/grastate.dat

        #. Once the node with the highest ``seqno`` has been select and ``safe_to_bootstrap`` is ``1`` in ``/var/lib/mysql/grastate.dat``, bootstrap the node

            .. code-block:: bash

                systemctl start mysql@bootstrap.service

        #. Assuming no failures are seen, now start the remaining nodes mysql service

            .. code-block:: bash

                systemctl start mysql

        #. After a short time, all nodes should come online

        #. Reference the following links to help verify the cluster, if needed:

            :ref:`Percona TLS RHEL Verify`
            :ref:`Percona TLS Ubuntu Verify`