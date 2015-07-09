#! /usr/bin/env python
# "Time-stamp: <10/14/2014  6:02:38 AM rsg>"
'''
tsWxPythonColorNames.py - Refactored color name data base
portion of tsWxGraphicalTextUserInterface for identifying the
members of the wxPython 68+ color palette.
'''
#################################################################
#
# File: tsWxPythonColorNames.py
#
# Purpose:
#
#     tsWxPythonColorNames.py - Refactored color name data base
#     portion of tsWxGraphicalTextUserInterface for identifying
#     the members of the wxPython 68+ color palette.
#
# Usage (example):
#
#     ## Import Module
#     from tsWxPythonColorNames import *
#
# Requirements:
#
#     Provide enumerated list of color names for identifying
#     the members of the wxPython 68+ color palette.#
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

__title__     = 'tsWxPythonColorNames'
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

from tsWxPythonColorRGBNames import *

#---------------------------------------------------------------------------

# Set of color identifiers that the character-mode wxPython
# emulation guarantees to be recognized.
COLOR_ALICE_BLUE               = COLOR_RGB_ALICE_BLUE
COLOR_ANTIQUE_WHITE            = COLOR_RGB_ANTIQUE_WHITE
COLOR_AQUAMARINE               = COLOR_RGB_AQUAMARINE
COLOR_AZURE                    = COLOR_RGB_AZURE
COLOR_BEIGE                    = COLOR_RGB_BEIGE
COLOR_BISQUE                   = COLOR_RGB_BISQUE
COLOR_BLACK                    = COLOR_RGB_BLACK
COLOR_BLANCHED_ALMOND          = COLOR_RGB_BLANCHED_ALMOND
COLOR_BLUE                     = COLOR_RGB_BLUE
COLOR_BLUE_VIOLET              = COLOR_RGB_BLUE_VIOLET
COLOR_BROWN                    = COLOR_RGB_BROWN
COLOR_BURLYWOOD                = COLOR_RGB_BURLYWOOD
COLOR_CADET_BLUE               = COLOR_RGB_CADET_BLUE
COLOR_CHARTREUSE               = COLOR_RGB_CHARTREUSE
COLOR_CHOCOLATE                = COLOR_RGB_CHOCOLATE
COLOR_CORAL                    = COLOR_RGB_CORAL
COLOR_CORNFLOWER_BLUE          = COLOR_RGB_CORNFLOWER_BLUE
COLOR_CORNSILK                 = COLOR_RGB_CORNSILK
COLOR_CRIMSON                  = COLOR_RGB_CRIMSON
COLOR_CYAN                     = COLOR_RGB_CYAN
COLOR_DARK_BLUE                = COLOR_RGB_DARK_BLUE
COLOR_DARK_CYAN                = COLOR_RGB_DARK_CYAN
COLOR_DARK_GOLDENROD           = COLOR_RGB_DARK_GOLDENROD
COLOR_DARK_GRAY                = COLOR_RGB_DARK_GRAY
COLOR_DARK_GREEN               = COLOR_RGB_DARK_GREEN
COLOR_DARK_KHAKI               = COLOR_RGB_DARK_KHAKI
COLOR_DARK_MAGENTA             = COLOR_RGB_DARK_MAGENTA
COLOR_DARK_OLIVE_GREEN         = COLOR_RGB_DARK_OLIVE_GREEN
COLOR_DARK_ORANGE              = COLOR_RGB_DARK_ORANGE
COLOR_DARK_ORCHID              = COLOR_RGB_DARK_ORCHID
COLOR_DARK_RED                 = COLOR_RGB_DARK_RED
COLOR_DARK_SALMON              = COLOR_RGB_DARK_SALMON
COLOR_DARK_SEA_GREEN           = COLOR_RGB_DARK_SEA_GREEN
COLOR_DARK_SLATE_BLUE          = COLOR_RGB_DARK_SLATE_BLUE
COLOR_DARK_SLATE_GRAY          = COLOR_RGB_DARK_SLATE_GRAY
COLOR_DARK_TURQUOISE           = COLOR_RGB_DARK_TURQUOISE
COLOR_DARK_VIOLET              = COLOR_RGB_DARK_VIOLET
COLOR_DEEP_PINK                = COLOR_RGB_DEEP_PINK
COLOR_DEEP_SKY_BLUE            = COLOR_RGB_DEEP_SKY_BLUE
COLOR_DIM_GRAY                 = COLOR_RGB_DIM_GRAY
COLOR_DODGER_BLUE              = COLOR_RGB_DODGER_BLUE
COLOR_FIREBRICK                = COLOR_RGB_FIREBRICK
COLOR_FLORAL_WHITE             = COLOR_RGB_FLORAL_WHITE
COLOR_FOREST_GREEN             = COLOR_RGB_FOREST_GREEN
COLOR_GAINSBORO                = COLOR_RGB_GAINSBORO
COLOR_GHOST_WHITE              = COLOR_RGB_GHOST_WHITE
COLOR_GOLD                     = COLOR_RGB_GOLD
COLOR_GOLDENROD                = COLOR_RGB_GOLDENROD
COLOR_GRAY                     = COLOR_RGB_GRAY
COLOR_GREEN                    = COLOR_RGB_GREEN
COLOR_GREEN_YELLOW             = COLOR_RGB_GREEN_YELLOW
COLOR_HONEYDEW                 = COLOR_RGB_HONEYDEW
COLOR_HOT_PINK                 = COLOR_RGB_HOT_PINK
COLOR_INDIAN_RED               = COLOR_RGB_INDIAN_RED
COLOR_INDIGO                   = COLOR_RGB_INDIGO
COLOR_IVORY                    = COLOR_RGB_IVORY
COLOR_KHAKI                    = COLOR_RGB_KHAKI
COLOR_LAVENDER                 = COLOR_RGB_LAVENDER
COLOR_LAVENDER_BLUSH           = COLOR_RGB_LAVENDER_BLUSH
COLOR_LAWN_GREEN               = COLOR_RGB_LAWN_GREEN
COLOR_LEMON_CHIFFON            = COLOR_RGB_LEMON_CHIFFON
COLOR_LIGHT_BLUE               = COLOR_RGB_LIGHT_BLUE
COLOR_LIGHT_CORAL              = COLOR_RGB_LIGHT_CORAL
COLOR_LIGHT_CYAN               = COLOR_RGB_LIGHT_CYAN
COLOR_LIGHT_GOLDENROD_YELLOW   = COLOR_RGB_LIGHT_GOLDENROD_YELLOW
COLOR_LIGHT_GRAY               = COLOR_RGB_LIGHT_GRAY
COLOR_LIGHT_GREEN              = COLOR_RGB_LIGHT_GREEN
COLOR_LIGHT_PINK               = COLOR_RGB_LIGHT_PINK
COLOR_LIGHT_SALMON             = COLOR_RGB_LIGHT_SALMON
COLOR_LIGHT_SEA_GREEN          = COLOR_RGB_LIGHT_SEA_GREEN
COLOR_LIGHT_SKY_BLUE           = COLOR_RGB_LIGHT_SKY_BLUE
COLOR_LIGHT_SLATE_GRAY         = COLOR_RGB_LIGHT_SLATE_GRAY
COLOR_LIGHT_STEEL_BLUE         = COLOR_RGB_LIGHT_STEEL_BLUE
COLOR_LIGHT_YELLOW             = COLOR_RGB_LIGHT_YELLOW
COLOR_LIME_GREEN               = COLOR_RGB_LIME_GREEN
COLOR_LINEN                    = COLOR_RGB_LINEN
COLOR_MAGENTA                  = COLOR_RGB_MAGENTA
COLOR_MAROON                   = COLOR_RGB_MAROON
COLOR_MEDIUM_AQUAMARINE        = COLOR_RGB_MEDIUM_AQUAMARINE
COLOR_MEDIUM_BLUE              = COLOR_RGB_MEDIUM_BLUE
COLOR_MEDIUM_FOREST_GREEN      = COLOR_RGB_MEDIUM_FOREST_GREEN
COLOR_MEDIUM_GOLDENROD         = COLOR_RGB_MEDIUM_GOLDENROD
COLOR_MEDIUM_ORCHID            = COLOR_RGB_MEDIUM_ORCHID
COLOR_MEDIUM_PURPLE            = COLOR_RGB_MEDIUM_PURPLE
COLOR_MEDIUM_SEA_GREEN         = COLOR_RGB_MEDIUM_SEA_GREEN
COLOR_MEDIUM_SLATE_BLUE        = COLOR_RGB_MEDIUM_SLATE_BLUE
COLOR_MEDIUM_SPRING_GREEN      = COLOR_RGB_MEDIUM_SPRING_GREEN
COLOR_MEDIUM_TURQUOISE         = COLOR_RGB_MEDIUM_TURQUOISE
COLOR_MEDIUM_VIOLET_RED        = COLOR_RGB_MEDIUM_VIOLET_RED
COLOR_MIDNIGHT_BLUE            = COLOR_RGB_MIDNIGHT_BLUE
COLOR_MINT_CREAM               = COLOR_RGB_MINT_CREAM
COLOR_MISTY_ROSE               = COLOR_RGB_MISTY_ROSE
COLOR_MOCCASIN                 = COLOR_RGB_MOCCASIN
COLOR_NAVAJO_WHITE             = COLOR_RGB_NAVAJO_WHITE
COLOR_NAVY                     = COLOR_RGB_NAVY
COLOR_OLD_LACE                 = COLOR_RGB_OLD_LACE
COLOR_OLIVE                    = COLOR_RGB_OLIVE
COLOR_OLIVE_DRAB               = COLOR_RGB_OLIVE_DRAB
COLOR_ORANGE                   = COLOR_RGB_ORANGE
COLOR_ORANGE_RED               = COLOR_RGB_ORANGE_RED
COLOR_ORCHID                   = COLOR_RGB_ORCHID
COLOR_PALE_GOLDENROD           = COLOR_RGB_PALE_GOLDENROD
COLOR_PALE_GREEN               = COLOR_RGB_PALE_GREEN
COLOR_PALE_TURQUOISE           = COLOR_RGB_PALE_TURQUOISE
COLOR_PALE_VIOLET_RED          = COLOR_RGB_PALE_VIOLET_RED
COLOR_PAPAYA_WHIP              = COLOR_RGB_PAPAYA_WHIP
COLOR_PEACH_PUFF               = COLOR_RGB_PEACH_PUFF
COLOR_PERU                     = COLOR_RGB_PERU
COLOR_PINK                     = COLOR_RGB_PINK
COLOR_PLUM                     = COLOR_RGB_PLUM
COLOR_POWDER_BLUE              = COLOR_RGB_POWDER_BLUE
COLOR_PURPLE                   = COLOR_RGB_PURPLE
COLOR_RED                      = COLOR_RGB_RED
COLOR_ROSY_BROWN               = COLOR_RGB_ROSY_BROWN
COLOR_ROYAL_BLUE               = COLOR_RGB_ROYAL_BLUE
COLOR_SADDLE_BROWN             = COLOR_RGB_SADDLE_BROWN
COLOR_SALMON                   = COLOR_RGB_SALMON
COLOR_SANDY_BROWN              = COLOR_RGB_SANDY_BROWN
COLOR_SEA_GREEN                = COLOR_RGB_SEA_GREEN
COLOR_SEA_SHELL                = COLOR_RGB_SEA_SHELL
COLOR_SIENNA                   = COLOR_RGB_SIENNA
COLOR_SILVER                   = COLOR_RGB_SILVER
COLOR_SKY_BLUE                 = COLOR_RGB_SKY_BLUE
COLOR_SLATE_BLUE               = COLOR_RGB_SLATE_BLUE
COLOR_SLATE_GRAY               = COLOR_RGB_SLATE_GRAY
COLOR_SNOW                     = COLOR_RGB_SNOW
COLOR_SPRING_GREEN             = COLOR_RGB_SPRING_GREEN
COLOR_STEEL_BLUE               = COLOR_RGB_STEEL_BLUE
COLOR_TAN                      = COLOR_RGB_TAN
COLOR_TEAL                     = COLOR_RGB_TEAL
COLOR_THISTLE                  = COLOR_RGB_THISTLE
COLOR_TOMATO                   = COLOR_RGB_TOMATO
COLOR_TURQUOISE                = COLOR_RGB_TURQUOISE
COLOR_VIOLET                   = COLOR_RGB_VIOLET
COLOR_VIOLET_RED               = COLOR_RGB_VIOLET_RED
COLOR_WHEAT                    = COLOR_RGB_WHEAT
COLOR_WHITE                    = COLOR_RGB_WHITE
COLOR_WHITE_SMOKE              = COLOR_RGB_WHITE_SMOKE
COLOR_YELLOW                   = COLOR_RGB_YELLOW
COLOR_YELLOW_GREEN             = COLOR_RGB_YELLOW_GREEN
