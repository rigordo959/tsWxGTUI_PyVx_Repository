#! /usr/bin/env python
# "Time-stamp: <04/08/2015  4:40:20 AM rsg>"
'''
tsWxPythonMonochromeDataBase.py - Refactored vt100/vt220 (black
with an unspecified single color shade of white, green or orange)
data base portion of tsWxGraphicalTextUserInterface for name keys
and code keys.
'''
#################################################################
#
# File: tsWxPythonMonochromeDataBase.py
#
# Purpose:
#
#     tsWxPythonMonochromeDataBase.py - Refactored vt100/vt220
#     (black with an unspecified single color shade of white,
#     green or orange) data base portion of
#     tsWxGraphicalTextUserInterface for name keys and code keys.
#
# Usage (example):
#
#     ## Import Module
#     from tsWxPythonMonochromeDataBase import *
#
# Requirements:
#
#     Provide cursesMonochromeNameFromCode dictionary.
#
#     Provide cursesMonochromeCodeFromName dictionary.
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

__title__     = 'tsWxPythonMonochromeDataBase'
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

# Set of monochrome color numbers and names
# which curses guarantees to recognize.
cursesMonochromeNameFromCode = {
    'name': 'cursesMonochromeNameFromCode',
    0: COLOR_BLACK
    }

#---------------------------------------------------------------------------

# Set of monochrome color names and numbers
# which curses guarantees to recognize.
cursesMonochromeCodeFromName = {
    'name': 'cursesMonochromeCodeFromName',
    COLOR_BLACK: 0
    }
