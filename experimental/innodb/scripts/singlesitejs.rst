MySQL Shell Cluster Multi Site JS Script
========================================

    .. tabs::

        .. group-tab:: JavaScript

            .. code-block:: js

                print('Setting up a Multi Site MySQL InnoDB Cluster, \n');

                var mysqlAdmin = "clusterAdmin";
                var nodeA = ["mydb-1", "mydb-2", "mydb-3"];
                var clusterA = "A";
                var dbPass = shell.prompt('Please enter a password for the MySQL clusterAdmin account: ', {type: "password"});

                try {
                    print('Setting required MySQL settings for cluster on the nodes....\n');

                    var nodes = nodeA; // Combine nodeA and nodeB arrays

                    nodes.forEach(function (node) {
                    dba.configureInstance(mysqlAdmin + "@" + node + ":3306", { password: dbPass });
                    });

                    print('.\nInstances ready to be clustered.');

                    print('Setting up Primary InnoDB Cluster...\n');
                    shell.connect(mysqlAdmin + "@" + nodeA[0] + ":3306", dbPass);

                    var cluster = dba.createCluster(clusterA);

                    print('Adding instances to the Cluster.');

                    nodeA.slice(1).forEach(function (node) {
                        cluster.addInstance({ user: mysqlAdmin, host: node, port: 3306, password: dbPass });
                        print('.');
                    });

                    print('.\nInstances successfully added to the Cluster.');

                    print('\nInnoDB Cluster deployed successfully.\n');
                } catch (e) {
                    print('\nThe InnoDB Cluster could not be created.\n\nError: ' + e.message + '\n');
                }