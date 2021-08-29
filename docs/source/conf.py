# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
import nbsphinx
import glob
import shutil
import sphinx_rtd_theme
import m2r2

# -- Project information -----------------------------------------------------

project = 'TenBagger'
copyright = '2021, Aram Koorn'
author = 'Aram Koorn'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.imgconverter",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_gallery.gen_gallery",
    "sphinx_search.extension",
    "m2r2"
]


exclude_patterns = [
    ".ipynb_checkpoints",
    "tutorials/logistic_regression.ipynb",
    "examples/*py",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# replace "# NumPyro" by "# Getting Started with NumPyro"
with open("../../README.md", "rt") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if "# TenBagger" == line.rstrip():
            break
    lines = lines[i:]
    lines[0] = "# Getting Started with TenBagger\n"
    text = "\n".join(lines)

with open("getting_started.rst", "wt") as f:
    f.write(nbsphinx.markdown2rst(text))


# -- Copy notebook files

if not os.path.exists("tutorials"):
    os.makedirs("tutorials")

for src_file in glob.glob("../../notebooks/source/*.ipynb"):
    dst_file = os.path.join("tutorials", src_file.split("/")[-1])
    shutil.copy(src_file, "tutorials/")

# add index file to `tutorials` path, `:orphan:` is used to
# tell sphinx that this rst file needs not to be appeared in toctree
with open("../../notebooks/source/index.rst", "rt") as f1:
    with open("tutorials/index.rst", "wt") as f2:
        f2.write(":orphan:\n\n")
        f2.write(f1.read())

sphinx_gallery_conf = {
    "examples_dirs": ["../../examples"],
    "gallery_dirs": ["examples"],
    # only execute files beginning with plot_
    "filename_pattern": "/plot_",
    "ignore_pattern": "__init__",
    # not display Total running time of the script because we do not execute it
    "min_reported_time": 1,
}
