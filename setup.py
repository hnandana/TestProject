#!/usr/bin/python
"""A setuptools based setup module.

"""
from setuptools import setup, find_packages
setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install TestProject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name='TestProject',  # Required
    version='1.2.0',  # Required
    packages=find_packages(exclude=['Test']),  # Required
)
