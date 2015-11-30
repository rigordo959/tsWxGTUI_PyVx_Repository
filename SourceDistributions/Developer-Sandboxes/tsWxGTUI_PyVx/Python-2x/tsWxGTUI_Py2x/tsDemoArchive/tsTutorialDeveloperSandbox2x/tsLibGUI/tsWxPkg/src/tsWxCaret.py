#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:27:02 AM rsg>"
'''
tsWxCaret.py - Class for representing and manipulating carets
(cursors). The caret has position (x, y), size (width, height)
and visibility properties.
'''
#################################################################
#
# File: tsWxCaret.py
#
# Purpose:
#
#    Class for representing and manipulating carets (cursors).
#    The caret has position (x, y), size (width, height) and
#    visibility properties.
#
# Usage (example):
#
#    # Import
#
#    from tsWxCaret import Caret
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

__title__     = 'tsWxCaret'
__version__   = '0.2.0'
__date__      = '07/18/2013'
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
from tsWxPoint import Point as wxPoint
from tsWxSize import Size as wxSize

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

#---------------------------------------------------------------------------

class Caret(object):
    '''
    A class for representing and manipulating carets (cursors). It has
    position (x, y), size (width, height) and visibility properties.
    '''
    def __init__(self, window, size):
        '''
        Create a new caret object.
        '''
        theClass = 'Caret'

        wx.RegisterFirstCallerClassName(self, theClass)

##        self.tsBeginClassRegistration(theClass, id)
        try:

            self.logger = tsLogger.TsLogger(threshold=tsLogger.ERROR,
                                            start=time.time(),
                                            name=tsLogger.StandardOutputFile)

        except AttributeError, e:

            self.logger = None
            msg = 'tsWxCaret.__init__: Exception = %s' % e
            raise tse.ProgramException(tse.APPLICATION_TRAP, msg)


        self.ts_Position = wxPoint(0, 0)
        self.ts_Size = wxSize(0, 0)

        self.ts_Window = window
        self.ts_visibility = wx.caretNormal
        self.theScreen = tsGTUI.GraphicalTextUserInterface(theClass)
        self.theScreen.curs_set(self.ts_visibility)

##        self.tsEndClassRegistration(theClass)

    #-----------------------------------------------------------------------

##    def __del__(self):
##        '''
##        '''
##        pass

    #-----------------------------------------------------------------------

    def __nonzero__(self):
        '''
        '''
        return (True)

    #-----------------------------------------------------------------------
 
    def Destroy(self):
        '''
        Deletes the C++ object this Python object is a proxy for.
        '''
        pass

    #-----------------------------------------------------------------------

    @staticmethod
    def GetBlinkTime():
        '''
        '''
        return (wx.caretBlinkMilliseconds)

    #-----------------------------------------------------------------------
 
    def GetPosition(self):
        '''
        '''
        if window is None or \
           window.Handle is None:
            # Physical window not yet available
            (y_characters, x_characters) = (0, 0)
        else:
            # Physical window already available
            (y_characters, x_characters) = window.Handle.getyx()

        (x_pixels, y_pixels) = wx.tsGetPixelValues(
            x_characters, y_characters)

        self.tsSetPosition(wxPoint(x_pixels, y_pixels))
        return (self.ts_Position)

    #-----------------------------------------------------------------------

    def GetPositionTuple(self):
        '''
        '''
        if window is None or \
           window.Handle is None:
            # Physical window not yet available
            (y_characters, x_characters) = (0, 0)
        else:
            # Physical window already available
            (y_characters, x_characters) = window.Handle.getyx()

        (x_pixels, y_pixels) = wx.tsGetPixelValues(
            x_characters, y_characters)

        self.tsSetPosition(wxPoint(x_pixels, y_pixels))
        return (x_pixels, y_pixels)

    #-----------------------------------------------------------------------

    def GetSize(self):
        '''
        '''
        # Ignore self.Size. It is always a single character
        (width, height) = wx.tsGetPixelValues(1, 1)
        return (wxSize(width, height))

    #-----------------------------------------------------------------------

    def GetSizeTuple(self):
        '''
        '''
        # Ignore self.Size. It is always a single character
        (width, height) = wx.tsGetPixelValues(1, 1)
        return (width, height)

    #-----------------------------------------------------------------------

    def GetWindow(self):
        '''
        '''
        return (self.Window)

    #-----------------------------------------------------------------------

    def Hide(self):
        '''
        '''
        self.ts_visibility = wx.caretInvisible
        self.theScreen.curs_set(self.ts_visibility)

    #-----------------------------------------------------------------------

    def IsOk(self):
        '''
        '''
        return (True)

    #-----------------------------------------------------------------------

    def IsVisible(self):
        '''
        '''
        if self.ts_visibility == wx.caretInvisible:
            return (False)
        else:
            return (True)

    #-----------------------------------------------------------------------

    def Move(self, pt):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def MoveXY(self, x, y):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    @staticmethod
    def SetBlinkTime(milliseconds):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def tsSetPosition(self, pos):
        '''
        '''
        self.ts_Position = pos

    #-----------------------------------------------------------------------

    def SetSize(self, size):
        '''
        '''
        self.ts_Size = size

    #-----------------------------------------------------------------------

    def SetSizeWH(self, width, height):
        '''
        '''
        pass

    #-----------------------------------------------------------------------

    def Show(self, show):
        '''
        Sets the cursor state. visibility can be set to 0, 1, or 2, for
        invisible, normal, or very visible. If the terminal supports the
        visibility requested, the previous cursor state is returned;
        otherwise, an exception is raised. On many terminals, the "visible"
        mode is an underline cursor and the "very visible" mode is a block
        cursor.

        NOTE: Available curses feature.

        curs_set(visibility)
        '''
        if show == False:

            self.ts_visibility = wx.caretInvisible

        else:

            self.ts_visibility = wx.caretNormal

        try:

            previousState = self.theScreen.curs_set(self.ts_visibility)

            return (previousState)

        except Exception, e:

            self.logger.error('tsWxCaret.Show: Exception=<%s>.' % str(e))

    #-----------------------------------------------------------------------

    Position = property(GetPosition, tsSetPosition)
    Size = property(GetSize, SetSize)
    Window = property(GetWindow)

#---------------------------------------------------------------------------

if __name__ == '__main__':

    print(__header__)

    wxCaret = Caret

    window = None
    size = wxSize(0, 0)
    theCaret = wxCaret(window, size)
    print('theCaret:', theCaret)
    print('theCaret.Position:', theCaret.Position)
    print('theCaret.Size:', theCaret.Size)
    print('theCaret.Visibility:', theCaret.ts_visibility)
