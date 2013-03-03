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
    long_description=open('README.md').read() + '\n\n' +
                     open('CHANGELOG.md').read(),
    py_modules= ['main'],
    platforms='any',
)