# coding: utf-8

"""
    Contacts

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from os.path import dirname, abspath, exists
from setuptools import setup, find_packages  # noqa: H301


NAME = "hubspot-api-client"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.15",
    "six >= 1.10",
    "certifi",
    "python-dateutil",
    "importlib-metadata<5; python_version<'3.8'"
]
DEV_REQUIRES = ["pytest", "black"]

DIR_PATH = dirname(abspath(__file__))

with open(DIR_PATH + "/VERSION", "r", encoding="utf-8") as f:
    VERSION = f.readline().strip()

LONG_DESCRIPTION = None
if exists(DIR_PATH + "/README.md"):
    with open(DIR_PATH + "/README.md", "r", encoding="utf-8") as f:
        LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    packages=find_packages(),
    version=VERSION,
    description="HubSpot API client",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/HubSpot/hubspot-api-python",
    author="HubSpot",
    author_email="support@hubspot.com",
    install_requires=REQUIRES,
    extras_require={"dev": DEV_REQUIRES},
    python_requires=">=3.7",
    include_package_data=True,
    license='Apache-2.0',
)
