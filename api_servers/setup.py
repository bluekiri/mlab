# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from application.conf.config import APP_NAME


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
    install_requires=[
        'falcon==1.3.0',
        'tox==2.8.2',
        'virtualenv==15.1.0',
        'json-logging-py==0.2',
        'yaml',
        'pymongo==3.5.1',
        'kazoo==2.4.0'
    ]
)
