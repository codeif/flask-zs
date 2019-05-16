#!/usr/bin/env python
from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()


setup(
    name='flask-zs',
    version='0.0.17',
    description='A helpers for Flask.',
    long_description=readme,
    author='codeif',
    author_email='me@codeif.com',
    url='https://github.com/codeif/flask-zs',
    license='MIT',
    install_requires=['requests', 'flask', 'WTForms', 'SQLAlchemy'],
    packages=find_packages(exclude=('example',)),
)
