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
LANGUAGES     = es

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile gettext intl-update intl-build html-es

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

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
