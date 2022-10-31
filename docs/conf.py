# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath("../mpltable"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "mpltable"
copyright = "2022, znstrider"
author = "znstrider"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "myst_nb"]

autodoc_member_order = "bysource"

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    "jupyter_execute",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_favicon = "_static/"
# html_logo = "_static/"
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "home_page_in_toc": True,
    "github_url": "https://github.com/znstrider/mpltable",
    "repository_url": "https://github.com/znstrider/mpltable",
    "repository_branch": "master",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_edit_page_button": True,
}
html_title = "mpltable"
