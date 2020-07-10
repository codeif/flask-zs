#!/usr/bin/env python
from setuptools import find_packages, setup

with open("README.rst", encoding="utf-8") as f:
    readme = f.read()


setup(
    name="flask-zs",
    version="0.0.25",
    description="A helpers for Flask.",
    long_description=readme,
    author="codeif",
    author_email="me@codeif.com",
    url="https://github.com/codeif/flask-zs",
    license="MIT",
    entry_points={
        "console_scripts": ["collect-models = flask_zs.bin.collect_models:main"]
    },
    install_requires=["requests", "flask", "WTForms", "SQLAlchemy"],
    packages=find_packages(exclude=("example",)),
)
