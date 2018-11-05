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

try:
    from .resource_py3 import Resource
    from .kind_py3 import Kind
    from .security_contact_py3 import SecurityContact
    from .pricing_py3 import Pricing
    from .workspace_setting_py3 import WorkspaceSetting
    from .auto_provisioning_setting_py3 import AutoProvisioningSetting
    from .compliance_segment_py3 import ComplianceSegment
    from .compliance_py3 import Compliance
    from .advanced_threat_protection_setting_py3 import AdvancedThreatProtectionSetting
    from .setting_py3 import Setting
    from .data_export_setting_py3 import DataExportSetting
    from .setting_kind1_py3 import SettingKind1
    from .sensitivity_label_py3 import SensitivityLabel
    from .information_protection_keyword_py3 import InformationProtectionKeyword
    from .information_type_py3 import InformationType
    from .information_protection_policy_py3 import InformationProtectionPolicy
    from .location_py3 import Location
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
    from .security_task_parameters_py3 import SecurityTaskParameters
    from .security_task_py3 import SecurityTask
    from .asc_location_py3 import AscLocation
    from .alert_entity_py3 import AlertEntity
    from .alert_confidence_reason_py3 import AlertConfidenceReason
    from .alert_py3 import Alert
    from .discovered_security_solution_py3 import DiscoveredSecuritySolution
    from .topology_single_resource_parent_py3 import TopologySingleResourceParent
    from .topology_single_resource_child_py3 import TopologySingleResourceChild
    from .topology_single_resource_py3 import TopologySingleResource
    from .topology_resource_py3 import TopologyResource
    from .jit_network_access_port_rule_py3 import JitNetworkAccessPortRule
    from .jit_network_access_policy_virtual_machine_py3 import JitNetworkAccessPolicyVirtualMachine
    from .jit_network_access_request_port_py3 import JitNetworkAccessRequestPort
    from .jit_network_access_request_virtual_machine_py3 import JitNetworkAccessRequestVirtualMachine
    from .jit_network_access_request_py3 import JitNetworkAccessRequest
    from .jit_network_access_policy_py3 import JitNetworkAccessPolicy
    from .jit_network_access_policy_initiate_port_py3 import JitNetworkAccessPolicyInitiatePort
    from .jit_network_access_policy_initiate_virtual_machine_py3 import JitNetworkAccessPolicyInitiateVirtualMachine
    from .jit_network_access_policy_initiate_request_py3 import JitNetworkAccessPolicyInitiateRequest
    from .external_security_solution_py3 import ExternalSecuritySolution
    from .cef_solution_properties_py3 import CefSolutionProperties
    from .cef_external_security_solution_py3 import CefExternalSecuritySolution
    from .ata_solution_properties_py3 import AtaSolutionProperties
    from .ata_external_security_solution_py3 import AtaExternalSecuritySolution
    from .connected_workspace_py3 import ConnectedWorkspace
    from .aad_solution_properties_py3 import AadSolutionProperties
    from .aad_external_security_solution_py3 import AadExternalSecuritySolution
    from .external_security_solution_kind1_py3 import ExternalSecuritySolutionKind1
    from .external_security_solution_properties_py3 import ExternalSecuritySolutionProperties
    from .aad_connectivity_state1_py3 import AadConnectivityState1
except (SyntaxError, ImportError):
    from .resource import Resource
    from .kind import Kind
    from .security_contact import SecurityContact
    from .pricing import Pricing
    from .workspace_setting import WorkspaceSetting
    from .auto_provisioning_setting import AutoProvisioningSetting
    from .compliance_segment import ComplianceSegment
    from .compliance import Compliance
    from .advanced_threat_protection_setting import AdvancedThreatProtectionSetting
    from .setting import Setting
    from .data_export_setting import DataExportSetting
    from .setting_kind1 import SettingKind1
    from .sensitivity_label import SensitivityLabel
    from .information_protection_keyword import InformationProtectionKeyword
    from .information_type import InformationType
    from .information_protection_policy import InformationProtectionPolicy
    from .location import Location
    from .operation_display import OperationDisplay
    from .operation import Operation
    from .security_task_parameters import SecurityTaskParameters
    from .security_task import SecurityTask
    from .asc_location import AscLocation
    from .alert_entity import AlertEntity
    from .alert_confidence_reason import AlertConfidenceReason
    from .alert import Alert
    from .discovered_security_solution import DiscoveredSecuritySolution
    from .topology_single_resource_parent import TopologySingleResourceParent
    from .topology_single_resource_child import TopologySingleResourceChild
    from .topology_single_resource import TopologySingleResource
    from .topology_resource import TopologyResource
    from .jit_network_access_port_rule import JitNetworkAccessPortRule
    from .jit_network_access_policy_virtual_machine import JitNetworkAccessPolicyVirtualMachine
    from .jit_network_access_request_port import JitNetworkAccessRequestPort
    from .jit_network_access_request_virtual_machine import JitNetworkAccessRequestVirtualMachine
    from .jit_network_access_request import JitNetworkAccessRequest
    from .jit_network_access_policy import JitNetworkAccessPolicy
    from .jit_network_access_policy_initiate_port import JitNetworkAccessPolicyInitiatePort
    from .jit_network_access_policy_initiate_virtual_machine import JitNetworkAccessPolicyInitiateVirtualMachine
    from .jit_network_access_policy_initiate_request import JitNetworkAccessPolicyInitiateRequest
    from .external_security_solution import ExternalSecuritySolution
    from .cef_solution_properties import CefSolutionProperties
    from .cef_external_security_solution import CefExternalSecuritySolution
    from .ata_solution_properties import AtaSolutionProperties
    from .ata_external_security_solution import AtaExternalSecuritySolution
    from .connected_workspace import ConnectedWorkspace
    from .aad_solution_properties import AadSolutionProperties
    from .aad_external_security_solution import AadExternalSecuritySolution
    from .external_security_solution_kind1 import ExternalSecuritySolutionKind1
    from .external_security_solution_properties import ExternalSecuritySolutionProperties
    from .aad_connectivity_state1 import AadConnectivityState1
from .pricing_paged import PricingPaged
from .security_contact_paged import SecurityContactPaged
from .workspace_setting_paged import WorkspaceSettingPaged
from .auto_provisioning_setting_paged import AutoProvisioningSettingPaged
from .compliance_paged import CompliancePaged
from .setting_paged import SettingPaged
from .information_protection_policy_paged import InformationProtectionPolicyPaged
from .operation_paged import OperationPaged
from .asc_location_paged import AscLocationPaged
from .security_task_paged import SecurityTaskPaged
from .alert_paged import AlertPaged
from .discovered_security_solution_paged import DiscoveredSecuritySolutionPaged
from .jit_network_access_policy_paged import JitNetworkAccessPolicyPaged
from .external_security_solution_paged import ExternalSecuritySolutionPaged
from .topology_resource_paged import TopologyResourcePaged
from .security_center_enums import (
    AlertNotifications,
    AlertsToAdmins,
    PricingTier,
    AutoProvision,
    SettingKind,
    SecurityFamily,
    Protocol,
    Status,
    StatusReason,
    AadConnectivityState,
    ExternalSecuritySolutionKind,
)

__all__ = [
    'Resource',
    'Kind',
    'SecurityContact',
    'Pricing',
    'WorkspaceSetting',
    'AutoProvisioningSetting',
    'ComplianceSegment',
    'Compliance',
    'AdvancedThreatProtectionSetting',
    'Setting',
    'DataExportSetting',
    'SettingKind1',
    'SensitivityLabel',
    'InformationProtectionKeyword',
    'InformationType',
    'InformationProtectionPolicy',
    'Location',
    'OperationDisplay',
    'Operation',
    'SecurityTaskParameters',
    'SecurityTask',
    'AscLocation',
    'AlertEntity',
    'AlertConfidenceReason',
    'Alert',
    'DiscoveredSecuritySolution',
    'TopologySingleResourceParent',
    'TopologySingleResourceChild',
    'TopologySingleResource',
    'TopologyResource',
    'JitNetworkAccessPortRule',
    'JitNetworkAccessPolicyVirtualMachine',
    'JitNetworkAccessRequestPort',
    'JitNetworkAccessRequestVirtualMachine',
    'JitNetworkAccessRequest',
    'JitNetworkAccessPolicy',
    'JitNetworkAccessPolicyInitiatePort',
    'JitNetworkAccessPolicyInitiateVirtualMachine',
    'JitNetworkAccessPolicyInitiateRequest',
    'ExternalSecuritySolution',
    'CefSolutionProperties',
    'CefExternalSecuritySolution',
    'AtaSolutionProperties',
    'AtaExternalSecuritySolution',
    'ConnectedWorkspace',
    'AadSolutionProperties',
    'AadExternalSecuritySolution',
    'ExternalSecuritySolutionKind1',
    'ExternalSecuritySolutionProperties',
    'AadConnectivityState1',
    'PricingPaged',
    'SecurityContactPaged',
    'WorkspaceSettingPaged',
    'AutoProvisioningSettingPaged',
    'CompliancePaged',
    'SettingPaged',
    'InformationProtectionPolicyPaged',
    'OperationPaged',
    'AscLocationPaged',
    'SecurityTaskPaged',
    'AlertPaged',
    'DiscoveredSecuritySolutionPaged',
    'JitNetworkAccessPolicyPaged',
    'ExternalSecuritySolutionPaged',
    'TopologyResourcePaged',
    'AlertNotifications',
    'AlertsToAdmins',
    'PricingTier',
    'AutoProvision',
    'SettingKind',
    'SecurityFamily',
    'Protocol',
    'Status',
    'StatusReason',
    'AadConnectivityState',
    'ExternalSecuritySolutionKind',
]