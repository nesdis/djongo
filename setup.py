from distutils.core import setup
from setuptools import find_packages
import os
import codecs
import re
import sys

LONG_DESCRIPTION = """

Use Mongodb as a backend database for your django project, without changing a
single django model!

Usage
-----

1. Install djongo::

      pip install djongo

2. Into settings.py file of your project, add::

      DATABASES = {
           'default': {
               'ENGINE': 'djongo',
               'NAME': 'your-db-name',
           }
       }

3. Run (ONLY the first time to create collections in mongoDB)::

      manage.py makemigrations
      manage.py migrate

YOUR ARE SET! HAVE FUN!

Requirements
------------

1. Djongo requires python 3.6 or above.


How it works
------------

Djongo is a SQL to mongodb query transpiler. It translates a SQL query string
into a mongoDB query document. As a result, all Django features, models etc
work as is.

Django contrib modules::

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',

and others... fully supported.

Important links
---------------

* `Full Documentation <https://nesdis.github.io/djongo/>`_
* `Source code <https://github.com/nesdis/djongo>`_
"""


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
packages = find_packages()


def read(*parts):
    with codecs.open(os.path.join(BASE_DIR, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


install_requires = [
    'sqlparse>=0.2.4',
    'pymongo>=3.2.0',
    'django>=2.1',
    'dnspython>=2.0',
]

if sys.version_info.major == 3 and sys.version_info.minor < 7:
    install_requires.append("dataclasses")

setup(
    name='djongo',
    version=find_version("djongo", "__init__.py"),
    include_package_data=True,
    packages=packages,
    url='https://nesdis.github.io/djongo/',
    license='AGPL',
    author='nesdis',
    author_email='nesdis@gmail.com',
    description=(
        'Driver for allowing Django to use MongoDB as the database backend.'),
    install_requires=install_requires,
    extras_require=dict(
        json=[
            'jsonfield>=2.0.2',
            'django-jsoneditor>=0.0.12',
        ],
    ),
    long_description=LONG_DESCRIPTION,
    python_requires='>=3.6',
    keywords='Django MongoDB driver connector',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
    ]
)
