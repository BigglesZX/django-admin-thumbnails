#!/usr/bin/env python

''' XXX: allow dist building on vagrant
    source: http://bugs.python.org/issue8876
    to build: $ python setup.py register sdist
    then: $ twine upload dist/*
'''
import os
del os.link

from setuptools import setup, find_packages  # noqa: E402


VERSION = '.'.join(('0', '1', '1'))

DESCRIPTION = 'A Django app for DRY thumbnails in admin list views and forms.'

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Framework :: Django',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.9',
    'Framework :: Django :: 1.10',
    'Framework :: Django :: 1.11',
]

setup(
    name='django-admin-thumbnails',
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='James Tiplady',
    maintainer='James Tiplady',
    license='MIT',
    keywords=['django'],
    platforms=['OS Independent'],
    url='http://github.com/BigglesZX/django-admin-thumbnails',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django<2.0'],
    extras_require={
        'dev': [
            'flake8>=3.7.7',
            'setuptools>=41.0.0',
            'twine>=1.13.0',
            'wheel>=0.33.1',
        ]
    },
    classifiers=CLASSIFIERS
)
