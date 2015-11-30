#! /usr/bin/env python
# "Time-stamp: <04/08/2015  7:58:21 AM rsg>"
'''
tsWxFocusEvent.py - Class to emulate the wxPython API for
non-graphical, curses-based platforms.
'''
#################################################################
#
# File: tsWxFocusEvent.py
#
# Purpose:
#
#    Class to emulate the wxPython API for non-graphical,
#    curses-based platforms.
#
# Usage (example):
#
#    # Import
#
#    from tsWxFocusEvent import FocusEvent
#
# Requirements:
#
#    wxPython 2.8.9.2
#
# Capabilities:
#
#    wxPython 2.8.9.2
#
# Limitations:
#
#    wxPython 2.8.9.2
#
# Notes:
#
#    None
#
# Methods:
#
#    wxPython 2.8.9.2
#
# Classes:
#
#    wxPython 2.8.9.2
#
# Modifications:
#
#    None.
#
# ToDo:
#
#    wxPython 2.8.9.2
#
#################################################################

__title__     = 'tsWxFocusEvent'
__version__   = '0.1.1'
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

#---------------------------------------------------------------------------

from tsWxGTUI_Py3x.tsLibGUI import tsWxGlobals as wx

from tsWxGTUI_Py3x.tsLibGUI.tsWxEvent import Event

#---------------------------------------------------------------------------

##DEBUG = True
DEBUG = wx.Debug_GUI_Launch | \
        wx.Debug_GUI_Progress | \
        wx.Debug_GUI_Termination | \
        wx.Debug_GUI_Exceptions

##VERBOSE = True
VERBOSE = wx.Debug_GUI_Configuration

EVT_NULL = 0

#---------------------------------------------------------------------------

class FocusEvent(Event):
    '''
    A data structure for representing a point or position with integer x
    and y properties. Most places in wxPython that expect a wx.FocusEvent can
    also accept a (x,y) tuple.
    '''
    def __init__(self, type=EVT_NULL, winid=0):
        '''
        Constructor. Create a wx.FocusEvent object.
        '''
        theClass = 'FocusEvent'

        wx.RegisterFirstCallerClassName(self, theClass)

        Event.__init__(self)

        self.tsBeginClassRegistration(theClass, id)

        self.Window = None
##        self.thisown = theClass

        self.tsEndClassRegistration(theClass)

    def GetWindow(self):
        '''
        Returns the other window associated with this event, that is the
        window which had the focus before for the EVT_SET_FOCUS event
        and the window which is going to receive focus for the
        wxEVT_KILL_FOCUS event.

        Warning: the window returned may be None!
        '''
        return (self.Window)

    def SetWindow(self, win):
        '''
        '''
        self.Window = win

    Window = property(GetWindow, SetWindow)

#---------------------------------------------------------------------------

if __name__ == '__main__':
    type = wx.EVT_NULL
    winid = 0
    theFocusEvent = FocusEvent(type=type, winid=winid)
    print('theFocusEvent: %s; type: %d; winid: %d' % (
        theFocusEvent, type, winid))
