import os
import sys

try:
    from setuptools import setup, Command
    import subprocess
except ImportError:
    from distutils.core import setup, Command
    import subprocess

import steam_stats

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
    name = steam_stats.__name__,
    version = steam_stats.__version__,
    url = steam_stats.__url__,
    license = steam_stats.__license__,
    author = steam_stats.__author__,
    description = steam_stats.__description__,
    long_description = open('README.md').read() + '\n\n' +
                     open('CHANGELOG.md').read(),
    packages = ['steam_stats'],
    scripts = ['steam_stats/main.py'],
    include_package_data = True,
    zip_safe = False,
    platforms ='any',
    install_requires =[
    	'Flask>=0.7',
    	],
    cmdclass = {'test': PyTest},
    classifiers = [
    	'Environment :: Web Environment',
    	'Programming Language :: Python'
    ]
)