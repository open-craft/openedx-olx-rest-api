"""
Studio URL configuration for openedx-olx-rest-api.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^api/olx-export/v1/', include([
        url(r'xblock/(?P<usage_key_str>[^/]+)/$', views.get_block_olx),
        # Get a static file from an XBlock that's not part of contentstore/GridFS
        url(r'xblock/(?P<usage_key_str>[^/]+)/export-file/(?P<path>.+)$', views.get_block_exportfs_file),
    ])),
]
