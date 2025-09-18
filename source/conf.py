# conf.py
# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'A Learner\'s Guide to Regular Expressions'
copyright = '2025, Ashwini'
author = 'Ashwini'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.mathjax',
    'sphinxcontrib.tikz',
    'sphinx_togglebutton',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = "Regular Expressions in TOC"

# Theme-specific options for mobile optimization
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Sidebar settings for mobile
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# -- Options for TikZ extension ----------------------------------------------
#tikz_proc_suite = 'pdflatex'
tikz_tikzlatex = 'pdflatex'
tikz_latex_preamble = r"""
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{tikz}
\usetikzlibrary{automata, positioning, arrows}
\usepackage[dvipsnames]{xcolor}

% --- Custom Color Definitions for TikZ diagrams ---
\definecolor{finalstatecolor}{RGB}{200, 0, 0} % Red for final states
"""

# -- Custom CSS for mobile-friendly styling ----------------------------------
def setup(app):
    app.add_css_file('custom.css')

