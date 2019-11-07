# -*- coding: utf-8 -*-
"""
openedx_olx_rest_api Django application initialization.
"""

from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig

from openedx.core.djangoapps.plugins.constants import PluginSettings, PluginURLs, ProjectType, SettingsType


class LxModulestoreExporterAppConfig(AppConfig):
    """
    Configuration for the openedx_olx_rest_api Django plugin application.

    See: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """

    name = 'openedx_olx_rest_api'
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.CMS: {
                # The namespace to provide to django's urls.include.
                PluginURLs.NAMESPACE: 'openedx_olx_rest_api',
            },
        },
        PluginSettings.CONFIG: {
            ProjectType.CMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: 'settings'},
            },
        },
    }

    def ready(self):
        """
        Load signal handlers when the app is ready.
        """
        pass
