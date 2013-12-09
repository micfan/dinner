#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='Dinner',
    version='1.0',
    description="Django testing project",
    author="Michael Fan",
    author_email='micfan.com',
    url='http://www.micfan.com',
    packages=find_packages(),
    package_data={'src': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
