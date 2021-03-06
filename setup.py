#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import versioneer
from os.path import exists


if exists("requirements.txt"):
    with open("requirements.txt") as f:
        install_requires = f.read().strip().split("\n")
else:
    install_requires = ["intake", "xarray", "pyyaml", "tqdm", "intake-xarray"]

if exists("README.rst"):
    with open("README.rst") as f:
        long_description = f.read()
else:
    long_description = ""


setup(
    name="intake-esm",
    description="An intake plugin for building and loading earth system data sets such as CMIP, CESM Large Ensemble",
    long_description=long_description,
    python_requires=">3.5",
    maintainer="Anderson Banihirwe",
    maintainer_email="abanihi@ucar.edu",
    url="https://github.com/NCAR/intake-esm",
    packages=find_packages(),
    package_dir={"intake-esm": "intake-esm"},
    include_package_data=True,
    install_requires=install_requires,
    license="Apache 2.0",
    zip_safe=False,
    keywords="intake-esm",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
