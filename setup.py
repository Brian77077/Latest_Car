# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="Car_Controller",
    version="0.0.1",
    description="Simple package for Car Controller Application/Script",
    long_description=readme,

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the terget machine.
    install_requires=['docutils>=0.3'],

    packages=find_packages(exclude=("test", "docs", "img", "math")),

    # Metadata to display on PyPI.
    author="Brian Salinas",
    url="https://github.com/Brian77077/Latest_Car",
    license=license,
    keywords="Learn Python Car Controller",
)
