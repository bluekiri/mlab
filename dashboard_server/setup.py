# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from api_servers.application.conf.config import APP_NAME


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
    version='1.0.0',
    author='Oscar García Peinado',
    author_email='oscar.garcia@bluekiri.com',
    description='ML dashboard skeleton',
    long_description=get_readme(),
    keywords='v5 mlab',
    url='',
    packages=find_packages(exclude=['tests', 'script']),
    install_requires=[
        'Babel==2.5.1',
        'blinker==1.4',
        'click==6.7',
        'Flask==0.12.2',
        'Flask-Admin==1.5.0',
        'Flask-BabelEx==0.9.3',
        'Flask-Login==0.4.0',
        'Flask-Mail==0.9.1',
        'flask-mongoengine==0.9.3',
        'Flask-Principal==0.4.0',
        'Flask-Security==3.0.0',
        'Flask-WTF==0.14.2',
        'itsdangerous==0.24',
        'Jinja2==2.9.6',
        'ldap3==2.3',
        'MarkupSafe==1.0',
        'mongoengine==0.14.3',
        'passlib==1.7.1',
        'pyasn1==0.3.7',
        'pymongo==3.5.1',
        'pytz==2017.3',
        'PyYAML==3.12',
        'six==1.11.0',
        'speaklater==1.3',
        'timeago==1.0.7',
        'Werkzeug==0.12.2',
        'WTForms==2.1',
    ]
)