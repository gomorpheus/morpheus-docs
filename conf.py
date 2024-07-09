import datetime

master_doc = 'index'

latex_documents = [
    (master_doc, 'morpheus_7.0.1-1.tex', u'Morpheus Documentation',
     u'Morpheus', 'manual'),
]

rst_prolog = """

.. |releasedate| replace:: Apr 10 2024
.. |releasetype| replace:: LTS
.. |morphAnnualVer| replace:: v7
.. |morphbranch| replace:: v7.0
.. |morphver| replace:: v7.0.1
.. |minUpgradeVer| replace:: v6.0.0
.. |minRollingUpgradeVer| replace:: v6.0.7
.. |nonRollingUpgradeVer| replace:: v6.0.6
.. |previousMorphVer| replace:: v7.0.0
.. |pluginVer| replace:: 1.1.1
.. |workerVer| replace:: 5.4.8+
.. |rmqbranch| replace:: v3.5-3.12
.. |rmqver| replace:: v3.12.9
.. |mysqlbranch| replace:: v5.7, v8.0
.. |mysqlver| replace:: v8.0.36
.. |mysqlverfips| replace:: v8.0.36
.. |esbranch| replace:: v8.11+
.. |esver| replace:: v8.11.2
.. |tcver| replace:: v9.0.83
.. |nginxver| replace:: v1.25.1
.. |nodePackageVer| replace:: 3.2.23
.. |linuxagentver| replace:: v2.6.0
.. |macagentver| replace:: v2.4.0
.. |winagentver| replace:: v2.5.0.0
.. |java| replace:: 11.0.22
.. |java-mac| replace:: 11.0.14+9
.. |openjdk-jre| replace:: 11.0.20+8
.. |openjdk-elasticsearch| replace::  17.0.5+8
.. |openssl| replace:: 1.1.1w
.. |openssl_fips| replace:: 1.0.2u
.. |erlang| replace:: 26.1.2
.. |mastertenant| replace:: Master Tenant

.. |morpheus| replace:: Morpheus
.. |morphues| replace:: Morpheus
.. |morphdat| replace:: Morpheus Data
.. |repo_host_url| replace:: https://downloads.morpheusdata.com
.. |master tenant| replace:: Master Tenant
.. |profileObjects| replace:: Clouds
.. |profileTypes| replace:: Terraform, Key/Value

.. |debianVersions| replace:: 10, 11
.. |oelVersions| replace:: 7.x, 8.x
.. |ubuntuVersions| replace:: 18.04, 20.04, 22.04
.. |centosVersions| replace:: 7.x. 8.x (stream) 9.x (stream)
.. |rhelVersions| replace:: 7.x, 8.x, 9.x
.. |suseVersions| replace:: 12, 15

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
.. |LibOptFor| replace:: Library > Options > Forms
.. |LibTem| replace:: Library > Templates
.. |LibTemSpe| replace:: Library > Templates > Spec Templates
.. |LibTemFil| replace:: Library > Templates > File Templates
.. |LibTemScr| replace:: Library > Templates > Script Templates
.. |LibTemSec| replace:: Library > Templates > Security Packages
.. |LibTemClu| replace:: Library > Templates > Cluster Packages
.. |LibInt| replace:: Library > Integrations
.. |Pro| replace:: Provisioning
.. |ProCat| replace:: Provisioning > Catalog
.. |ProCatInv| replace:: Provisioning > Catalog > Inventory
.. |ProIns| replace:: Provisioning > Instances
.. |ProApp| replace:: Provisioning > Apps
.. |ProJob| replace:: Provisioning > Jobs
.. |ProJobJob| replace:: Provisioning > Jobs > Job Executions
.. |ProExe| replace:: Provisioning > Executions
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
.. |InfNetFlo| replace:: Infrastructure > Network > Floating IPs
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
.. |AdmSetCli| replace:: Administration > Settings > Clients

.. |trash| unicode:: 0x0001F5D1 .. TRASH ICON
.. |gear| unicode:: U+02699 .. GEAR ICON
.. |info| unicode:: U+2139 .. INFO ICON
.. |triangledown| unicode:: U+25BD .. TRIANGLE DOWN ICON
.. |rightarrow| unicode:: U+2192 .. RIGHT ARROW ICON
.. |pencil| unicode:: U+270E .. EDIT ICON
.. |checkmark| unicode:: U+2713 .. CHECK MARK
.. role:: redguilabel

.. |advSevCrit| replace:: Critical ⬛️
.. |advSevHigh| replace:: High 🟥
.. |advSevMed| replace:: Medium 🟨
.. |advSevLow| replace:: Low 🟩
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
extensions = ['myst_parser','sphinx.ext.autosectionlabel','sphinx_rtd_theme','sphinx_tabs.tabs','sphinxcontrib.contentui','sphinxcontrib.images','sphinx_search.extension','notfound.extension','sphinx.ext.autosectionlabel'] #sphinx_tabs
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


# -- Copy the upgrade table from master ------------------------------------------

import urllib.request
from urllib.request import urlretrieve

urlretrieve (
    "https://github.com/gomorpheus/morpheus-docs/raw/master/release_notes/upgrade_table.rst",
    "release_notes/upgrade_table2.rst")
