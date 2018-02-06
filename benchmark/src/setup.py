# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from api_server.application.conf.config import APP_NAME


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
    description=('ML benchmark server'),
    long_description=get_readme(),
    keywords='v5 mlab',
    url='',
    packages=find_packages(exclude=['tests', 'script']),
    install_requires=[
        'dill==0.2.7.1',
        'falcon==1.3.0',
        'gunicorn==19.7.1',
        'json-logging-py==0.2',
        'kazoo==2.4.0',
        'mongoengine==0.14.3',
        'pluggy==0.5.2',
        'py==1.4.34',
        'pymongo==3.5.1',
        'python-mimeparse==1.6.0',
        'PyYAML==3.12',
        'six==1.11.0',
        'tox==2.8.2',
    ]
)
