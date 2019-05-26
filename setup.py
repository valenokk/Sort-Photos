#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name='sortphotos',
    version='1.1',
    description='Organizes photos and videos into folders using date/time information ',
    author='Andrew Ning',
    packages=find_packages(),
    url='https://github.com/valenokk/Sort-Photos',
    include_package_data=False,
    license='MIT License',
    entry_points={
        'console_scripts': [
          'sortphotos = src.sortphotos:main',
        ]
      }
)

