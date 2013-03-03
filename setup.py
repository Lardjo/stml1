import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Steam-Stats',
    version='1.0.0',
    url='http://github.com/Lardjo/steam-stats',
    license='MIT',
    author='Konstantin',
    description='Steam Stats',
    long_description=open('README.rst').read() + '\n\n' +
                     open('CHANGES.rst').read(),
    py_modules= ['main'],
    platforms='any',
    install_requires=[
        'Flask>=0.8',
    ],
)