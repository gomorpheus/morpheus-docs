"""
Sphinx extension for HPE Morpheus product tier annotations.

Provides:
- :tier:`Enterprise` / :tier:`Advanced` / :tier:`Essentials` inline role (badge)
- .. tier-note:: directive for block-level tier callouts
- |enterprise-only|, |advanced-plus|, |essentials| substitutions (via rst_prolog)

Usage in RST:

    Inline badge:
        This feature :tier:`Enterprise` requires an Enterprise license.

    Block callout:
        .. tier-note:: Enterprise
           :exclude: Essentials, Advanced

           Multi-tenancy allows creating isolated sub-tenants with separate branding.
"""

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.docutils import SphinxRole


# --- Inline role: :tier:`Enterprise` ---

class TierRole(SphinxRole):
    """Renders an inline tier badge like [Enterprise] with appropriate styling."""

    VALID_TIERS = {'enterprise', 'advanced', 'essentials'}

    def run(self):
        tier = self.text.strip().lower()
        if tier not in self.VALID_TIERS:
            tier = 'enterprise'  # fallback

        node = nodes.inline(
            self.rawtext,
            self.text.strip(),
            classes=['tier-badge', f'tier-{tier}']
        )
        return [node], []


# --- Block directive: .. tier-note:: ---

class TierNoteDirective(Directive):
    """
    Block-level tier annotation. Renders as a styled admonition indicating
    which tiers include or exclude this feature.

    Usage:
        .. tier-note:: Enterprise
           :exclude: Essentials, Advanced

           Content describing the tier-restricted feature.

        .. tier-note:: Advanced, Enterprise

           Content available in Advanced and Enterprise.
    """

    has_content = True
    required_arguments = 1  # tier name(s), comma-separated
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'exclude': directives.unchanged,  # tiers that DON'T have this
    }

    def run(self):
        tiers = [t.strip() for t in self.arguments[0].split(',')]
        excluded = []
        if 'exclude' in self.options:
            excluded = [t.strip() for t in self.options['exclude'].split(',')]

        # Build the header text
        if excluded:
            header_text = f"Not available in: {', '.join(excluded)}"
        else:
            header_text = f"Available in: {', '.join(tiers)}"

        # Determine CSS class based on most restrictive tier
        tier_lower = tiers[0].lower() if tiers else 'enterprise'
        css_class = f'tier-note-{tier_lower}'

        # Create container
        container = nodes.container(classes=['tier-note', css_class])

        # Header paragraph with tier badges
        header = nodes.paragraph(classes=['tier-note-header'])
        for tier in tiers:
            badge = nodes.inline(tier, tier, classes=['tier-badge', f'tier-{tier.lower()}'])
            header += badge
            header += nodes.Text(' ')
        header += nodes.Text(f'— {header_text}')
        container += header

        # Body content
        if self.content:
            body = nodes.container(classes=['tier-note-body'])
            self.state.nested_parse(self.content, self.content_offset, body)
            container += body

        return [container]


# --- Setup ---

def setup(app):
    app.add_role('tier', TierRole())
    app.add_directive('tier-note', TierNoteDirective)
    app.add_css_file('tier_badges.css')

    return {
        'version': '1.0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
