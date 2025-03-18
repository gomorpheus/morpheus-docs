MySQL Shell Cluster Multi Site JS Script
========================================

    .. tabs::

        .. group-tab:: JavaScript

            .. code-block:: js
        
                print('Setting up a Multi Site MySQL InnoDB Cluster, \n');

                var mysqlAdmin = "clusterAdmin";
                var nodeA = ["cdb-1", "cdb-2", "cdb-3"];
                var nodeB = ["ddb-4", "ddb-5", "ddb-6"];
                var mySqlRouterUserPassword = 'P@ssw0rd!'
                var clusterSet = "clusterSet";
                var clusterA = "A";
                var clusterB = "B";
                var dbPass = shell.prompt('Please enter a password for the MySQL clusterAdmin account: ', {type: "password"});

                try {
                    print('Setting required MySQL settings for cluster on the nodes....\n');

                    var nodes = [...nodeA, ...nodeB]; // Combine nodeA and nodeB arrays

                    nodes.forEach(function (node) {
                         dba.configureInstance({user: mysqlAdmin, host: node, port: 3306, password: dbPass});
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

                    print('Creating Cluster Set.');
                    var clusterset = cluster.createClusterSet(clusterSet);
                    print('.\nCluster Set Successfully Created.');

                    print('Creating Replica Cluster.');
                    var replicaCluster = clusterset.createReplicaCluster(nodeB[0] + ":3306", clusterB);

                    print('Adding instances to the Replica Cluster.');
                    nodeB.slice(1).forEach(function (node) {
                        replicaCluster.addInstance(node + ":3306");
                    });

                    print('\nInnoDB Cluster deployed successfully.\n');

                    print('\nCreating "routeruser" for the MySQL routers\n');
                    cluster.setupRouterAccount('routeruser', {password: mySqlRouterUserPassword})
                } catch (e) {
                    print('\nThe InnoDB Cluster could not be created.\n\nError: ' + e.message + '\n');
                }