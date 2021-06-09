# coding: utf-8

# flake8: noqa
"""
    Calling Extensions API

    Provides a way for apps to add custom calling options to a contact record. This works in conjunction with the [Calling SDK](#), which is used to build your phone/calling UI. The endpoints here allow your service to appear as an option to HubSpot users when they access the *Call* action on a contact record. Once accessed, your custom phone/calling UI will be displayed in an iframe at the specified URL with the specified dimensions on that record.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from hubspot.crm.extensions.calling.models.error import Error
from hubspot.crm.extensions.calling.models.error_detail import ErrorDetail
from hubspot.crm.extensions.calling.models.settings_patch_request import SettingsPatchRequest
from hubspot.crm.extensions.calling.models.settings_request import SettingsRequest
from hubspot.crm.extensions.calling.models.settings_response import SettingsResponse