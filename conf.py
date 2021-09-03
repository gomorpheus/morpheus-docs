master_doc = 'index'

rst_prolog = """
.. |morpheus| replace:: Morpheus
.. |morphbranch| replace:: v5.3
.. |morphver| replace:: v5.3.3
.. |minUpgradeVer| replace:: v4.2.0
.. |previousMorphVer| replace:: v5.3.1
.. |rmqbranch| replace:: v3.5-3.8
.. |rmqver| replace:: v3.8.9
.. |mysqlbranch| replace:: v5.7
.. |mysqlver| replace:: v5.7.32
.. |mysqlverfips| replace:: v.5.7.29
.. |esbranch| replace:: v7.x
.. |esver| replace:: v7.8.1
.. |tcver| replace:: v9.0.50
.. |morphdat| replace:: Morpheus Data, LLC
.. |nginxver| replace:: v1.19.9
.. |nodePackageVer| replace:: 3.2.0
.. |java| replace:: v8u302-b08
.. |openjdk-jre| replace:: v8u292
.. |openjdk-elasticsearch| replace:: 14.0.2+12
.. |erlang| replace:: 22.3
.. |repo_host_url| replace:: https://downloads.morpheusdata.com
.. |master tenant| replace:: Master Tenant

.. |trash| unicode:: 0x0001F5D1 .. TRASH ICON
.. |gear| unicode:: U+02699 .. GEAR ICON
.. |info| unicode:: U+2139 .. INFO ICON
.. |triangledown| unicode:: U+25BD .. TRIANGLE DOWN ICON
.. |rightarrow| unicode:: U+2192 .. RIGHT ARROW ICON
.. |pencil| unicode:: U+270E .. EDIT ICON

.. role:: redguilabel

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


extensions = ['recommonmark','sphinx_markdown_tables','sphinxcontrib.contentui','sphinx_tabs.tabs','sphinxcontrib.images','sphinx_search.extension','notfound.extension'] #sphinx_tabs
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
project = u'Morpheus Docs'
copyright = u'2021, Morpheus Data'
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
    (master_doc, 'morpheus5.3.2-1.tex', u'Morpheus Documentation',
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
