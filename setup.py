#!/usr/bin/env python3

import os
from setuptools import setup, find_packages
from tenbagger.version import __version__

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

INSTALL_REQUIRES = [
  'requests==2.26.0',
  'urllib3==1.26.6',
  "yfinance==0.1.63",
  "pytest",
  "pandas==1.3.0",
  "numpy==1.21.0",
  "matplotlib==3.4.2",
  "seaborn==0.11.1",
  "pyyaml==5.4.1",
  "pyfiglet",
  "yahoo_earnings_calendar",
  "beautifulsoup4==4.9.3",
  "html5lib",
  "plotly==5.1.0",
  "dash==1.20.0",
  'dash-bootstrap-components==0.12.2',
  "tqdm==4.59.0",
  "python-telegram-bot==13.7",
  'forex-python==1.6',
  "typeguard==2.12.0",
  "termgraph==0.5.1"
]

EXTRAS_REQUIRE = {"doc": ['nbsphinx>=0.8.5',
                          'm2r2',
                          'sphinx_rtd_theme',
                          'sphinx-gallery',
                          'readthedocs-sphinx-search'],
                  "examples": ["matplotlib"]}

setup(name='tenbagger',
      version=__version__,
      url="https://github.com/AramKoorn/TenBagger",
      entry_points={"console_scripts": ["tenbagger=tenbagger.cli:main"]},
      description='test',
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      author='Aram Koorn',
      packages=find_packages()
      )
