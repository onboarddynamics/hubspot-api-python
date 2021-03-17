# coding: utf-8

"""
    Files

    Upload and manage files.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.files.files.configuration import Configuration


class FolderInput(object):
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
    openapi_types = {"name": "str", "parent_folder_id": "str", "parent_path": "str"}

    attribute_map = {"name": "name", "parent_folder_id": "parentFolderId", "parent_path": "parentPath"}

    def __init__(self, name=None, parent_folder_id=None, parent_path=None, local_vars_configuration=None):  # noqa: E501
        """FolderInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._parent_folder_id = None
        self._parent_path = None
        self.discriminator = None

        self.name = name
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if parent_path is not None:
            self.parent_path = parent_path

    @property
    def name(self):
        """Gets the name of this FolderInput.  # noqa: E501

        Desired name for the folder.  # noqa: E501

        :return: The name of this FolderInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FolderInput.

        Desired name for the folder.  # noqa: E501

        :param name: The name of this FolderInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this FolderInput.  # noqa: E501

        Folder ID of the parent of the created folder. If not specified, the folder will be created at the root level. parentFolderId and parentFolderPath cannot be set at the same time.  # noqa: E501

        :return: The parent_folder_id of this FolderInput.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this FolderInput.

        Folder ID of the parent of the created folder. If not specified, the folder will be created at the root level. parentFolderId and parentFolderPath cannot be set at the same time.  # noqa: E501

        :param parent_folder_id: The parent_folder_id of this FolderInput.  # noqa: E501
        :type: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def parent_path(self):
        """Gets the parent_path of this FolderInput.  # noqa: E501

        Path of the parent of the created folder. If not specified the folder will be created at the root level. parentFolderPath and parentFolderId cannot be set at the same time.  # noqa: E501

        :return: The parent_path of this FolderInput.  # noqa: E501
        :rtype: str
        """
        return self._parent_path

    @parent_path.setter
    def parent_path(self, parent_path):
        """Sets the parent_path of this FolderInput.

        Path of the parent of the created folder. If not specified the folder will be created at the root level. parentFolderPath and parentFolderId cannot be set at the same time.  # noqa: E501

        :param parent_path: The parent_path of this FolderInput.  # noqa: E501
        :type: str
        """

        self._parent_path = parent_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FolderInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderInput):
            return True

        return self.to_dict() != other.to_dict()
