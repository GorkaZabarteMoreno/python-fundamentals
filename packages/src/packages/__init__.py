"""
This distinguishes a Python module
from a Python package.

A package is a directory which includes a __init__.py
file inside of it. And inside the directory it is possible
to create many modules.

All the code inside this file is going to be executed
first whatever module of the package it is imported. (Initialization code)
"""

__all__ = ['Point']

from .Point import Point
