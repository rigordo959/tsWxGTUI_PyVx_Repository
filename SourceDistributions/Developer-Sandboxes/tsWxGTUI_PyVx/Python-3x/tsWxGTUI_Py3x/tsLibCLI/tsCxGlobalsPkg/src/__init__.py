#! /usr/bin/env python
# "Time-stamp: <02/09/2014  7:18:44 AM rsg>"
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
#    import tsApplicationPkg
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
#    1. tsCxGlobals must NOT be in the tsCxGlobals package because
#       it must be shared with and be accessible to all packages
#       in tsLibCLI.
#
# Notes:
#
#    N/A
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
#    2013/10/13 rsg Initial release.
#
#    2014/02/09 rsg Corrected inappropriate use of Python 2.x
#                   syntax for __init__ import exception handling.
#
# ToDo:
#
#    None
#
#################################################################

__title__     = '__init__'
__version__   = '1.1.0'
__date__      = '02/09/2014'
__authors__   = 'Frederick A. Kier & Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2014 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibCLI Import & Application Launch Features: ' + \
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

tsImportRoot = 'tsLibCLI'
libraryImportRoot = 'library'
theName = 'tsCxGlobalsPkg'

if sys.version < '3':
      package_dir = {'src': 'src'}
      test_dir = {'test': 'test'}
else:
      package_dir = {'src': 'src'}
      test_dir = {'test': 'test'}

theContainer = package_dir['src']

# Is the user coming through ts?
if os.path.abspath(__file__).find('library') == -1:
    # Yes
    theTop = tsImportRoot
else:
    # No
    theTop = libraryImportRoot
path = [theTop, theName, theContainer]

__myAll__ = [
    # Sub modules
    # 'tsCxGlobals'
    ]

if Debug_CLI_Launch:

    print('      init in %s' % theName)

for theModule in __myAll__:

    fullModuleName = ''
    for item in path:
        fullModuleName += '%s.' % item
    fullModuleName += theModule

    if Debug_CLI_Launch:
        print('        Importing %s' % fullModuleName)
    try:
        __import__(fullModuleName)
    except ImportError as e:
        print('***** Failed: %s' % e)

    sys.modules[theModule] = sys.modules[fullModuleName]
    del sys.modules[fullModuleName]
 
#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
