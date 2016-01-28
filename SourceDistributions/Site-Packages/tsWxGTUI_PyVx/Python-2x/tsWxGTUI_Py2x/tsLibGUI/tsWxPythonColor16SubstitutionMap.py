#! /usr/bin/env python
# "Time-stamp: <04/08/2015  4:35:27 AM rsg>"
'''
tsWxPythonColor16SubstitutionMap.py - Refactored xterm-16color
substitution data base portion of tsWxGraphicalTextUserInterface
which maps wxPython color names to the available xterm-16color
names.
'''
#################################################################
#
# File: tsWxPythonColor16SubstitutionMap.py
#
# Purpose:
#
#     tsWxPythonColor16SubstitutionMap.py - Refactored xterm-
#     16color substitution data base portion of
#     tsWxGraphicalTextUserInterface which maps wxPython color
#     names to the available xterm-16color names.
#
# Usage (example):
#
#     ## Import Module
#     from tsWxPythonColor16SubstitutionMap import *
#
# Requirements:
#
#     Provide color16SubstitutionMap dictionary.
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

__title__     = 'tsWxPythonColor16SubstitutionMap'
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

# Dictionary mapping the set of wxPython colors, guaranteed to be recognized,
# into the standard set of 16 available curses colors.
#
# Note: This tabulation will not apply when the terminal type is
#       xterm-8color. Needless to say, it will not apply when the terminal
#       type is ansi, vt100 or xterm.
Color16SubstitutionMap = {
    'name': 'Color16SubstitutionMap',
    COLOR_AQUAMARINE: COLOR_CYAN,
    COLOR_BLACK: COLOR_BLACK,
    COLOR_BLUE: COLOR_BLUE,
    COLOR_BLUE_VIOLET: COLOR_BLUE,
    COLOR_BROWN: COLOR_MAROON,
    COLOR_CADET_BLUE: COLOR_BLUE,
    COLOR_CORAL: COLOR_RED,
    COLOR_CORNFLOWER_BLUE: COLOR_BLUE,
    COLOR_CYAN: COLOR_CYAN,
    COLOR_DARK_GRAY: COLOR_BLACK,
    COLOR_DARK_GREEN: COLOR_GREEN,
    COLOR_DARK_OLIVE_GREEN: COLOR_GREEN,
    COLOR_DARK_ORCHID: COLOR_MAGENTA,
    COLOR_DARK_SLATE_BLUE: COLOR_BLUE,
    COLOR_DARK_SLATE_GRAY: COLOR_BLACK,
    COLOR_DARK_TURQUOISE: COLOR_CYAN,
    COLOR_DIM_GRAY: COLOR_GRAY,
    COLOR_FIREBRICK: COLOR_RED,
    COLOR_FOREST_GREEN: COLOR_GREEN,
    COLOR_GOLD: COLOR_YELLOW,
    COLOR_GOLDENROD: COLOR_YELLOW,
    COLOR_GRAY: COLOR_GRAY,
    COLOR_GREEN: COLOR_GREEN,
    COLOR_GREEN_YELLOW: COLOR_GREEN,
    COLOR_INDIAN_RED: COLOR_RED,
    COLOR_KHAKI: COLOR_YELLOW,
    COLOR_LIGHT_BLUE: COLOR_BLUE,
    COLOR_LIGHT_GRAY: COLOR_BLACK,
    COLOR_LIGHT_STEEL_BLUE: COLOR_BLUE,
    COLOR_LIME_GREEN: COLOR_LIME_GREEN,
    COLOR_MAGENTA: COLOR_MAGENTA,
    COLOR_MAROON: COLOR_MAROON,
    COLOR_MEDIUM_AQUAMARINE: COLOR_CYAN,
    COLOR_MEDIUM_BLUE: COLOR_BLUE,
    COLOR_MEDIUM_FOREST_GREEN: COLOR_GREEN,
    COLOR_MEDIUM_GOLDENROD: COLOR_YELLOW,
    COLOR_MEDIUM_ORCHID: COLOR_MAGENTA,
    COLOR_MEDIUM_SEA_GREEN: COLOR_GREEN,
    COLOR_MEDIUM_SLATE_BLUE: COLOR_BLUE,
    COLOR_MEDIUM_SPRING_GREEN: COLOR_GREEN,
    COLOR_MEDIUM_TURQUOISE: COLOR_CYAN,
    COLOR_MEDIUM_VIOLET_RED: COLOR_RED,
    COLOR_MIDNIGHT_BLUE: COLOR_BLUE,
    COLOR_NAVY: COLOR_NAVY,
    COLOR_OLIVE: COLOR_OLIVE,
    COLOR_ORANGE: COLOR_RED,
    COLOR_ORANGE_RED: COLOR_RED,
    COLOR_ORCHID: COLOR_MAGENTA,
    COLOR_PALE_GREEN: COLOR_GREEN,
    COLOR_PINK: COLOR_RED,
    COLOR_PLUM: COLOR_MAGENTA,
    COLOR_PURPLE: COLOR_PURPLE,
    COLOR_RED: COLOR_RED,
    COLOR_SALMON: COLOR_RED,
    COLOR_SEA_GREEN: COLOR_GREEN,
    COLOR_SIENNA: COLOR_RED,
    COLOR_SILVER: COLOR_SILVER,
    COLOR_SKY_BLUE: COLOR_CYAN,
    COLOR_SLATE_BLUE: COLOR_BLUE,
    COLOR_SPRING_GREEN: COLOR_GREEN,
    COLOR_STEEL_BLUE: COLOR_BLUE,
    COLOR_TAN: COLOR_YELLOW,
    COLOR_TEAL: COLOR_TEAL,
    COLOR_THISTLE: COLOR_BLACK,
    COLOR_TURQUOISE: COLOR_CYAN,
    COLOR_VIOLET: COLOR_MAGENTA,
    COLOR_VIOLET_RED: COLOR_RED,
    COLOR_WHEAT: COLOR_YELLOW,
    COLOR_WHITE: COLOR_WHITE,
    COLOR_YELLOW: COLOR_YELLOW,
    COLOR_YELLOW_GREEN: COLOR_YELLOW
    }
