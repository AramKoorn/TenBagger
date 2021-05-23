#!/usr/bin/env python3

import os
from setuptools import setup, find_packages
from tenbagger.version import __version__

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

INSTALL_REQUIRES = [
  "yfinance",
  "pytest",
  "pandas",
  "numpy",
  "matplotlib",
  "seaborn",
  "pyyaml",
  "pyfiglet",
  "yahoo_earnings_calendar",
  "urllib3",
  "beautifulsoup4",
  "html5lib",
  "plotly",
  "dash",
  'dash-bootstrap-components',
  "tqdm==4.59.0",
  "python-telegram-bot",
  'CurrencyConverter==0.16.1',
  "typeguard==2.12.0",
  "termgraph"
]

setup(name='tenbaggger',
      version=__version__,
      url="https://github.com/AramKoorn/TenBagger",
      entry_points={"console_scripts": ["tenbagger=tenbagger.cli:main"]},
      description='test',
      install_requires=INSTALL_REQUIRES,
      author='Aram Koorn',
      packages=find_packages()
      )
