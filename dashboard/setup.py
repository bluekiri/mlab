#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import find_packages, setup
import io
import re
from os.path import dirname
from os.path import join


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


project_name = 'mlab'
module_name = project_name + '_dashboard'
setup(
    name=module_name,
    version='1.0.0',
    author='Oscar García Peinado',
    author_email='oscar.garcia@bluekiri.com',
    description='Mlab dashboard orchestator',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.md')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    url='',
    zip_safe=False,
    include_package_data=True,
    packages=[project_name + '_' + x for x in find_packages('src', exclude=("tests", "tests.*"))],
    package_dir={
        module_name: 'src/dashboard/'
    },
    classifiers=[
        'Programming Language :: Python :: 3.5.2',
        'Operating System :: Unix',
    ],
    install_requires=[
        'Babel==2.5.1',
        'blinker==1.4',
        'click==6.7',
        'cycler==0.10.0',
        'falcon==1.3.0',
        'Flask==0.12.2',
        'Flask-Admin==1.5.0',
        'Flask-BabelEx==0.9.3',
        'Flask-Login==0.4.0',
        'Flask-Mail==0.9.1',
        'flask-mongoengine==0.9.3',
        'Flask-Principal==0.4.0',
        'Flask-Security==3.0.0',
        'Flask-WTF==0.14.2',
        'gunicorn==19.7.1',
        'itsdangerous==0.24',
        'Jinja2==2.9.6',
        'kazoo==2.4.0',
        'ldap3==2.3',
        'MarkupSafe==1.0',
        'mongoengine==0.14.3',
        'passlib==1.7.1',
        'pyasn1==0.3.7',
        'pymongo==3.5.1',
        'pyparsing==2.2.0',
        'python-dateutil==2.6.1',
        'pytz==2017.3',
        'PyYAML==3.12',
        'six==1.11.0',
        'speaklater==1.3',
        'timeago==1.0.7',
        'Werkzeug==0.12.2',
        'WTForms==2.1',
    ]
)
