#! /usr/bin/env python
# "Time-stamp: <07/04/2014  1:23:23 PM rsg>"
'''
tsWxPythonColor8DataBase.py - Refactored xterm (8-color) data
base portion of tsWxGraphicalTextUserInterface for name keys
and code keys.
'''
#################################################################
#
# File: tsWxPythonColor8DataBase.py
#
# Purpose:
#
#     tsWxPythonColor8DataBase.py - Refactored xterm (8-color)
#     data base portion of tsWxGraphicalTextUserInterface for
#     name keys and code keys.
#
# Usage (example):
#
#     ## Import Module
#     from junk import *
#
# Requirements:
#
#     Provide xterm8ColorNameFromCode dictionary.
#
#     Provide xterm8ColorCodeFromName dictionary.
#
#     Provide xterm8BuiltinColorNameFromCode dictionary.
#
#     Provide xterm8BuiltinColorCodeFromName dictionary.
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
# ToDo:
#
#
#################################################################

__title__     = 'tsWxPythonColor8DataBase'
__version__   = '1.0.0'
__date__      = '07/03/2014'
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

from tsWxPythonColorNames import *

###---------------------------------------------------------------------------

### Set of color names and numbers
### which curses guarantees to recognize.
##curses8ColorCodeFromName = {
##    'name': 'curses8ColorCodeFromName',
##    COLOR_BLACK: 0,
##    COLOR_RED: 1,
##    COLOR_GREEN: 2,
##    COLOR_YELLOW: 3,
##    COLOR_BLUE: 4,
##    COLOR_MAGENTA: 5,
##    COLOR_CYAN: 6,
##    COLOR_WHITE: 7
##    }

###---------------------------------------------------------------------------

### Set of color numbers and names
### which curses guarantees to recognize.
##curses8ColorNameFromCode = {
##    'name': 'curses8ColorNameFromCode',
##    curses.COLOR_BLACK: COLOR_BLACK,
##    curses.COLOR_RED: COLOR_RED,
##    curses.COLOR_GREEN: COLOR_GREEN,
##    curses.COLOR_YELLOW: COLOR_YELLOW,
##    curses.COLOR_BLUE: COLOR_BLUE,
##    curses.COLOR_MAGENTA: COLOR_MAGENTA,
##    curses.COLOR_CYAN: COLOR_CYAN,
##    curses.COLOR_WHITE: COLOR_WHITE
##    }

###---------------------------------------------------------------------------

### Set of color numbers which wxPython emulator will recognize.
##COLOR8_NUMBER_BLACK = curses.COLOR_BLACK      # 0
##COLOR8_NUMBER_RED = curses.COLOR_RED          # 1
##COLOR8_NUMBER_GREEN = curses.COLOR_GREEN      # 2
##COLOR8_NUMBER_YELLOW = curses.COLOR_YELLOW    # 3
##COLOR8_NUMBER_BLUE = curses.COLOR_BLUE        # 4
##COLOR8_NUMBER_MAGENTA = curses.COLOR_MAGENTA  # 5
##COLOR8_NUMBER_CYAN = curses.COLOR_CYAN        # 6
##COLOR8_NUMBER_WHITE = curses.COLOR_WHITE      # 7

#---------------------------------------------------------------------------

xterm8ColorNameFromCode = {
    'name': 'xterm8ColorNameFromCode',
    0: COLOR_BLACK,
    1: COLOR_RED,
    2: COLOR_GREEN,
    3: COLOR_YELLOW,
    4: COLOR_BLUE,
    5: COLOR_MAGENTA,
    6: COLOR_CYAN,
    7: COLOR_WHITE
    }

#---------------------------------------------------------------------------

xterm8ColorCodeFromName = {}
for colorCode in xterm8ColorNameFromCode.keys():
    if colorCode == 'name':
        xterm8ColorCodeFromName['name'] = 'xterm8ColorCodeFromName'
    else:
        colorName = xterm8ColorNameFromCode[colorCode]
        xterm8ColorCodeFromName[colorName] = colorCode

#---------------------------------------------------------------------------

xterm8BuiltinColorNameFromCode = {
    'name': 'xterm8BuiltinColorNameFromCode',
    0: COLOR_BLACK,
    1: COLOR_RED,
    2: COLOR_GREEN,
    3: COLOR_YELLOW,
    4: COLOR_BLUE,
    5: COLOR_MAGENTA,
    6: COLOR_CYAN,
    7: COLOR_WHITE
    }

#---------------------------------------------------------------------------

xterm8BuiltinColorCodeFromName = {}
for colorCode in xterm8BuiltinColorNameFromCode.keys():
    if colorCode == 'name':
        xterm8BuiltinColorCodeFromName[
            'name'] = 'xterm8BuiltinColorCodeFromName'
    else:
        colorName = xterm8BuiltinColorNameFromCode[colorCode]
        xterm8BuiltinColorCodeFromName[colorName] = colorCode
