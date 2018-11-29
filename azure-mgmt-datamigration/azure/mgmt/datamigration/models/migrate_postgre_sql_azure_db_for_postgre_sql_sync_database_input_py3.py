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


class MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInput(Model):
    """Database specific information for PostgreSQL to Azure Database for
    PostgreSQL migration task inputs.

    :param name: Name of the database
    :type name: str
    :param target_database_name: Name of target database. Note: Target
     database will be truncated before starting migration.
    :type target_database_name: str
    :param migration_setting: Migration settings which tune the migration
     behavior
    :type migration_setting: dict[str, str]
    :param source_setting: Source settings to tune source endpoint migration
     behavior
    :type source_setting: dict[str, str]
    :param target_setting: Target settings to tune target endpoint migration
     behavior
    :type target_setting: dict[str, str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'target_database_name': {'key': 'targetDatabaseName', 'type': 'str'},
        'migration_setting': {'key': 'migrationSetting', 'type': '{str}'},
        'source_setting': {'key': 'sourceSetting', 'type': '{str}'},
        'target_setting': {'key': 'targetSetting', 'type': '{str}'},
    }

    def __init__(self, *, name: str=None, target_database_name: str=None, migration_setting=None, source_setting=None, target_setting=None, **kwargs) -> None:
        super(MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInput, self).__init__(**kwargs)
        self.name = name
        self.target_database_name = target_database_name
        self.migration_setting = migration_setting
        self.source_setting = source_setting
        self.target_setting = target_setting
