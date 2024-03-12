# coding: utf-8

"""
    Webhooks Webhooks

    Provides a way for apps to subscribe to certain change events in HubSpot. Once configured, apps will receive event payloads containing details about the changes at a specified target URL. There can only be one target URL for receiving event notifications per app.  # noqa: E501

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

from hubspot.webhooks.configuration import Configuration


class SettingsChangeRequest(object):
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
    openapi_types = {"throttling": "ThrottlingSettings", "target_url": "str"}

    attribute_map = {"throttling": "throttling", "target_url": "targetUrl"}

    def __init__(self, throttling=None, target_url=None, local_vars_configuration=None):  # noqa: E501
        """SettingsChangeRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._throttling = None
        self._target_url = None
        self.discriminator = None

        self.throttling = throttling
        self.target_url = target_url

    @property
    def throttling(self):
        """Gets the throttling of this SettingsChangeRequest.  # noqa: E501


        :return: The throttling of this SettingsChangeRequest.  # noqa: E501
        :rtype: ThrottlingSettings
        """
        return self._throttling

    @throttling.setter
    def throttling(self, throttling):
        """Sets the throttling of this SettingsChangeRequest.


        :param throttling: The throttling of this SettingsChangeRequest.  # noqa: E501
        :type throttling: ThrottlingSettings
        """
        if self.local_vars_configuration.client_side_validation and throttling is None:  # noqa: E501
            raise ValueError("Invalid value for `throttling`, must not be `None`")  # noqa: E501

        self._throttling = throttling

    @property
    def target_url(self):
        """Gets the target_url of this SettingsChangeRequest.  # noqa: E501

        A publicly available URL for HubSpot to call where event payloads will be delivered.  # noqa: E501

        :return: The target_url of this SettingsChangeRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """Sets the target_url of this SettingsChangeRequest.

        A publicly available URL for HubSpot to call where event payloads will be delivered.  # noqa: E501

        :param target_url: The target_url of this SettingsChangeRequest.  # noqa: E501
        :type target_url: str
        """
        if self.local_vars_configuration.client_side_validation and target_url is None:  # noqa: E501
            raise ValueError("Invalid value for `target_url`, must not be `None`")  # noqa: E501

        self._target_url = target_url

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
        if not isinstance(other, SettingsChangeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsChangeRequest):
            return True

        return self.to_dict() != other.to_dict()
