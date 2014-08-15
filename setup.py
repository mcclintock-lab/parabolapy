#!/usr/bin/env python

try:
      from setuptools import setup
except ImportError:
      from distutils.core import setup

setup(name='parabolapy',
      version='0.1',
      description='Parabola Geoprocessing Server Utilities',
      author='McClintock Lab, UCSB',
      author_email='admin@seasketch.org',
      url='https://github.com/mcclintock-lab/parabolapy',
      packages=['parabolapy'],
      package_dir={'parabolapy': 'parabolapy'},
     )
