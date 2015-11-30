#! /usr/bin/env python
# "Time-stamp: <03/17/2015  7:32:12 AM rsg>"
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
#    import tsWxGraphicalUserInterfacePkg
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
#       named 'tsLibGUI' or 'library'.
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
#    2011/11/27 rsg Added StaticBox.
#
#    2011/12/13 rsg Added tsWxCommandLineEnv library module.
#
#    2012/01/30 rsg Added tsWxScrolled and tsWxScroolledWindow
#                   library modules.
#
#    2012/02/02 rsg Added tsWxScrollBarButton library module.
#
#    2012/02/21 rsg Added tsWxScrollBarGauge library module.
#
#    2012/02/21 rsg Added tsWxScrolledText library module.
#
#    2012/07/03 rsg Added tsWxStaticLine library module.
#
#    2012/07/05 rsg Added tsWxPasswordEntryDialog and
#                   tsWxTextEntryDialog library modules.
#
#    2012/08/10 rsg Added tsWxTextEditBox library module.
#
#    2012/10/07 rsg Added tsWxNonLinkedList library module.
#
#    2013/07/06 rsg Added FrameButton and DialogButton.
#
#    2013/09/16 rsg Revised __myAll__ to reflect dependencies
#                   as identified with Python-3x.
#
#    2014/07/03 rsg Added the following modules:
#			tsWxPythonColor16DataBase
#			tsWxPythonColor16SubstitutionMap
#			tsWxPythonColor256DataBase
#			tsWxPythonColor88DataBase
#			tsWxPythonColor8DataBase
#			tsWxPythonColor8SubstitutionMap
#			tsWxPythonColorDataBaseRGB
#			tsWxPythonColorNames
#			tsWxPythonColorRGBNames
#			tsWxPythonColorRGBValues
#			tsWxPythonMonochromeDataBase
#			tsWxPythonPrivateLogger
#
# ToDo:
#
#    None
#<
#################################################################

__title__     = '__init__'
__version__   = '2.4.0'
__date__      = '07/03/2014'
__authors__   = 'Frederick A. Kier & Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2014 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibGUI Import & Application Launch Features: ' + \
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

tsImportRoot = 'tsLibGUI'
libraryImportRoot = 'library'
theName = 'tsWxPkg'

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
    'tsWxDoubleLinkedList',
    'tsWxNonLinkedList',
    'tsWxGlobals',
    'tsWxPoint',
    'tsWxSize',
    'tsWxRect',
    'tsWxPythonColorRGBNames',
    'tsWxPythonColorRGBValues',
    'tsWxPythonColorNames',
    'tsWxPythonColor16DataBase',
    'tsWxPythonColor16SubstitutionMap',
    'tsWxPythonColor256DataBase',
    'tsWxPythonColor88DataBase',
    'tsWxPythonColor8DataBase',
    'tsWxPythonColor8SubstitutionMap',
    'tsWxPythonColorDataBaseRGB',
    'tsWxPythonMonochromeDataBase',
    'tsWxPythonPrivateLogger',

    'tsWxCursesKeyCodesDataBase',
    'tsWxCursesMouseButtonCodesDataBase',
    'tsWxGraphicalTextUserInterface',

    'tsWxDebugHandlers',
    'tsWxDisplay',
    'tsWxObject',

    'tsWxPyEventBinder',
    'tsWxEvent',
    'tsWxEventDaemon',
    'tsWxEventQueueEntry',
    'tsWxEventTableEntry',
    'tsWxEventLoop',
    'tsWxEvtHandler',

    'tsWxKeyboardState',
    'tsWxMouseState',

    'tsWxSystemSettings',

    'tsWxWindowCurses',
    'tsWxWindow',
    'tsWxTopLevelWindow',
    'tsWxColor',
    'tsWxColorDatabase',
    'tsWxCursor',
    'tsWxAcceleratorEntry',
    'tsWxKeyEvent',
    'tsWxMouseEvent',
    'tsWxShowEvent',
    'tsWxControl',
    'tsWxStaticBox',
    'tsWxStaticLine',
    'tsWxButton',
    'tsWxFrameButton',
    'tsWxDialogButton',
    'tsWxTextCtrl',
    'tsWxStaticText',
    'tsWxStatusBar',
    'tsWxAcceleratorTable',
    'tsWxFrame',
    'tsWxTaskBar',
    'tsWxDialog',
    'tsWxScreen',
    'tsWxPyApp',
    'tsWxPyOnDemandOutputWindow',
    'tsWxApp',
    'tsWxPySimpleApp',
    # 'tsWxCommandLineEnv',
    'tsWxMultiFrameEnv',
    'tsWxSizerFlags',
    'tsWxSizerSpacer',
    'tsWxSizerItemList',
    'tsWxSizerItem',
    'tsWxSizer',
    'tsWxPySizer',
    'tsWxBoxSizer',
    'tsWxCaret',
    'tsWxCheckBox',
    'tsWxItemContainer',
    'tsWxControlWithItems',
    'tsWxChoice',
    'tsWxEventLoopActivator',
    'tsWxGridSizer',
    'tsWxFlexGridSizer',
    'tsWxFocusEvent',
    'tsWxGauge',
    'tsWxGridBagSizer',
    'tsWxKeyEvent',
    # 'tsWxLayoutAlgorithm',
    'tsWxListBox',
    'tsWxMenu',
    'tsWxMenuBar',
    'tsWxMouseEvent',
    'tsWxPanel',
    'tsWxRadioButton',
    'tsWxRadioBox',
    'tsWxScrolledText',
    'tsWxScrollBarButton',
    'tsWxScrollBarGauge',
    'tsWxScrollBar',
    'tsWxScrolled',
    'tsWxScrolledWindow',
    'tsWxSlider',
    'tsWxSplashScreen',
    'tsWxStaticBoxSizer',
    'tsWxTextEditBox',
    'tsWxTextEntryDialog',
    'tsWxPasswordEntryDialog',
    'tsWxTimer',
    'tsWxToggleButton',
    'tsWxValidator',
    #
    'tsWx'
]

if Debug_CLI_Launch:
    print('      init in %s' % theName)

importDictionary = {}
importCount = -1

__theLeftovers__ = []

for theModule in __myAll__:

    fullModuleName = ''
    for item in path:
        fullModuleName += '%s.' % item
    fullModuleName += theModule

    if Debug_CLI_Launch:
        print('        Importing %s' % fullModuleName)
    try:
##        __import__(fullModuleName)
####        importlib.import_module(fullModuleName)
        __import__(fullModuleName)
        importCount += 1
        importDictionary[theModule] = importCount
        if Debug_CLI_Launch:
            print('\t***** Imported: %s' % theModule)

        sys.modules[theModule] = sys.modules[fullModuleName]
        del sys.modules[fullModuleName]

    except ImportError as e:
        if Debug_CLI_Launch:
            print('\t***** ImportError: %s' % e)
        __theLeftovers__ += [theModule]

    except Exception as e:
        if Debug_CLI_Launch:
            print('\t***** Exception: %s' % e)
        __theLeftovers__ += [theModule]

    if Debug_CLI_Launch:
        print('\t***** importDictionary: %s' % importDictionary)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
