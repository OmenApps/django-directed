"""Sphinx configuration."""
import os
import sys

import django
from sphinx.ext.autodoc import between


project = "django-directed"
author = "Jack Linke"
copyright = "2023, Jack Linke"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
    "sphinxcontrib.mermaid",
]
autodoc_typehints = "description"
html_theme = "furo"

sys.path.insert(0, os.path.abspath(".."))
os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
django.setup()


def setup(app):
    # Register a sphinx.ext.autodoc.between listener to ignore everything
    # between lines that contain the word IGNORE
    app.connect("autodoc-process-docstring", between("^.*<sphinx-skip>.*$", exclude=True))
    return app
