#! /usr/bin/env python
# "Time-stamp: <04/08/2015  4:35:59 AM rsg>"
'''
tsWxPythonColor88DataBase.py - Refactored xterm-88color data
base portion of tsWxGraphicalTextUserInterface for name keys
and code keys.
'''
#################################################################
#
# File: tsWxPythonColor88DataBase.py
#
# Purpose:
#
#     tsWxPythonColor88DataBase.py - Refactored xterm-88color
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
#     Provide xterm88colorNameFromCode dictionary.
#
#     Provide xterm88colorCodeFromName dictionary.
#
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
#
#################################################################

__title__     = 'tsWxPythonColor88DataBase'
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

#---------------------------------------------------------------------------

##from tsWxGTUI_Py3x.tsLibGUI import tsWxPythonColorNames

##from tsWxPythonColorNames import *

from tsWxGTUI_Py3x.tsLibGUI.tsWxPythonColorNames import *

#---------------------------------------------------------------------------

xterm88ColorNameFromCode = {
    'name': 'xterm88ColorNameFromCode',
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
    15: COLOR_SILVER,
    16: COLOR_AQUAMARINE,
    17: COLOR_BLUE_VIOLET,
    18: COLOR_BROWN,
    19: COLOR_CADET_BLUE,
    20: COLOR_CORAL,
    21: COLOR_CORNFLOWER_BLUE,
    22: COLOR_DARK_GRAY,
    23: COLOR_DARK_GREEN,
    24: COLOR_DARK_OLIVE_GREEN,
    25: COLOR_DARK_ORCHID,
    26: COLOR_DARK_SLATE_BLUE,
    27: COLOR_DARK_SLATE_GRAY,
    28: COLOR_DARK_TURQUOISE,
    29: COLOR_DIM_GRAY,
    30: COLOR_FIREBRICK,
    31: COLOR_FOREST_GREEN,
    32: COLOR_GOLD,
    33: COLOR_GOLDENROD,
    34: COLOR_GREEN_YELLOW,
    35: COLOR_INDIAN_RED,
    36: COLOR_KHAKI,
    37: COLOR_LIGHT_BLUE,
    38: COLOR_LIGHT_GRAY,
    39: COLOR_LIGHT_STEEL_BLUE,
    40: COLOR_MEDIUM_AQUAMARINE,
    41: COLOR_MEDIUM_BLUE,
    42: COLOR_MEDIUM_FOREST_GREEN,
    43: COLOR_MEDIUM_GOLDENROD,
    44: COLOR_MEDIUM_ORCHID,
    45: COLOR_MEDIUM_SEA_GREEN,
    46: COLOR_MEDIUM_SLATE_BLUE,
    47: COLOR_MEDIUM_SPRING_GREEN,
    48: COLOR_MEDIUM_TURQUOISE,
    49: COLOR_MEDIUM_VIOLET_RED,
    50: COLOR_MIDNIGHT_BLUE,
    51: COLOR_ORANGE,
    52: COLOR_ORANGE_RED,
    53: COLOR_ORCHID,
    54: COLOR_PALE_GREEN,
    55: COLOR_PINK,
    56: COLOR_PLUM,
    57: COLOR_SALMON,
    58: COLOR_SEA_GREEN,
    59: COLOR_SIENNA,
    60: COLOR_SKY_BLUE,
    61: COLOR_SLATE_BLUE,
    62: COLOR_SPRING_GREEN,
    63: COLOR_STEEL_BLUE,
    64: COLOR_TAN,
    65: COLOR_THISTLE,
    66: COLOR_TURQUOISE,
    67: COLOR_VIOLET,
    68: COLOR_VIOLET_RED,
    69: COLOR_WHEAT,
    70: COLOR_YELLOW_GREEN
    }

#---------------------------------------------------------------------------

xterm88ColorCodeFromName = {}
for colorCode in xterm88ColorNameFromCode.keys():
    if colorCode == 'name':
        xterm88ColorCodeFromName['name'] = 'xterm88ColorCodeFromName'
    else:
        colorName = xterm88ColorNameFromCode[colorCode]
        xterm88ColorCodeFromName[colorName] = colorCode
