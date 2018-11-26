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


class EnvelopeEncryption(Model):
    """Class for EnvelopeEncryption encryption scheme.

    :param enabled_protocols: Representing supported protocols
    :type enabled_protocols: ~azure.mgmt.media.models.EnabledProtocols
    :param clear_tracks: Representing which tracks should not be encrypted
    :type clear_tracks: list[~azure.mgmt.media.models.TrackSelection]
    :param content_keys: Representing default content key for each encryption
     scheme and separate content keys for specific tracks
    :type content_keys: ~azure.mgmt.media.models.StreamingPolicyContentKeys
    :param custom_key_acquisition_url_template: KeyAcquisitionUrlTemplate is
     used to point to user specified service to delivery content keys
    :type custom_key_acquisition_url_template: str
    """

    _attribute_map = {
        'enabled_protocols': {'key': 'enabledProtocols', 'type': 'EnabledProtocols'},
        'clear_tracks': {'key': 'clearTracks', 'type': '[TrackSelection]'},
        'content_keys': {'key': 'contentKeys', 'type': 'StreamingPolicyContentKeys'},
        'custom_key_acquisition_url_template': {'key': 'customKeyAcquisitionUrlTemplate', 'type': 'str'},
    }

    def __init__(self, *, enabled_protocols=None, clear_tracks=None, content_keys=None, custom_key_acquisition_url_template: str=None, **kwargs) -> None:
        super(EnvelopeEncryption, self).__init__(**kwargs)
        self.enabled_protocols = enabled_protocols
        self.clear_tracks = clear_tracks
        self.content_keys = content_keys
        self.custom_key_acquisition_url_template = custom_key_acquisition_url_template
