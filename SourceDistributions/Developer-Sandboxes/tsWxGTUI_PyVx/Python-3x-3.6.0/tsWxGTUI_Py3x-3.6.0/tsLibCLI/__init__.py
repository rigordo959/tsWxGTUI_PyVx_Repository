#! /usr/bin/env python
# "Time-stamp: <03/22/2015 12:29:52 AM rsg>"
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
#    import tsLibCLI
#
# Requirements:
#
#    Python 3.0 or later.
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
#       named 'tsLibCLI'.
#
#    3. It is recommended that the name of each package module
#       that contains two or more files or sub-directories use the
#       suffix 'Pkg'.
#
#    4. Each lower level module must be imported in a sequence
#       that permits non-recursive resolution of import dependency.
#       For example, "tsExceptions" must have been imported before
#       "tsReportUtilities". To enable the non-recursive resolution
#       of import dependency, it is required that any and all import
#       statements be placed at the beginning and outer most scope
#       of each lower level module. Adherance to this convention
#       ensures that imported module names are placed in the importing
#       module's global symbol table.
#
# Notes:
#
#    ------------------------------------------------------------
#
#    Directory Structure (example):
#
#      tsLibCLI/ # Package for imported library building blocks
#                # and associated non-imported test applications
#
#        __init__.py
#          |
#        tsApplicationPkg
#          |   |
#          |   +-- src (Subpackage for imported building blocks)
#          |   |     |
#          |   |     +-- __init__.py
#          |   |     |
#          |   |     +-- tsApplication.py
#          |   |
#          |   +-- test (Container for non-imported test applications)
#          |         |
#          |         +-- test_tsApplication.py
#          |
#        tsCxGlobalsPkg
#          |
#        tsExceptionPkg
#          |
#        tsPlatformRunTimeEnvironmentPkg
#          |
#        tsReportUtilityPkg
#
#    Deprecated or skeleton modules are preserved only as "tarballs".
#
#    ------------------------------------------------------------
#
#    TeamSTARS "tsWxGTUI_Py3x" Toolkit (Dynamic Import)
#
#       Source Code, Tests, Tools and Utilities for users of
#       the third generation language, Python 3.0.0-3.4.2.
#
#       This version uses a dynamic import mechanism, suitable
#       for nested multi-level packages, in which each appli-
#       cation and building block module:
#
#       a) imports required library packages simply by name.
#          Examples:
#
#             import tsLibCLI
#             import tsLibGUI
#
#       b) imports required building block modules, and defines
#          optional aliases, simply by name. Examples:
#
#             import tsCxGlobals
#             import tsExceptions as tse
#             import tsWx as wx
#             from tsReportUtilities import TsReportUtilities as tsrpu
#
#       c) Library package "__init__.py" modules dynamically
#          construct any associated full paths.
#
#    ------------------------------------------------------------
#
#    TeamSTARS "tsWxGTUI_PyX3" Toolkit (Static Import)
#
#       Source Code, Tests, Tools and Utilities for users of
#       the third generation language, Python 3.0.0-3.4.2.
#
#       This version uses a static import mechanism, suitable
#       for a Python Global Module Index-style single-level of
#       packages, in which each application and building block
#       module:
#
#       a) imports required library packages simply by name.
#
#          examples:
#
#             import tsLibCLI
#             import tsLibGUI
#
#       b) imports required building block modules, and defines
#          optional aliases, explicitly by path.
#
#          examples:
#
#             from tsLibCLI import tsCxGlobals
#             from tsLibCLI import tsExceptions as tse
#             from tsLibGUI import tsWx
#             from tsLibCLI import tsReportUtilities
#
#             tsrpu = tsReportUtilities.TsReportUtilities()
#
#       c) Library package "__init__.py" modules are empty.
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
#    2013/03/01 rsg Added import tsLibCLI.
#
#    2013/05/25 rsg Added, renamed and modified packages from
#                   tsLibCLI inorder to add their functionality
#                   but without creating dependancy on tsLibCLI.
#
#    2013/05/26 rsg Added import tsOperatorSettingsParser.
#
#    2013/08/17 rsg Renamed directory from tsOptionParserPkg to
#                   tsMultiLevelOptionParserAdded.
#
#    2013/08/17 rsg Added import tsLogging.
#
#    2013/10/22 rsg Added import tsCxGlobalsPkg.
#
#    2014/02/06 rsg Commented-out the following unimplemented
#                   modules:
#                   'tsLoggingPkg',
#                   'tsMultiLevelOptionParserPkg',
#
#    2014/02/06 rsg Commented-out the following deprecated
#                   modules:
#                   'tsCommandLineParserPkg' (superceded by
#                   'tsOperatorSettingsParser'),
#
#    2014/02/06 rsg Commented-out the following third-party
#                   modules (prototypes were never used):
#                   'tsBuzhugPkg',
#                   'tsConfigObjectPkg',
#                   'tsDataBasePkg',
#                   'tsDecoratorPkg',
#                   'tsThreadPoolPkg'
#
#    2015/03/20 rsg Added import tsGistGetTerminalSizePkg.
#
# ToDo:
#
#    None
#
#################################################################

__title__     = '__init__'
__version__   = '2.8.0'
__date__      = '03/20/2015'
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

#---------------------------------------------------------------------------

import imp
import os.path
import sys

#---------------------------------------------------------------------------

importRoot = 'tsLibCLI'

if sys.version < '3':
      package_dir = {'src': 'src'}
      test_dir = {'test': 'test'}
else:
      package_dir = {'src': 'src'}
      test_dir = {'test': 'test'}

theContainer = package_dir['src']

__myAll__ = [
    # Sub modules. Troubleshooting will be required before uncommenting.
    'tsGistGetTerminalSizePkg',        # Imports none of the following
    'tsCxGlobalsPkg',                  # Imports none of the following
    # 'tsBuzhugPkg',                     # Imports none of the following
    'tsCommandLineInterfacePkg',       # Imports none of the following
    # 'tsConfigObjectPkg',               # Imports none of the following
    # 'tsDataBasePkg',                   # Imports none of the following
    # 'tsDecoratorPkg',                  # Imports none of the following
    'tsExceptionPkg',                  # Imports none of the following

    'tsReportUtilityPkg',              # Imports tsExceptions

    # 'tsLoggingPkg',                    # Imports tsExceptions,
    #                                    # tsReportUtilities

    'tsLoggerPkg',                     # Imports tsExceptions,
                                       # tsReportUtilities

    'tsDoubleLinkedListPkg',           # Imports none of the following
    'tsPlatformRunTimeEnvironmentPkg', # Imports tsExceptions,
    #                                   # tsReportUtilities,
    #                                   # tsLogger, tsApplication

    # 'tsCommandLineParserPkg',          # Imports tsExceptions,
    #                                    # tsLogger

    'tsApplicationPkg',                # Imports tsExceptions,
                                       # tsLogger

    'tsCommandLineEnvPkg',             # Imports tsExceptions,
                                       # tsReportUtilities,
                                       # tsLogger, tsApplication

    # 'tsMultiLevelOptionParserPkg',     # Imports tsExceptions
    #                                    # tsLogger,
    #                                    # tsApplicationPkg,
    #                                    # tsCommandLineEnvPkg

    'tsOperatorSettingsParserPkg',     # Imports tsExceptions,
                                       # tsLogger,
                                       # tsApplicationPkg,
                                       # tsCommandLineEnvPkg

    'tsSysCommandsPkg'                 # Imports tsExceptions,
                                       # tsReportUtilities,
                                       # tsLogger, tsApplication

    # 'tsThreadPoolPkg'                  # Imports tsExceptions,
                                       # tsReportUtilities,
                                       # tsLogger, tsApplication

    # 'tsWxPkg'                          # Imports any or all of the above
    ]

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

#--------------------------------------------------------------------------

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
    # Cannot delete tsLibCLI entry; leave dot at end of startswith string.
    if k.startswith('%s.' % theName):
        if Debug_CLI_Launch:
            print('    Deleting %s' % k)
        del sys.modules[k]

if Debug_CLI_Launch:
    print('  End Cleanup %s' % fullModuleName)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)