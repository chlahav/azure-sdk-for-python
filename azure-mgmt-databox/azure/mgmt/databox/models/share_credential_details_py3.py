# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ShareCredentialDetails(Model):
    """Credential details of the shares in account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar share_name: Name of the share.
    :vartype share_name: str
    :ivar share_type: Type of the share. Possible values include:
     'UnknownType', 'HCS', 'BlockBlob', 'PageBlob', 'AzureFile', 'ManagedDisk'
    :vartype share_type: str or
     ~azure.mgmt.databox.models.ShareDestinationFormatType
    :ivar user_name: User name for the share.
    :vartype user_name: str
    :ivar password: Password for the share.
    :vartype password: str
    :ivar supported_access_protocols: Access protocols supported on the
     device.
    :vartype supported_access_protocols: list[str or
     ~azure.mgmt.databox.models.AccessProtocol]
    """

    _validation = {
        'share_name': {'readonly': True},
        'share_type': {'readonly': True},
        'user_name': {'readonly': True},
        'password': {'readonly': True},
        'supported_access_protocols': {'readonly': True},
    }

    _attribute_map = {
        'share_name': {'key': 'shareName', 'type': 'str'},
        'share_type': {'key': 'shareType', 'type': 'ShareDestinationFormatType'},
        'user_name': {'key': 'userName', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'supported_access_protocols': {'key': 'supportedAccessProtocols', 'type': '[AccessProtocol]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ShareCredentialDetails, self).__init__(**kwargs)
        self.share_name = None
        self.share_type = None
        self.user_name = None
        self.password = None
        self.supported_access_protocols = None