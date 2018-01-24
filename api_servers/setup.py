# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from api_servers.application.conf.config import APP_NAME


def get_requirements():
    with open('requirements.txt') as fp:
        return fp.readlines()

def get_readme():
    readme = ''
    try:
        import pypandoc
        readme = pypandoc.convert('README.md', 'rst')
    except (ImportError, IOError):
        with open('README.md', 'r') as file_data:
            readme = file_data.read()
    return readme


setup(
    name=APP_NAME,
    version='0.1.0',
    author='Oscar García Peinado',
    author_email='oscar.garcia@bluekiri.com',
    description=('ML server'),
    long_description=get_readme(),
    keywords='v5 mlab',
    url='',
    packages=find_packages(exclude=['tests', 'script']),
    install_requires= get_requirements()

)
