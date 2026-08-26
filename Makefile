# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python3 -msphinx
SPHINXINTL    = sphinx-intl
SPHINXPROJ    = jwtest
SOURCEDIR     = .
BUILDDIR      = _build
LOCALEDIR     = locale
LANGUAGES     = es pt fr de

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile build gettext intl-update intl-build html-es html-pt html-fr html-de

# Project-standard build target
build:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Extract translatable strings into .pot files
gettext:
	@$(SPHINXBUILD) -M gettext "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Update .po files for all configured languages from .pot files
intl-update: gettext
	@for lang in $(LANGUAGES); do \
		$(SPHINXINTL) update -p "$(BUILDDIR)/gettext" -l $$lang -d "$(LOCALEDIR)"; \
	done

# Build HTML for a specific language (usage: make intl-build LANG=es)
LANG ?= es
intl-build:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)/$(LANG)" $(SPHINXOPTS) -D language=$(LANG) $(O)

# Shortcut: build Spanish HTML
html-es:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)/es" $(SPHINXOPTS) -D language=es $(O)

# Shortcut: build Portuguese HTML
html-pt:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)/pt" $(SPHINXOPTS) -D language=pt $(O)

# Shortcut: build French HTML
html-fr:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)/fr" $(SPHINXOPTS) -D language=fr $(O)

# Shortcut: build German HTML
html-de:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)/de" $(SPHINXOPTS) -D language=de $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
