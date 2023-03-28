#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import sys

if sys.version_info < (2, 6) or (3, 0) <= sys.version_info < (3, 6):
    sys.exit("Sorry, Python version 2.6 and 3.0-3.5 are not supported.")

setup(
    name             = 'cssmin',
    version          = '0.2.0',
    author           = "LEKO LABS",
    url              = 'https://github.com/LekoLabs/cssmin',
    description      = "A Python port of the YUI CSS compression algorithm.",
    py_modules       = ['cssmin'],
    package_dir      = {'': 'src'},
    entry_points     = {'console_scripts': ['cssmin = cssmin:main']},
)
