#! /usr/bin/env python
# "Time-stamp: <11/12/2014  8:34:48 AM rsg>"
'''
tsWxPythonColorRGBNames.py - Refactored color name data base
portion of tsWxGraphicalTextUserInterface for identifying the
current and potential members of the wxPython 68+ color palette.
'''
#################################################################
#
# File: tsWxPythonColorRGBNames.py
#
# Purpose:
#
#     tsWxPythonColorRGBNames.py - Refactored color name data
#     base portion of tsWxGraphicalTextUserInterface for
#     identifying the current and potential members of the
#     wxPython 68+ color palette.
#
# Usage (example):
#
#     ## Import Module
#     from tsWxPythonColorRGBNames import *
#
# Requirements:
#
#     Provide enumerated list of color names for identifying
#     the current and potential members of the wxPython 68+
#     color palette.
#
#     By convention:
#
#        Each name string shall contain only lower case
#        alphabetic and and optional suffix of numeric
#        characters ('gray99').
#
#        Multiple words may be separated by a single blank
#        space character ('lime green').
#
#        Names must not contain leading or traling blank
#        spaces.
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

__title__     = 'tsWxPythonColorRGBNames'
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

# Set of color identifiers for RGB values. It includes, but is not
# limited to, those colors which wxPython guarantees to recognize.

# RGB values for set of color identifiers. It includes, but is not
# limited to, those colors which wxPython guarantees to recognize.
#
# The RGB values were obtained from a master copy of a document
# that resides at "http://web.njit.edu/~walsh/rgb.html". That
# document can be copied with or without modification provided
# that you indicate that it came from http://web.njit.edu/~walsh
# and that it is "Copyright (c) 2010 Kevin J. Walsh".
COLOR_RGB_ALICE_BLUE               = 'alice blue'
COLOR_RGB_ANTIQUE_WHITE            = 'antique white'
COLOR_RGB_ANTIQUE_WHITE1           = 'antique white1'
COLOR_RGB_ANTIQUE_WHITE2           = 'antique white2'
COLOR_RGB_ANTIQUE_WHITE3           = 'antique white3'
COLOR_RGB_ANTIQUE_WHITE4           = 'antique white4'
COLOR_RGB_AQUAMARINE               = 'aquamarine'
COLOR_RGB_AQUAMARINE1              = 'aquamarine1'
COLOR_RGB_AQUAMARINE2              = 'aquamarine2'
COLOR_RGB_AQUAMARINE3              = 'aquamarine3'
COLOR_RGB_AQUAMARINE4              = 'aquamarine4'
COLOR_RGB_AZURE                    = 'azure'
COLOR_RGB_AZURE1                   = 'azure1'
COLOR_RGB_AZURE2                   = 'azure2'
COLOR_RGB_AZURE3                   = 'azure3'
COLOR_RGB_AZURE4                   = 'azure4'
COLOR_RGB_BEIGE                    = 'beige'
COLOR_RGB_BISQUE                   = 'bisque'
COLOR_RGB_BISQUE1                  = 'bisque1'
COLOR_RGB_BISQUE2                  = 'bisque2'
COLOR_RGB_BISQUE3                  = 'bisque3'
COLOR_RGB_BISQUE4                  = 'bisque4'
COLOR_RGB_BLACK                    = 'black'
COLOR_RGB_BLANCHED_ALMOND          = 'blanched almond'
COLOR_RGB_BLUE                     = 'blue'
COLOR_RGB_BLUE1                    = 'blue1'
COLOR_RGB_BLUE2                    = 'blue2'
COLOR_RGB_BLUE3                    = 'blue3'
COLOR_RGB_BLUE4                    = 'blue4'
COLOR_RGB_BLUE_VIOLET              = 'blue violet'
COLOR_RGB_BROWN                    = 'brown'
COLOR_RGB_BROWN1                   = 'brown1'
COLOR_RGB_BROWN2                   = 'brown2'
COLOR_RGB_BURLYWOOD                = 'burlywood'
COLOR_RGB_BURLYWOOD1               = 'burlywood1'
COLOR_RGB_BURLYWOOD2               = 'burlywood2'
COLOR_RGB_BURLYWOOD3               = 'burlywood3'
COLOR_RGB_BURLYWOOD4               = 'burlywood4'
COLOR_RGB_CADET_BLUE               = 'cadet blue'
COLOR_RGB_CADET_BLUE1              = 'cadet blue1'
COLOR_RGB_CADET_BLUE2              = 'cadet blue2'
COLOR_RGB_CADET_BLUE3              = 'cadet blue3'
COLOR_RGB_CADET_BLUE4              = 'cadet blue4'
COLOR_RGB_CHARTREUSE               = 'chartreuse'
COLOR_RGB_CHARTREUSE1              = 'chartreuse1'
COLOR_RGB_CHARTREUSE2              = 'chartreuse2'
COLOR_RGB_CHARTREUSE3              = 'chartreuse3'
COLOR_RGB_CHARTREUSE4              = 'chartreuse4'
COLOR_RGB_CHOCOLATE                = 'chocolate'
COLOR_RGB_CHOCOLATE1               = 'chocolate1'
COLOR_RGB_CHOCOLATE2               = 'chocolate2'
COLOR_RGB_CHOCOLATE3               = 'chocolate3'
COLOR_RGB_CHOCOLATE4               = 'chocolate4'
COLOR_RGB_CORAL                    = 'coral'
COLOR_RGB_CORAL1                   = 'coral1'
COLOR_RGB_CORAL2                   = 'coral2'
COLOR_RGB_CORAL3                   = 'coral3'
COLOR_RGB_CORAL4                   = 'coral4'
COLOR_RGB_CORNFLOWER_BLUE          = 'cornflower blue'
COLOR_RGB_CORNSILK                 = 'cornsilk'
COLOR_RGB_CORNSILK1                = 'cornsilk1'
COLOR_RGB_CORNSILK2                = 'cornsilk2'
COLOR_RGB_CORNSILK3                = 'cornsilk3'
COLOR_RGB_CORNSILK4                = 'cornsilk4'
COLOR_RGB_CRIMSON                  = 'crimson'
COLOR_RGB_CYAN                     = 'cyan'
COLOR_RGB_CYAN1                    = 'cyan1'
COLOR_RGB_CYAN2                    = 'cyan2'
COLOR_RGB_CYAN3                    = 'cyan3'
COLOR_RGB_CYAN4                    = 'cyan4'
COLOR_RGB_DARK_BLUE                = 'dark blue'
COLOR_RGB_DARK_CYAN                = 'dark cyan'
COLOR_RGB_DARK_GOLDENROD           = 'dark goldenrod'
COLOR_RGB_DARK_GOLDENROD1          = 'dark goldenrod1'
COLOR_RGB_DARK_GOLDENROD2          = 'dark goldenrod2'
COLOR_RGB_DARK_GOLDENROD3          = 'dark goldenrod3'
COLOR_RGB_DARK_GRAY                = 'dark gray'
COLOR_RGB_DARK_GREEN               = 'dark green'
COLOR_RGB_DARK_KHAKI               = 'dark khaki'
COLOR_RGB_DARK_MAGENTA             = 'dark magenta'
COLOR_RGB_DARK_OLIVE_GREEN         = 'dark olive green'
COLOR_RGB_DARK_OLIVE_GREEN1        = 'dark olive green1'
COLOR_RGB_DARK_OLIVE_GREEN2        = 'dark olive green2'
COLOR_RGB_DARK_OLIVE_GREEN3        = 'dark olive green3'
COLOR_RGB_DARK_OLIVE_GREEN4        = 'dark olive green4'
COLOR_RGB_DARK_ORANGE              = 'dark orange'
COLOR_RGB_DARK_ORANGE1             = 'dark orange1'
COLOR_RGB_DARK_ORANGE2             = 'dark orange2'
COLOR_RGB_DARK_ORANGE3             = 'dark orange3'
COLOR_RGB_DARK_ORANGE4             = 'dark orange4'
COLOR_RGB_DARK_ORCHID              = 'dark orchid'
COLOR_RGB_DARK_ORCHID1             = 'dark orchid1'
COLOR_RGB_DARK_ORCHID2             = 'dark orchid2'
COLOR_RGB_DARK_ORCHID3             = 'dark orchid3'
COLOR_RGB_DARK_ORCHID4             = 'dark orchid4'
COLOR_RGB_DARK_RED                 = 'dark red'
COLOR_RGB_DARK_SALMON              = 'dark salmon'
COLOR_RGB_DARK_SEA_GREEN           = 'dark sea green'
COLOR_RGB_DARK_SEA_GREEN1          = 'dark sea green1'
COLOR_RGB_DARK_SEA_GREEN2          = 'dark sea green2'
COLOR_RGB_DARK_SEA_GREEN3          = 'dark sea green3'
COLOR_RGB_DARK_SEA_GREEN4          = 'dark sea green4'
COLOR_RGB_DARK_SLATE_BLUE          = 'dark slate blue'
COLOR_RGB_DARK_SLATE_GRAY          = 'dark slate gray'
COLOR_RGB_DARK_TURQUOISE           = 'dark turquoise'
COLOR_RGB_DARK_VIOLET              = 'dark violet'
COLOR_RGB_DEEP_PINK                = 'deep pink'
COLOR_RGB_DEEP_PINK4               = 'deep pink4'
COLOR_RGB_DEEP_SKY_BLUE            = 'deep sky blue'
COLOR_RGB_DEEP_SKY_BLUE1           = 'deep sky blue1'
COLOR_RGB_DEEP_SKY_BLUE2           = 'deep sky blue2'
COLOR_RGB_DEEP_SKY_BLUE3           = 'deep sky blue3'
COLOR_RGB_DEEP_SKY_BLUE4           = 'deep sky blue4'
COLOR_RGB_DIM_GRAY                 = 'dim gray'
COLOR_RGB_DODGER_BLUE              = 'dodger blue'
COLOR_RGB_DODGER_BLUE1             = 'dodger blue1'
COLOR_RGB_DODGER_BLUE2             = 'dodger blue2'
COLOR_RGB_DODGER_BLUE3             = 'dodger blue3'
COLOR_RGB_DODGER_BLUE4             = 'dodger blue4'
COLOR_RGB_FIREBRICK                = 'firebrick'
COLOR_RGB_FIREBRICK1               = 'firebrick1'
COLOR_RGB_FIREBRICK2               = 'firebrick2'
COLOR_RGB_FIREBRICK3               = 'firebrick3'
COLOR_RGB_FIREBRICK4               = 'firebrick4'
COLOR_RGB_FLORAL_WHITE             = 'floral white'
COLOR_RGB_FOREST_GREEN             = 'forest green'
COLOR_RGB_GAINSBORO                = 'gainsboro'
COLOR_RGB_GHOST_WHITE              = 'ghost white'
COLOR_RGB_GOLD                     = 'gold'
COLOR_RGB_GOLD1                    = 'gold1'
COLOR_RGB_GOLD2                    = 'gold2'
COLOR_RGB_GOLD3                    = 'gold3'
COLOR_RGB_GOLD4                    = 'gold4'
COLOR_RGB_GOLDENROD                = 'goldenrod'
COLOR_RGB_GOLDENROD1               = 'goldenrod1'
COLOR_RGB_GOLDENROD2               = 'goldenrod2'
COLOR_RGB_GOLDENROD3               = 'goldenrod3'
COLOR_RGB_GOLDENROD4               = 'goldenrod4'
COLOR_RGB_GRAY                     = 'gray'
COLOR_RGB_GRAY2                    = 'gray2'
COLOR_RGB_GRAY3                    = 'gray3'
COLOR_RGB_GRAY4                    = 'gray4'
COLOR_RGB_GRAY5                    = 'gray5'
COLOR_RGB_GRAY6                    = 'gray6'
COLOR_RGB_GRAY7                    = 'gray7'
COLOR_RGB_GRAY8                    = 'gray8'
COLOR_RGB_GRAY9                    = 'gray9'
COLOR_RGB_GRAY10                   = 'gray10'
COLOR_RGB_GRAY11                   = 'gray11'
COLOR_RGB_GRAY12                   = 'gray12'
COLOR_RGB_GRAY13                   = 'gray13'
COLOR_RGB_GRAY14                   = 'gray14'
COLOR_RGB_GRAY15                   = 'gray15'
COLOR_RGB_GRAY16                   = 'gray16'
COLOR_RGB_GRAY17                   = 'gray17'
COLOR_RGB_GRAY18                   = 'gray18'
COLOR_RGB_GRAY19                   = 'gray19'
COLOR_RGB_GRAY20                   = 'gray20'
COLOR_RGB_GRAY21                   = 'gray21'
COLOR_RGB_GRAY22                   = 'gray22'
COLOR_RGB_GRAY23                   = 'gray23'
COLOR_RGB_GRAY24                   = 'gray24'
COLOR_RGB_GRAY25                   = 'gray25'
COLOR_RGB_GRAY26                   = 'gray26'
COLOR_RGB_GRAY36                   = 'gray36'
COLOR_RGB_GRAY37                   = 'gray37'
COLOR_RGB_GRAY38                   = 'gray38'
COLOR_RGB_GRAY39                   = 'gray39'
COLOR_RGB_GRAY40                   = 'gray40'
COLOR_RGB_GRAY41                   = 'gray41'
COLOR_RGB_GRAY42                   = 'gray42'
COLOR_RGB_GRAY43                   = 'gray43'
COLOR_RGB_GRAY44                   = 'gray44'
COLOR_RGB_GRAY45                   = 'gray45'
COLOR_RGB_GRAY46                   = 'gray46'
COLOR_RGB_GRAY47                   = 'gray47'
COLOR_RGB_GRAY48                   = 'gray48'
COLOR_RGB_GRAY49                   = 'gray49'
COLOR_RGB_GRAY50                   = 'gray50'
COLOR_RGB_GRAY51                   = 'gray51'
COLOR_RGB_GRAY52                   = 'gray52'
COLOR_RGB_GRAY53                   = 'gray53'
COLOR_RGB_GRAY54                   = 'gray54'
COLOR_RGB_GRAY55                   = 'gray55'
COLOR_RGB_GRAY56                   = 'gray56'
COLOR_RGB_GRAY57                   = 'gray57'
COLOR_RGB_GRAY58                   = 'gray58'
COLOR_RGB_GRAY59                   = 'gray59'
COLOR_RGB_GRAY60                   = 'gray60'
COLOR_RGB_GRAY74                   = 'gray74'
COLOR_RGB_GRAY75                   = 'gray75'
COLOR_RGB_GRAY76                   = 'gray76'
COLOR_RGB_GRAY77                   = 'gray77'
COLOR_RGB_GRAY78                   = 'gray78'
COLOR_RGB_GRAY79                   = 'gray79'
COLOR_RGB_GRAY80                   = 'gray80'
COLOR_RGB_GRAY81                   = 'gray81'
COLOR_RGB_GRAY82                   = 'gray82'
COLOR_RGB_GRAY83                   = 'gray83'
COLOR_RGB_GRAY84                   = 'gray84'
COLOR_RGB_GRAY85                   = 'gray85'
COLOR_RGB_GRAY86                   = 'gray86'
COLOR_RGB_GRAY87                   = 'gray87'
COLOR_RGB_GRAY88                   = 'gray88'
COLOR_RGB_GRAY89                   = 'gray89'
COLOR_RGB_GRAY90                   = 'gray90'
COLOR_RGB_GRAY91                   = 'gray91'
COLOR_RGB_GRAY92                   = 'gray92'
COLOR_RGB_GRAY93                   = 'gray93'
COLOR_RGB_GRAY94                   = 'gray94'
COLOR_RGB_GRAY95                   = 'gray95'
COLOR_RGB_GRAY96                   = 'gray96'
COLOR_RGB_GRAY97                   = 'gray97'
COLOR_RGB_GRAY98                   = 'gray98'
COLOR_RGB_GRAY99                   = 'gray99'
COLOR_RGB_GRAY100                  = 'gray100'
COLOR_RGB_GREEN                    = 'green'
COLOR_RGB_GREEN1                   = 'green1'
COLOR_RGB_GREEN2                   = 'green2'
COLOR_RGB_GREEN3                   = 'green3'
COLOR_RGB_GREEN4                   = 'green4'
COLOR_RGB_GREEN_YELLOW             = 'green yellow'
COLOR_RGB_HONEYDEW                 = 'honeydew'
COLOR_RGB_HONEYDEW1                = 'honeydew1'
COLOR_RGB_HONEYDEW2                = 'honeydew2'
COLOR_RGB_HONEYDEW3                = 'honeydew3'
COLOR_RGB_HONEYDEW4                = 'honeydew4'
COLOR_RGB_HOT_PINK                 = 'hot pink'
COLOR_RGB_HOT_PINK1                = 'hot pink1'
COLOR_RGB_HOT_PINK2                = 'hot pink2'
COLOR_RGB_HOT_PINK3                = 'hot pink3'
COLOR_RGB_HOT_PINK4                = 'hot pink4'
COLOR_RGB_INDIAN_RED               = 'indian red'
COLOR_RGB_INDIGO                   = 'indigo'
COLOR_RGB_IVORY                    = 'ivory'
COLOR_RGB_IVORY1                   = 'ivory1'
COLOR_RGB_IVORY2                   = 'ivory2'
COLOR_RGB_IVORY3                   = 'ivory3'
COLOR_RGB_IVORY4                   = 'ivory4'
COLOR_RGB_KHAKI                    = 'khaki'
COLOR_RGB_KHAKI1                   = 'khaki1'
COLOR_RGB_KHAKI2                   = 'khaki2'
COLOR_RGB_KHAKI3                   = 'khaki3'
COLOR_RGB_KHAKI4                   = 'khaki4'
COLOR_RGB_LAVENDER                 = 'lavender'
COLOR_RGB_LAVENDER_BLUSH           = 'lavender blush'
COLOR_RGB_LAVENDER_BLUSH1          = 'lavender blush1'
COLOR_RGB_LAVENDER_BLUSH2          = 'lavender blush2'
COLOR_RGB_LAVENDER_BLUSH3          = 'lavender blush3'
COLOR_RGB_LAVENDER_BLUSH4          = 'lavender blush4'
COLOR_RGB_LAWN_GREEN               = 'lawn green'
COLOR_RGB_LEMON_CHIFFON            = 'lemon chiffon'
COLOR_RGB_LEMON_CHIFFON1           = 'lemon chiffon1'
COLOR_RGB_LEMON_CHIFFON2           = 'lemon chiffon2'
COLOR_RGB_LEMON_CHIFFON3           = 'lemon chiffon3'
COLOR_RGB_LEMON_CHIFFON4           = 'lemon chiffon4'
COLOR_RGB_LIGHT_BLUE               = 'light blue'
COLOR_RGB_LIGHT_BLUE1              = 'light blue1'
COLOR_RGB_LIGHT_BLUE2              = 'light blue2'
COLOR_RGB_LIGHT_BLUE3              = 'light blue3'
COLOR_RGB_LIGHT_BLUE4              = 'light blue4'
COLOR_RGB_LIGHT_CORAL              = 'light coral'
COLOR_RGB_LIGHT_CYAN               = 'light cyan'
COLOR_RGB_LIGHT_CYAN1              = 'light cyan1'
COLOR_RGB_LIGHT_CYAN2              = 'light cyan2'
COLOR_RGB_LIGHT_CYAN3              = 'light cyan3'
COLOR_RGB_LIGHT_CYAN4              = 'light cyan4'
COLOR_RGB_LIGHT_GOLDENROD          = 'light goldenrod'
COLOR_RGB_LIGHT_GOLDENROD1         = 'light goldenrod1'
COLOR_RGB_LIGHT_GOLDENROD2         = 'light goldenrod2'
COLOR_RGB_LIGHT_GOLDENROD3         = 'light goldenrod3'
COLOR_RGB_LIGHT_GOLDENROD4         = 'light goldenrod4'
COLOR_RGB_LIGHT_GOLDENROD_YELLOW   = 'light goldenrod yellow'
COLOR_RGB_LIGHT_GRAY               = 'light gray'
COLOR_RGB_LIGHT_GREEN              = 'light green'
COLOR_RGB_LIGHT_PINK               = 'light pink'
COLOR_RGB_LIGHT_PINK1              = 'light pink1'
COLOR_RGB_LIGHT_PINK2              = 'light pink2'
COLOR_RGB_LIGHT_PINK3              = 'light pink3'
COLOR_RGB_LIGHT_PINK4              = 'light pink4'
COLOR_RGB_LIGHT_SALMON             = 'light salmon'
COLOR_RGB_LIGHT_SALMON1            = 'light salmon1'
COLOR_RGB_LIGHT_SALMON2            = 'light salmon2'
COLOR_RGB_LIGHT_SALMON3            = 'light salmon3'
COLOR_RGB_LIGHT_SALMON4            = 'light salmon4'
COLOR_RGB_LIGHT_SEA_GREEN          = 'light sea green'
COLOR_RGB_LIGHT_SKY_BLUE           = 'light sky blue'
COLOR_RGB_LIGHT_SKY_BLUE1          = 'light sky blue1'
COLOR_RGB_LIGHT_SKY_BLUE2          = 'light sky blue2'
COLOR_RGB_LIGHT_SKY_BLUE3          = 'light sky blue3'
COLOR_RGB_LIGHT_SKY_BLUE4          = 'light sky blue4'
COLOR_RGB_LIGHT_SLATE_BLUE         = 'light slate blue'
COLOR_RGB_LIGHT_SLATE_GRAY         = 'light slate gray'
COLOR_RGB_LIGHT_STEEL_BLUE         = 'light steel blue'
COLOR_RGB_LIGHT_STEEL_BLUE1        = 'light steel blue1'
COLOR_RGB_LIGHT_STEEL_BLUE2        = 'light steel blue2'
COLOR_RGB_LIGHT_STEEL_BLUE3        = 'light steel blue3'
COLOR_RGB_LIGHT_STEEL_BLUE4        = 'light steel blue4'
COLOR_RGB_LIGHT_YELLOW             = 'light yellow'
COLOR_RGB_LIGHT_YELLOW1            = 'light yellow1'
COLOR_RGB_LIGHT_YELLOW2            = 'light yellow2'
COLOR_RGB_LIGHT_YELLOW3            = 'light yellow3'
COLOR_RGB_LIGHT_YELLOW4            = 'light yellow4'
COLOR_RGB_LIME_GREEN               = 'lime green'
COLOR_RGB_LINEN                    = 'linen'
COLOR_RGB_MAGENTA                  = 'magenta'
COLOR_RGB_MAGENTA1                 = 'magenta1'
COLOR_RGB_MAGENTA2                 = 'magenta2'
COLOR_RGB_MAGENTA3                 = 'magenta3'
COLOR_RGB_MAGENTA4                 = 'magenta4'
COLOR_RGB_MAROON                   = 'maroon'
COLOR_RGB_MAROON1                  = 'maroon1'
COLOR_RGB_MAROON2                  = 'maroon2'
COLOR_RGB_MAROON3                  = 'maroon3'
COLOR_RGB_MAROON4                  = 'maroon4'
COLOR_RGB_MEDIUM_AQUAMARINE        = 'medium aquamarine'
COLOR_RGB_MEDIUM_BLUE              = 'medium blue'
COLOR_RGB_MEDIUM_FOREST_GREEN      = 'medium forest green'
COLOR_RGB_MEDIUM_GOLDENROD         = 'medium goldenrod'
COLOR_RGB_MEDIUM_ORCHID            = 'medium orchid'
COLOR_RGB_MEDIUM_ORCHID1           = 'medium orchid1'
COLOR_RGB_MEDIUM_ORCHID2           = 'medium orchid2'
COLOR_RGB_MEDIUM_ORCHID3           = 'medium orchid3'
COLOR_RGB_MEDIUM_ORCHID4           = 'medium orchid4'
COLOR_RGB_MEDIUM_PURPLE            = 'medium purple'
COLOR_RGB_MEDIUM_SEA_GREEN         = 'medium sea green'
COLOR_RGB_MEDIUM_SLATE_BLUE        = 'medium slate blue'
COLOR_RGB_MEDIUM_SPRING_GREEN      = 'medium spring green'
COLOR_RGB_MEDIUM_TURQUOISE         = 'medium turquoise'
COLOR_RGB_MEDIUM_VIOLET_RED        = 'medium violet red'
COLOR_RGB_MIDNIGHT_BLUE            = 'midnight blue'
COLOR_RGB_MINT_CREAM               = 'mint cream'
COLOR_RGB_MISTY_ROSE               = 'misty rose'
COLOR_RGB_MISTY_ROSE1              = 'misty rose1'
COLOR_RGB_MISTY_ROSE2              = 'misty rose2'
COLOR_RGB_MISTY_ROSE3              = 'misty rose3'
COLOR_RGB_MISTY_ROSE4              = 'misty rose4'
COLOR_RGB_MOCCASIN                 = 'moccasin'
COLOR_RGB_NAVAJO_WHITE             = 'navajo white'
COLOR_RGB_NAVAJO_WHITE1            = 'navajo white1'
COLOR_RGB_NAVAJO_WHITE2            = 'navajo white2'
COLOR_RGB_NAVAJO_WHITE3            = 'navajo white3'
COLOR_RGB_NAVAJO_WHITE4            = 'navajo white4'
COLOR_RGB_NAVY                     = 'navy'
COLOR_RGB_NAVY_BLUE                = 'navy blue'
COLOR_RGB_OLD_LACE                 = 'old lace'
COLOR_RGB_OLIVE                    = 'olive'
COLOR_RGB_OLIVE_DRAB               = 'olive drab'
COLOR_RGB_OLIVE_DRAB1              = 'olive drab1'
COLOR_RGB_OLIVE_DRAB2              = 'olive drab2'
COLOR_RGB_OLIVE_DRAB3              = 'olive drab3'
COLOR_RGB_OLIVE_DRAB4              = 'olive drab4'
COLOR_RGB_ORANGE                   = 'orange'
COLOR_RGB_ORANGE1                  = 'orange1'
COLOR_RGB_ORANGE2                  = 'orange2'
COLOR_RGB_ORANGE3                  = 'orange3'
COLOR_RGB_ORANGE4                  = 'orange4'
COLOR_RGB_ORANGE_RED               = 'orange red'
COLOR_RGB_ORANGE_RED1              = 'orange red1'
COLOR_RGB_ORANGE_RED2              = 'orange red2'
COLOR_RGB_ORCHID                   = 'orchid'
COLOR_RGB_ORCHID1                  = 'orchid1'
COLOR_RGB_ORCHID2                  = 'orchid2'
COLOR_RGB_ORCHID3                  = 'orchid3'
COLOR_RGB_ORCHID4                  = 'orchid4'
COLOR_RGB_PALE_GOLDENROD           = 'pale goldenrod'
COLOR_RGB_PALE_GREEN               = 'pale green'
COLOR_RGB_PALE_GREEN1              = 'pale green1'
COLOR_RGB_PALE_GREEN2              = 'pale green2'
COLOR_RGB_PALE_GREEN3              = 'pale green3'
COLOR_RGB_PALE_GREEN4              = 'pale green4'
COLOR_RGB_PALE_TURQUOISE           = 'pale turquoise'
COLOR_RGB_PALE_TURQUOISE1          = 'pale turquoise1'
COLOR_RGB_PALE_TURQUOISE2          = 'pale turquoise2'
COLOR_RGB_PALE_TURQUOISE3          = 'pale turquoise3'
COLOR_RGB_PALE_TURQUOISE4          = 'pale turquoise4'
COLOR_RGB_PALE_VIOLET_RED          = 'pale violet red'
COLOR_RGB_PALE_VIOLET_RED1         = 'pale violet red1'
COLOR_RGB_PALE_VIOLET_RED2         = 'pale violet red2'
COLOR_RGB_PALE_VIOLET_RED3         = 'pale violet red3'
COLOR_RGB_PALE_VIOLET_RED4         = 'pale violet red4'
COLOR_RGB_PAPAYA_WHIP              = 'papaya whip'
COLOR_RGB_PEACH_PUFF               = 'peach puff'
COLOR_RGB_PEACH_PUFF1              = 'peach puff1'
COLOR_RGB_PEACH_PUFF2              = 'peach puff2'
COLOR_RGB_PEACH_PUFF3              = 'peach puff3'
COLOR_RGB_PEACH_PUFF4              = 'peach puff4'
COLOR_RGB_PERU                     = 'peru'
COLOR_RGB_PINK                     = 'pink'
COLOR_RGB_PINK1                    = 'pink1'
COLOR_RGB_PINK2                    = 'pink2'
COLOR_RGB_PINK3                    = 'pink3'
COLOR_RGB_PINK4                    = 'pink4'
COLOR_RGB_PLUM                     = 'plum'
COLOR_RGB_PLUM1                    = 'plum1'
COLOR_RGB_PLUM2                    = 'plum2'
COLOR_RGB_PLUM3                    = 'plum3'
COLOR_RGB_PLUM4                    = 'plum4'
COLOR_RGB_POWDER_BLUE              = 'powder blue'
COLOR_RGB_PURPLE                   = 'purple'
COLOR_RGB_PURPLE1                  = 'purple1'
COLOR_RGB_PURPLE2                  = 'purple2'
COLOR_RGB_PURPLE3                  = 'purple3'
COLOR_RGB_PURPLE4                  = 'purple4'
COLOR_RGB_RED                      = 'red'
COLOR_RGB_ROSY_BROWN               = 'rosy brown'
COLOR_RGB_ROYAL_BLUE               = 'royal blue'
COLOR_RGB_ROYAL_BLUE1              = 'royal blue1'
COLOR_RGB_ROYAL_BLUE2              = 'royal blue2'
COLOR_RGB_ROYAL_BLUE3              = 'royal blue3'
COLOR_RGB_ROYAL_BLUE4              = 'royal blue4'
COLOR_RGB_SADDLE_BROWN             = 'saddle brown'
COLOR_RGB_SALMON                   = 'salmon'
COLOR_RGB_SALMON2                  = 'salmon2'
COLOR_RGB_SALMON3                  = 'salmon3'
COLOR_RGB_SALMON4                  = 'salmon4'
COLOR_RGB_SANDY_BROWN              = 'sandy brown'
COLOR_RGB_SEA_GREEN                = 'sea green'
COLOR_RGB_SEA_GREEN1               = 'sea green1'
COLOR_RGB_SEA_GREEN2               = 'sea green2'
COLOR_RGB_SEA_GREEN3               = 'sea green3'
COLOR_RGB_SEA_GREEN4               = 'sea green4'
COLOR_RGB_SEA_SHELL                = 'sea shell'
COLOR_RGB_SEA_SHELL1               = 'sea shell1'
COLOR_RGB_SEA_SHELL2               = 'sea shell2'
COLOR_RGB_SEA_SHELL3               = 'sea shell3'
COLOR_RGB_SEA_SHELL4               = 'sea shell4'
COLOR_RGB_SIENNA                   = 'sienna'
COLOR_RGB_SIENNA2                  = 'sienna2'
COLOR_RGB_SIENNA3                  = 'sienna3'
COLOR_RGB_SIENNA4                  = 'sienna4'
COLOR_RGB_SILVER                   = 'silver'
COLOR_RGB_SKY_BLUE                 = 'sky blue'
COLOR_RGB_SKY_BLUE1                = 'sky blue1'
COLOR_RGB_SKY_BLUE2                = 'sky blue2'
COLOR_RGB_SKY_BLUE3                = 'sky blue3'
COLOR_RGB_SKY_BLUE4                = 'sky blue4'
COLOR_RGB_SLATE_BLUE               = 'slate blue'
COLOR_RGB_SLATE_BLUE1              = 'slate blue1'
COLOR_RGB_SLATE_BLUE2              = 'slate blue2'
COLOR_RGB_SLATE_BLUE3              = 'slate blue3'
COLOR_RGB_SLATE_BLUE4              = 'slate blue4'
COLOR_RGB_SLATE_GRAY               = 'slate gray'
COLOR_RGB_SNOW                     = 'snow'
COLOR_RGB_SNOW1                    = 'snow1'
COLOR_RGB_SNOW2                    = 'snow2'
COLOR_RGB_SNOW3                    = 'snow3'
COLOR_RGB_SNOW4                    = 'snow4'
COLOR_RGB_SPRING_GREEN             = 'spring green'
COLOR_RGB_SPRING_GREEN1            = 'spring green1'
COLOR_RGB_SPRING_GREEN2            = 'spring green2'
COLOR_RGB_SPRING_GREEN3            = 'spring green3'
COLOR_RGB_SPRING_GREEN4            = 'spring green4'
COLOR_RGB_STEEL_BLUE               = 'steel blue'
COLOR_RGB_STEEL_BLUE1              = 'steel blue1'
COLOR_RGB_STEEL_BLUE2              = 'steel blue2'
COLOR_RGB_STEEL_BLUE3              = 'steel blue3'
COLOR_RGB_STEEL_BLUE4              = 'steel blue4'
COLOR_RGB_TAN                      = 'tan'
COLOR_RGB_TAN1                     = 'tan1'
COLOR_RGB_TAN2                     = 'tan2'
COLOR_RGB_TAN3                     = 'tan3'
COLOR_RGB_TAN4                     = 'tan4'
COLOR_RGB_TEAL                     = 'teal'
COLOR_RGB_THISTLE                  = 'thistle'
COLOR_RGB_TOMATO                   = 'tomato'
COLOR_RGB_TOMATO1                  = 'tomato1'
COLOR_RGB_TOMATO2                  = 'tomato2'
COLOR_RGB_TOMATO3                  = 'tomato3'
COLOR_RGB_TOMATO4                  = 'tomato4'
COLOR_RGB_TURQUOISE                = 'turquoise'
COLOR_RGB_TURQUOISE1               = 'turquoise1'
COLOR_RGB_TURQUOISE2               = 'turquoise2'
COLOR_RGB_TURQUOISE3               = 'turquoise3'
COLOR_RGB_TURQUOISE4               = 'turquoise4'
COLOR_RGB_VIOLET                   = 'violet'
COLOR_RGB_VIOLET_RED               = 'violet red'
COLOR_RGB_VIOLET_RED1              = 'violet red1'
COLOR_RGB_VIOLET_RED2              = 'violet red2'
COLOR_RGB_VIOLET_RED3              = 'violet red3'
COLOR_RGB_VIOLET_RED4              = 'violet red4'
COLOR_RGB_WHEAT                    = 'wheat'
COLOR_RGB_WHEAT1                   = 'wheat1'
COLOR_RGB_WHEAT2                   = 'wheat2'
COLOR_RGB_WHEAT3                   = 'wheat3'
COLOR_RGB_WHEAT4                   = 'wheat4'
COLOR_RGB_WHITE                    = 'white'
COLOR_RGB_WHITE_SMOKE              = 'white smoke'
COLOR_RGB_YELLOW                   = 'yellow'
COLOR_RGB_YELLOW1                  = 'yellow1'
COLOR_RGB_YELLOW2                  = 'yellow2'
COLOR_RGB_YELLOW3                  = 'yellow3'
COLOR_RGB_YELLOW4                  = 'yellow4'
COLOR_RGB_YELLOW_GREEN             = 'yellow green'
