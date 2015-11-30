#! /usr/bin/env python
# "Time-stamp: <04/08/2015  4:31:13 AM rsg>"
'''
tsWxPythonColorRGBValues.py - Refactored color value data base
portion of tsWxGraphicalTextUserInterface for identifying the
Red-Green-Blue components of current and potential members of
the wxPython 68+ color palette.
'''
#################################################################
#
# File: tsWxPythonColor16DataBase.py
#
# Purpose:
#
#     tsWxPythonColorRGBValues.py - Refactored color value
#     data base portion of tsWxGraphicalTextUserInterface
#     for identifying the Red-Green-Blue components of
#     current and potential members of the wxPython 68+
#     color palette.
#
# Usage (example):
#
#     ## Import Module
#     from tsWxPythonColorRGBValues import *
#
# Requirements:
#
#     Provide a dictionary of RGB color key names and an
#     associate tuple of RGB values for the current and
#     potential members of the wxPython 68+ color palette.
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

__title__     = 'tsWxPythonColorRGBValues'
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
                '\n\t  nCurses README,v 1.23 2006/04/22' + \
                '\n\n\t  RGB to Color Name Mapping (Triplet and Hex)' + \
                '\n\t  Copyright (c) 2010 Kevin J. Walsh' + \
                '\n\t\t\tAll rights reserved.'

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

##from tsWxGTUI_Py2x.tsLibGUI import tsWxPythonColorRGBNames

##from tsWxPythonColorRGBNames import *

from tsWxGTUI_Py2x.tsLibGUI.tsWxPythonColorRGBNames import *

#---------------------------------------------------------------------------

# RGB values for set of color identifiers. It includes, but is not
# limited to, those colors which wxPython guarantees to recognize.
#
# The RGB values were obtained from a master copy of a document
# that resides at "http://web.njit.edu/~walsh/rgb.html". That
# document can be copied with or without modification provided
# that you indicate that it came from http://web.njit.edu/~walsh
# and that it is "Copyright (c) 2010 Kevin J. Walsh".

ExtendedColorDataBaseRGB = {
    'name': 'ExtendedColorDataBaseRGB',
    COLOR_RGB_ALICE_BLUE: (240, 248, 255),
    COLOR_RGB_ANTIQUE_WHITE: (250, 235, 215),
    COLOR_RGB_ANTIQUE_WHITE1: (255, 239, 219),
    COLOR_RGB_ANTIQUE_WHITE2: (238, 223, 204),
    COLOR_RGB_ANTIQUE_WHITE3: (205, 192, 176),
    COLOR_RGB_ANTIQUE_WHITE4: (139, 131, 120),
    COLOR_RGB_AQUAMARINE: (127, 255, 212),
    COLOR_RGB_AQUAMARINE1: (127, 255, 212),
    COLOR_RGB_AQUAMARINE2: (118, 238, 198),
    COLOR_RGB_AQUAMARINE3: (102, 205, 170),
    COLOR_RGB_AQUAMARINE4: (69, 139, 116),
    COLOR_RGB_AZURE: (240, 255, 255),
    COLOR_RGB_AZURE1: (240, 255, 255),
    COLOR_RGB_AZURE2: (224, 238, 238),
    COLOR_RGB_AZURE3: (193, 205, 205),
    COLOR_RGB_AZURE4: (131, 139, 139),
    COLOR_RGB_BEIGE: (245, 245, 220),
    COLOR_RGB_BISQUE: (255, 228, 196),
    COLOR_RGB_BISQUE1: (255, 228, 196),
    COLOR_RGB_BISQUE2: (238, 213, 183),
    COLOR_RGB_BISQUE3: (205, 183, 158),
    COLOR_RGB_BISQUE4: (139, 125, 107),
    COLOR_RGB_BLACK: (0, 0, 0),
    COLOR_RGB_BLANCHED_ALMOND: (255, 235, 205),
    COLOR_RGB_BLUE: (0, 0, 255),
    COLOR_RGB_BLUE1: (0, 0, 255),
    COLOR_RGB_BLUE2: (0, 0, 238),
    COLOR_RGB_BLUE3: (0, 0, 205),
    COLOR_RGB_BLUE4: (0, 0, 139),
    COLOR_RGB_BLUE_VIOLET: (138, 43, 226),
    COLOR_RGB_BROWN: (165, 42, 42),
    COLOR_RGB_BROWN1: (255, 64, 64),
    COLOR_RGB_BROWN2: (238, 59, 59),
    COLOR_RGB_BURLYWOOD: (222, 184, 135),
    COLOR_RGB_BURLYWOOD1: (255, 211, 155),
    COLOR_RGB_BURLYWOOD2: (238, 197, 145),
    COLOR_RGB_BURLYWOOD3: (205, 170, 125),
    COLOR_RGB_BURLYWOOD4: (139, 115, 85),
    COLOR_RGB_CADET_BLUE: (95, 158, 160),
    COLOR_RGB_CADET_BLUE1: (152, 245, 255),
    COLOR_RGB_CADET_BLUE2: (142, 229, 238),
    COLOR_RGB_CADET_BLUE3: (122, 197, 205),
    COLOR_RGB_CADET_BLUE4: (83, 134, 139),
    COLOR_RGB_CHARTREUSE: (127, 255, 0),
    COLOR_RGB_CHARTREUSE1: (127, 255, 0),
    COLOR_RGB_CHARTREUSE2: (118, 238, 0),
    COLOR_RGB_CHARTREUSE3: (102, 205, 0),
    COLOR_RGB_CHARTREUSE4: (69, 139, 0),
    COLOR_RGB_CHOCOLATE: (210, 105, 30),
    COLOR_RGB_CHOCOLATE1: (255, 127, 36),
    COLOR_RGB_CHOCOLATE2: (238, 118, 33),
    COLOR_RGB_CHOCOLATE3: (205, 102, 29),
    COLOR_RGB_CHOCOLATE4: (139, 69, 19),
    COLOR_RGB_CORAL: (255, 127, 80),
    COLOR_RGB_CORAL1: (255, 114, 86),
    COLOR_RGB_CORAL2: (238, 106, 80),
    COLOR_RGB_CORAL3: (205, 91, 69),
    COLOR_RGB_CORAL4: (139, 62, 47),
    COLOR_RGB_CORNFLOWER_BLUE: (100, 149, 237),
    COLOR_RGB_CORNSILK: (255, 248, 220),
    COLOR_RGB_CORNSILK1: (255, 248, 220),
    COLOR_RGB_CORNSILK2: (238, 232, 205),
    COLOR_RGB_CORNSILK3: (205, 200, 177),
    COLOR_RGB_CORNSILK4: (139, 136, 120),
    COLOR_RGB_CRIMSON: (220, 20, 60),
    COLOR_RGB_CYAN: (0, 255, 255),
    COLOR_RGB_CYAN1: (0, 255, 255),
    COLOR_RGB_CYAN2: (0, 238, 238),
    COLOR_RGB_CYAN3: (0, 205, 205),
    COLOR_RGB_CYAN4: (0, 139, 139),
    COLOR_RGB_DARK_BLUE: (0, 0, 139),
    COLOR_RGB_DARK_CYAN: (0, 139, 139),
    COLOR_RGB_DARK_GOLDENROD: (184, 134, 11),
    COLOR_RGB_DARK_GOLDENROD1: (255, 185, 15),
    COLOR_RGB_DARK_GOLDENROD2: (238, 173, 14),
    COLOR_RGB_DARK_GOLDENROD3: (205, 149, 12),
    COLOR_RGB_DARK_GRAY: (169, 169, 169),
    COLOR_RGB_DARK_GREEN: (0, 100, 0),
    COLOR_RGB_DARK_KHAKI: (189, 183, 107),
    COLOR_RGB_DARK_MAGENTA: (139, 0, 139),
    COLOR_RGB_DARK_OLIVE_GREEN: (85, 107, 47),
    COLOR_RGB_DARK_OLIVE_GREEN1: (202, 255, 112),
    COLOR_RGB_DARK_OLIVE_GREEN2: (188, 238, 104),
    COLOR_RGB_DARK_OLIVE_GREEN3: (162, 205, 90),
    COLOR_RGB_DARK_OLIVE_GREEN4: (110, 139, 61),
    COLOR_RGB_DARK_ORANGE: (255, 140, 0),
    COLOR_RGB_DARK_ORANGE1: (255, 127, 0),
    COLOR_RGB_DARK_ORANGE2: (238, 118, 0),
    COLOR_RGB_DARK_ORANGE3: (205, 102, 0),
    COLOR_RGB_DARK_ORANGE4: (139, 69, 0),
    COLOR_RGB_DARK_ORCHID: (153, 50, 204),
    COLOR_RGB_DARK_ORCHID1: (191, 62, 255),
    COLOR_RGB_DARK_ORCHID2: (178, 58, 238),
    COLOR_RGB_DARK_ORCHID3: (154, 50, 205),
    COLOR_RGB_DARK_ORCHID4: (104, 34, 139),
    COLOR_RGB_DARK_RED: (139, 0, 0),
    COLOR_RGB_DARK_SALMON: (233, 150, 122),
    COLOR_RGB_DARK_SEA_GREEN: (143, 188, 143),
    COLOR_RGB_DARK_SEA_GREEN1: (193, 255, 193),
    COLOR_RGB_DARK_SEA_GREEN2: (180, 238, 180),
    COLOR_RGB_DARK_SEA_GREEN3: (155, 205, 155),
    COLOR_RGB_DARK_SEA_GREEN4: (105, 139, 105),
    COLOR_RGB_DARK_SLATE_BLUE: (72, 61, 139),
    COLOR_RGB_DARK_SLATE_GRAY: (47, 79, 79),
    COLOR_RGB_DARK_TURQUOISE: (0, 206, 209),
    COLOR_RGB_DARK_VIOLET: (148, 0, 211),
    COLOR_RGB_DEEP_PINK: (255, 20, 147),
    COLOR_RGB_DEEP_PINK4: (139, 10, 80),
    COLOR_RGB_DEEP_SKY_BLUE: (0, 191, 255),
    COLOR_RGB_DEEP_SKY_BLUE1: (0, 191, 255),
    COLOR_RGB_DEEP_SKY_BLUE2: (0, 178, 238),
    COLOR_RGB_DEEP_SKY_BLUE3: (0, 154, 205),
    COLOR_RGB_DEEP_SKY_BLUE4: (0, 104, 139),
    COLOR_RGB_DIM_GRAY: (105, 105, 105),
    COLOR_RGB_DODGER_BLUE: (30, 144, 255),
    COLOR_RGB_DODGER_BLUE1: (30, 144, 255),
    COLOR_RGB_DODGER_BLUE2: (28, 134, 238),
    COLOR_RGB_DODGER_BLUE3: (24, 116, 205),
    COLOR_RGB_DODGER_BLUE4: (16, 78, 139),
    COLOR_RGB_FIREBRICK: (178, 34, 34),
    COLOR_RGB_FIREBRICK1: (255, 48, 48),
    COLOR_RGB_FIREBRICK2: (238, 44, 44),
    COLOR_RGB_FIREBRICK3: (205, 38, 38),
    COLOR_RGB_FIREBRICK4: (139, 26, 26),
    COLOR_RGB_FLORAL_WHITE: (255, 250, 240),
    COLOR_RGB_FOREST_GREEN: (34, 139, 34),
    COLOR_RGB_GAINSBORO: (220, 220, 220),
    COLOR_RGB_GHOST_WHITE: (248, 248, 255),
    COLOR_RGB_GOLD: (255, 215, 0),
    COLOR_RGB_GOLD1: (255, 215, 0),
    COLOR_RGB_GOLD2: (238, 201, 0),
    COLOR_RGB_GOLD3: (205, 173, 0),
    COLOR_RGB_GOLD4: (139, 117, 0),
    COLOR_RGB_GOLDENROD: (218, 165, 32),
    COLOR_RGB_GOLDENROD1: (255, 193, 37),
    COLOR_RGB_GOLDENROD2: (238, 180, 34),
    COLOR_RGB_GOLDENROD3: (205, 155, 29),
    COLOR_RGB_GOLDENROD4: (139, 105, 20),
    COLOR_RGB_GRAY: (190, 190, 190),
    COLOR_RGB_GRAY2: (5, 5, 5),
    COLOR_RGB_GRAY3: (8, 8, 8),
    COLOR_RGB_GRAY4: (10, 10, 10),
    COLOR_RGB_GRAY5: (13, 13, 13),
    COLOR_RGB_GRAY6: (15, 15, 15),
    COLOR_RGB_GRAY7: (18, 18, 18),
    COLOR_RGB_GRAY8: (20, 20, 20),
    COLOR_RGB_GRAY9: (23, 23, 23),
    COLOR_RGB_GRAY10: (26, 26, 26),
    COLOR_RGB_GRAY11: (28, 28, 28),
    COLOR_RGB_GRAY12: (31, 31, 31),
    COLOR_RGB_GRAY13: (33, 33, 33),
    COLOR_RGB_GRAY14: (36, 36, 36),
    COLOR_RGB_GRAY15: (38, 38, 38),
    COLOR_RGB_GRAY16: (41, 41, 41),
    COLOR_RGB_GRAY17: (43, 43, 43),
    COLOR_RGB_GRAY18: (46, 46, 46),
    COLOR_RGB_GRAY19: (48, 48, 48),
    COLOR_RGB_GRAY20: (51, 51, 51),
    COLOR_RGB_GRAY21: (54, 54, 54),
    COLOR_RGB_GRAY22: (56, 56, 56),
    COLOR_RGB_GRAY23: (59, 59, 59),
    COLOR_RGB_GRAY24: (61, 61, 61),
    COLOR_RGB_GRAY25: (64, 64, 64),
    COLOR_RGB_GRAY26: (66, 66, 66),
    COLOR_RGB_GRAY36: (92, 92, 92),
    COLOR_RGB_GRAY37: (94, 94, 94),
    COLOR_RGB_GRAY38: (97, 97, 97),
    COLOR_RGB_GRAY39: (99, 99, 99),
    COLOR_RGB_GRAY40: (102, 102, 102),
    COLOR_RGB_GRAY41: (105, 105, 105),
    COLOR_RGB_GRAY42: (107, 107, 107),
    COLOR_RGB_GRAY43: (110, 110, 110),
    COLOR_RGB_GRAY44: (112, 112, 112),
    COLOR_RGB_GRAY45: (115, 115, 115),
    COLOR_RGB_GRAY46: (117, 117, 117),
    COLOR_RGB_GRAY47: (120, 120, 120),
    COLOR_RGB_GRAY48: (122, 122, 122),
    COLOR_RGB_GRAY49: (125, 125, 125),
    COLOR_RGB_GRAY50: (127, 127, 127),
    COLOR_RGB_GRAY51: (130, 130, 130),
    COLOR_RGB_GRAY52: (133, 133, 133),
    COLOR_RGB_GRAY53: (135, 135, 135),
    COLOR_RGB_GRAY54: (138, 138, 138),
    COLOR_RGB_GRAY55: (140, 140, 140),
    COLOR_RGB_GRAY56: (143, 143, 143),
    COLOR_RGB_GRAY57: (145, 145, 145),
    COLOR_RGB_GRAY58: (148, 148, 148),
    COLOR_RGB_GRAY59: (150, 150, 150),
    COLOR_RGB_GRAY60: (153, 153, 153),
    COLOR_RGB_GRAY74: (189, 189, 189),
    COLOR_RGB_GRAY75: (191, 191, 191),
    COLOR_RGB_GRAY76: (194, 194, 194),
    COLOR_RGB_GRAY77: (196, 196, 196),
    COLOR_RGB_GRAY78: (199, 199, 199),
    COLOR_RGB_GRAY79: (201, 201, 201),
    COLOR_RGB_GRAY80: (204, 204, 204),
    COLOR_RGB_GRAY81: (207, 207, 207),
    COLOR_RGB_GRAY82: (209, 209, 209),
    COLOR_RGB_GRAY83: (212, 212, 212),
    COLOR_RGB_GRAY84: (214, 214, 214),
    COLOR_RGB_GRAY85: (217, 217, 217),
    COLOR_RGB_GRAY86: (219, 219, 219),
    COLOR_RGB_GRAY87: (222, 222, 222),
    COLOR_RGB_GRAY88: (224, 224, 224),
    COLOR_RGB_GRAY89: (227, 227, 227),
    COLOR_RGB_GRAY90: (229, 229, 229),
    COLOR_RGB_GRAY91: (232, 232, 232),
    COLOR_RGB_GRAY92: (235, 235, 235),
    COLOR_RGB_GRAY93: (237, 237, 237),
    COLOR_RGB_GRAY94: (240, 240, 240),
    COLOR_RGB_GRAY95: (242, 242, 242),
    COLOR_RGB_GRAY96: (245, 245, 245),
    COLOR_RGB_GRAY97: (247, 247, 247),
    COLOR_RGB_GRAY98: (250, 250, 250),
    COLOR_RGB_GRAY99: (252, 252, 252),
    COLOR_RGB_GRAY100: (255, 255, 255),
    COLOR_RGB_GREEN: (0, 255, 0),
    COLOR_RGB_GREEN1: (0, 255, 0),
    COLOR_RGB_GREEN2: (0, 238, 0),
    COLOR_RGB_GREEN3: (0, 205, 0),
    COLOR_RGB_GREEN4: (0, 139, 0),
    COLOR_RGB_GREEN_YELLOW: (173, 255, 47),
    COLOR_RGB_HONEYDEW: (240, 255, 240),
    COLOR_RGB_HONEYDEW1: (240, 255, 240),
    COLOR_RGB_HONEYDEW2: (224, 238, 224),
    COLOR_RGB_HONEYDEW3: (193, 205, 193),
    COLOR_RGB_HONEYDEW4: (131, 139, 131),
    COLOR_RGB_HOT_PINK: (255, 105, 180),
    COLOR_RGB_HOT_PINK1: (255, 110, 180),
    COLOR_RGB_HOT_PINK2: (238, 106, 167),
    COLOR_RGB_HOT_PINK3: (205, 96, 144),
    COLOR_RGB_HOT_PINK4: (139, 58, 98),
    COLOR_RGB_INDIAN_RED: (205, 92, 92),
    COLOR_RGB_INDIGO: (75, 0, 130),
    COLOR_RGB_IVORY: (255, 255, 240),
    COLOR_RGB_IVORY1: (255, 255, 240),
    COLOR_RGB_IVORY2: (238, 238, 224),
    COLOR_RGB_IVORY3: (205, 205, 193),
    COLOR_RGB_IVORY4: (139, 139, 131),
    COLOR_RGB_KHAKI: (240, 230, 140),
    COLOR_RGB_KHAKI1: (255, 246, 143),
    COLOR_RGB_KHAKI2: (238, 230, 133),
    COLOR_RGB_KHAKI3: (205, 198, 115),
    COLOR_RGB_KHAKI4: (139, 134, 78),
    COLOR_RGB_LAVENDER: (230, 230, 250),
    COLOR_RGB_LAVENDER_BLUSH: (255, 240, 245),
    COLOR_RGB_LAVENDER_BLUSH1: (255, 240, 245),
    COLOR_RGB_LAVENDER_BLUSH2: (238, 224, 229),
    COLOR_RGB_LAVENDER_BLUSH3: (205, 193, 197),
    COLOR_RGB_LAVENDER_BLUSH4: (139, 131, 134),
    COLOR_RGB_LAWN_GREEN: (124, 252, 0),
    COLOR_RGB_LEMON_CHIFFON: (255, 250, 205),
    COLOR_RGB_LEMON_CHIFFON1: (255, 250, 205),
    COLOR_RGB_LEMON_CHIFFON2: (238, 233, 191),
    COLOR_RGB_LEMON_CHIFFON3: (205, 201, 165),
    COLOR_RGB_LEMON_CHIFFON4: (139, 137, 112),
    COLOR_RGB_LIGHT_BLUE: (173, 216, 230),
    COLOR_RGB_LIGHT_BLUE1: (191, 239, 255),
    COLOR_RGB_LIGHT_BLUE2: (178, 223, 238),
    COLOR_RGB_LIGHT_BLUE3: (154, 192, 205),
    COLOR_RGB_LIGHT_BLUE4: (104, 131, 139),
    COLOR_RGB_LIGHT_CORAL: (240, 128, 128),
    COLOR_RGB_LIGHT_CYAN: (224, 255, 255),
    COLOR_RGB_LIGHT_CYAN1: (224, 255, 255),
    COLOR_RGB_LIGHT_CYAN2: (209, 238, 238),
    COLOR_RGB_LIGHT_CYAN3: (180, 205, 205),
    COLOR_RGB_LIGHT_CYAN4: (122, 139, 139),
    COLOR_RGB_LIGHT_GOLDENROD: (238, 221, 130),
    COLOR_RGB_LIGHT_GOLDENROD1: (255, 236, 139),
    COLOR_RGB_LIGHT_GOLDENROD2: (238, 220, 130),
    COLOR_RGB_LIGHT_GOLDENROD3: (205, 190, 112),
    COLOR_RGB_LIGHT_GOLDENROD4: (139, 129, 76),
    COLOR_RGB_LIGHT_GOLDENROD_YELLOW: (250, 250, 210),
    COLOR_RGB_LIGHT_GRAY: (211, 211, 211),
    COLOR_RGB_LIGHT_GREEN: (144, 238, 144),
    COLOR_RGB_LIGHT_PINK: (255, 182, 193),
    COLOR_RGB_LIGHT_PINK1: (255, 174, 185),
    COLOR_RGB_LIGHT_PINK2: (238, 162, 173),
    COLOR_RGB_LIGHT_PINK3: (205, 140, 149),
    COLOR_RGB_LIGHT_PINK4: (139, 95, 101),
    COLOR_RGB_LIGHT_SALMON: (255, 160, 122),
    COLOR_RGB_LIGHT_SALMON1: (255, 160, 122),
    COLOR_RGB_LIGHT_SALMON2: (238, 149, 114),
    COLOR_RGB_LIGHT_SALMON3: (205, 129, 98),
    COLOR_RGB_LIGHT_SALMON4: (139, 87, 66),
    COLOR_RGB_LIGHT_SEA_GREEN: (32, 178, 170),
    COLOR_RGB_LIGHT_SKY_BLUE: (135, 206, 250),
    COLOR_RGB_LIGHT_SKY_BLUE1: (176, 226, 255),
    COLOR_RGB_LIGHT_SKY_BLUE2: (164, 211, 238),
    COLOR_RGB_LIGHT_SKY_BLUE3: (141, 182, 205),
    COLOR_RGB_LIGHT_SKY_BLUE4: (96, 123, 139),
    COLOR_RGB_LIGHT_SLATE_BLUE: (132, 112, 255),
    COLOR_RGB_LIGHT_SLATE_GRAY: (119, 136, 153),
    COLOR_RGB_LIGHT_STEEL_BLUE: (176, 196, 222),
    COLOR_RGB_LIGHT_STEEL_BLUE1: (202, 225, 255),
    COLOR_RGB_LIGHT_STEEL_BLUE2: (188, 210, 238),
    COLOR_RGB_LIGHT_STEEL_BLUE3: (162, 181, 205),
    COLOR_RGB_LIGHT_STEEL_BLUE4: (110, 123, 139),
    COLOR_RGB_LIGHT_YELLOW: (255, 255, 224),
    COLOR_RGB_LIGHT_YELLOW1: (255, 255, 224),
    COLOR_RGB_LIGHT_YELLOW2: (238, 238, 209),
    COLOR_RGB_LIGHT_YELLOW3: (205, 205, 180),
    COLOR_RGB_LIGHT_YELLOW4: (139, 139, 122),
    COLOR_RGB_LIME_GREEN: (50, 205, 50),
    COLOR_RGB_LINEN: (250, 240, 230),
    COLOR_RGB_MAGENTA: (255, 0, 255),
    COLOR_RGB_MAGENTA1: (255, 0, 255),
    COLOR_RGB_MAGENTA2: (238, 0, 238),
    COLOR_RGB_MAGENTA3: (205, 0, 205),
    COLOR_RGB_MAGENTA4: (139, 0, 139),
    COLOR_RGB_MAROON: (176, 48, 96),
    COLOR_RGB_MAROON1: (255, 52, 179),
    COLOR_RGB_MAROON2: (238, 48, 167),
    COLOR_RGB_MAROON3: (205, 41, 144),
    COLOR_RGB_MAROON4: (139, 28, 98),
    COLOR_RGB_MEDIUM_AQUAMARINE: (102, 205, 170),
    COLOR_RGB_MEDIUM_BLUE: (0, 0, 205),
    COLOR_RGB_MEDIUM_FOREST_GREEN: (107, 142, 35),
    COLOR_RGB_MEDIUM_GOLDENROD: (192, 192, 174),
    COLOR_RGB_MEDIUM_ORCHID: (186, 85, 211),
    COLOR_RGB_MEDIUM_ORCHID1: (224, 102, 255),
    COLOR_RGB_MEDIUM_ORCHID2: (209, 95, 238),
    COLOR_RGB_MEDIUM_ORCHID3: (180, 82, 205),
    COLOR_RGB_MEDIUM_ORCHID4: (122, 55, 139),
    COLOR_RGB_MEDIUM_PURPLE: (147, 112, 219),
    COLOR_RGB_MEDIUM_SEA_GREEN: (60, 179, 113),
    COLOR_RGB_MEDIUM_SLATE_BLUE: (123, 104, 238),
    COLOR_RGB_MEDIUM_SPRING_GREEN: (0, 250, 154),
    COLOR_RGB_MEDIUM_TURQUOISE: (72, 209, 204),
    COLOR_RGB_MEDIUM_VIOLET_RED: (199, 21, 133),
    COLOR_RGB_MIDNIGHT_BLUE: (25, 25, 112),
    COLOR_RGB_MINT_CREAM: (245, 255, 250),
    COLOR_RGB_MISTY_ROSE: (255, 228, 225),
    COLOR_RGB_MISTY_ROSE1: (255, 228, 225),
    COLOR_RGB_MISTY_ROSE2: (238, 213, 210),
    COLOR_RGB_MISTY_ROSE3: (205, 183, 181),
    COLOR_RGB_MISTY_ROSE4: (139, 125, 123),
    COLOR_RGB_MOCCASIN: (255, 228, 181),
    COLOR_RGB_NAVAJO_WHITE: (255, 222, 173),
    COLOR_RGB_NAVAJO_WHITE1: (255, 222, 173),
    COLOR_RGB_NAVAJO_WHITE2: (238, 207, 161),
    COLOR_RGB_NAVAJO_WHITE3: (205, 179, 139),
    COLOR_RGB_NAVAJO_WHITE4: (139, 121, 94),
    COLOR_RGB_NAVY: (0, 0, 128),
    COLOR_RGB_NAVY_BLUE: (0, 0, 128),
    COLOR_RGB_OLD_LACE: (253, 245, 230),
    COLOR_RGB_OLIVE: (128, 128, 0),
    COLOR_RGB_OLIVE_DRAB: (107, 142, 35),
    COLOR_RGB_OLIVE_DRAB1: (192, 255, 62),
    COLOR_RGB_OLIVE_DRAB2: (179, 238, 58),
    COLOR_RGB_OLIVE_DRAB3: (154, 205, 50),
    COLOR_RGB_OLIVE_DRAB4: (105, 139, 34),
    COLOR_RGB_ORANGE: (255, 165, 0),
    COLOR_RGB_ORANGE1: (255, 165, 0),
    COLOR_RGB_ORANGE2: (238, 154, 0),
    COLOR_RGB_ORANGE3: (205, 133, 0),
    COLOR_RGB_ORANGE4: (139, 90, 0),
    COLOR_RGB_ORANGE_RED: (255, 69, 0),
    COLOR_RGB_ORANGE_RED1: (255, 69, 0),
    COLOR_RGB_ORANGE_RED2: (238, 64, 0),
    COLOR_RGB_ORCHID: (218, 112, 214),
    COLOR_RGB_ORCHID1: (255, 131, 250),
    COLOR_RGB_ORCHID2: (238, 122, 233),
    COLOR_RGB_ORCHID3: (205, 105, 201),
    COLOR_RGB_ORCHID4: (139, 71, 137),
    COLOR_RGB_PALE_GOLDENROD: (238, 232, 170),
    COLOR_RGB_PALE_GREEN: (152, 251, 152),
    COLOR_RGB_PALE_GREEN1: (154, 255, 154),
    COLOR_RGB_PALE_GREEN2: (144, 238, 144),
    COLOR_RGB_PALE_GREEN3: (124, 205, 124),
    COLOR_RGB_PALE_GREEN4: (84, 139, 84),
    COLOR_RGB_PALE_TURQUOISE: (175, 238, 238),
    COLOR_RGB_PALE_TURQUOISE1: (187, 255, 255),
    COLOR_RGB_PALE_TURQUOISE2: (174, 238, 238),
    COLOR_RGB_PALE_TURQUOISE3: (150, 205, 205),
    COLOR_RGB_PALE_TURQUOISE4: (102, 139, 139),
    COLOR_RGB_PALE_VIOLET_RED: (219, 112, 147),
    COLOR_RGB_PALE_VIOLET_RED1: (255, 130, 171),
    COLOR_RGB_PALE_VIOLET_RED2: (238, 121, 159),
    COLOR_RGB_PALE_VIOLET_RED3: (205, 104, 137),
    COLOR_RGB_PALE_VIOLET_RED4: (139, 71, 93),
    COLOR_RGB_PAPAYA_WHIP: (255, 239, 213),
    COLOR_RGB_PEACH_PUFF: (255, 218, 185),
    COLOR_RGB_PEACH_PUFF1: (255, 218, 185),
    COLOR_RGB_PEACH_PUFF2: (238, 203, 173),
    COLOR_RGB_PEACH_PUFF3: (205, 175, 149),
    COLOR_RGB_PEACH_PUFF4: (139, 119, 101),
    COLOR_RGB_PERU: (205, 133, 63),
    COLOR_RGB_PINK: (255, 192, 203),
    COLOR_RGB_PINK1: (255, 181, 197),
    COLOR_RGB_PINK2: (238, 169, 184),
    COLOR_RGB_PINK3: (205, 145, 158),
    COLOR_RGB_PINK4: (139, 99, 108),
    COLOR_RGB_PLUM: (221, 160, 221),
    COLOR_RGB_PLUM1: (255, 187, 255),
    COLOR_RGB_PLUM2: (238, 174, 238),
    COLOR_RGB_PLUM3: (205, 150, 205),
    COLOR_RGB_PLUM4: (139, 102, 139),
    COLOR_RGB_POWDER_BLUE: (176, 224, 230),
    COLOR_RGB_PURPLE: (160, 32, 240),
    COLOR_RGB_PURPLE1: (155, 48, 255),
    COLOR_RGB_PURPLE2: (145, 44, 238),
    COLOR_RGB_PURPLE3: (125, 38, 205),
    COLOR_RGB_PURPLE4: (85, 26, 139),
    COLOR_RGB_RED: (255, 0, 0),
    COLOR_RGB_ROSY_BROWN: (188, 143, 143),
    COLOR_RGB_ROYAL_BLUE: (65, 105, 225),
    COLOR_RGB_ROYAL_BLUE1: (72, 118, 255),
    COLOR_RGB_ROYAL_BLUE2: (67, 110, 238),
    COLOR_RGB_ROYAL_BLUE3: (58, 95, 205),
    COLOR_RGB_ROYAL_BLUE4: (39, 64, 139),
    COLOR_RGB_SADDLE_BROWN: (139, 69, 19),
    COLOR_RGB_SALMON: (250, 128, 114),
    COLOR_RGB_SALMON2: (238, 130, 98),
    COLOR_RGB_SALMON3: (205, 112, 84),
    COLOR_RGB_SALMON4: (139, 76, 57),
    COLOR_RGB_SANDY_BROWN: (244, 164, 96),
    COLOR_RGB_SEA_GREEN: (46, 139, 87),
    COLOR_RGB_SEA_GREEN1: (84, 255, 159),
    COLOR_RGB_SEA_GREEN2: (78, 238, 148),
    COLOR_RGB_SEA_GREEN3: (67, 205, 128),
    COLOR_RGB_SEA_GREEN4: (46, 139, 87),
    COLOR_RGB_SEA_SHELL: (255, 245, 238),
    COLOR_RGB_SEA_SHELL1: (255, 245, 238),
    COLOR_RGB_SEA_SHELL2: (238, 229, 222),
    COLOR_RGB_SEA_SHELL3: (205, 197, 191),
    COLOR_RGB_SEA_SHELL4: (139, 134, 130),
    COLOR_RGB_SIENNA: (160, 82, 45),
    COLOR_RGB_SIENNA2: (238, 121, 66),
    COLOR_RGB_SIENNA3: (205, 104, 57),
    COLOR_RGB_SIENNA4: (139, 71, 38),
    COLOR_RGB_SILVER: (192, 192, 192),
    COLOR_RGB_SKY_BLUE: (135, 206, 235),
    COLOR_RGB_SKY_BLUE1: (135, 206, 255),
    COLOR_RGB_SKY_BLUE2: (126, 192, 238),
    COLOR_RGB_SKY_BLUE3: (108, 166, 205),
    COLOR_RGB_SKY_BLUE4: (74, 112, 139),
    COLOR_RGB_SLATE_BLUE: (106, 90, 205),
    COLOR_RGB_SLATE_BLUE1: (131, 111, 255),
    COLOR_RGB_SLATE_BLUE2: (122, 103, 238),
    COLOR_RGB_SLATE_BLUE3: (105, 89, 205),
    COLOR_RGB_SLATE_BLUE4: (71, 60, 139),
    COLOR_RGB_SLATE_GRAY: (112, 128, 144),
    COLOR_RGB_SNOW: (255, 250, 250),
    COLOR_RGB_SNOW1: (255, 250, 250),
    COLOR_RGB_SNOW2: (238, 233, 233),
    COLOR_RGB_SNOW3: (205, 201, 201),
    COLOR_RGB_SNOW4: (139, 137, 137),
    COLOR_RGB_SPRING_GREEN: (0, 255, 127),
    COLOR_RGB_SPRING_GREEN1: (0, 255, 127),
    COLOR_RGB_SPRING_GREEN2: (0, 238, 118),
    COLOR_RGB_SPRING_GREEN3: (0, 205, 102),
    COLOR_RGB_SPRING_GREEN4: (0, 139, 69),
    COLOR_RGB_STEEL_BLUE: (70, 130, 180),
    COLOR_RGB_STEEL_BLUE1: (99, 184, 255),
    COLOR_RGB_STEEL_BLUE2: (92, 172, 238),
    COLOR_RGB_STEEL_BLUE3: (79, 148, 205),
    COLOR_RGB_STEEL_BLUE4: (54, 100, 139),
    COLOR_RGB_TAN: (210, 180, 140),
    COLOR_RGB_TAN1: (255, 165, 79),
    COLOR_RGB_TAN2: (238, 154, 73),
    COLOR_RGB_TAN3: (205, 133, 63),
    COLOR_RGB_TAN4: (139, 90, 43),
    COLOR_RGB_TEAL: (0, 128, 128),
    COLOR_RGB_THISTLE: (216, 191, 216),
    COLOR_RGB_TOMATO: (255, 99, 71),
    COLOR_RGB_TOMATO1: (255, 99, 71),
    COLOR_RGB_TOMATO2: (238, 92, 66),
    COLOR_RGB_TOMATO3: (205, 79, 57),
    COLOR_RGB_TOMATO4: (139, 54, 38),
    COLOR_RGB_TURQUOISE: (64, 224, 208),
    COLOR_RGB_TURQUOISE1: (0, 245, 255),
    COLOR_RGB_TURQUOISE2: (0, 229, 238),
    COLOR_RGB_TURQUOISE3: (0, 197, 205),
    COLOR_RGB_TURQUOISE4: (0, 134, 139),
    COLOR_RGB_VIOLET: (238, 130, 238),
    COLOR_RGB_VIOLET_RED: (208, 32, 144),
    COLOR_RGB_VIOLET_RED1: (255, 62, 150),
    COLOR_RGB_VIOLET_RED2: (238, 58, 140),
    COLOR_RGB_VIOLET_RED3: (205, 50, 120),
    COLOR_RGB_VIOLET_RED4: (139, 34, 82),
    COLOR_RGB_WHEAT: (245, 222, 179),
    COLOR_RGB_WHEAT1: (255, 231, 186),
    COLOR_RGB_WHEAT2: (238, 216, 174),
    COLOR_RGB_WHEAT3: (205, 186, 150),
    COLOR_RGB_WHEAT4: (139, 126, 102),
    COLOR_RGB_WHITE: (255, 255, 255),
    COLOR_RGB_WHITE_SMOKE: (245, 245, 245),
    COLOR_RGB_YELLOW: (255, 255, 0),
    COLOR_RGB_YELLOW1: (255, 255, 0),
    COLOR_RGB_YELLOW2: (238, 238, 0),
    COLOR_RGB_YELLOW3: (205, 205, 0),
    COLOR_RGB_YELLOW4: (139, 139, 0),
    COLOR_RGB_YELLOW_GREEN: (154, 205, 50)
    }
