Alibaba
-------

Features
^^^^^^^^

- Brownfield discovery
- Instance cloning
- Security group creation and management
- Docker and Kubernetes provisioning and management
- Usage tracking
- Two-way tag sync

Supported Regions
^^^^^^^^^^^^^^^^^

- ap-northeast-1 (亚太东北 1 (东京)
- ap-south-1 (亚太南部 1 (孟买)
- ap-southeast-1 (亚太东南 1 (新加坡)
- ap-southeast-2 (亚太东南 2 (悉尼)
- ap-southeast-3 (亚太东南 3 (吉隆坡)
- ap-southeast-5 (亚太东南 5 (雅加达)
- cn-beijing (华北 2)
- cn-chengdu (西南1（成都）)
- cn-guangzhou (华南3（广州）)
- cn-hangzhou (华东 1)
- cn-heyuan (华南2（河源）)
- cn-hongkong (香港)
- cn-huhehaote (华北 5)
- cn-qingdao (华北 1)
- cn-shanghai (华东 2)
- cn-shenzhen (华南 1)
- cn-wulanchabu (华北6（乌兰察布）)
- cn-zhangjiakou (华北 3)
- eu-central-1 (欧洲中部 1 (法兰克福)
- eu-west-1 (英国（伦敦）)
- me-east-1 (中东东部 1 (迪拜)
- us-east-1 (美国东部 1 (弗吉尼亚)

Integrate an Alibaba Cloud with |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add a new Cloud, navigate to |InfClo| and click :guilabel:`+ ADD`. Select "Alibaba Cloud" and click :guilabel:`NEXT`. Once the "ADD CLOUD" modal appears, configure the following:

- **NAME:** A friendly name for the Cloud in |morpheus|
- **CODE:** A Cloud code used to reference this Cloud in |morpheus| API
- **LOCATION:** An optional field for tracking location data related to this Cloud
- **VISIBILITY:** Public Clouds are available to all Tenants, Private Clouds are available to one selected Tenant
- **TENANT:** If the Cloud visibility is set to "Private", this field determines which Tenant the Cloud is exposed to
- **ENABLED:** When marked, the Cloud is available as a provisioning target
- **AUTOMATICALLY POWER ON VMS:** When marked, |moprheus| is the source of truth for the expected power state of Instances. |morpheus| tools should be used to control power state and |morpheus| will override any unexpected power states (such as if an instance were powered on or off from the Alibaba web console)
- **CREDENTIALS:** Select Local Credentials to enter authentication credentials on this modal, Existing Credentials to choose a pre-saved credential set, or New Credentials to enter authentication credentials on this modal and save them (in |InfTru|) for other uses later
- **ACCESS KEY:** (When Local Credentials or New Credentials are selected) A valid Access Key for an Alibaba Cloud account
- **SECRET KEY:** (When Local Credentials or New Credentials are selected) A valid Secret Key for an Alibaba Cloud account
- **INVENTORY:** When marked, |morpheus| will automatically onboard existing instances in the Alibaba Cloud account as unmanaged servers
- **REGION:** Select the Alibaba Cloud region to associate with the Cloud (if this list is empty, check your Access and Secret Key credentials)
- **VPC:** Select the Alibaba Cloud VPC to associate with the Cloud (if this list is empty, check your Access and Secret Key credentials)

.. include:: ../advanced_options.rst

Following Integration
^^^^^^^^^^^^^^^^^^^^^

After the integration has been created, |morpheus| will sync existing workloads (if you've opted to inventory), security groups, tags, and more. Synced workloads can be viewed from |InfCom|. If Plans aren't immediately available within a few minutes after the integration is created, navigate to the Cloud detail page (|InfClo| > Your Integrated Alibaba Cloud), click :guilabel:`REFRESH` and click "Daily". Shortly thereafter, the Plans should be synced and selectable at provision time. Without manually syncing the Plans, you may be unable to provision to this Cloud until it undertakes its next daily sync overnight as Plan selection is required.

You're now able to provision new Instances and Apps to the Alibaba Cloud. |morpheus| includes a default catalog that includes Alibaba images which can be provisioned out of the box. Additionally, you can begin to create your own custom library of Alibaba workloads by adding Virtual Images and building out Instance Types.
