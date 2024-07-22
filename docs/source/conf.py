# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] =r'office_emp_proj.settings'
django.setup()

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'rst2pdf.pdfbuilder',
    'sphinxcontrib.programoutput',
    
]
# Project information
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
copyright = 'Copyright © kanimozhi'
version = '1.0'
release = '1.0.0'
project = 'Django_Employeepayroll_Website'
author = 'kanimozhi'

# General configuration
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'english'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
pdf_documents = [('index', 'MyProjectDocs', 'My Project Documentation', 'Author Name')]