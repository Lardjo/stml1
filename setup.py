import os
import sys

try:
    from setuptools import setup, Command
    import subprocess
except ImportError:
    from distutils.core import setup, Command
    import subprocess

VERSION = '1.0.0'
DESCRIPTION = 'Steam Stats'

class PyTest(Command):
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		errno = subprocess.call(['py.test'])
		raise SystemExit(errno)

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
    install_requires=[
    	'Flask>=0.7',
    	],
    cmdclass={'test': PyTest},
    classifiers=[
    	'Environment :: Web Environment',
    	'Programming Language :: Python'
    ]
)