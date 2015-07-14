#! /usr/bin/env python
# "Time-stamp: <04/08/2015  4:35:42 AM rsg>"
'''
tsWxPythonColor256DataBase.py - Refactored xterm-256color data
base portion of tsWxGraphicalTextUserInterface for name keys
and code keys.
'''
#################################################################
#
# File: tsWxPythonColor16DataBase.py
#
# Purpose:
#
#     tsWxPythonColor256DataBase.py - Refactored xterm-256color
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
#     Provide xterm256colorNameFromCode dictionary.
#
#     Provide xterm256colorCodeFromName dictionary.
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

__title__     = 'tsWxPythonColor256DataBase'
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

##from tsWxGTUI_Py2x.tsLibGUI import tsWxPythonColorNames

##from tsWxPythonColorNames import *

from tsWxGTUI_Py2x.tsLibGUI.tsWxPythonColorNames import *

#---------------------------------------------------------------------------

xterm256ColorNameFromCode = {
    'name': 'xterm256ColorNameFromCode',
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
    70: COLOR_YELLOW_GREEN,
    71: COLOR_ALICE_BLUE,
    72: COLOR_ANTIQUE_WHITE,
    73: COLOR_AZURE,
    74: COLOR_BEIGE,
    75: COLOR_BISQUE,
    76: COLOR_BLANCHED_ALMOND,
    77: COLOR_BURLYWOOD,
    78: COLOR_CHARTREUSE,
    79: COLOR_CHOCOLATE,
    80: COLOR_CORNSILK,
    81: COLOR_CRIMSON,
    82: COLOR_DARK_BLUE,
    83: COLOR_DARK_CYAN,
    84: COLOR_DARK_GOLDENROD,
    85: COLOR_DARK_KHAKI,
    86: COLOR_DARK_MAGENTA,
    87: COLOR_DARK_ORANGE,
    88: COLOR_DARK_RED,
    89: COLOR_DARK_SALMON,
    90: COLOR_DARK_SEA_GREEN,
    91: COLOR_DARK_VIOLET,
    92: COLOR_DEEP_PINK,
    93: COLOR_DEEP_SKY_BLUE,
    94: COLOR_DODGER_BLUE,
    95: COLOR_FLORAL_WHITE,
    96: COLOR_GAINSBORO,
    97: COLOR_GHOST_WHITE,
    98: COLOR_HONEYDEW,
    99: COLOR_HOT_PINK,
    100: COLOR_INDIGO,
    101: COLOR_IVORY,
    102: COLOR_LAVENDER,
    103: COLOR_LAVENDER_BLUSH,
    104: COLOR_LAWN_GREEN,
    105: COLOR_LEMON_CHIFFON,
    106: COLOR_LIGHT_CORAL,
    107: COLOR_LIGHT_CYAN,
    108: COLOR_LIGHT_GOLDENROD_YELLOW,
    109: COLOR_LIGHT_GREEN,
    110: COLOR_LIGHT_PINK,
    111: COLOR_LIGHT_SALMON,
    112: COLOR_LIGHT_SEA_GREEN,
    113: COLOR_LIGHT_SKY_BLUE,
    114: COLOR_LIGHT_SLATE_GRAY,
    115: COLOR_LIGHT_YELLOW,
    116: COLOR_LINEN,
    117: COLOR_MEDIUM_PURPLE,
    118: COLOR_MINT_CREAM,
    119: COLOR_MISTY_ROSE,
    120: COLOR_MOCCASIN,
    121: COLOR_NAVAJO_WHITE,
    122: COLOR_OLD_LACE,
    123: COLOR_OLIVE_DRAB,
    124: COLOR_PALE_GOLDENROD,
    125: COLOR_PALE_TURQUOISE,
    126: COLOR_PALE_VIOLET_RED,
    127: COLOR_PAPAYA_WHIP,
    128: COLOR_PEACH_PUFF,
    129: COLOR_PERU,
    130: COLOR_POWDER_BLUE,
    131: COLOR_ROSY_BROWN,
    132: COLOR_ROYAL_BLUE,
    133: COLOR_SADDLE_BROWN,
    134: COLOR_SANDY_BROWN,
    135: COLOR_SEA_SHELL,
    136: COLOR_SLATE_GRAY,
    137: COLOR_SNOW,
    138: COLOR_TOMATO,
    139: COLOR_WHITE_SMOKE
    }

#---------------------------------------------------------------------------

xterm256ColorCodeFromName = {}
for colorCode in xterm256ColorNameFromCode.keys():
    if colorCode == 'name':
        xterm256ColorCodeFromName['name'] = 'xterm256ColorCodeFromName'
    else:
        colorName = xterm256ColorNameFromCode[colorCode]
        xterm256ColorCodeFromName[colorName] = colorCode
