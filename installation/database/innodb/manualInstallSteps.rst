Manual Install Steps
====================

Single Site Full Install 
^^^^^^^^^^^^^^^^^^^^^^^^

    .. include:: ./manualInstall.rst
      :start-after: Manual-Section-Start
      :end-before: Manual-Section-Stop

* Install MySQL Shell. (This does not have to be installed on the DB nodes. In prod it would probably be installed on each Morpheus app node)
    
    .. include:: ./mysqlShell.rst
      :start-after: Install-Section-Start
      :end-before: Install-Section-Stop

* Setup Cluster using MySQL Shell (clusterAdmin is the admin user we created, dba-1 is one of the DB Nodes)

    .. include:: ./manualInstall.rst
      :start-after: Single-Section-Start
      :end-before: Single-Section-Stop

* Install MySQL Router 

    This should be installed on each Morpheus App Node

      .. include:: ./mysqlRouter.rst
        :start-after: Install-Section-Start
        :end-before: Install-Section-Stop

* Configure MySQL Router
      
      .. include:: ./mysqlRouter.rst
        :start-after: Config-Section-Start
        :end-before: Config-Section-Stop
        
* InnoDB MySQL Config (my.cnf)

    .. include:: ./mysql-cnf.rst

MultiSite Full Install 
^^^^^^^^^^^^^^^^^^^^^^

    .. include:: ./manualInstall.rst
      :start-after: Manual-Section-Start
      :end-before: Manual-Section-Stop

* Install MySQL Shell. (This does not have to be installed on the DB nodes. In prod it would probably be installed on each Morpheus app node)

    .. include:: ./mysqlShell.rst
      :start-after: Install-Section-Start
      :end-before: Install-Section-Stop

* Setup Cluster using MySQL Shell (clusterAdmin is the admin user we created, dba-1 is one of the DB Nodes)

    .. include:: ./manualInstall.rst
      :start-after: Multi-Section-Start
      :end-before: Multi-Section-Stop    

* Install MySQL Router 

    This should be installed on each Morpheus App Node

      .. include:: ./mysqlRouter.rst
        :start-after: Install-Section-Start
        :end-before: Install-Section-Stop

* Configure MySQL Router
      
      .. include:: ./mysqlRouter.rst
        :start-after: Config-Section-Start
        :end-before: Config-Section-Stop
        
* InnoDB MySQL Config (my.cnf)

    .. include:: ./mysql-cnf.rst

* Create Morpheus User and Database 
    
    .. include:: ./innodb-config-generic.rst        

    


    

    



                
