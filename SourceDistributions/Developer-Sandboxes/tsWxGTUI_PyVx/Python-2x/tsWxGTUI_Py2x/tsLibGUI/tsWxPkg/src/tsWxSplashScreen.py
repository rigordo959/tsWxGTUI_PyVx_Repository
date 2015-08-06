#! /usr/bin/env python
# "Time-stamp: <10/25/2013  6:49:41 AM rsg>"
'''
tsWxSplashScreen.py - Class to show a window with a thin border,
displaying a "bitmap" (text) describing your application.
The splash screen is shown during application initialisation.
The application then either explicitly destroyes it or lets
it time-out.
'''
#################################################################
#
# File: tsWxSplashScreen.py
#
# Purpose:
#
#    Class to show a window with a thin border, displaying a
#    "bitmap" (text) describing your application. The splash
#    screen is shown during application initialisation.
#    The application then either explicitly destroyes it or
#    lets it time-out.
#
# Usage (example):
#
#    # Import
#
#    from tsWxSplashScreen import SplashScreen
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

__title__     = 'tsWxSplashScreen'
__version__   = '1.0.0'
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

import tsWxGlobals as wx
from tsWxFrame import Frame
from tsWxPoint import Point as wxPoint
from tsWxRect import Rect as wxRect
from tsWxSize import Size as wxSize
from tsWxTextCtrl import TextCtrl as wxTextCtrl
from tsWxTopLevelWindow import TopLevelWindow

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

BlackOnWhiteDefault = ['cygwin', 'vt100']

WhiteOnBlackDefault = ['xterm-color', 'xterm', 'ansi']

#---------------------------------------------------------------------------

class SplashScreen(Frame):
    '''
    Class to show a window with a thin border, displaying a "bitmap" (text)
    describing your application. The splash screen is shown during
    application initialisation. The application then either explicitly
    destroyes it or lets it time-out.
    '''
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 bitmap=None,
                 splashStyle=0,
                 milliseconds=0,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.DEFAULT_SPLASHSCREEN_STYLE):
        '''
        Construct class.
        '''
        theClass = 'SplashScreen'

        # Capture initial caller parametsrs before they are changed
        self.caller_bitmap = bitmap
        self.caller_splashStyle = splashStyle
        self.caller_milliseconds = milliseconds
        self.caller_parent = parent
        self.caller_id = id
        self.caller_pos = pos
        self.caller_size = size
        self.caller_style = style

        wx.RegisterFirstCallerClassName(self, theClass)

        TopLevelWindow.__init__(self)

        self.tsBeginClassRegistration(theClass, id)

##        size = wxSize(500, 300)
        Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=wx.EmptyString,
            pos=pos,
            size=size,
            style=wx.BORDER_SIMPLE, #wx.DEFAULT_SPLASHSCREEN_STYLE,
            name=wx.SplashScreenNameStr)

        splashWindow = self
        splashWindow.ts_ForegroundColour = wx.COLOR_RED
        splashWindow.ts_BackgroundColour = wx.COLOR_WHITE

        self.ts_SplashStyle = splashStyle
        self.ts_SplashWindow = splashWindow
        self.ts_SplashTimeout = milliseconds

        self.ts_bitmap = wxTextCtrl(
            splashWindow,
            id=-1,
            value=wx.EmptyString,
            pos=wxPoint(
                splashWindow.ts_ClientRect.x + wx.pixelWidthPerCharacter,
                splashWindow.ts_ClientRect.y + wx.pixelHeightPerCharacter),
            size=wxSize(
                splashWindow.ts_ClientRect.width - (
                    2 * wx.pixelWidthPerCharacter),
                splashWindow.ts_ClientRect.height -(
                    2 * wx.pixelHeightPerCharacter)),
            style=0, # wx.TE_MULTILINE |wx.TE_READONLY,
            validator=wx.DefaultValidator,
            name=wx.TextCtrlNameStr)

        self.ts_bitmap.AppendText(bitmap)
        self.ts_bitmap.Show()

        self.SetFocus()

##        print('SplashScreen: Show')
##        self.Show()
##        print('SplashScreen: Sleep(%d)' % self.ts_SplashTimeout)
##        time.sleep(self.ts_SplashTimeout / 1000)
##        print('SplashScreen: Hide')
##        self.Hide()

        self.tsEndClassRegistration(theClass)

    def GetSplashStyle(self):
        '''
        Return the SplashScreen style.
        '''
        return (self.ts_SplashStyle)

    def GetSplashWindow(self):
        '''
        Return the SplashScreen window.
        '''
        return (self.ts_SplashWindow)

    def GetTimeout(self):
        '''
        Return the SplashScreen timeout milliseconds.
        '''
        return (self.ts_SplashTimeout)

    #-----------------------------------------------------------------------
    # Begin tsWx API Extensions

    # End tsWx API Extensions
    #-----------------------------------------------------------------------

    SplashStyle = property(GetSplashStyle)
    SplashWindow = property(GetSplashWindow)
    Timeout = property(GetTimeout)

##    #-----------------------------------------------------------------------
##    # Begin tsWx API Extensions

##    # End tsWx API Extensions
##    #-----------------------------------------------------------------------

#---------------------------------------------------------------------------
 
if __name__ == '__main__':

    print(__header__)
