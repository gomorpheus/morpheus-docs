import datetime
import os
import sys

sys.path.insert(0, os.path.abspath('_ext'))

master_doc = 'index'

latex_documents = [
    (master_doc, 'morpheus_9.1.0-1.tex', u'Morpheus Documentation',
     u'Morpheus', 'manual'),
]

rst_prolog = """

.. |releasedate| replace:: TBD
.. |releasetype| replace:: Feature
.. |morphAnnualVer| replace:: v9
.. |morphbranch| replace:: v9.1
.. |morphver| replace:: v9.1.0
.. |minUpgradeVer| replace:: v6.0.0
.. |minRollingUpgradeVer| replace:: v9.0.0
.. |nonRollingUpgradeVer| replace:: v8.0.4
.. |previousMorphVer| replace:: v9.0.0
.. |pluginVer| replace:: 1.4.1
.. |workerVer| replace:: 9.0.0
.. |rmqbranch| replace:: v3.5-3.13
.. |rmqver| replace:: v3.13.7
.. |mysqlbranch| replace:: v8.0
.. |mysqlver| replace:: v8.0.40
.. |mysqlverfips| replace:: v8.0.36
.. |esbranch| replace:: v8.9+
.. |esver| replace:: v8.15.5
.. |tcver| replace:: v9.0.106
.. |nginxver| replace:: v1.26.2
.. |nodePackageVer| replace:: 3.3.11
.. |linuxagentver| replace:: v3.2.7
.. |macagentver| replace:: v2.4.0
.. |winagentver| replace:: v2.6.1.0
.. |java| replace:: 17.0.14+7
.. |java-mac| replace:: 11.0.14+9
.. |openjdk-jre| replace:: 17.0.14+7
.. |openjdk-elasticsearch| replace::  17.0.5+8
.. |openssl| replace:: 1.1.1w
.. |openssl_fips| replace:: 1.0.2u
.. |erlang| replace:: 26.2.5.6
.. |mastertenant| replace:: Master Tenant

.. |morphfirst| replace:: HPE Morpheus Software
.. |morpheus| replace:: HPE Morpheus Software
.. |morphues| replace:: HPE Morpheus Software
.. |morphdat| replace:: Morpheus Data
.. |hpe| replace:: Hewlett Packard Enterprise
.. |repo_host_url| replace:: https://www.hpe.com/support/hpesc
.. |master tenant| replace:: Master Tenant
.. |profileObjects| replace:: Clouds
.. |profileTypes| replace:: Terraform, Key/Value
.. |mvm| replace:: HVM
.. |hvm| replace:: HVM
.. |cluster| replace:: HVM Cluster
.. |clusters| replace:: HVM Clusters
.. |host| replace:: HVM Host
.. |hosts| replace:: HVM Hosts
.. |hypervisor| replace:: HVM Hypervisor
.. |hypervisors| replace:: HVM Hypervisors

.. |debianVersions| replace:: 11, 12
.. |oelVersions| replace:: 7.x (deprecated), 8.x, 9.x
.. |ubuntuVersions| replace:: 20.04, 22.04, 24.04
.. |centosVersions| replace:: 7.x (deprecated). 8.x (stream) 9.x (stream)
.. |rhelVersions| replace:: 7.x (deprecated), 8.x, 9.x
.. |suseVersions| replace:: 15

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
.. |LibOpe| replace:: Library > Operating Systems
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
.. |TooAI| replace:: Tools > AI Services
.. |TooAIInt| replace:: Tools > AI Services > Integrations
.. |TooAIMCP| replace:: Tools > AI Services > MCP Servers
.. |TooAIAge| replace:: Tools > AI Services > Agents
.. |Adm| replace:: Administration
.. |AdmTen| replace:: Administration > Tenants
.. |AdmPla| replace:: Administration > Plans & Pricing
.. |AdmPlans| replace:: Administration > Plans
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

.. |enterprise-only| raw:: html

   <span class="tier-badge tier-enterprise">ENTERPRISE</span>

.. |advanced-plus| raw:: html

   <span class="tier-badge tier-advanced">ADVANCED</span> <span class="tier-badge tier-enterprise">ENTERPRISE</span>

.. |essentials-plus| raw:: html

   <span class="tier-badge tier-essentials">ESSENTIALS</span> <span class="tier-badge tier-advanced">ADVANCED</span> <span class="tier-badge tier-enterprise">ENTERPRISE</span>

.. |all-tiers| raw:: html

   <span class="tier-badge tier-essentials">ESSENTIALS</span> <span class="tier-badge tier-advanced">ADVANCED</span> <span class="tier-badge tier-enterprise">ENTERPRISE</span>

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
extensions = ['myst_parser','sphinx.ext.autosectionlabel','sphinx_immaterial','sphinx_tabs.tabs','sphinxcontrib.contentui','sphinxcontrib.images','notfound.extension','sphinx.ext.autosectionlabel','tier_roles']
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
project = u'Morpheus Docs'
html_title = u'Morpheus Documentation'

# Version + locale selectors (POC) — populate the side-nav version dropdown and
# the header language dropdown. Docs deploy RTD-style at /<lang>/<version>/<page>.
# `path`/`code` are the URL segments each build is deployed under.
html_context = {
    "doc_versions": [
        {"path": "9.1", "title": "9.1 (latest)"},
        {"path": "9.0", "title": "9.0"},
        {"path": "8.0", "title": "8.0"},
    ],
    "doc_locales": [
        {"code": "en", "title": "English"},
        {"code": "es", "title": "Español"},
        {"code": "fr", "title": "Français"},
        {"code": "de", "title": "Deutsch"},
        {"code": "pt", "title": "Português"},
    ],
}
copyright = f"{year}, Morpheus Data"
author = u'Morpheus'
language = 'en'
locale_dirs = ['locale/']
gettext_compact = False
gettext_additional_targets = ['literal-block', 'image']
exclude_patterns = ['_build', '_out*', '.venv', 'Thumbs.db', '.DS_Store','z_in_progress','.hero','.opencode','locale','diagrams']
pygments_style = 'none'
todo_include_todos = False
html_theme = 'sphinx_immaterial'
html_use_opensearch = 'https://docs.morpheusdata.com/en/latest'
linkcheck_request_headers = {
    "*": {
        "Accept": "text/html,application/atom+xml",
    }
}
html_static_path = ['_static']

# HPE Graphik + DESIGN.md skin over the sphinx-immaterial baseline. Each file is
# a focused layer; load order matters (graphik first, dark last).
html_css_files = [
    'hpe-graphik.css', 'hpe-pagemap.css', 'hpe-layout.css', 'hpe-header.css',
    'hpe-footer.css', 'hpe-nav.css', 'hpe-admonitions.css', 'hpe-responsive.css',
    'hpe-search.css', 'hpe-dark.css',
]
html_js_files = ['hpe-nav-fix.js']

# immaterial suppresses Sphinx's classic search page in favour of its own
# instant/dropdown search. We keep the original RTD behaviour: type -> Enter ->
# a full "Search Results" page with snippets. _templates/search.html re-renders
# that page (forced via html_additional_pages) and reuses Sphinx's own stock
# search engine, whose scripts + a stock-format index are emitted by setup().
html_additional_pages = {'search': 'search.html'}

html_theme_options = {
    # Three-way header toggle: light -> dark -> system (follow OS), cycling.
    # Icons show the current mode; HPE dark values live in hpe-dark.css (slate).
    'palette': [
        {'media': '(prefers-color-scheme: light)', 'scheme': 'default',
         'toggle': {'icon': 'material/weather-sunny', 'name': 'Switch to dark mode'}},
        {'media': '(prefers-color-scheme: dark)', 'scheme': 'slate',
         'toggle': {'icon': 'material/weather-night', 'name': 'Switch to system preference'}},
        {'media': '(prefers-color-scheme)',
         'toggle': {'icon': 'material/brightness-auto', 'name': 'Switch to light mode'}},
    ],
}

html_show_sourcelink = False
html_show_sphinx = False
keep_warnings = False
github_edit_url = False

html_favicon = "_static/hpe-favicon.svg"
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
def setup(app):
    """Emit a stock-format search index + copy Sphinx's own search scripts.

    sphinx-immaterial monkeypatches the search index into its own instant-search
    format (``docurls`` with URLs baked in) which stock ``searchtools.js`` can't
    read. After the build we convert that adapted ``searchindex.js`` back to the
    classic shape (``docnames`` + ``filenames``) and write it to
    ``searchindex_classic.js``, which _templates/search.html loads. No-op for
    builds that already emit a stock-format index.

    immaterial also omits Sphinx's classic search scripts (it ships its own
    instant search), so we copy ``searchtools/doctools/sphinx_highlight.js``
    straight from the *installed* Sphinx package into ``_static/`` at build time
    rather than vendoring frozen copies into the repo — they always match the
    installed Sphinx version and never appear in the source diff.
    """
    import json
    import os
    import re
    import shutil

    import sphinx

    def _emit_classic_searchindex(app, exception):
        if exception is not None:
            return
        src = os.path.join(app.outdir, 'searchindex.js')
        if not os.path.exists(src):
            return
        raw = open(src, encoding='utf-8').read().strip()
        m = re.match(r'^Search\.setIndex\((.*)\)\s*;?\s*$', raw, re.S)
        if not m:
            return
        try:
            idx = json.loads(m.group(1))
        except ValueError:
            return
        if 'docurls' not in idx:
            return  # already stock format — nothing to convert
        docurls = idx.pop('docurls')
        idx['docnames'] = [re.sub(r'\.html$', '', u) for u in docurls]
        idx['filenames'] = list(docurls)  # unused for display; kept parallel
        dst = os.path.join(app.outdir, 'searchindex_classic.js')
        with open(dst, 'w', encoding='utf-8') as f:
            f.write('Search.setIndex(' + json.dumps(idx) + ')')

    def _copy_stock_search_assets(app, exception):
        if exception is not None:
            return
        basic = os.path.join(
            os.path.dirname(sphinx.__file__), 'themes', 'basic', 'static'
        )
        dst_dir = os.path.join(app.outdir, '_static')
        for name in ('searchtools.js', 'doctools.js', 'sphinx_highlight.js'):
            src = os.path.join(basic, name)
            if os.path.exists(src) and os.path.isdir(dst_dir):
                shutil.copyfile(src, os.path.join(dst_dir, name))

    app.connect('build-finished', _emit_classic_searchindex)
    app.connect('build-finished', _copy_stock_search_assets)


# -- Upgrade table is maintained locally in release_notes/upgrade_table2.rst ---
# Previously downloaded from gomorpheus/morpheus-docs master on every build.
# Removed in v9.0.0 as the table is now maintained directly in this repository.
