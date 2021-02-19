# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in signup/__init__.py
from signup import __version__ as version

setup(
	name='signup',
	version=version,
	description='Customer Sigup',
	author='Bantoo Accounting',
	author_email='duncan@thebantoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
