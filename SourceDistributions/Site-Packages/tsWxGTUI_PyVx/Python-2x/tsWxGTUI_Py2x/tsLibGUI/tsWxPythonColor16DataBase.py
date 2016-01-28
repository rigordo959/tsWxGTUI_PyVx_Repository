#! /usr/bin/env python
# "Time-stamp: <04/08/2015  4:34:51 AM rsg>"
'''
tsWxPythonColor16DataBase.py - Refactored xterm-16color data
base portion of tsWxGraphicalTextUserInterface for name keys
and code keys.
'''
#################################################################
#
# File: tsWxPythonColor16DataBase.py
#
# Purpose:
#
#     tsWxPythonColor16DataBase.py - Refactored xterm-16color
#     data base portion of tsWxGraphicalTextUserInterface for
#     name keys and code keys.
#
# Usage (example):
#
#     ## Import Module
#     from tsWxPythonColor16DataBase import *
#
# Requirements:
#
#     Provide xterm16ColorNameFromCode dictionary.
#
#     Provide xterm16ColorCodeFromName dictionary.
#
#     Provide xterm16BuiltinColorNameFromCode dictionary.
#
#     Provide xterm16BuiltinColorCodeFromName dictionary.
#
# Capabilities:
#
#
# Limitations:
#
#
# Notes:
#
#
# Classes:
#
#
# Methods:
#
#
# Modifications:
#
#    2014/07/03 rsg Added the following modules:
#                       tsWxPythonColor16DataBase
#                       tsWxPythonColor16SubstitutionMap
#                       tsWxPythonColor256DataBase
#                       tsWxPythonColor88DataBase
#                       tsWxPythonColor8DataBase
#                       tsWxPythonColor8SubstitutionMap
#                       tsWxPythonColorDataBaseRGB
#                       tsWxPythonColorNames
#                       tsWxPythonColorRGBNames
#                       tsWxPythonColorRGBValues
#                       tsWxPythonMonochromeDataBase
#                       tsWxPythonPrivateLogger
#
#    2014/07/03 rsg Added control switch in effort to resolve
#                   built-in color palette issue. The control
#                   switch ReassignBuiltinColorCodeslogic
#                   changes the color code associated with
#                   the color names so that the appropriate
#                   Red-Green-Blue component values is applied.
#
# ToDo:
#
#
#################################################################

__title__     = 'tsWxPythonColor16DataBase'
__version__   = '1.0.1'
__date__      = '07/04/2014'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2014 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = '\n\n  Credits: ' + \
                '\n\n\t  tsLibGUI Import & Application Launch Features: ' + \
                '\n\t  Copyright (c) 2007-2009 Frederick A. Kier.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\n\t  Python Curses Module API & ' + \
                'Run Time Library Features:' + \
                '\n\t  Copyright (c) 2001-2013 ' +\
                'Python Software Foundation.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  PSF License Agreement for Python 2.7.3 & 3.3.0' + \
                '\n\n\t  wxWidgets (formerly wxWindows) & ' + \
                'wxPython API Features:' + \
                '\n\t  Copyright (c) 1992-2008 Julian Smart, ' + \
                'Robert Roebling,' + \
                '\n\t\t\tVadim Zeitlin and other members of the ' + \
                '\n\t\t\twxWidgets team.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  wxWindows Library License' + \
                '\n\n\t  nCurses character-mode Terminal Control Library' + \
                '\n\t\t\tfor Unix-like systems and API Features:' + \
                '\n\t  Copyright (c) 1998-2004, 2006 Free Software ' + \
                '\n\t\t\tFoundation, Inc.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  nCurses README,v 1.23 2006/04/22'

__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Author(s): %s' % __authors__
__line3__ = '%s' % __copyright__

if len( __credits__) == 0:
    __line4__ = '%s' % __license__
else:
    __line4__ = '%s%s' % (__license__, __credits__)

__header__ = '\n\n%s\n\n  %s\n  %s\n  %s\n' % (__line1__,
                                               __line2__,
                                               __line3__,
                                               __line4__)

mainTitleVersionDate = __line1__

#---------------------------------------------------------------------------

##from tsWxGTUI_Py2x.tsLibGUI import tsWxPythonColorNames

##from tsWxPythonColorNames import *

from tsWxGTUI_Py2x.tsLibGUI.tsWxPythonColorNames import *

#---------------------------------------------------------------------------

##xterm16ColorNameFromCode = {
##    'name': 'xterm16ColorNameFromCode',
##    0: COLOR_BLACK,
##    1: COLOR_RED,
##    2: COLOR_GREEN,
##    3: COLOR_YELLOW,
##    4: COLOR_BLUE,
##    5: COLOR_MAGENTA,
##    6: COLOR_CYAN,
##    7: COLOR_WHITE,
##    8: COLOR_MAROON,
##    9: COLOR_OLIVE,
##    10: COLOR_NAVY,
##    11: COLOR_PURPLE,
##    12: COLOR_TEAL,
##    13: COLOR_SILVER,
##    14: COLOR_GRAY,
##    15: COLOR_LIME_GREEN
##    }

xterm16ColorNameFromCode = {
    'name': 'xterm16ColorNameFromCode',
    0: COLOR_BLACK,
    1: COLOR_RED,
    2: COLOR_GREEN,
    3: COLOR_YELLOW,
    4: COLOR_BLUE,
    5: COLOR_MAGENTA,
    6: COLOR_CYAN,
    7: COLOR_WHITE,
    8: COLOR_GRAY,
    9: COLOR_MAROON,
    10: COLOR_LIME_GREEN,
    11: COLOR_OLIVE,
    12: COLOR_NAVY,
    13: COLOR_PURPLE,
    14: COLOR_TEAL,
    15: COLOR_SILVER
    }

#---------------------------------------------------------------------------

xterm16ColorCodeFromName = {}
for colorCode in xterm16ColorNameFromCode.keys():
    if colorCode == 'name':
        xterm16ColorCodeFromName['name'] = 'xterm16ColorCodeFromName'
    else:
        colorName = xterm16ColorNameFromCode[colorCode]
        xterm16ColorCodeFromName[colorName] = colorCode

#---------------------------------------------------------------------------

ReassignBuiltinColorCodes = True

if ReassignBuiltinColorCodes:

    xterm16BuiltinColorNameFromCode = {
        'name': 'xterm16BuiltinColorNameFromCode',
        0: COLOR_BLACK,
        1: COLOR_MAROON,
        2: COLOR_LIME_GREEN,
        3: COLOR_OLIVE,
        4: COLOR_NAVY,
        5: COLOR_PURPLE,
        6: COLOR_TEAL,
        7: COLOR_SILVER,
        8: COLOR_GRAY,
        9: COLOR_RED,
        10: COLOR_GREEN,
        11: COLOR_YELLOW,
        12: COLOR_BLUE,
        13: COLOR_MAGENTA,
        14: COLOR_CYAN,
        15: COLOR_WHITE
        }

else:

    xterm16BuiltinColorNameFromCode = {
        'name': 'xterm16BuiltinColorNameFromCode',
        0: COLOR_BLACK,
        1: COLOR_RED,
        2: COLOR_GREEN,
        3: COLOR_YELLOW,
        4: COLOR_BLUE,
        5: COLOR_MAGENTA,
        6: COLOR_CYAN,
        7: COLOR_WHITE,
        8: COLOR_GRAY,
        9: COLOR_MAROON,
        10: COLOR_LIME_GREEN,
        11: COLOR_OLIVE,
        12: COLOR_NAVY,
        13: COLOR_PURPLE,
        14: COLOR_TEAL,
        15: COLOR_SILVER
        }

#---------------------------------------------------------------------------

xterm16BuiltinColorCodeFromName = {}
for colorCode in xterm16BuiltinColorNameFromCode.keys():
    if colorCode == 'name':
        xterm16ColorCodeFromName['name'] = 'xterm16BuiltinColorCodeFromName'
    else:
        colorName = xterm16BuiltinColorNameFromCode[colorCode]
        xterm16BuiltinColorCodeFromName[colorName] = colorCode
