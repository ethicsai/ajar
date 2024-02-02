# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


# -- Project information -----------------------------------------------------

project = 'AJAR'
copyright = '2024, Benoît Alcaraz, Olivier Boissier, Rémy Chaput & Christopher Leturc'
author = 'Benoît Alcaraz, Olivier Boissier, Rémy Chaput & Christopher Leturc'


# -- General configuration ---------------------------------------------------

extensions = [
    # Include documentation from docstrings
    'sphinx.ext.autodoc',
    # Generate summaries (tables/listings) for autodoc
    'sphinx.ext.autosummary',
    # Automatically add a 'copy button' to our code blocks
    'sphinx_copybutton',
    # Add a link to the source code on each of the "API pages"
    'sphinx.ext.viewcode',
]

# Enable autosummary
autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
