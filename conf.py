import datetime

master_doc = 'index'

latex_documents = [
    (master_doc, 'morpheus_5.4.4-1.tex', u'Morpheus Documentation',
     u'Morpheus', 'manual'),
]

rst_prolog = """

.. |releasedate| replace:: Mar 9 2022
.. |morpheus| replace:: Morpheus
.. |morphues| replace:: Morpheus
.. |morphdat| replace:: Morpheus Data
.. |morphbranch| replace:: v5.4
.. |morphver| replace:: v5.4.4
.. |minUpgradeVer| replace::
.. |previousMorphVer| replace:: v5.4.3
.. |rmqbranch| replace:: v3.5-3.9
.. |rmqver| replace:: v3.9.8
.. |mysqlbranch| replace:: v5.7
.. |mysqlver| replace:: v5.7.37
.. |mysqlverfips| replace:: v.5.7.35
.. |esbranch| replace:: v7.x
.. |esver| replace:: v7.8.1
.. |tcver| replace:: v9.0.58
.. |nginxver| replace:: v1.20.1
.. |linuxagentver| replace:: v2.2.2
.. |winagentver| replace:: v1.8.0.0
.. |macagentver| replace:: v2.2.2
.. |nodePackageVer| replace:: 3.2.5
.. |java| replace:: 11.0.14
.. |java-mac| replace:: 11.0.14
.. |openjdk-jre| replace:: 11.0.14
.. |openjdk-elasticsearch| replace:: 14.0.2+12
.. |openssl| replace:: 1.1.1k
.. |openssl_fips| replace:: 1.0.2u
.. |erlang| replace:: 23.2
.. |repo_host_url| replace:: https://downloads.morpheusdata.com
.. |master tenant| replace:: Master Tenant
.. |profileObjects| replace:: Clouds
.. |profileTypes| replace:: Terraform, Key/Value

.. |trash| unicode:: 0x0001F5D1 .. TRASH ICON
.. |gear| unicode:: U+02699 .. GEAR ICON
.. |info| unicode:: U+2139 .. INFO ICON
.. |triangledown| unicode:: U+25BD .. TRIANGLE DOWN ICON
.. |rightarrow| unicode:: U+2192 .. RIGHT ARROW ICON
.. |pencil| unicode:: U+270E .. EDIT ICON

.. role:: redguilabel

.. |debianVersion| replace:: 9,10,11

.. |Lib| replace:: Library
.. |LibAut| replace:: Library > Automation
.. |LibAutTas| replace:: Library > Automation > Tasks
.. |LibAutWor| replace:: Library > Automation > Workflows
.. |LibAutSca| replace:: Library > Automation > Scale Thresholds
.. |LibAutPow| replace:: Library > Automation > Power Scheduling
.. |LibAutExe| replace:: Library > Automation > Execute Scheduling
.. |LibBlu| replace:: Library > Blueprints
.. |LibBluCat| replace:: Library > Blueprints > Catalog Items
.. |LibBluApp| replace:: Library > Blueprints > App Blueprints
.. |LibBluIns| replace:: Library > Blueprints > Instance Types
.. |LibBluLay| replace:: Library > Blueprints > Layouts
.. |LibBluNod| replace:: Library > Blueprints > Node Types
.. |LibBluClu| replace:: Library > Blueprints > Cluster Layouts
.. |LibVir| replace:: Library > Virtual Images
.. |LibOpt| replace:: Library > Options
.. |LibOptInp| replace:: Library > Options > Inputs
.. |LibOptOpt| replace:: Library > Options > Option Lists
.. |LibTem| replace:: Library > Templates
.. |LibTemSpe| replace:: Library > Templates > Spec Templates
.. |LibTemFil| replace:: Library > Templates > File Templates
.. |LibTemScr| replace:: Library > Templates > Script Templates
.. |LibTemSec| replace:: Library > Templates > Security Packages
.. |LibInt| replace:: Library > Integrations
.. |Pro| replace:: Provisioning
.. |ProCat| replace:: Provisioning > Catalog
.. |ProCatInv| replace:: Provisioning > Catalog > Inventory
.. |ProIns| replace:: Provisioning > Instances
.. |ProApp| replace:: Provisioning > Apps
.. |ProJob| replace:: Provisioning > Jobs
.. |ProJobJob| replace:: Provisioning > Jobs > Job Executions
.. |ProCod| replace:: Provisioning > Code
.. |ProCodRep| replace:: Provisioning > Code > Repositories
.. |ProCodDep| replace:: Provisioning > Code > Deployments
.. |ProCodInt| replace:: Provisioning > Code > Integrations
.. |Ope| replace:: Operations
.. |OpeDas| replace:: Operations > Dashboard
.. |OpeRep| replace:: Operations > Reports
.. |OpeAna| replace:: Operations > Analytics
.. |OpeGui| replace:: Operations > Guidance
.. |OpeWik| replace:: Operations > Wiki
.. |OpeCos| replace:: Operations > Costing
.. |OpeCosBud| replace:: Operations > Costing > Budgets
.. |OpeCosInv| replace:: Operations > Costing > Invoices
.. |OpeCosUsa| replace:: Operations > Costing > Usage
.. |OpeApp| replace:: Operations > Approvals
.. |OpeAct| replace:: Operations > Activity
.. |OpeActAla| replace:: Operations > Activity > Alarms
.. |OpeActHis| replace:: Operations > Activity > History
.. |Inf| replace:: Infrastructure
.. |InfGro| replace:: Infrastructure > Groups
.. |InfClo| replace:: Infrastructure > Clouds
.. |InfClu| replace:: Infrastructure > Clusters
.. |InfCom| replace:: Infrastructure > Compute
.. |InfComHos| replace:: Infrastructure > Compute > Hosts
.. |InfComVir| replace:: Infrastructure > Compute > Virtual Machines
.. |InfComCon| replace:: Infrastructure > Compute > Containers
.. |InfComRes| replace:: Infrastructure > Compute > Resources
.. |InfComBar| replace:: Infrastructure > Compute > Bare Metal
.. |InfNet| replace:: Infrastructure > Network
.. |InfNetNet| replace:: Infrastructure > Network > Networks
.. |InfNetNetG| replace:: Infrastructure > Network > Network Groups
.. |InfNetRou| replace:: Infrastructure > Network > Routers
.. |InfNetIP| replace:: Infrastructure > Network > IP Pools
.. |InfNetDom| replace:: Infrastructure > Network > Domains
.. |InfNetPro| replace:: Infrastructure > Network > Proxies
.. |InfNetSec| replace:: Infrastructure > Network > Security Groups
.. |InfNetInt| replace:: Infrastructure > Network > Integrations
.. |InfLoa| replace:: Infrastructure > Load Balancers
.. |InfLoaLoa| replace:: Infrastructure > Load Balancers > Load Balancers
.. |InfLoaVir| replace:: Infrastructure > Load Balancers > Virtual Servers
.. |InfSto| replace:: Infrastructure > Storage
.. |InfStoBuc| replace:: Infrastructure > Storage > Buckers
.. |InfStoFil| replace:: Infrastructure > Storage > File Shares
.. |InfStoVol| replace:: Infrastructure > Storage > Volumes
.. |InfStoDat| replace:: Infrastructure > Storage > Data Stores
.. |InfStoSer| replace:: Infrastructure > Storage > Servers
.. |InfTru| replace:: Infrastructure > Trust
.. |InfTruInt| replace:: Infrastructure > Trust > Integrations
.. |InfTruCre| replace:: Infrastructure > Trust > Credentials
.. |InfKey| replace:: Infrastructure > Trust
.. |InfKeyKey| replace:: Infrastructure > Trust > Key Pairs
.. |InfKeySSL| replace:: Infrastructure > Trust > SSL Certificates
.. |InfKeyInt| replace:: Infrastructure > Trust > Integrations
.. |InfBooMap| replace:: Infrastructure > Boot > Mapping
.. |InfBooBoo| replace:: Infrastructure > Boot > Boot Menus
.. |InfBooAns| replace:: Infrastructure > Boot > Answer Files
.. |InfBooIma| replace:: Infrastructure > Boot > Images
.. |InfBooDis| replace:: Infrastructure > Boot > Discovered MAC Addresses
.. |InfBoo| replace:: Infrastructure > Boot
.. |Bac| replace:: Backups
.. |BacSum| replace:: Backups > Summary
.. |BacJob| replace:: Backups > Jobs
.. |BacBac| replace:: Backups > Backups
.. |BacHis| replace:: Backups > History
.. |BacHisBac| replace:: Backups > History > Backups
.. |BacHisRes| replace:: Backups > History > Restores
.. |BacInt| replace:: Backups > Integrations
.. |Mon| replace:: Monitoring
.. |MonSta| replace:: Monitoring > Status
.. |MonLog| replace:: Monitoring > Logs
.. |MonApp| replace:: Monitoring > Apps
.. |MonChe| replace:: Monitoring > Checks
.. |MonGro| replace:: Monitoring > Groups
.. |MonInc| replace:: Monitoring > Incidents
.. |MonCon| replace:: Monitoring > Contacts
.. |MonAle| replace:: Monitoring > Alert Rules
.. |Too| replace:: Tools
.. |TooCyp| replace:: Tools > Cypher
.. |TooArc| replace:: Tools > Archives
.. |TooIma| replace:: Tools > Image Builder
.. |TooImaIma| replace:: Tools > Image Builder > Image Builds
.. |TooImaBoo| replace:: Tools > Image Builder > Boot Scripts
.. |TooImaPre| replace:: Tools > Image Builder > Preseed Scripts
.. |TooVDI| replace:: Tools > VDI Pools
.. |TooVDIPoo| replace:: Tools > VDI Pools > VDI Pools
.. |TooVDIApp| replace:: Tools > VDI Pools > VDI Apps
.. |TooVDIGat| replace:: Tools > VDI Pools > VDI Gateways
.. |Adm| replace:: Administration
.. |AdmTen| replace:: Administration > Tenants
.. |AdmPla| replace:: Administration > Plans & Pricing
.. |AdmPlaPla| replace:: Administration > Plans & Pricing > Plans
.. |AdmPlaSet| replace:: Administration > Plans & Pricing > Price Sets
.. |AdmPlaPri| replace:: Administration > Plans & Pricing > Prices
.. |AdmRol| replace:: Administration > Roles
.. |AdmUse| replace:: Administration > Users
.. |AdmUseUse| replace:: Administration > Users > Users
.. |AdmUseUGp| replace:: Administration > Users > User Groups
.. |AdmInt| replace:: Administration > Integrations
.. |AdmIntInt| replace:: Administration > Integrations > Integrations
.. |AdmIntPac| replace:: Administration > Integrations > Packages
.. |AdmIntPlu| replace:: Administration > Integrations > Plugins
.. |AdmIntDis| replace:: Administration > Integrations > Distributed Workers
.. |AdmPol| replace:: Administration > Policies
.. |AdmHea| replace:: Administration > Health
.. |AdmHeaMorHea| replace:: Administration > Health > Morpheus Health
.. |AdmHeaMorLog| replace:: Administration > Health > Morpheus Logs
.. |AdmSet| replace:: Administration > Settings
.. |AdmSetApp| replace:: Administration > Settings > Appliance
.. |AdmSetWhi| replace:: Administration > Settings > Whitelabel
.. |AdmSetPro| replace:: Administration > Settings > Provisioning
.. |AdmSetMon| replace:: Administration > Settings > Monitoring
.. |AdmSetBac| replace:: Administration > Settings > Backups
.. |AdmSetLog| replace:: Administration > Settings > Logs
.. |AdmSetGui| replace:: Administration > Settings > Guidance
.. |AdmSetEnv| replace:: Administration > Settings > Environments
.. |AdmSetSof| replace:: Administration > Settings > Software Licenses
.. |AdmSetLic| replace:: Administration > Settings > License
.. |AdmSetUti| replace:: Administration > Settings > Utilities
"""


# -- levels -----
#
# ***************
# LEVEL 1 HEADING
# ***************
#
# LEVEL 2 HEADING
# ===============
#
# LEVEL 3 HEADING
# ---------------
#
# LEVEL 4 HEADING
# ^^^^^^^^^^^^^^^
#
# LEVEL 5 HEADING
# ```````````````
#
# LEVEL 6 HEADING
# ...............


year = datetime.datetime.now().date().strftime("%Y")
extensions = ['recommonmark','sphinx_markdown_tables','sphinxcontrib.contentui','sphinx_tabs.tabs','sphinxcontrib.images','sphinx_search.extension','notfound.extension','sphinx.ext.autosectionlabel','sphinx_rtd_dark_mode'] #sphinx_tabs
templates_path = ['_templates']
default_dark_mode = False
source_suffix = ['.rst', '.md']
project = u'Morpheus Docs'
copyright = f"{year}, Morpheus Data"
author = u'Morpheus'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','z_in_progress']
pygments_style = 'none'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
html_use_opensearch = 'https://docs.morpheusdata.com/en/latest'
linkcheck_request_headers = {
    "*": {
        "Accept": "text/html,application/atom+xml",
    }
}
html_theme_options = {
'logo_only': True,
'sticky_navigation': True,
'navigation_depth': 5,
}
html_logo = "_static/logo.svg"
html_static_path = ['_static']

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        # 'donate.html',
    ]
}

html_show_sourcelink = False
html_show_sphinx = False
keep_warnings = False
github_edit_url = False

def setup(app):
# Disable the GitHub link display
    app.config.html_context['display_github'] = False

context = {
    'display_github': False,
}
html_favicon = "_static/morpheus_fav_64.ico"
htmlhelp_basename = 'morpheusdocs'

latex_elements = {

}

latex_documents = [
    (master_doc, 'morpheus5.3.3-1.tex', u'Morpheus Documentation',
     u'Morpheus', 'manual'),
]

man_pages = [
    (master_doc, 'morpheusdocs', u'Morpheus Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'morpheusdocs', u'Morpheus Documentation',
     author, 'Morpheus', 'Morpheus Documentation',
     'UI Docs'),
]
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

def setup(app):
    app.add_css_file('morpheusTheme.css')
