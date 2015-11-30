#! /usr/bin/env python
# "Time-stamp: <09/15/2013  3:10:12 PM rsg>"
'''
__init__.py - Package initialization module.
'''
#################################################################
#
# File: __init__.py
#
# Purpose:
#
#    Package initialization module.
#
# Usage (example):
#
#    import tsToolsCLI
#
# Requirements:
#
#    Python 2.5 or later.
#
# Capabilities:
#
#    Performs initialization for the package.
#
# Limitations:
#
#    1. The name of each library module is expected to use the
#       prefix 'ts'.
#
#    2. The top level file directory module is expected to be
#       named 'tsToolsCLI'.
#
#    3. It is recommended that the name of each package module
#       that contains two or more files or sub-directories use the
#       suffix 'Pkg'.
#
#    4. Each lower level module must be imported in a sequence
#       that permits non-recursive resolution of import dependency.
#       For example, "tsLinesOfCode" must have been imported before
#       "tsTrimTreeLines". To enable the non-recursive resolution
#       of import dependency, it is required that any and all import
#       statements be placed at the beginning and outer most scope
#       of each lower level module. Adherance to this convention
#       ensures that imported module names are placed in the importing
#       module's global symbol table.
#
# Notes:
#
#    Directory Structure (example):
#
#      tsToolsCLI/ # Subpackage for command line tool components
#
#        __init__.py
#
#        tsLinesOfCodePkg/     # Subpackage for source code metrics
#
#          __init__.py
#
#          tsLinesOfCode.py
#
#        tsTrimTreeLinesPkg/   # Subpackage for log device/file interface
#
#          __init__.py
#
#          tsTrimTreeLines.py
#
# Methods:
#
#    N/A
#
# Classes:
#
#    N/A
#
# Modifications:
#
#    2013/05/25 rsg Added import tsToolsCLI.
#
#    2013/07/31 rsg Renamed directory from tsLinesOfCodePkg to
#                   tsLinesOfCodeProjectMetricsPkg to reflect
#                   name of application launch module.
#
#    2013/09/14 rsg Removed import tsLibCLI because it was not
#                   needed and prevented tsStripComments re-use
#                   of tsOperatorSettingParser name.
#
# ToDo:
#
#    None
#
#################################################################

__title__     = '__init__'
__version__   = '2.1.1'
__date__      = '09/14/2013'
__authors__   = 'Frederick A. Kier & Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsToolsCLI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier.' + \
                '\n\t\t\tAll rights reserved.'
 
__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Author(s): %s' % __authors__
__line3__ = '%s' % __copyright__

if ((len(__credits__) == 0)):
    __line4__ = '%s' % __license__
else:
    __line4__ = '%s%s' % (__license__, __credits__)

__header__ = '\n\n%s\n\n  %s\n  %s\n  %s\n' % (__line1__,
                                               __line2__,
                                               __line3__,
                                               __line4__)

mainTitleVersionDate = __line1__

#--------------------------------------------------------------------------

import imp
import sys
import os

#--------------------------------------------------------------------------

from tsCxGlobals import ThemeToUse

Troubleshooting = ThemeToUse['Troubleshooting']

Debug_CLI_Configuration = Troubleshooting['Debug_CLI_Configuration'],
Debug_CLI_Exceptions = Troubleshooting['Debug_CLI_Exceptions']
Debug_CLI_Launch = Troubleshooting['Debug_CLI_Launch']
Debug_CLI_Progress = Troubleshooting['Debug_CLI_Progress']
Debug_CLI_Termination = Troubleshooting['Debug_CLI_Termination']
Debug_GUI_Configuration = Troubleshooting['Debug_GUI_Configuration']
Debug_GUI_Exceptions = Troubleshooting['Debug_GUI_Exceptions']
Debug_GUI_Launch = Troubleshooting['Debug_GUI_Launch']
Debug_GUI_Progress = Troubleshooting['Debug_GUI_Progress']
Debug_GUI_Termination = Troubleshooting['Debug_GUI_Termination']

#---------------------------------------------------------------------------

importRoot = 'tsToolsCLI'

if sys.version < '3':
      package_dir = {'src': 'src'}
      test_dir = {'test': 'test'}
else:
      package_dir = {'src': 'src'}
      test_dir = {'test': 'test'}

theContainer = package_dir['src']

__myAll__ = [
    # Sub modules. Troubleshooting will be required before uncommenting.
    # 'tsLibraryImportPkg',
    'tsLinesOfCodeProjectMetricsPkg',
    'tsPlatformQueryPkg',
    # 'tsPublishPkg',
    # 'tsReAuthorPkg',
    # 'tsReImportPkg',
    # 'tsReVersionPkg',
    'tsStripCommentsPkg',
    'tsStripLineNumbersPkg',
    'tsTreeCopyPkg',
    'tsTreeTrimLinesPkg'
    ]

theName = importRoot

if Debug_CLI_Launch:

    print('  init in %s' % theName)
    pathToTs = imp.find_module(theName)[1]
    print('    %s = %s' %  (theName, pathToTs))
 
# Import all of our modules
for theModule in __myAll__:

    fullModuleName = '%s.%s.%s' % (theName, theModule, theContainer)
    if Debug_CLI_Launch:
        print('    Importing %s' % fullModuleName)
    try:
        __import__(fullModuleName)
    except ImportError as e:
        print('***** Failed: %s' % e)


if Debug_CLI_Launch:
    print('  Begin Cleanup %s' % fullModuleName)

for k, v in list(sys.modules.items()):
    # Cannot delete tsLibraries entry; leave dot at end of startswith string.
    if k.startswith('%s.' % theName):
        if Debug_CLI_Launch:
            print('    Deleting %s' % k)
        del sys.modules[k]

if Debug_CLI_Launch:
    print('  End Cleanup %s' % fullModuleName)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
