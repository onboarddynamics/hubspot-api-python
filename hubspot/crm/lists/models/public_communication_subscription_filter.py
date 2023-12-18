# coding: utf-8

"""
    Lists

    CRUD operations to manage lists and list memberships  # noqa: E501

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

from hubspot.crm.lists.configuration import Configuration


class PublicCommunicationSubscriptionFilter(object):
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
    openapi_types = {"filter_type": "str", "subscription_ids": "list[int]", "channel": "str", "accepted_opt_states": "list[str]", "business_unit_id": "int", "subscription_type": "str"}

    attribute_map = {
        "filter_type": "filterType",
        "subscription_ids": "subscriptionIds",
        "channel": "channel",
        "accepted_opt_states": "acceptedOptStates",
        "business_unit_id": "businessUnitId",
        "subscription_type": "subscriptionType",
    }

    def __init__(
        self, filter_type="COMMUNICATION_SUBSCRIPTION", subscription_ids=None, channel=None, accepted_opt_states=None, business_unit_id=None, subscription_type=None, local_vars_configuration=None
    ):  # noqa: E501
        """PublicCommunicationSubscriptionFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._filter_type = None
        self._subscription_ids = None
        self._channel = None
        self._accepted_opt_states = None
        self._business_unit_id = None
        self._subscription_type = None
        self.discriminator = None

        self.filter_type = filter_type
        self.subscription_ids = subscription_ids
        self.channel = channel
        self.accepted_opt_states = accepted_opt_states
        if business_unit_id is not None:
            self.business_unit_id = business_unit_id
        self.subscription_type = subscription_type

    @property
    def filter_type(self):
        """Gets the filter_type of this PublicCommunicationSubscriptionFilter.  # noqa: E501


        :return: The filter_type of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this PublicCommunicationSubscriptionFilter.


        :param filter_type: The filter_type of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :type filter_type: str
        """
        if self.local_vars_configuration.client_side_validation and filter_type is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_type`, must not be `None`")  # noqa: E501
        allowed_values = ["COMMUNICATION_SUBSCRIPTION"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and filter_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `filter_type` ({0}), must be one of {1}".format(filter_type, allowed_values))  # noqa: E501

        self._filter_type = filter_type

    @property
    def subscription_ids(self):
        """Gets the subscription_ids of this PublicCommunicationSubscriptionFilter.  # noqa: E501


        :return: The subscription_ids of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._subscription_ids

    @subscription_ids.setter
    def subscription_ids(self, subscription_ids):
        """Sets the subscription_ids of this PublicCommunicationSubscriptionFilter.


        :param subscription_ids: The subscription_ids of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :type subscription_ids: list[int]
        """
        if self.local_vars_configuration.client_side_validation and subscription_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription_ids`, must not be `None`")  # noqa: E501

        self._subscription_ids = subscription_ids

    @property
    def channel(self):
        """Gets the channel of this PublicCommunicationSubscriptionFilter.  # noqa: E501


        :return: The channel of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this PublicCommunicationSubscriptionFilter.


        :param channel: The channel of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :type channel: str
        """
        if self.local_vars_configuration.client_side_validation and channel is None:  # noqa: E501
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def accepted_opt_states(self):
        """Gets the accepted_opt_states of this PublicCommunicationSubscriptionFilter.  # noqa: E501


        :return: The accepted_opt_states of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._accepted_opt_states

    @accepted_opt_states.setter
    def accepted_opt_states(self, accepted_opt_states):
        """Sets the accepted_opt_states of this PublicCommunicationSubscriptionFilter.


        :param accepted_opt_states: The accepted_opt_states of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :type accepted_opt_states: list[str]
        """
        if self.local_vars_configuration.client_side_validation and accepted_opt_states is None:  # noqa: E501
            raise ValueError("Invalid value for `accepted_opt_states`, must not be `None`")  # noqa: E501

        self._accepted_opt_states = accepted_opt_states

    @property
    def business_unit_id(self):
        """Gets the business_unit_id of this PublicCommunicationSubscriptionFilter.  # noqa: E501


        :return: The business_unit_id of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :rtype: int
        """
        return self._business_unit_id

    @business_unit_id.setter
    def business_unit_id(self, business_unit_id):
        """Sets the business_unit_id of this PublicCommunicationSubscriptionFilter.


        :param business_unit_id: The business_unit_id of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :type business_unit_id: int
        """

        self._business_unit_id = business_unit_id

    @property
    def subscription_type(self):
        """Gets the subscription_type of this PublicCommunicationSubscriptionFilter.  # noqa: E501


        :return: The subscription_type of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        """Sets the subscription_type of this PublicCommunicationSubscriptionFilter.


        :param subscription_type: The subscription_type of this PublicCommunicationSubscriptionFilter.  # noqa: E501
        :type subscription_type: str
        """
        if self.local_vars_configuration.client_side_validation and subscription_type is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription_type`, must not be `None`")  # noqa: E501

        self._subscription_type = subscription_type

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
        if not isinstance(other, PublicCommunicationSubscriptionFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicCommunicationSubscriptionFilter):
            return True

        return self.to_dict() != other.to_dict()