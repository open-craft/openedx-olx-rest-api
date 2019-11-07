"""
Helpers required to adapt to differing APIs
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from contextlib import contextmanager

from fs.memoryfs import MemoryFS
from fs.wrapfs import WrapFS

from xmodule.xml_module import XmlParserMixin


@contextmanager
def override_export_fs(block):
    """
    Hack required for some legacy XBlocks which inherit
    XModuleDescriptor.add_xml_to_node() instead of the usual
    XmlSerializationMixin.add_xml_to_node() method.

    This method temporarily replaces a block's runtime's
    'export_fs' system with an in-memory filesystem.

    This method also abuses the XmlParserMixin.export_to_file()
    API to prevent the XModule export code from exporting each
    block as two files (one .olx pointing to one .xml file).
    The export_to_file was meant to be used only by the
    customtag XModule but it makes our lives here much easier.
    """
    fs = WrapFS(MemoryFS())
    fs.makedir('course')
    fs.makedir('course/static')  # Video XBlock requires this directory to exists, to put srt files etc.

    old_export_fs = block.runtime.export_fs
    block.runtime.export_fs = fs
    if hasattr(block, 'export_to_file'):
        old_export_to_file = block.export_to_file
        block.export_to_file = lambda: False
    old_global_export_to_file = XmlParserMixin.export_to_file
    XmlParserMixin.export_to_file = lambda _: False  # So this applies to child blocks that get loaded during export
    yield fs
    block.runtime.export_fs = old_export_fs
    if hasattr(block, 'export_to_file'):
        block.export_to_file = old_export_to_file
    XmlParserMixin.export_to_file = old_global_export_to_file
