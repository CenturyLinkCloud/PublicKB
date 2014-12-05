
#
# python setup.py sdist
# python setup.py bdist_dumb
# python setup.py bdist_rpm
#

from setuptools import setup, find_packages

setup(
	name = "clc-cli",
	version = "0.4",
	packages = find_packages("."),

	install_requires = ['prettytable','clint','argparse','requests'],

	entry_points = {
		'console_scripts': [
			'clc  = clc.cli:main',
		],
	},


	# metadata for upload to PyPI
	author = "Keith Resar",
	author_email = "Keith.Resar@CenturyLinkCloud.com",
	description = "CenturyLink Cloud CLI",
	keywords = "CenturyLink Cloud CLI",
	url = "https://github.com/CenturyLinkCloud/clc",

	# could also include long_description, download_url, classifiers, etc.
)

