#!/usr/bin/env python3

import os
from setuptools import setup, find_packages
from tenbagger.version import __version__

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='tenbaggger',
      version=__version__,
      url="https://github.com/AramKoorn/TenBagger",
      py_modules=["tenbagger"],
      entry_points={"console_scripts": ["tenbagger=tenbagger.terminal:main"]},
      description='test',
      install_requires=[
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
          "forex-python==1.5",
          "python-telegram-bot",
          "termgraph"],  # Maybe fork and modify
      author='Aram Koorn',
      packages=find_packages(),
      zip_safe=False)
