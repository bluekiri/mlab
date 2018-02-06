#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from setuptools import find_packages, setup
import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='ml.api.server',
    version='0.1.0',
    author='Oscar García Peinado',
    author_email='oscar.garcia@bluekiri.com',
    description=('Mlab api server module will be used in order to response the client model request.'),
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.md')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    zip_safe=False,
    url='',
    include_package_data=True,
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    classifiers=['Programming Language :: Python :: 3.5',
                 'Operating System :: Unix',
                 ],
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
