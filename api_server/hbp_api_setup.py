# coding: utf-8

from setuptools import setup, find_packages

NAME = "api_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python hbp_api_setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Hotel booking prob api server.",
    author_email="oscar.garcia@logitravelgroup.com",
    url="",
    keywords=["Swagger", "BookProb"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    Book prob swagger
    """
)
