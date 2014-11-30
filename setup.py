#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'six'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pychatscript',
    version='0.1.0',
    description='Python ChatScript Client library and programme',
    long_description=readme + '\n\n' + history,
    author='Rory McCann',
    author_email='rory@technomancy.org',
    url='https://github.com/rory/pychatscript',
    packages=[
        'chatscript',
    ],
    package_dir={'chatscript':
                 'chatscript'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3+",
    zip_safe=False,
    keywords='pychatscript',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'chatscript = chatscript.interactivesession:interactive_session',
        ]
    },
)
