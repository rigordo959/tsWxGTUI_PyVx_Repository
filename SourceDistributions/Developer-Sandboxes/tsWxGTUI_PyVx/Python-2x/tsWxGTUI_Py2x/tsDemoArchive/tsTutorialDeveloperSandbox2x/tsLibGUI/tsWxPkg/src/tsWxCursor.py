#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:29:05 AM rsg>"
'''
tsWxCursor.py - Class to establish a cursor from a small bitmap.
The cursor is usually used for denoting where the mouse pointer
is, with a picture that might indicate the interpretation of a
mouse click.
'''
#################################################################
#
# File: tsWxCursor.py
#
# Purpose:
#
#    Class to establish a cursor from a small bitmap. The cursor
#    is usually used for denoting where the mouse pointer is,
#    with a picture that might indicate the interpretation of a
#    mouse click.
#
# Usage (example):
#
#    # Import
#
#    from tsWxCursor import Cursor
#
# Requirements:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Capabilities:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Limitations:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Classes:
#
#    wxPython 2.8.9.2 (New wxPyDocs)/wxWidgets 2.9.2 (Ref. Man.).
#
# Modifications:
#
#    None.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsWxCursor'
__version__   = '0.0.0'
__date__      = '04/01/2013'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2007-2013 ' + \
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
                '\n\n\t  nCurses API & Run Time Library Features:' + \
                '\n\t  Copyright (c) 1998-2011 ' + \
                'Free Software Foundation, Inc.' + \
                '\n\t\t\tAll rights reserved.' + \
                '\n\t  GNU General Public License, ' + \
                'Version 3, 29 June 2007'

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

import time

import tsExceptions as tse
import tsLogger
import tsWxGlobals as wx
import tsWxGraphicalTextUserInterface as tsGTUI
from tsWxObject import Object

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

cursesInvisibleCursorMode = 0
cursesUnderlineCursorMode = 1
cursesVeryVisibleCursorMode = 2

#---------------------------------------------------------------------------

class Cursor(Object):
    '''
    A cursor is a small bitmap usually used for denoting where the mouse
    pointer is, with a picture that might indicate the interpretation of
    a mouse click.

    A single cursor object may be used in many windows (any subwindow type).
    The wxWindows convention is to set the cursor for a window, as in X,
    rather than to set it globally as in MS Windows, although a global
    wx.SetCursor function is also available for use on MS Windows.

    Stock Cursor Names

    CURSOR_ARROW          A standard arrow cursor.
    CURSOR_ARROWWAIT      An arrow and an hourglass, (windows.)
    CURSOR_BLANK          Transparent cursor.
    CURSOR_BULLSEYE       Bullseye cursor.
    CURSOR_CHAR           Rectangular character cursor.
    CURSOR_CROSS          A cross cursor.
    CURSOR_DEFAULT        A platform dependent default cursor.
    CURSOR_HAND           A hand cursor.
    CURSOR_IBEAM          An I-beam cursor (vertical line).
    CURSOR_LEFT_BUTTON    Represents a mouse with the left button depressed.
    CURSOR_MAGNIFIER      A magnifier icon.
    CURSOR_MIDDLE_BUTTON  Represents a mouse with the middle button depressed.
    CURSOR_NO_ENTRY       A no-entry sign cursor.
    CURSOR_PAINT_BRUSH    A paintbrush cursor.
    CURSOR_PENCIL         A pencil cursor.
    CURSOR_POINT_LEFT     A cursor that points left.
    CURSOR_POINT_RIGHT    A cursor that points right.
    CURSOR_QUESTION_ARROW An arrow and question mark.
    CURSOR_RIGHT_ARROW    A standard arrow cursor pointing to the right.
    CURSOR_RIGHT_BUTTON   Represents a mouse with the right button depressed.
    CURSOR_SIZENESW       A sizing cursor pointing NE-SW.
    CURSOR_SIZENS         A sizing cursor pointing N-S.
    CURSOR_SIZENWSE       A sizing cursor pointing NW-SE.
    CURSOR_SIZEWE         A sizing cursor pointing W-E.
    CURSOR_SIZING         A general sizing cursor.
    CURSOR_SPRAYCAN       A spraycan cursor.
    CURSOR_WAIT           A wait cursor.
    CURSOR_WATCH          A watch cursor.
    '''

    def __init__(self, cursorName, type, hotSpotX=0, hotSpotY=0):
        '''
        Associate a curses cursor visibility mode with a wxPython cursor
        name instead of the following.
 
        Construct a Cursor from a file. Specify the type of file using
        wx.BITMAP_TYPE* constants, and specify the hotspot if not using
        a .cur file. :see: Alternate constructors wx.StockCursor,
        `wx.CursorFromImage`
        '''
        theClass = 'Cursor'

        wx.RegisterFirstCallerClassName(self, theClass)

        Object.__init__(self)
        try:
            self.theFirstCallerName != theClass
        except AttributeError:
            self.theFirstCallerName = theClass

        self.tsBeginClassRegistration(theClass, wx.ID_ANY)
        try:

            self.logger = tsLogger.TsLogger(threshold=tsLogger.ERROR,
                                            start=time.time(),
                                            name=tsLogger.StandardOutputFile)

        except AttributeError, e:

            self.logger = None
            msg = 'tsWxCursor.__init__: Exception = %s' % e
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)

        if tsGTUI:

            self.ts_CursorName = cursorName
            self.ts_CursorHotSpotX = hotSpotX
            self.ts_CursorHotSpotY = hotSpotY

            if cursorName == wx.CURSOR_BLANK_NAME:

                self.ts_CursorType = cursesInvisibleCursorMode

            elif cursorName == wx.CURSOR_CHAR_NAME:

                self.ts_CursorType = cursesVeryVisibleCursorMode

            else:

                # cursorName == wx.CURSOR_DEFAULT_NAME
                self.ts_CursorType = cursesUnderlineCursorMode

            tsGTUI.tsSetCursesCursor(self.ts_CursorType)

        else:
            self.ts_CursorName = cursorName
            self.ts_CursorType = type
            self.ts_CursorHotSpotX = hotSpotX
            self.ts_CursorHotSpotY = hotSpotY

        self.tsEndClassRegistration(theClass)
 
##    def __del__(self):
##        '''
##        '''
##        pass

    def __nonzero__(self):
        '''
        '''
        return (True)

    def IsOk(self):
        '''
        '''
        return (True)

    def Ok(self):
        '''
        '''
        return (True)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)
