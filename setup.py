#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

# setup(name='TenBagger',
#       version='0.0.1',
#       description='CLI for finance',
#       author='Aram Koorn',
#       license='MIT',
#       long_description=long_description,
#       long_description_content_type='text/markdown',
#       packages = ['tenbagger'],
#       classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License"
#       ],
#       python_requires='>=3.8'
#       )

setup(name='tenbaggger',
      version="0.0.1",
      description='test',
      author='Aram Koorn',
      packages=find_packages(),
      zip_safe=False)
