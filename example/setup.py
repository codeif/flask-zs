import io

from setuptools import find_packages, setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="demo",
    version="1.0.0",
    url="https://github.com/codeif/flask-zs/example",
    license="MIT",
    maintainer="codeif",
    maintainer_email="me@codeif.com",
    description="An example for flask-ws.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
)
