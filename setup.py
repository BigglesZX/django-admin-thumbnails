#!/usr/bin/env python

"""To make a new release:
1. Bump version number in setup.py
2. Update CHANGELOG
3. $ git commit ...
4. $ git tag -a x.x.x  # see `git tags` for latest
5. $ git push origin main
6. $ git push --tags
7. $ python setup.py sdist
8. $ twine upload dist/*
"""

from setuptools import setup, find_packages  # noqa: E402

VERSION = ".".join(("1", "0", "0"))

DESCRIPTION = "A Django app for DRY thumbnails in admin list views and forms."

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Framework :: Django",
    "Framework :: Django :: 4.2",
    "Framework :: Django :: 5.0",
    "Framework :: Django :: 5.1",
    "Framework :: Django :: 5.2",
]

setup(
    name="django-admin-thumbnails",
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="James Tiplady",
    maintainer="James Tiplady",
    license="MIT",
    keywords=["django"],
    platforms=["OS Independent"],
    url="http://github.com/BigglesZX/django-admin-thumbnails",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8,<4",
    install_requires=["Django>=4.2"],
    extras_require={
        "dev": [
            "black~=25.9.0",
            "Django~=5.2.8",
            "easy-thumbnails~=2.10.1",
            "flake8~=7.3.0",
            "setuptools~=80.9.0",
            "tox~=4.32.0",
            "twine~=6.2.0",
            "wheel~=0.45.1",
        ]
    },
    classifiers=CLASSIFIERS,
)
