master_doc = 'index'

latex_documents = [
    (master_doc, 'morpheus5.2.12-1.tex', u'Morpheus Documentation',
     u'Morpheus', 'manual'),
]

rst_prolog = """
.. |morpheus| replace:: Morpheus
.. |morphdat| replace:: Morpheus Data, LLC
.. |repo_host_url| replace:: https://downloads.morpheusdata.com
.. |morphbranch| replace:: v5.2
.. |morphver| replace:: v5.2.13
.. |previousMorphVer| replace:: v5.2.12
.. |minUpgradeVer| replace:: v4.2.0
.. |rmqbranch| replace:: v3.5-3.9
.. |rmqver| replace:: v3.9.8
.. |mysqlbranch| replace:: v5.7
.. |mysqlver| replace:: v5.7.35
.. |mysqlverfips| replace:: v.5.7.35
.. |esbranch| replace:: v7.x
.. |esver| replace:: v7.8.1
.. |tcver| replace:: v9.0.54
.. |nginxver| replace:: v1.20.1
.. |linuxagentver| replace:: v2.1.1
.. |winagentver| replace:: v1.7.0.0
.. |nodePackageVer| replace:: 3.2.3
.. |java| replace:: v8u312-b07
.. |java-mac| replace:: v8u312-b07
.. |openjdk-jre| replace:: v8u312
.. |openjdk-elasticsearch| replace:: 14.0.2+12
.. |openssl| replace:: 1.1.1k
.. |openssl_fips| replace:: 1.0.2u
.. |erlang| replace:: 22.3
.. |master tenant| replace:: Master Tenant

.. |trash| unicode:: 0x0001F5D1 .. TRASH ICON
.. |gear| unicode:: U+02699 .. GEAR ICON
.. |info| unicode:: U+2139 .. INFO ICON
.. |triangledown| unicode:: U+25BD .. TRIANGLE DOWN ICON
.. |rightarrow| unicode:: U+2192 .. RIGHT ARROW ICON
.. |pencil| unicode:: U+270E .. EDIT ICON

.. role:: redguilabel

.. |debianVersion| replace:: 9,10,11


"""


# -- levels -----
#****************
#       H1
#****************
#
#       H2
#================
#----------------
#^^^^^^^^^^^^^^^^
#````````````````
#................

extensions = ['recommonmark','sphinx_markdown_tables','sphinx_tabs.tabs','sphinxcontrib.contentui','sphinxcontrib.images']
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
html_use_opensearch = 'https://docs.morpheusdata.com'
linkcheck_request_headers = {
    "*": {
        "Accept": "text/html,application/atom+xml",
    }
}
html_theme_options = {
'logo_only': True,
'sticky_navigation': True
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
    app.add_stylesheet('morpheusTheme.css')
