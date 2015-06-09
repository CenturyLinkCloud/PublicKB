
#
# python setup.py sdist
# python setup.py bdist_dumb
# python setup.py bdist_rpm
#

from setuptools import setup, find_packages

setup(
	name = "clc-sdk",
	version = "2.18",
	packages = find_packages("."),

	install_requires = ['prettytable','clint','argparse','requests'],

	entry_points = {
		'console_scripts': [
			'clc  = clc.APIv1.cli:main',
		],
	},


	# metadata for upload to PyPI
	author = "Keith Resar",
	author_email = "Keith.Resar@CenturyLinkCloud.com",
	description = "CenturyLink Cloud SDK and CLI",
	keywords = "CenturyLink Cloud SDK CLI",
	url = "https://github.com/CenturyLinkCloud/clc-python-sdk",

	# could also include long_description, download_url, classifiers, etc.
)

