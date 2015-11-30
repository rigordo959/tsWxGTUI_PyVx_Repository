#! /usr/bin/env python
# "Time-stamp: <07/26/2013  7:37:59 PM rsg>"
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
#    import tsStripCommentsPkg
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
#       named 'tsToolsCLI' or 'library'.
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
#    N/A
#
# ToDo:
#
#    None
#
#################################################################

__title__     = '__init__'
__version__   = '1.0.0'
__date__      = '07/26/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2013 ' + \
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

DEBUG = True

import imp
import sys
import os

#---------------------------------------------------------------------------

tsImportRoot = 'tsToolsCLI'
libraryImportRoot = 'library'
theName = 'tsStripCommentsPkg'

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
    'tsStripSettingsParser',
    'tsStripComments'
    ]

if DEBUG:

    print('      init in %s' % theName)

for theModule in __myAll__:

    fullModuleName = ''
    for item in path:
        fullModuleName += '%s.' % item
    fullModuleName += theModule

    if DEBUG:
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
