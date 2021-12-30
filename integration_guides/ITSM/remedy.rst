Remedy
------

PreRequisites
^^^^^^^^^^^^^

The user used for this integration need to be an Administrator in Remedy or have all the permissions to the form that is outlined in the table below.

    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | API Endpoint                                                                        | Action | BMC Form                  | Existing BMC Role            |
    +=====================================================================================+========+===========================+==============================+
    |/api/arsys/v1/entry/CTM:People                                                       | GET    | CTM:People                | Contact People Admin         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/COM:Company?q=%27Status%27=%22Enabled%22&fields=values(Company) | GET    | COM:Company               | Atrium Foundation Admin      |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/User                                                            | GET    | User                      | User Administrator           |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/Group                                                           | GET    | Group                     | User Administrator           |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/CHG:Infrastructure%20Change                                     | POST   | CHG:Infrastructure Change | Infrastructure Change Master |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/CHG:Infrastructure%20Change                                     | PUT    | CHG:Infrastructure Change | Infrastructure Change Master |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/CHG:Infrastructure%20Change                                     | GET    | CHG:Infrastructure Change | Infrastructure Change Master |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_DiskDrive                           | POST   | BMC.CORE:BMC_DiskDrive    | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_DiskDrive                           | PATCH  | BMC.CORE:BMC_DiskDrive    | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_DiskDrive                           | GET    | BMC.CORE:BMC_DiskDrive    | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_DiskDrive                           | DELETE | BMC.CORE:BMC_DiskDrive    | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_IPEndpoint                          | POST   | BMC.CORE:BMC_IPEndpoint   | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_IPEndpoint                          | PATCH  | BMC.CORE:BMC_IPEndpoint   | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_IPEndpoint                          | GET    | BMC.CORE:BMC_IPEndpoint   | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_IPEndpoint                          | DELETE | BMC.CORE:BMC_IPEndpoint   | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_Memory                              | POST   | BMC.CORE:BMC_Memory       | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_Memory                              | PATCH  | BMC.CORE:BMC_Memory       | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_Memory                              | GET    | BMC.CORE:BMC_Memory       | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_Memory                              | DELETE | BMC.CORE:BMC_Memory       | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_Processor                           | POST   | BMC.CORE:BMC_Processor    | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_Processor                           | PATCH  | BMC.CORE:BMC_Processor    | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_Processor                           | GET    | BMC.CORE:BMC_Processor    | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/cmdb/v1.0/instances/BMC.ASSET/BMC.CORE/BMC_Processor                           | DELETE | BMC.CORE:BMC_Processor    | CMDB Data Change All         |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:ComputerSystem                                              | GET    | AST:ComputeSystem         | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:ComputerSystem                                              | PUT    | AST:ComputeSystem         | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:ComputerSystem                                              | POST   | AST:ComputeSystem         | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:IPEndpoint                                                  | GET    | AST:IPEndpoint            | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:IPEndpoint                                                  | PUT    | AST:IPEndpoint            | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:IPEndpoint                                                  | POST   | AST:IPEndpoint            | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:DiskDrive                                                   | GET    | AST:DiskDrive             | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:DiskDrive                                                   | PUT    | AST:DiskDrive             | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:DiskDrive                                                   | POST   | AST:DiskDrive             | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:Processor                                                   | GET    | AST:Processor             | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:Processor                                                   | PUT    | AST:Processor             | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:Processor                                                   | POST   | AST:Processor             | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:Memory                                                      | GET    | AST:Memory                | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:Memory                                                      | PUT    | AST:Memory                | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/arsys/v1/entry/AST:Memory                                                      | POST   | AST:Memory                | Asset Admin                  |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+
    | /api/jwt/login                                                                      | POST   |                           |                              |
    +-------------------------------------------------------------------------------------+--------+---------------------------+------------------------------+

Add Remedy Integration
^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmInt|
#. Select ``+ NEW INTEGRATION``
#. Select ``Remedy`` from the dropdown.
#. Add the following:

    NAME
     Name of the Integration in Morpheus.
    ENABLE
     Leave checked to enable the Integration.
    REMEDY HOST
     Url of the Remedy Instance. e.g: http://xx.xx.xx.xx:8008
    USER
     Enter in username
    PASSWORD
     Above Remedy user's password
    COMPANY
     The dropdown will populate with values as soon as the auth using the above creds are successful
    APPROVAL USER
     Full name of the user as it appear in Remedy. E.g: userid 'anish' would have full name as "Anish Abraham"
#. Save Changes
