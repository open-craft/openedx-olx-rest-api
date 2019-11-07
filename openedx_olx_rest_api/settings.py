"""
Common settings for the openedx-olx-rest-api app.

See apps.py for details on how this sort of plugin configures itself for
integration with Open edX.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

# Declare defaults: ############################################################



# Register settings: ###########################################################


def plugin_settings(settings):
    """
    Add our default settings to the edx-platform settings. Other settings files
    may override these values later, e.g. via envs/private.py.
    """
    pass
