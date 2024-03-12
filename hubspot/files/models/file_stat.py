# coding: utf-8

"""
    Files Files

    Upload and manage files.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.files.configuration import Configuration


class FileStat(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"file": "File", "folder": "Folder"}

    attribute_map = {"file": "file", "folder": "folder"}

    def __init__(self, file=None, folder=None, local_vars_configuration=None):  # noqa: E501
        """FileStat - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._file = None
        self._folder = None
        self.discriminator = None

        if file is not None:
            self.file = file
        if folder is not None:
            self.folder = folder

    @property
    def file(self):
        """Gets the file of this FileStat.  # noqa: E501


        :return: The file of this FileStat.  # noqa: E501
        :rtype: File
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FileStat.


        :param file: The file of this FileStat.  # noqa: E501
        :type file: File
        """

        self._file = file

    @property
    def folder(self):
        """Gets the folder of this FileStat.  # noqa: E501


        :return: The folder of this FileStat.  # noqa: E501
        :rtype: Folder
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this FileStat.


        :param folder: The folder of this FileStat.  # noqa: E501
        :type folder: Folder
        """

        self._folder = folder

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileStat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileStat):
            return True

        return self.to_dict() != other.to_dict()
