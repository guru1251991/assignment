from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in auriga_test/__init__.py
from auriga_test import __version__ as version

setup(
	name="auriga_test",
	version=version,
	description="test app for ui",
	author="auriga",
	author_email="guruprasad.kondiba@aurigait.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
