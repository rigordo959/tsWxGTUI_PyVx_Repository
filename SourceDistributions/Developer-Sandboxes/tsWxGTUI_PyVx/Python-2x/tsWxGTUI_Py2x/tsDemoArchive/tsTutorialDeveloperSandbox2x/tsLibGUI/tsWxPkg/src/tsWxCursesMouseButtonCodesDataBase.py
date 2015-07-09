#! /usr/bin/env python
# "Time-stamp: <03/18/2015  4:48:33 AM rsg>"
'''
tsWxCursesMouseButtonCodesDataBase.py.py - Dictionary of Python
Curses Mouse Button Codes to be associared with the terminal
console mouse (touchpad or touchscreen).
'''
#################################################################
#
# File: tsWxCursesKeyCodesDataBase.py
#
# Purpose:
#
#     Dictionary of Python Curses Mouse Button Codes to be
#     associared with the terminal console mouse (touchpad
#     or touchscreen).
#
# Usage (example):
#
#     ## Import Module
#     import tsWxCursesMouseButtonCodesDataBase
#
# Requirements:
#
#    1. Input Interface
#
#       Optional: Computer Mouse (industry standard mult-button).
#
#    2. Output Interface
#
#       Required: Computer Monitor (industry standard 256-color,
#       8-color recommended minimum or monochrome) able to display
#       text characters (80-column by 25-row is recommended minimum
#       format).
#
#       Optional: Font type, font size, screen columns and screen
#       rows are established by manual user actions.
#
# Capabilities:
#
#    1. Defines the Mouse Button Codes to be associared with
#       the terminal console mouse (touchpad or touchscreen)..
#
# Limitations:
#
#    None
#
# Notes:
#
#    None
#
# Classes:
#
#    None
#
# Methods:
#
#    None
#
# Modifications:
#
#    2015/03/17 rsg Extracted this code from the module named
#                   tsWxGraphicalTextUserInterface.py so as
#                   to facilitate the editing and maintenance
#                   of both files.
#
# ToDo:
#
#    None
#
##############################################################

__title__     = 'tsWxCursesMouseButtonCodesDataBase'
__version__   = '2.42.1'
__date__      = '03/17/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2015 ' + \
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

import curses

#---------------------------------------------------------------------------

# Set of mouse button codes that curses guarantees to recognize
MouseButtonCodes = {
    'name': 'MouseButtonCodes',
    curses.BUTTON1_PRESSED: 'button 1 pressed',
    curses.BUTTON1_RELEASED: 'button 1 released',
    curses.BUTTON1_CLICKED: 'button 1 clicked',
    curses.BUTTON1_DOUBLE_CLICKED: 'button 1 double clicked',
    curses.BUTTON1_TRIPLE_CLICKED: 'button 1 triple clicked',
    curses.BUTTON2_PRESSED: 'button 2 pressed',
    curses.BUTTON2_RELEASED: 'button 2 released',
    curses.BUTTON2_CLICKED: 'button 2 clicked',
    curses.BUTTON2_DOUBLE_CLICKED: 'button 2 double clicked',
    curses.BUTTON2_TRIPLE_CLICKED: 'button 2 triple clicked',
    curses.BUTTON3_PRESSED: 'button 3 pressed',
    curses.BUTTON3_RELEASED: 'button 3 released',
    curses.BUTTON3_CLICKED: 'button 3 clicked',
    curses.BUTTON3_DOUBLE_CLICKED: 'button 3 double clicked',
    curses.BUTTON3_TRIPLE_CLICKED: 'button 3 triple clicked',
    curses.BUTTON4_PRESSED: 'button 4 pressed',
    curses.BUTTON4_RELEASED: 'button 4 released',
    curses.BUTTON4_CLICKED: 'button 4 clicked',
    curses.BUTTON4_DOUBLE_CLICKED: 'button 4 double clicked',
    curses.BUTTON4_TRIPLE_CLICKED: 'button 4 triple clicked',
    curses.BUTTON_SHIFT: 'button shift',
    curses.BUTTON_CTRL: 'button ctrl',
    curses.BUTTON_ALT: 'button alt'
    #
    # These last two codes are commented out because their inclusion
    # preempts identification of the specific mouse and button state
    # changes.
    #
    ## curses.ALL_MOUSE_EVENTS: 'report all button state changes',
    ## curses.REPORT_MOUSE_POSITION: 'report mouse movement',
    }

#---------------------------------------------------------------------------

if __name__ == '__main__':
 
    print(__header__)
